from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import getpass
from selenium.webdriver.common.keys import Keys
import os
from time import sleep


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.down = 0
        self.up = 0
        self.driver.maximize_window()

    def get_internet_speed(self):
        btn_path = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]'
        dow_path = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]' \
                   '/div[1]/div[2]/div/div[2]/span'
        up_path ='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]' \
                '/div[1]/div[3]/div/div[2]/span'

        self.driver.get('https://www.speedtest.net')
        btn = self.driver.find_element_by_xpath(btn_path)
        btn.click()
        sleep(65)
        down_speed = self.driver.find_element_by_xpath(dow_path).text
        up_speed = self.driver.find_element_by_xpath(up_path).text
        self.down = float(down_speed)
        self.up = float(up_speed)

    def tweet_at_provider(self, email, password, paid_down, paid_up, at_company):
        input_email_path ='//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div[1]/div/form/div/div[1]' \
                          '/div/label/div/div[2]/div/input'
        input2_email_path ='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]' \
                           '/div/input'

        input_password_path = '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div[1]/div/form/div/div[2]' \
                              '/div/label/div/div[2]/div/input'
        input2_password_path = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]' \
                               '/label/div/div[2]/div/input'

        btn_login_path = '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div[1]/div/form/div/div[3]/div'
        btn2_login_path = '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]'
        btn3_login_path ='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div'

        btn_twit_path = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a'

        div_twit_path = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]' \
                        '/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]' \
                        '/div'

        btn_tweet_path = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]' \
                         '/div/div/div/div/div[2]/div[4]/div/div/div[2]/div[4]'

        message = f"Olá, {at_company}. Eu gostaria de saber o porquê da minha velocidade" \
                  f" de internet está como {self.down}down/{self.up}up quando eu pago por {paid_down}down/{paid_up}up"

        print(self.up, self.down)
        self.driver.get('https://twitter.com')
        sleep(3)
        try:
            input_email = self.driver.find_element_by_xpath(input_email_path)
            input_email.send_keys(email)
            input_password = self.driver.find_element_by_xpath(input_password_path)
            input_password.send_keys(password)
            btn_login = self.driver.find_element_by_xpath(btn_login_path)
            btn_login.click()
        except NoSuchElementException:
            btn2_login = self.driver.find_element_by_xpath(btn2_login_path)
            btn2_login.click()
            input2_email = self.driver.find_element_by_xpath(input2_email_path)
            input2_email.send_keys(email)
            input2_password = self.driver.find_element_by_xpath(input2_password_path)
            input2_password.send_keys(password)
            btn3_login = self.driver.find_element_by_xpath(btn3_login_path)
            btn3_login.click()
        sleep(1.5)
        btn_twit = self.driver.find_element_by_xpath(btn_twit_path)
        btn_twit.click()
        sleep(0.5)
        div_twit = self.driver.find_element_by_xpath(div_twit_path)
        div_twit.click()
        div_twit.send_keys(f'{message}')
        btn_tweet = self.driver.find_element_by_xpath(btn_tweet_path)
        btn_tweet.click()

