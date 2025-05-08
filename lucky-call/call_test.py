import sys
import time
from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



def launch_call(browser, number: str) -> None:
    browser.set_page_load_timeout(10.0)
    try:
        browser.get("https://accounts.google.com/signin")
        browser.get(f"https://voice.google.com/u/0/calls?a=nc,%2B{number}")
    except:
        print("failed to get call URL")

    while True:
        pass


def main(argv: list[str]) -> None:
    """
    service = ChromeService(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()

    options.add_argument("user-data-dir=/Users/alec/Library/Application Support/Google/Chrome")
    options.add_argument("--disable-web-security")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument('--profile-directory=Default')

    browser = webdriver.Chrome(service=service, options=options)
    """

    options = Options()
    firefox_profile = FirefoxProfile("/Users/alec/Library/Application Support/Firefox/Profiles/3dvx3lug.default-release")
    firefox_profile.set_preference("javascript.enabled", False)
    firefox_profile.set_preference("dom.webdriver.enabled", False)
    firefox_profile.set_preference('useAutomationExtension', False)
    firefox_profile.update_preferences()
    options.profile = firefox_profile
    desired = DesiredCapabilities.FIREFOX

    browser = webdriver.Firefox(options=options)
    launch_call(browser, "12027621401")

if __name__ == "__main__":
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print("\nbye!")

