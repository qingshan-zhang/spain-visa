import time
import telebot
from utils import config
from utils.log import logger
from visa import Visa
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from twilio.rest import Client

bot = telebot.TeleBot(config.BOT_TOKEN)
account_sid = 'ACbac6b43eb1f4589950aaa758c57e62bc'
auth_token = '4f7cc141d296203a470f7f0400eb1504'
client = Client(account_sid, auth_token)

def init_driver():
    profile = {
        "profile.default_content_setting_values.notifications": 2  # block notifications
    }
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('prefs', profile)

#     chrome_options.add_argument("--user-data-dir=/Users/qzhang/Library/Application Support/Google/Chrome")
#     driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.implicitly_wait(1)
    return driver


def monitor():
    try:
        driver = init_driver()
        visa = Visa(driver)
        visa.go_to_appointment_page()
        visa.login()
        visa.go_to_book_appointment()
        visa.select_centre('Greater London', 'London', 'Normal')
        while True:
            dates = visa.check_available_dates()
            if dates:
                logger.info(f"DAY AVAILABLE: {dates}")
#                 bot.send_message(chat_id=config.CHAT_ID, text=f'DAY AVAILABLE: {dates}')
                client.messages.create(body=f'DAY AVAILABLE: {dates}', from_='MG8a1a180d040f10a5ea32db50089c07b5', to='+447920206756')
                # driver.back()
            else:
                logger.info(f"NO DAY AVAILABLE..")
                time.sleep(config.TIMEOUT)
                driver.refresh()

    except Exception as e:
        logger.error(f'Monitor runtime error. {e}')
#         monitor()


def test_notify():
    try:
        dates = {'sth'}
        client.messages.create(body=f'DAY AVAILABLE: {dates}', from_='MG8a1a180d040f10a5ea32db50089c07b5', to='+447920206756')
    except Exception as e:
        logger.error(
            f'Test notify error. please make sure that you\'ve sent a message to wongs_bot if you didn\'t change the CHAT_ID in the config.\n\n {e}')
        exit(0)


if __name__ == "__main__":
#     test_notify()
    monitor()
