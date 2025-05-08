from selenium import webdriver
from selenium_stealth import stealth
import time
import sys

def main(argv: list[str]) -> None:

    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")

    # options.add_argument("--headless")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("user-data-dir=/Users/alec/Library/Application Support/Google/Chrome")
    options.add_argument("--disable-web-security")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument('--profile-directory=Default')
    driver = webdriver.Chrome(options=options)

    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

    number = "12027621401"
    driver.get(f"https://voice.google.com/u/0/calls?a=nc,%2B{number}")

    while True:
        pass

if __name__ == "__main__":
    main(sys.argv)

