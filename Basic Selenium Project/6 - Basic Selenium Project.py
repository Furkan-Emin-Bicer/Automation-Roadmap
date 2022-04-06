from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LCW:
    CATEGORY_PAGE_BUTTON = (By.CLASS_NAME, "dropdown")  # [2]
    PRODUCT_PAGE_BUTTON = (By.CSS_SELECTOR, ".a_model_item")  # [30]
    CHOOSE_SIZE_BUTTON = (By.CSS_SELECTOR, "a[key]")  # [2]
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".add-to-cart")
    CART_PAGE_BUTTON = (By.CSS_SELECTOR, ".header-cart")
    MAIN_PAGE_BUTTON = (By.CSS_SELECTOR, ".header-logo")
    website = 'https://www.lcwaikiki.com/tr-TR/TR'
    product_code = (By.CSS_SELECTOR,".product-code")

    def __init__(self):
        self.driver = webdriver.Chrome('C:/Users/emin.bicer/Desktop/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get(self.website)
        self.wait = WebDriverWait(self.driver, 20)

    def test_navigate(self):
        self.wait.until(ec.presence_of_all_elements_located(self.CATEGORY_PAGE_BUTTON))[2].click()
        category_current_url = self.driver.current_url
        assert "https://www.lcwaikiki.com/tr-TR/TR/lp/32-33-erkek" in category_current_url, "Erkek Kategorisinde Değilsin"
        self.wait = WebDriverWait(self.driver, 30)



        self.wait.until(ec.presence_of_all_elements_located(self.PRODUCT_PAGE_BUTTON))[5].click()
        product_code = self.wait.until(ec.presence_of_all_elements_located(self.product_code))[1].text
        assert "S1CT15Z8" in product_code, "Ürün kodu doğru değil"

        self.wait.until(ec.presence_of_all_elements_located(self.CHOOSE_SIZE_BUTTON))[2].click()
        size_number = self.wait.until(ec.presence_of_all_elements_located(self.CHOOSE_SIZE_BUTTON))[2].text
        assert "42" in size_number, "Ürün boyutu doğru değil"

        self.wait.until(ec.element_to_be_clickable(self.ADD_TO_CART_BUTTON)).click()
        self.wait.until(ec.element_to_be_clickable(self.CART_PAGE_BUTTON)).click()
        self.wait.until(ec.element_to_be_clickable(self.MAIN_PAGE_BUTTON)).click()
        self.driver.quit()


LCW().test_navigate()
