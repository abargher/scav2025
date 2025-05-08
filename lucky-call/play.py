from time import sleep
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    profile_dir = "/Users/alec/Library/Application Support/Firefox/Profiles/pfr87xer.default"
    browser = p.firefox.launch_persistent_context(
        user_data_dir=profile_dir,
        headless=False,
    )
    page = browser.new_page()
    page.goto("https://playwright.dev")
    print(page.title())
    while True:
        pass
    browser.close()
