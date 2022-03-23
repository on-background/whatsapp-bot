# Whatsapp-bot
Tool to automate the sending of messages on WhatsApp. 
The code can be easily editable to make it a permanent chatbot (remove the logout at the end) or a message broadcasting tool (use a list of contacts instead of just one).
The message sending loop could also be changed to modify its shape.

**IMPORTANT**: This tool was tested and developed for Firefox 97.0. In order to use it with Chrome, it is necessary to change the driver in the source code.

## Arguments
- -t: target - Contact or group name 
- -m: message - Message that you want to send to target n-times (accepts NON-ASCII characters p.e. emojis)
- -n: number - Number of messages that you want to send

## Usage
If you want to send 2 "hello" messages to the conversation called "Tests": 
  - python3 whatsapp_bot.py -t Test -m hello -n 2

If you want send 999 "PRANK!" messages to the group called "Friends": 
  - python3 whatsapp_bot.py -t Friends -m PRANK! -n 999

## Dependencies
- *Selenium*: pip install selenium
- *Geckodriver*: @https://www.guru99.com/gecko-marionette-driver-selenium.html

