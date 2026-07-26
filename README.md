# tiktok-streak-hero
## 📖 The Backstory  Legend has it that a 100+ day TikTok streak was lost due to negligence.   To redeem myself and restore honor to the group chat, I built this script to automate and safeguard future streaks so nobody ever loses a 100-day streak again.


**Automated Activity:** Runs daily so you never miss a streak window.
* ⏰ **Hands-Off Scheduling:** Integrates with Windows Task Scheduler for 100% automation.
* ⚙️ **Simple Config:** Uses session cookies to manage authentication easily.


#### How to Export Your Cookies:

1. **Log in to TikTok** in your web browser (Chrome, Firefox, or Edge).
2. Install a trusted cookie exporter extension, such as **Get cookies.txt LOCALLY** or **Cookie-Editor**.
3. Open the extension while on `tiktok.com` and export your cookies in **JSON** format.
4. Rename the exported file to **`cookies.json`**.
5. Move `cookies.json` into the main folder of this project (the same folder where `local_streak.py` is located).


#### Setup Instructions for automation:
1.Press Win + R, type taskschd.msc, and press Enter.

2.On the right panel, click Create Basic Task...

3.Name: Give it a name like TikTok Streak Bot.

4.Trigger: Select Daily and choose a time (e.g., 9:00 AM every day). (I recommend setting up multiple time so you dont miss it when your computer isnt opened at certain time.)

5.Action: Select Start a program.

6.Program/script: Click Browse... and select your run_bot.bat file.

7.Start in (optional): Important! Paste the full path to your project folder here (e.g., C:\Users\YourName\Projects\tikstreak). This ensures the script can find your cookies.json file when running automatically.

8.Click Finish.


#### MAKE SURE YOUR FOLDERS ARE MATCHED IN THE RUN_BOT.BAT FILE DO NOT JUST SIMPLY COPY MINE, ITS JUST AN EXAMPLE.

This is what it looks like in the terminal when running the script.
<img width="643" height="367" alt="image" src="https://github.com/user-attachments/assets/1ca1814e-b6af-44a2-864a-99d817d40cfb" />


