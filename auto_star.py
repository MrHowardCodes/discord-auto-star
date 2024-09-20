from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

email = "email@domain.com"
pw = "_your_discord_pw"

PATH = "path_to_your_chromedriver"
driver = webdriver.Chrome(PATH)
driver.get('https://discord.com/channels/xxxxxxxxxxxxxxx/xxxxxxxxxxxxx')
login_btn = driver.find_element_by_css_selector("[type=submit]")
fill_email = driver.find_element_by_css_selector("[type=email]")
fill_pw = driver.find_element_by_css_selector("[type=password]")
message = "!d bump"


def login():
    fill_email.send_keys(email)
    fill_pw.send_keys(pw)
    login_btn.click()
    time.sleep(10)


def msg():
    while True:
        xpaths = {
            'textArea': "//*[@id=\"app-mount\"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div",
            'submitMessage': "//*[@id=\"app-mount\"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div/button"
        }
        driver.find_element_by_xpath(xpaths['textArea']).send_keys(message, Keys.ENTER)
        time.sleep(7200)


login()
msg()
