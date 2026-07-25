import asyncio
import random
import datetime
import json
import os
from playwright.async_api import async_playwright

# ==================== CONFIGURATION ====================
EMOJI_POOL = ["🔥", "⚡", "💯", "😎", "👾", "✨", "🚀"]
TARGET_NAMES = ["rein", "ireach"]
TRACKER_FILE = "last_run.txt"
# =======================================================

def already_ran_today():
    """Checks if the script has already run successfully today."""
    if os.path.exists(TRACKER_FILE):
        with open(TRACKER_FILE, "r") as f:
            last_date = f.read().strip()
            today = datetime.date.today().strftime("%Y-%m-%d")
            return last_date == today
    return False

def mark_as_ran_today():
    """Saves today's date so the script knows it finished successfully."""
    with open(TRACKER_FILE, "w") as f:
        today = datetime.date.today().strftime("%Y-%m-%d")
        f.write(today)

async def send_streak_to_friend(page, name):
    try:
        print(f"\nNavigating to messages inbox...")
        await page.goto("https://www.tiktok.com/messages", wait_until="networkidle")
        await asyncio.sleep(5.0)

        print(f"Searching for chat row named: '{name}'")
        name_element = page.get_by_text(name, exact=True).first
        
        if await name_element.count() > 0 and await name_element.is_visible():
            print(f"🎯 Found element for '{name}'! Clicking directly...")
            await name_element.click(force=True)
            await asyncio.sleep(3.0)
            
            text_box_selector = 'div[role="textbox"]'
            await page.wait_for_selector(text_box_selector, timeout=5000)
            await page.click(text_box_selector)
            
            num_emojis = random.randint(1, 3)
            chosen_emojis = "".join(random.choices(EMOJI_POOL, k=num_emojis))
            
            await page.type(text_box_selector, chosen_emojis, delay=120)
            await asyncio.sleep(1.0)
            await page.keyboard.press("Enter")
            
            print(f"✅ Streak sent to {name}: {chosen_emojis}")
            return True # Success
        else:
            print(f"❌ Could not find a chat element matching '{name}' on screen.")
            return False
            
    except Exception as e:
        print(f"⚠️ Error running tasks for {name}: {e}")
        return False

async def main():
    # 🛡️ THE GATEKEEPER: Instantly exit if already done today
    if already_ran_today():
        print(f"\n🛑 Streaks were already sent today! Exiting to prevent duplicate run.")
        return

    if not os.path.exists("cookies.json"):
        print("Error: cookies.json not found in this folder!")
        return

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        
        with open("cookies.json", "r") as f:
            cookies = json.load(f)
            for cookie in cookies:
                if 'sameSite' in cookie and cookie['sameSite'] is not None:
                    cookie['sameSite'] = str(cookie['sameSite']).replace('_', '').capitalize()
                    if cookie['sameSite'] not in ["Strict", "Lax", "None"]:
                        cookie['sameSite'] = "None"
                else:
                    cookie['sameSite'] = "None"

        await context.add_cookies(cookies)
        page = await context.new_page()

        print("\n--- STARTING STREAK RUN ---")
        overall_success = True
        
        for name in TARGET_NAMES:
            success = await send_streak_to_friend(page, name)
            if not success:
                overall_success = False
            await asyncio.sleep(random.uniform(3.0, 6.0))
            
        print("\n--- ALL STREAKS SENT ---")
        
        # Only lock out the day if it actually managed to send them
        if overall_success:
            mark_as_ran_today()
            print("📝 Success logged. The script won't run again until tomorrow.")
        
        await asyncio.sleep(3.0)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())