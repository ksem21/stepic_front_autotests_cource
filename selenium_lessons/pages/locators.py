from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    REGISTRATION_FORM = (By.XPATH, "//form[@id='register_form']")
    EMAIL_REGISTRATION_FIELD = (By.XPATH, "//input[@type='email'][@name='registration-email']")
    PASSWORD_REGISTRATION_FIELD = (By.XPATH, "//input[@type='password'][@name='registration-password1']")
    REPEAT_PASSWORD_REGISTRATION_FIELD = (By.XPATH, "//input[@type='password'][@name='registration-password2']")
    REGISTRATION_BUTTON = (By.XPATH, "//button[@name='registration_submit']")

class ProductPageLocators():
    ADD_BTN = (By.XPATH, "//button[@value='Добавить в корзину']")
    NAME_OF_PRODUCT_IN_CART = (By.XPATH, "//div[@id='messages']/div[1]/div[@class='alertinner ']/strong")
    NAME_OF_PRODUCT = (By.XPATH, "//div[@id='content_inner']/article/div[1]/div[2]/h1")
    COST_OF_PRODUCT = (By.XPATH, "//p[@class='price_color']")
    TOTAL_COST_OF_CART = (By.XPATH, "//div[@class='alertinner ']/p/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']//div[1]//div[1]")


class BasePageLocators():
    LOGIN_LINK = (By.XPATH, "//a[@id='login_link']")
    CART_BUTTON = (By.XPATH, "//a[@class='btn btn-default']")
    LOGIN_IMAGE = (By.XPATH, "//i[@class='icon-user']")


class BasketLocators():
    BASKET_ITEMS = (By.XPATH, "//div[@class='basket-items']")
    EMPTY_CART_PHRASE = (By.XPATH, "//p[contains(text(),'Ваша корзина пуста')]")
