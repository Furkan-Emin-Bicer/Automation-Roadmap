from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class locators:
    UTM_Settings= (By.CSS_SELECTOR, ".qa-checkbox.fl-l") # $$(".qa-checkbox.fl-l")

    INPUT_Journey= (By.CSS_SELECTOR, ".in-text-input-wrapper__input") # [1] $$(".in-text-input-wrapper__input")- https://inshoppingcart.inone.useinsider.com/journey-builder/169133/design/2/sms?disableMode=false

    INPUT_Journey_Warning_Message = (By.CSS_SELECTOR, ".in-text-input-wrapper__error-message") # $$(".in-text-input-wrapper__error-message")https://inshoppingcart.inone.useinsider.com/journey-builder/169133/design/2/sms?disableMode=false

    INPUT_Journey_Filter = (By.CSS_SELECTOR, ".in-form-item") # [13] $$(".in-form-item")- https://inshoppingcart.inone.useinsider.com/journey-builder

    RECO_Test_Radio_Button = (By.CSS_SELECTOR, ".in-form-item.in-radio-button-wrapper") # [5] $$(".in-form-item.in-radio-button-wrapper")- https://inshoppingcart.inone.useinsider.com/web-smart-recommender/1144655/launch
    STATISTICS_Button = (By.CSS_SELECTOR, ".vuetable-slot.statistics") # [2] $$(".vuetable-slot.statistics") https://inshoppingcart.inone.useinsider.com/journey-builder
    MESSAGEBOX_Delete_Button = (By.CSS_SELECTOR, ".in-button-wrapper") # [3] $$(".in-button-wrapper") https://inshoppingcart.inone.useinsider.com/message-box/1144685/design
    ALERT_Toaster = (By.CSS_SELECTOR, ".in-toasts-wrapper.m-4.qa-toasts") # [0] $$(".in-toasts-wrapper.m-4.qa-toasts") https://inshoppingcart.inone.useinsider.com/journey-builder/169258/canvas/3/sms?disableMode=false
    Create_New_Personalization = (By.CSS_SELECTOR, ".in-button-wrapper_create-default") #$$(".in-button-wrapper_create-default") https://inshoppingcart.inone.useinsider.com/journey-builder