#!/usr/bin/env python3
"""
Seedance 2.5 - 30-Second Quebec Lifestyle Commercial (Fal.ai)
No talking-head dialogues. Focuses on authentic Quebec / FR-CA characters enjoying a warm Douceurs Lakay feast,
sensory food ASMR, and festive community sharing.
"""

import os
import json
import fal_client

# Ensure API key is loaded
api_key = os.environ.get("FAL_KEY", "66211860-0032-48a1-9f47-fb19e23c403e:aae38f4e9045b37d1952dbfe79ea669c")
os.environ["FAL_KEY"] = api_key

# 30-SECOND SEEDANCE 2.5 MASTER PROMPT (FR-CA QUEBEC CHARACTERS & SENSORY FEAST)
SEEDANCE_30S_PROMPT_FR_CA = (
    "A continuous 30-second cinematic lifestyle and culinary commercial in vertical 9:16 format, 24fps filmic color grade. "
    "NO TALKING TO CAMERA, pure sensory action and authentic human interaction. "
    "[0:00-0:10 - The Sizzle & Searing Heat]: Extreme macro 24mm lens, slow dynamic push-in. "
    "Golden seasoned Griot pork sizzling violently in a black cast-iron pan with curling aromatic steam and brief amber flames. "
    "Double-fried yellow plantains (bananes pesées) emerging crispy from hot oil, fresh lime juice squeezing in micro-droplets. "
    "[0:10-0:20 - The Unboxing & First Bite in Quebec]: Seamless camera transition into a cozy, warmly lit Quebec apartment dining room. "
    "A diverse group of cheerful 20s-30s friends gathering around a wooden table as steaming hot Douceurs Lakay takeout boxes are opened. "
    "A smiling young woman in a cozy sweater takes a crispy, crunchy bite of golden Griot topped with vibrant spicy pikliz, her eyes lighting up in pure delight. "
    "[0:20-0:30 - The Festive Toast & Community Energy]: Camera sweeps across the joyful table. "
    "Friends clinking glasses filled with velvety thick Kremas, laughing and sharing food with generous hands, warm evening amber lighting. "
    "Atmospheric depth of field, photorealistic steam, natural candid facial expressions, rich appetizing food textures. "
    "--no talking head, no speech monologue to camera, no plastic CGI skin, no morphing geometry, no artificial glow"
)

def run_30s_generation(image_reference=None):
    print("\n" + "="*75)
    print("🎬 SEEDANCE 2.5 // 30-SECOND QUEBEC (FR-CA) LIFESTYLE COMMERCIAL")
    print("📐 Format: Vertical 9:16 | Duration: 30 Seconds | Engine: Fal.ai")
    print("="*75)
    print(f"\n📝 Master Prompt (No Dialogue / Authentic FR-CA Characters):\n{SEEDANCE_30S_PROMPT_FR_CA}\n")

    args = {
        "prompt": SEEDANCE_30S_PROMPT_FR_CA,
        "resolution": "1080p",
        "aspect_ratio": "9:16",
        "duration": "30"
    }

    model = "bytedance/seedance-2.0/text-to-video"

    if image_reference and os.path.exists(image_reference):
        print(f"🖼️ Anchoring with reference image: {image_reference}")
        img_url = fal_client.upload_file(image_reference)
        args["image_url"] = img_url
        model = "bytedance/seedance-2.0/image-to-video"

    print("🚀 Submitting 30-second render to Fal.ai...")
    try:
        handler = fal_client.submit(model, arguments=args)
        result = handler.get()
        print("✅ 30-Second Video Rendered Successfully!")
        print(json.dumps(result, indent=2))
        return result
    except Exception as e:
        print(f"❌ Execution Note: {e}")
        return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--execute":
        run_30s_generation(image_reference="/Users/instant/Dev/douceurs-lakay/assets/fritay.webp")
    else:
        print("✨ Seedance 30-Second FR-CA Commercial Ready!")
        print("Run with `python3 seedance_30s_commercial.py --execute` to trigger rendering on Fal.ai.")
