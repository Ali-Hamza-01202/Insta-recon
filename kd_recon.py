#!/usr/bin/env python3

import os
import sys
from termcolor import colored
import instaloader
import re

def banner():
    print(colored("╔═══════════════════════════════════════╗", "cyan", attrs=["bold"]))
    print(colored("║        🔍 KD Instagram Recon Tool     ║", "cyan", attrs=["bold"]))
    print(colored("╚═══════════════════════════════════════╝", "cyan", attrs=["bold"]))


def extract_username(input_value):
    match = re.search(r"(?:https?://)?(?:www\.)?instagram\.com/([a-zA-Z0-9._]+)/?", input_value)
    return match.group(1) if match else input_value


def fetch_instagram_user(username):
    try:
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(loader.context, username)

        print(colored("\n🔍 Instagram Recon Report", "green", attrs=["bold"]))
        print(colored("=================================", "cyan"))
        print(f"👤 Username           : {profile.username}")
        print(f"📛 Full Name          : {profile.full_name}")
        print(f"📝 Bio                : {profile.biography}")
        print(f"✔️ Verified           : {'Yes' if profile.is_verified else 'No'}")
        print(f"🔒 Private Account    : {'Yes' if profile.is_private else 'No'}")
        print(f"📍 Followers          : {profile.followers}")
        print(f"🔄 Following          : {profile.followees}")
        print(f"📸 Posts              : {profile.mediacount}")
        print(f"🖼️ Profile Pic URL    : {profile.profile_pic_url}")
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
    fetch_instagram_user(username)
