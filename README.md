# python_automation
Let's start to automate in Python!

from selene import browser, have, be

browser.config.hold_browser_open = True
browser.config.timeout = 8.0

def login():

    browser.element('.login-form [name=password]').type('password').press_enter()
    browser.open('https://.../system/login')
    browser.element('.login-form [name=email]').type('bot@gmail.com').press_enter()

    browser.element("main-header_login').click()
    browser.element('logined-form").should(have(text('BOT')
