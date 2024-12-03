#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Path to your virtual environment
VENV_DIR=".venv"

# Check if the virtual environment exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Virtual environment not found. Creating one..."
    # Create the virtual environment
    python -m venv "$VENV_DIR"
    echo "Virtual environment created."

    # Activate the virtual environment
    source "$VENV_DIR/Scripts/activate"

    # Install the requirements
    if [ -f "requirements.txt" ]; then
        echo "Installing dependencies..."
        pip install -r requirements.txt
        echo "Dependencies installed."
    else
        echo "Error: 'requirements.txt' not found!"
        exit 1
    fi
else
    # Activate the virtual environment
    source "$VENV_DIR/Scripts/activate"
    echo "Virtual environment activated."
fi

# Navigate to the app directory
if [ -d "app" ]; then
    cd app || { echo "Error: Failed to navigate to 'app' directory!"; exit 1; }
else
    echo "Error: 'app' directory not found!"
    exit 1
fi

# Run the Python script
if [ -f "main.py" ]; then
    python main.py
else
    echo "Error: 'main.py' not found in 'app' directory!"
    exit 1
fi
