#!/bin/bash
set -e
apt-get update && apt-get install -y --no-install-recommends python3 python3-pip python3-venv && rm -rf /var/lib/apt/lists/*
pip3 install fastapi==0.110.0 uvicorn==0.27.1
