# Lucky Call notes (item 84)

A corded telephone that call the office of a random U.S. House Representative
when you dial "777".

- 777 detected by raspberry pi zero w script on GPIO pins
- Once dialed, select a random phone number from the list
- Then, plug it into the Google Voice call URL
- Open the URL with Selenium
    - PROBLEM: Selenium browser must be logged in to Google
    - SOLUTION: Use a logged-in Chrome profile (see here
        https://stackoverflow.com/a/62244793)

- Speaker of phone is hooked up as speaker, mic as mic

