import os
from internet_speed_twitter_bot import InternetSpeedTwitterBot

at_company = '@vivobr'
PROMISE_DOWN = 200
PROMISED_UP = 120
CHROME_DRIVER_PATH = "C:\DevTools\chromedriver\chromedriver.exe"
TWITTER_EMAIL = os.getenv('PY_EMAIL')
TWITTER_PASSWORD = os.getenv('PY_EMAIL_PASSWORD')

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
internet_speed = bot.get_internet_speed()
bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD, PROMISE_DOWN, PROMISED_UP, at_company)