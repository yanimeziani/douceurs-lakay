#!/usr/bin/env bash
# Deploy script to sync Douceurs Lakay landing page to VPS
set -e

VPS_HOST="${1:-2.24.70.132}"
SSH_KEY="${HOME}/.ssh/id_ed25519"
TARGET_DIR="/docker/douceurs-lakay/html/"

echo "🚀 Deploying Douceurs Lakay to root@${VPS_HOST}:${TARGET_DIR}..."

# Sync files (excluding env, git, and caches)
rsync -avz --delete \
  -e "ssh -i ${SSH_KEY} -o StrictHostKeyChecking=accept-new" \
  --exclude '.env' \
  --exclude '.git' \
  --exclude 'facebook_videos' \
  --exclude '__pycache__' \
  --exclude '.DS_Store' \
  /Users/instant/Dev/douceurs-lakay/ "root@${VPS_HOST}:${TARGET_DIR}"

echo "✅ Deployment successful! Douceurs Lakay is live on your VPS."
