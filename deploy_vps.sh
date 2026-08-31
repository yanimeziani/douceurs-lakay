#!/usr/bin/env bash
# Quick deploy script to sync Douceurs Lakay landing page to VPS
set -e

VPS_IP="${1}"

if [ -z "$VPS_IP" ]; then
  echo "Usage: ./deploy_vps.sh <VPS_IP_OR_HOSTNAME>"
  echo "Example: ./deploy_vps.sh 123.45.67.89"
  exit 1
fi

echo "🚀 Deploying Douceurs Lakay landing page to root@${VPS_IP}:/var/www/douceurs-lakay..."

# Create directory on VPS
ssh -o StrictHostKeyChecking=no "root@${VPS_IP}" "mkdir -p /var/www/douceurs-lakay"

# Sync files (excluding env and git)
rsync -avz --delete \
  --exclude '.env' \
  --exclude '.git' \
  --exclude 'facebook_videos' \
  --exclude '__pycache__' \
  /Users/instant/Dev/douceurs-lakay/ "root@${VPS_IP}:/var/www/douceurs-lakay/"

echo "✅ Deployment successful! Landing page is live on your VPS."
