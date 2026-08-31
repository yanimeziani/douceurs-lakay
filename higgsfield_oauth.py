#!/usr/bin/env python3
"""
Higgsfield MCP OAuth 2.0 PKCE Authorization Flow
Spawns a local listener, opens the browser to authenticate with Higgsfield,
and captures the Bearer token to authorize the MCP server.
"""

import os
import sys
import json
import base64
import hashlib
import secrets
import urllib.parse
import http.server
import socketserver
import urllib.request

PORT = 8089
REDIRECT_URI = f"http://localhost:{PORT}/callback"
AUTH_ENDPOINT = "https://mcp.higgsfield.ai/oauth2/authorize"
TOKEN_ENDPOINT = "https://mcp.higgsfield.ai/oauth2/token"
REGISTRATION_ENDPOINT = "https://mcp.higgsfield.ai/oauth2/register"

def generate_pkce():
    verifier = base64.urlsafe_b64encode(secrets.token_bytes(32)).decode('utf-8').rstrip('=')
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode('utf-8')).digest()).decode('utf-8').rstrip('=')
    return verifier, challenge

def register_client():
    try:
        reg_payload = {
            "client_name": "Antigravity CLI MCP Client",
            "redirect_uris": [REDIRECT_URI],
            "response_types": ["code"],
            "grant_types": ["authorization_code", "refresh_token"],
            "token_endpoint_auth_method": "none"
        }
        req = urllib.request.Request(
            REGISTRATION_ENDPOINT,
            data=json.dumps(reg_payload).encode('utf-8'),
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print("✅ Dynamic client registered:", data.get("client_id"))
            return data.get("client_id")
    except Exception as e:
        print("Note on registration (using public client):", e)
        return "higgsfield-mcp-client"

def main():
    verifier, challenge = generate_pkce()
    client_id = register_client()
    state = secrets.token_hex(16)

    params = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": "openid email offline_access",
        "code_challenge": challenge,
        "code_challenge_method": "S256",
        "state": state
    }

    auth_url = f"{AUTH_ENDPOINT}?{urllib.parse.urlencode(params)}"
    print("\n" + "="*75)
    print("🔐 HIGGSFIELD MCP OAUTH 2.0 PKCE AUTHENTICATION")
    print("="*75)
    print(f"\n🌐 Opening browser for authorization:\n{auth_url}\n")

    # Spawn browser
    os.system(f"open '{auth_url}'")

    auth_code = None

    class OAuthHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            nonlocal auth_code
            parsed = urllib.parse.urlparse(self.path)
            if parsed.path == "/callback":
                query = urllib.parse.parse_qs(parsed.query)
                auth_code = query.get("code", [None])[0]
                self.send_response(200)
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                self.wfile.write(b"<h1>Authentication successful!</h1><p>You can close this tab and return to Antigravity.</p>")
            else:
                self.send_response(404)
                self.end_headers()
        def log_message(self, format, *args):
            pass

    print("⏳ Waiting for browser callback on http://localhost:8089/callback...")
    with socketserver.TCPServer(("", PORT), OAuthHandler) as httpd:
        httpd.handle_request()

    if auth_code:
        print(f"\n✅ Authorization code received! Exchanging for tokens...")
        token_payload = {
            "grant_type": "authorization_code",
            "client_id": client_id,
            "code": auth_code,
            "redirect_uri": REDIRECT_URI,
            "code_verifier": verifier
        }
        try:
            req = urllib.request.Request(
                TOKEN_ENDPOINT,
                data=urllib.parse.urlencode(token_payload).encode('utf-8'),
                headers={"Content-Type": "application/x-www-form-urlencoded"}
            )
            with urllib.request.urlopen(req) as resp:
                tokens = json.loads(resp.read().decode('utf-8'))
                print("🎉 Tokens successfully received!")
                
                # Save token
                token_file = os.path.expanduser("~/.gemini/config/higgsfield_token.json")
                with open(token_file, "w") as f:
                    json.dump(tokens, f, indent=2)
                print(f"📁 Saved to {token_file}")
                
                # Update mcp_config.json with Authorization header
                mcp_file = os.path.expanduser("~/.gemini/config/mcp_config.json")
                if os.path.exists(mcp_file):
                    with open(mcp_file, "r") as f:
                        mcp_cfg = json.load(f)
                    mcp_cfg["mcpServers"]["higgsfield"] = {
                        "serverUrl": "https://mcp.higgsfield.ai/mcp",
                        "headers": {
                            "Authorization": f"Bearer {tokens.get('access_token')}"
                        }
                    }
                    with open(mcp_file, "w") as f:
                        json.dump(mcp_cfg, f, indent=2)
                    print("✅ Updated ~/.gemini/config/mcp_config.json with Bearer token!")
        except Exception as e:
            print("❌ Token exchange error:", e)
    else:
        print("❌ No authorization code received.")

if __name__ == "__main__":
    main()
