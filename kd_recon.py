#!/usr/bin/env python3

import requests
from termcolor import colored
import sys
import os
import re

def banner():
    print(colored(r"""
  _  __ ____       ____                      
 | |/ // ___|  ___|  _ \ ___  ___ ___  _ __  
 | ' / \___ \ / _ \ | | / _ \/ __/ _ \| '_ \ 
 | . \  ___) |  __/ |_| |  __/ (_| (_) | | | |
 |_|\_\|____/ \___|____/ \___|\___\___/|_| |_|

               🔍 KD - Recon Tool 🔍
    """, "cyan", attrs=["bold"]))


def extract_username(input_value):
    match = re.search(r"(?:https?://)?(?:www\.)?instagram\.com/([a-zA-Z0-9._]+)/?", input_value)
    return match.group(1) if match else input_value


def fetch_user_info(username):
    url = f"https://www.instagram.com/{username}/?__a=1&__d=dis"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(colored("❌ Error fetching data. User may not exist or is private.", "red"))
            sys.exit(1)

        json_data = response.json()
        user = json_data["graphql"]["user"]

        print(colored("\n🔍 Instagram Recon Report", "green", attrs=["bold"]))
        print(colored("=================================", "cyan"))
        print(f"👤 Username           : {user['username']}")
        print(f"📛 Full Name          : {user['full_name']}")
        print(f"📝 Bio                : {user['biography']}")
        print(f"✔️ Verified           : {'Yes' if user['is_verified'] else 'No'}")
        print(f"🔒 Private Account    : {'Yes' if user['is_private'] else 'No'}")
        print(f"📍 Followers          : {user['edge_followed_by']['count']}")
        print(f"🔄 Following          : {user['edge_follow']['count']}")
        print(f"📸 Posts              : {user['edge_owner_to_timeline_media']['count']}")
        print(f"🖼️ Profile Pic URL    : {user['profile_pic_url_hd']}")
        print(colored("=================================\n", "cyan"))

    except Exception as e:
        print(colored(f"❌ Error: {e}", "red"))
        sys.exit(1)


if __name__ == "__main__":
    os.system("clear")
    banner()

    if len(sys.argv) != 2:
        print(colored("Usage: python3 kd_recon.py <username_or_instagram_profile_url>", "yellow"))
        sys.exit(1)

    input_value = sys.argv[1]
    username = extract_username(input_value)
    fetch_user_info(username)
