# Skyblock Profile Telegram Bot

A simple Telegram bot that displays Hypixel SkyBlock player stats and Minecraft profile avatars

## Features

View SkyBlock player skill levels directly in Telegram  
Display Minecraft profile avatars
Uses Hypixel API and Telegram Bot API

## Local installation

### Requirements

- Python 3.11+
- Git

### Step 1: Clone the repository

```bash
git clone https://github.com/F3NCE-Dev/hypixel-skyblock-profile-viewer-telegram-bot
cd hypixel-skyblock-profile-viewer-telegram-bot
```

### Step 2: Install requirements.txt

Create a venv

```bash
python -m venv venv

source venv/bin/activate # for Linux/Mac
# or
venv/Scripts/activate # for windows
```

Install the requirements

```bash
pip install -r requirements.txt
```

### Step 3: Create a file named *.env*

```bash
echo "" > .env
```

Add  required variables

Example:

```bash
BOT_API="your bot api"
HYPIXEL_API="your hypixel api"
```

### Step 4: Run the bot

```bash
python main.py