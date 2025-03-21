#!/bin/bash

# Install Python
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.10
sudo apt install -y python3.10-venv

# Create virtual environment
python3.10 -m venv .venv

# Activate virtual environment and install dependencies
source .venv/bin/activate
pip install matplotlib nltk streamlit tensorflow tf-keras transformers 
pip list --format=freeze > requirements.txt

# Start the app
streamlit run app.py --server.port 8000
