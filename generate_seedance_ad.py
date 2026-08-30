#!/usr/bin/env python3
"""
Douceurs Lakay - Seedance 2.5 AI Video Ad Generator via Fal.ai
Automates performance UGC and cinematic food ad generation for TikTok / Instagram Reels / Facebook.
"""

import os
import sys
import json
import fal_client

# Ensure FAL_KEY is available
api_key = os.environ.get("FAL_KEY", "66211860-0032-48a1-9f47-fb19e23c403e:aae38f4e9045b37d1952dbfe79ea669c")
os.environ["FAL_KEY"] = api_key

def generate_video_ad(prompt, image_path=None, model="bytedance/seedance-2.0/text-to-video"):
    print(f"🎬 Initiating Seedance generation with model: {model}")
    print(f"📝 Prompt: {prompt}\n")

    arguments = {
        "prompt": prompt,
        "resolution": "1080p",
        "aspect_ratio": "9:16"
    }

    if image_path and os.path.exists(image_path):
        print(f"🖼️ Uploading reference image: {image_path}")
        image_url = fal_client.upload_file(image_path)
        arguments["image_url"] = image_url
        model = "bytedance/seedance-2.0/image-to-video"

    try:
        print("⏳ Submitting task to Fal.ai...")
        handler = fal_client.submit(model, arguments=arguments)
        result = handler.get()
        print("✅ Generation Complete!")
        print(json.dumps(result, indent=2))
        return result
    except Exception as e:
        print(f"❌ Error during generation: {e}")
        return None

if __name__ == "__main__":
    # High converting prompt for Douceurs Lakay Griot
    sample_prompt = (
        "Smartphone selfie video, vertical 9:16, natural handheld camera. A friendly customer in Quebec holding "
        "a steaming hot takeout box of authentic Haitian golden crispy Griot pork and yellow fried plantains (banane pesée). "
        "They pick up a golden crispy piece of pork with spicy pikliz on top, take a bite with pure delight and excitement, "
        "smiling at the camera with authentic natural expressions. Cozy warm indoor lighting, realistic phone camera texture."
    )
    
    if len(sys.argv) > 1 and sys.argv[1] == "--run":
        generate_video_ad(sample_prompt, image_path="/Users/instant/Dev/douceurs-lakay/assets/griot.jpg")
    else:
        print("💡 Seedance 2.5 Ad Pipeline configured!")
        print("Run with `--run` to trigger generation, or call `generate_video_ad(prompt, image_path)`.")
