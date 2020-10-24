from selenium.webdriver.common.by import By

class StartPageLocators():
    #start_page
    START_GAME  = (By.CLASS_NAME, "btn-start-inner")#start game without registration
    LOGIN = (By.CSS_SELECTOR, "a.go-btn")#ФИОЛЕТОВАЯ КНОПКА ВОЙТИ
    LOGINED_BY_FB = (By.CLASS_NAME, "_fb")#logined - facebook
    LOGINED_BY_VK = (By.CLASS_NAME, "_vk")#logined v kontakte
    LOGINED_BY_OK = (By.CLASS_NAME, "_ok")#logined odnoclassniki
    ENTER_LOGIN = (By.ID, "login")#user name
    ENTER_PASSWORD = (By.ID, "password")#user password
    AKCEPT_LOGIN_AND_PASSWORD = (By.ID, "submit")#зеленая кнопка войти
    FEEDBACK_PANEL_ERROR = (By.CSS_SELECTOR, ".feedbackPanelERROR>span")#error logined


class AutorizationWithSocialNetwork():
    #start_page
    LOGIN_FB = (By.ID, "m_login_email")
    PASSWORD_FB = (By.ID, "m_login_password")
    SUBMIT_FB = (By.NAME, "login")
    ERROR_FB = (By.ID, "#login_error")
    ACCEPT_COOKIE_BUTTON = (By.ID ,"accept-cookie-banner-label")

    LOGIN_VK = (By.CSS_SELECTOR, ".fi_row:nth-child(5)  input")
    PASSWORD_VK = (By.CSS_SELECTOR, ".fi_row:nth-child(6)  input")
    SUBMIT_VK = (By.CSS_SELECTOR, "input.button")
    ERROR_VK = (By.CLASS_NAME, "service_msg_warning")
    ALLOW_ACCES_VK = (By.CLASS_NAME, "button")

    LOGIN_OK = (By.ID,"field_email")
    PASSWORD_OK = (By.ID, "field_password")
    SUBMIT_OK = (By.CLASS_NAME, "form-actions_yes")
    ERROR_OK = (By.CLASS_NAME, "input-e")
    ALLOW_ACCES_OK = (By.CLASS_NAME, "form-actions_yes")