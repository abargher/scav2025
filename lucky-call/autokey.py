from time import sleep
import pyautogui as p

p.keyDown("command")
p.press("space")
p.keyUp("command")
p.write("chrome")
p.press("enter")
p.keyDown("command")
p.press("t")
p.keyUp("command")

number = "12027621401"
url = f"https://voice.google.com/u/0/calls?a=nc,%2B{number}"
p.write(url)
p.press("enter")
sleep(1.5)
p.press("enter")
sleep(2.0)
p.keyDown("command")
p.press("w")
p.keyUp("command")
p.press("enter")

