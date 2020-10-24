# -*- coding: utf-8 -*-

from selenium import webdriver
import config
from selenium.webdriver.support.ui import WebDriverWait

class Bot:
    """Bor for game gladiatus"""
    def __init__(self):
        self.url=config.url_login_page_gladiatus
        self.bot = webdriver.Chrome()
        self.bot.implicitly_wait(10)
    
    def open(self):
        """goto start url"""
        self.bot.get(self.url)
        print('bot started')
        print(f'bot goto url {self.url}')


    def quit(self):
        """Stoped webdriver"""
        self.bot.quit()#exit from webdriver
        print('bot stoped')