#!/bin/bash

# LandWise Obsidian Vault — Auto-Commit Script
# Automatically commits vault changes to git with timestamp

set -e

VAULT_PATH="/Users/shaunducker/Desktop/LandWise/Obsidian-Vault"
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
COMMIT_MSG="Vault auto-update: $TIMESTAMP"

if [ ! -d "$VAULT_PATH/.git" ]; then
    echo "ERROR: Vault is not a git repository"
    exit 1
fi

cd "$VAULT_PATH"

# Check if there are changes
if ! git diff-index --quiet HEAD --; then
    echo "Committing vault changes..."
    git add -A
    git commit -m "$COMMIT_MSG"
    echo "✓ Committed: $COMMIT_MSG"
else
    echo "No changes to commit"
fi
