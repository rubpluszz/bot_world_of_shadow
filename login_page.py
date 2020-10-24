# -*-coding: utf-8 -*-
import time
from selenium import webdriver
from bot import Bot
from locators import StartPageLocators as LOCATORS
from save_errors import add_new_record_in_table as record_error
from locators import AutorizationWithSocialNetwork

class StartPage(Bot):


    def __init__(self):
        Bot.__init__(self)

    
    def start_new_game(self):#click to button "Новая игра"
        """Use this method to start  new game without used social network or login"""
        try:
            self.bot.find_element(*LOCATORS.START_GAME).click()
            print("Button 'Новая игра' clicked")
        except Exception as e:
            print("Button 'Новая игра' is not clicked\n e==", e)
            record_error("start_page.StartPage.start_new_game", str(e))


    def login_user(self, login, password):
        """login user - логування корристувача з акаунтом
           click button 'Войти' and enter login, password"""
        try:
            print("Start logging in with a login and password")
            self.bot.find_element(*LOCATORS.LOGIN).click()#click to button "Войти"
            print('clicked to button "Войти"')
            self.bot.find_element(*LOCATORS.ENTER_LOGIN).send_keys(login)#enter login
            self.bot.find_element(*LOCATORS.ENTER_PASSWORD).send_keys(password)#enter password
            self.bot.find_element(*LOCATORS.AKCEPT_LOGIN_AND_PASSWORD).click()#clicked submit
            print("logging data entry is complete")
            if self.bot.find_element(*LOCATORS.FEEDBACK_PANEL_ERROR):
                print("Logined data is file...\nPlease check your login data before restarting...")
                record_error("start_page.StartPage.login_user", 'Not corect logging data')
                self.quit()
        except Exception as e:
            print("Filed entry logined data\n e==", e)
            record_error("start_page.StartPage.login_user", str(e))


    def logined_with_vk(self, login, password):#Login it's e-mail or phone number 
        """Use this method to loging in using vk"""
        try:
            print("Start logging in with VK")
            self.bot.find_element(*LOCATORS.LOGINED_BY_VK).click()#click to button "Войти"
            print('clicked to button "VK"')
            self.bot.find_element(*AutorizationWithSocialNetwork.LOGIN_VK).send_keys(login)#enter login
            self.bot.find_element(*AutorizationWithSocialNetwork.PASSWORD_VK).send_keys(password)#enter password
            self.bot.find_element(*AutorizationWithSocialNetwork.SUBMIT_VK).click()#clicked submit
            print("logging data entry is complete")
            try:
                self.bot.find_element(*AutorizationWithSocialNetwork.ERROR_VK)
                print("Logined data is file...\nPlease check your login data before restarting...")
                record_error("start_page.StartPage.login_user", 'Not corect logging data')
                self.quit()
            except:
                self.bot.find_element(*AutorizationWithSocialNetwork.ALLOW_ACCES_VK).click()
                print("bot is logined")
        except Exception as e:
            print("Filed entry logined data\n e==", e)
            record_error("start_page.StartPage.login_user", str(e))


    def logined_with_fb(self, login, password):#Login it's e-mail or phone number 
        """Use this method to loging in using fb"""
        try:
            print("Start logging in with a FB")
            self.bot.find_element(*LOCATORS.LOGINED_BY_FB).click()#click to button "Войти"
            print('clicked to button "FB"')
            self.bot.find_element(*AutorizationWithSocialNetwork.ACCEPT_COOKIE_BUTTON).click()

            self.bot.find_element(*AutorizationWithSocialNetwork.LOGIN_FB).send_keys(login)#enter login
            self.bot.find_element(*AutorizationWithSocialNetwork.PASSWORD_FB).send_keys(password)#enter password
            self.bot.find_element(*AutorizationWithSocialNetwork.SUBMIT_FB).click()#clicked submit
            print("logging data entry is complete")
            if self.bot.find_element(*AutorizationWithSocialNetwork.ERROR_FB):
                print("Logined data is file...\nPlease check your login data before restarting...")
                record_error("start_page.StartPage.login_user", 'Not corect logging data')
                self.quit()
        except Exception as e:
            print("Filed entry logined data\n e==", e)
            record_error("start_page.StartPage.login_user", str(e))


    def logined_with_ok(self, login, password):
        """Use this method to loging in using 'ok'"""
        try:
            print("Start logging in with a FB")
            self.bot.find_element(*LOCATORS.LOGINED_BY_OK).click()#click to button "Войти"
            print('clicked to button "OK"')
            self.bot.find_element(*AutorizationWithSocialNetwork.LOGIN_OK).send_keys(login)#enter login
            self.bot.find_element(*AutorizationWithSocialNetwork.PASSWORD_OK).send_keys(password)#enter password
            self.bot.find_element(*AutorizationWithSocialNetwork.SUBMIT_OK).click()#clicked submit
            print("logging data entry is complete")
            if self.bot.find_element(*AutorizationWithSocialNetwork.ERROR_OK):
                print("Logined data is file...\nPlease check your login data before restarting...")
                record_error("start_page.StartPage.login_user", 'Not corect logging data')
                self.quit()
        except Exception as e:
            print("Filed entry logined data\n e==", e)
            record_error("start_page.StartPage.login_user", str(e))


    def test(self):
        self.open()
        self.logined_with_ok("galjazz@ukr.net", 'vova2506')
        self.quit()

if __name__ in "__main__":
    sp = StartPage()
    sp.test()1