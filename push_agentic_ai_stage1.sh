#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Navigate to the project directory
cd "$(dirname "$0")"

# Initialize git if not already initialized
if [ ! -d ".git" ]; then
  git init
  git branch -M main
  git remote add origin https://github.com/SidNirmal-DS/agentic-ai-stage-1.git
fi

# Stage all files
git add .

# Commit changes
git commit -m "Pushing all agentic AI stage 1 files"

# Push to GitHub
git push -u origin main
