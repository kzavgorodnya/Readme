import unittest
import time
import re
import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


DEFAULT_WAIT_TIME = 2


def run_test():
    driver = webdriver.Chrome()
    driver.get("https://dash.readme.io/login")
    driver.maximize_window()

    EmailField = driver.find_element_by_id('email')
    EmailValue=os.environ.get("readmeLogin")
    EmailField.send_keys(EmailValue)

    PasswordField = driver.find_element_by_id("password")
    PasswordValue=os.environ.get("readmePass")
    PasswordField.send_keys(PasswordValue)
    #PasswordField.send_keys("uIhe_B64G")

    LoginButton = driver.find_element_by_xpath('//form/div[@class="form-actions"]/button')
    # print(LoginButton)
    LoginButton.click()
    time.sleep(DEFAULT_WAIT_TIME)

    DeviceHiveIcon = driver.find_element_by_xpath('//div[@class="info-sub ng-binding"]')
    DeviceHiveIcon.click()
    sleep()

    GeneralSettings = driver.find_element_by_xpath("//span[text()='General Settings']")
    GeneralSettings.click()
    sleep()

    UpgradePlan = driver.find_element_by_xpath("//span[text()='Upgrade Plan']")
    UpgradePlan.click()
    sleep()

    ViewInvoicesButton = driver.find_element_by_xpath("//*[@id='plans']/div[1]/div/a")
    ViewInvoicesButton.click()
    sleep()

    # Row=driver.find_element_by_xpath('//table[@id="transactionsTable"]/tbody/tr')
    # for rowElement in driver.find_element_by_xpath('//table[@id="transactionsTable"]/tbody/tr'):
        # Cell= rowElement.find_element_by_xpath(".//td[1]")
        # print (Cell.text)
    # driver.switchTo().frame("filepicker_comm_iframe")

    # we can find the iframe with this xpath
    # iframe = driver.find_element_by_xpath('//iframe[not(@id)][1]')
    # But there are a lot of them, to make sure we find the right one
    # lets go through each of them and try to find our table
    TABLE_PATH = '//table[@id="transactionsTable"]'
    iframe = find_transactions_iframe(driver, TABLE_PATH)

    driver.switch_to_frame(iframe)
    table = driver.find_element_by_xpath(TABLE_PATH)
    # do something with table here

    # and finally switch to default content
    driver.switch_to_default_content()

    # iframe = driver.find_element_by_xpath('//iframe[not(@id)][1]')
    # for frame in driver.find_elements_by_tag_name("iframe"):
    #     print(frame.get_attribute('id'))
    #     if iframe == frame:
    #         print ('MATCH')


def find_transactions_iframe(d, xp):
    for frame in d.find_elements_by_tag_name("iframe"):
        try:
            d.switch_to_frame(frame)
            d.find_element_by_xpath(xp)
            print('table found!')
            return frame
        except NoSuchElementException:
            pass
        finally:
            d.switch_to_default_content()

    return None


def sleep(interval=DEFAULT_WAIT_TIME):
    time.sleep(interval)


#trs = driver.find_elements(By.TAG_NAME, "tr")

#tds = trs[1].find_elements(By.TAG_NAME, "td")

#

if __name__ == '__main__':
    run_test()
