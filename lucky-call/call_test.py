import sys
from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def launch_call(browser, number: str) -> None:
    browser.set_page_load_timeout(10.0)
    try:
        browser.get(f"https://voice.google.com/u/0/calls?a=nc,%2B{number}")
    except:
        print("failed to get call URL")


def main(argv: list[str]) -> None:
    service = ChromeService(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()

    chrome_options.add_argument("user-data-dir=~/.config/google-chrome")

    browser = webdriver.Chrome(service=service, options=options)

    launch_call(browser, "2027621401")

if __name__ == "__main__":
    main(sys.argv)

