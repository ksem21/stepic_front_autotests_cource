from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.XPATH, "//a[@id='registration_link']")


class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    REGISTRATION_FORM = (By.XPATH, "//form[@id='register_form']")


class ProductPageLocators():
    ADD_BTN = (By.XPATH, "//button[@value='Добавить в корзину']")
    NAME_OF_PRODUCT_IN_CART = (By.XPATH, "//div[@id='messages']/div[1]/div[@class='alertinner ']/strong")
    NAME_OF_PRODUCT = (By.XPATH, "//div[@id='content_inner']/article/div[1]/div[2]/h1")
    COST_OF_PRODUCT = (By.XPATH, "//p[@class='price_color']")
    TOTAL_COST_OF_CART = (By.XPATH, "//div[@class='alertinner ']/p/strong")