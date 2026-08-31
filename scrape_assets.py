import urllib.request
import re
import os
import urllib.parse

output_dir = "/Users/instant/Dev/douceurs-lakay/scraped_assets"
os.makedirs(output_dir, exist_ok=True)

urls = [
    "https://douceurslakay.com/",
    "https://douceurslakay.com/produits",
    "https://douceurslakay.com/a-propos",
    "https://douceurslakay.com/contact"
]

all_images = set()
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

print("--> Scraping website pages...")
for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode("utf-8", errors="ignore")
            # find all image assets
            matches = re.findall(r'(https?://(?:assets|cdn)\.zyrosite\.com/[^"\'\s<>\)]+)', content)
            for m in matches:
                clean = m.replace('&amp;', '&').replace('\\"', '').replace('\\', '')
                all_images.add(clean)
    except Exception as e:
        print(f"Error fetching {u}: {e}")

print(f"Found {len(all_images)} assets from website.")

downloaded = []
for idx, img_url in enumerate(sorted(all_images)):
    try:
        ext = ".jpg"
        if ".png" in img_url.lower():
            ext = ".png"
        elif ".webp" in img_url.lower():
            ext = ".webp"
        elif ".svg" in img_url.lower():
            ext = ".svg"
        
        filename = f"web_asset_{idx+1}{ext}"
        filepath = os.path.join(output_dir, filename)
        
        req = urllib.request.Request(img_url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp, open(filepath, "wb") as f:
            f.write(resp.read())
        print(f"Downloaded: {filename} from {img_url}")
        downloaded.append((filename, img_url))
    except Exception as e:
        print(f"Failed to download {img_url}: {e}")

print(f"\n--> Successfully downloaded {len(downloaded)} assets to {output_dir}")
