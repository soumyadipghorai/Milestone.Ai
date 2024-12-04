#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Navigate to the app directory
if [ -d "app" ]; then
    cd app || { echo "Error: Failed to navigate to 'app' directory!"; exit 1; }
else
    echo "Error: 'app' directory not found!"
    exit 1
fi

# Run the Python script
if [ -f "main.py" ]; then
    echo "Starting the app..."
    python main.py
else
    echo "Error: 'main.py' not found in 'app' directory!"
    exit 1
fi
