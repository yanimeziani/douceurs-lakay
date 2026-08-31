#!/usr/bin/env python3
"""
Seedance 2.5 Reference-to-Video Engine (BytePlus ModelArk Standard)
Model: bytedance/seedance-2.5/reference-to-video
Engineered with:
- Omni-Reference visual anchoring
- Multi-Timestamp choreography (0-8s, 8-18s, 18-30s)
- Native Latent Audio cues (<sound: ...>, [music: ...])
- BytePlus Consistency Blocks
"""

import os
import sys
import argparse
import json
import fal_client

os.environ["FAL_KEY"] = os.environ.get("FAL_KEY", "559d75ba-13dd-416c-9304-a8e89fc077a5:afb75ae80a4a0cbd789be26ddb6ef9cc")
MODEL_ID = "bytedance/seedance-2.5/reference-to-video"

# Master BytePlus-Compliant 30s Production Brief
BYTEPLUS_30S_BRIEF = (
    "[0-8s - Cast Iron Ignition]: Low-angle 24mm macro dolly-in following rising steam toward the golden Griot pork from Image 1 sizzling in a heavy cast-iron skillet. "
    "Aromatic oil crackling, amber sparks dancing under warm key light. "
    "<sound: violent cast-iron sizzling, explosive searing crackle, rising steam hiss> "
    "[8-18s - Through-Steam Transition & The Quebec Feast]: Camera moves through the steam into a warm, candlelit Quebec City apartment dining room. "
    "A cheerful group of 20s-30s friends gathering around the steaming Douceurs Lakay catering box. "
    "A smiling young woman takes a crunchy bite of Griot with pikliz, eyes widening with spontaneous joy. "
    "<sound: audible crisp crunch of golden crust, warm room laughter, enthusiastic chatter> "
    "[18-30s - Swirling Toast & Climax]: Camera executes a smooth 360-degree orbital crane rising above the table. "
    "Thick, velvety Haitian Kremas pours into crystal glasses with airborne cinnamon dust, friends clinking glasses and sharing food. "
    "[music: warm rhythmic acoustic compas groove with mellow bass] <sound: crystal glasses clinking, happy shared laughter> "
    "[Consistency Block]: Preserve 100% of the food geometry, golden-brown color, and texture of the Griot from Image 1. "
    "Maintain consistent warm amber lighting. Exclude on-screen text, cartoon CGI gloss, and geometric morphing."
)

def render_seedance_25_brief(image_path="/Users/instant/Dev/douceurs-lakay/assets/griot.jpg", custom_prompt=None, aspect_ratio="9:16", resolution="720p"):
    prompt = custom_prompt or BYTEPLUS_30S_BRIEF
    
    print("\n" + "="*80)
    print(f"🎬 SEEDANCE 2.5 // BYTEPLUS MODELARK PRODUCTION BRIEF")
    print(f"📌 Model: {MODEL_ID}")
    print(f"🖼️ Reference Anchor: {image_path}")
    print(f"📐 Aspect Ratio: {aspect_ratio} | Resolution: {resolution} | Latent Audio: Active")
    print("="*80)
    print(f"\n📝 Production Brief:\n{prompt}\n")

    if not os.path.exists(image_path):
        print(f"❌ Error: Asset not found: {image_path}")
        return None

    print("1. Uploading reference asset to Fal.ai CDN...")
    image_url = fal_client.upload_file(image_path)
    print(f"✅ Uploaded CDN URL: {image_url}")

    args = {
        "prompt": prompt,
        "image_urls": [image_url],
        "aspect_ratio": aspect_ratio,
        "resolution": resolution,
        "generate_audio": True
    }

    print(f"2. Submitting production brief to {MODEL_ID}...")
    handler = fal_client.submit(MODEL_ID, arguments=args)
    print(f"✅ Job Dispatched. Request ID: {handler.request_id}")
    print("3. Generating video + latent audio on ByteDance cluster...")
    result = handler.get()
    print("\n🎉 GENERATION COMPLETE!")
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Seedance 2.5 BytePlus Director")
    parser.add_argument("--image", type=str, default="/Users/instant/Dev/douceurs-lakay/assets/griot.jpg")
    parser.add_argument("--prompt", type=str, default=None)
    parser.add_argument("--aspect", type=str, default="9:16")
    parser.add_argument("--resolution", type=str, default="720p", choices=["720p", "1080p"])
    parser.add_argument("--execute", action="store_true")

    args = parser.parse_args()

    if args.execute:
        render_seedance_25_brief(args.image, args.prompt, aspect_ratio=args.aspect, resolution=args.resolution)
    else:
        print(f"🔒 BytePlus ModelArk Seedance 2.5 Brief Ready!")
        print(f"Run with `--execute` to submit to Fal.ai.")
