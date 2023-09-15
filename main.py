from internet_speed_twitter_bot import InternetSpeedTwitterBot
from selenium import webdriver
import time

PROMISED_DOWN = 100
PROMISED_UP = 120
TWITTER_USERNAME = ""
TWITTER_PASSWORD = ""

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider(username=TWITTER_USERNAME, password=TWITTER_PASSWORD)
bot.tweet_field.send_keys(f"Hey UC Berkeley, why is my internet speed {bot.down}down/{bot.up}up when I pay for ur stupidly expenisve rent and deserve "
                      f"{PROMISED_DOWN}down/{PROMISED_UP}up")
time.sleep(10)
bot.tweet_button.click()
time.sleep(10)
