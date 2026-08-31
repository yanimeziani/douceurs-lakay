#!/usr/bin/env python3
"""
Seedance 2.5 - 30-Second Wedding & Event Catering Dialogue Commercial
Target ICP: Haitian Diaspora & Quebec families planning Weddings, Anniversaries, and 100-300 person Banquets.
"""

import os
import json
import fal_client

os.environ["FAL_KEY"] = os.environ.get("FAL_KEY", "559d75ba-13dd-416c-9304-a8e89fc077a5:afb75ae80a4a0cbd789be26ddb6ef9cc")
MODEL_ID = "bytedance/seedance-2.5/reference-to-video"

# OFFICIAL SD25-PE COMPILED CATERING & WEDDING DIALOGUE BRIEF
CATERING_WEDDING_30S_BRIEF = (
    "【Generation Goal】 "
    "A continuous 30-second high-end event catering commercial in vertical 9:16 format, ARRI Alexa Mini LF luxury filmic look, 24fps. "
    "Focuses on a stylish Haitian-Quebec couple (Nathalie, 29, elegant dress, and Jean-Marc, 32, tailored jacket) planning a 150-guest wedding and anniversary banquet in Quebec. "
    "【Reference Asset Roles】 "
    "@Image1 is used for the grand catering feast with golden Griot, slow-simmered Lalo, and crispy plantains; do not use the background. "
    "【Event Script & Dialogue】 "
    "[0-8s - The Wedding Tasting Hook]: Camera opens on a warm, elegant banquet room with soft candlelit tables. "
    "Nathalie looks at the menu with anticipation: {Nathalie: \"Pour notre mariage de 150 personnes... je voulais la saveur de chez nous, digne d'un grand banquet.\"} "
    "Jean-Marc smiles proudly as steaming stainless steel chafing dishes are uncovered, revealing the lavish feast from @Image1. <sound: lid opening, rich savory steam release hiss> "
    "[8-18s - The Taste of Home & Culinary Mastery]: Jean-Marc takes a forkful of tender braised meat and fragrant rice: "
    "{Jean-Marc: \"Nathalie, goûte à ça... C'est exactement comme à la maison. Les épices, la tendreté, tout est parfait.\"} "
    "Nathalie tastes the golden crispy Griot with a smile of pure relief and joy: {Nathalie: \"Woy! C'est délicieux... Nos invités vont capoter !\"} <sound: audible crunch of golden crust, happy chuckle> "
    "[18-30s - The Grand Celebration & Kremas Toast]: Camera executes a sweeping 360-degree orbital crane shot revealing a joyful hall full of 100+ dressed-up wedding guests laughing, dancing, and toasting crystal glasses filled with velvety Kremas. "
    "{Jean-Marc: \"Mariage, anniversaire, grand événement... Chef Jude s'occupe de tout.\"} "
    "[music: elegant and uplifting Haitian konpa wedding melody with rich acoustic guitar] <sound: crystal glasses clinking, cheering, festive room applause> "
    "【Maintain Consistency】 "
    "Preserve 100% of the food geometry, rich color, and appetizing texture from @Image1. "
    "Maintain consistent luxury wedding aesthetics, warm amber lighting, and natural French/Haitian dialogue delivery. "
    "Exclude on-screen subtitles and cartoon CGI gloss."
)

def render_catering_commercial(image_path="/Users/instant/Dev/douceurs-lakay/assets/fritay.webp", execute=False):
    print("\n" + "="*80)
    print("👑 SEEDANCE 2.5 // 30-SECOND WEDDING & CATERING DIALOGUE COMMERCIAL")
    print(f"📌 Model: {MODEL_ID}")
    print(f"🎯 Target ICP: Haitian Diaspora & Quebec Event Planners (Weddings / 50th Birthdays / Corpo)")
    print(f"🖼️ Reference Anchor: {image_path}")
    print(f"📐 Aspect Ratio: 9:16 | Duration: 30s | Audio: Native Latent Synced Dialogue")
    print("="*80)
    print(f"\n📝 Production Brief:\n{CATERING_WEDDING_30S_BRIEF}\n")

    if not execute:
        print("💡 Preview Mode. Pass `--execute` to submit to Fal.ai.")
        return

    print("1. Uploading reference asset to Fal.ai CDN...")
    image_url = fal_client.upload_file(image_path)
    print(f"✅ Image URL: {image_url}")

    args = {
        "prompt": CATERING_WEDDING_30S_BRIEF,
        "image_urls": [image_url],
        "aspect_ratio": "9:16",
        "resolution": "720p",
        "generate_audio": True
    }

    print(f"2. Submitting wedding catering brief to {MODEL_ID}...")
    handler = fal_client.submit(MODEL_ID, arguments=args)
    print(f"✅ Dispatched. Request ID: {handler.request_id}")
    print("3. Generating video with synchronized French/Creole wedding dialogue...")
    result = handler.get()
    print("\n🎉 CATERING COMMERCIAL COMPLETE!")
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    import sys
    do_exec = "--execute" in sys.argv
    render_catering_commercial(execute=do_exec)
