
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDefaultSuite():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_signuptest(self):
    self.driver.get("http://127.0.0.1:8080/#/register?redirect=/")
    self.driver.set_window_size(1280, 712)
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("lian")
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("lian33@gmail.com")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("lian")
    self.driver.find_element(By.ID, "passwordConfirm").click()
    self.driver.find_element(By.ID, "passwordConfirm").send_keys("lian")
    self.driver.find_element(By.CSS_SELECTOR, ".mt-3").send_keys(Keys.ENTER)
  
  def test_signuptest(self):
    self.driver.get("http://127.0.0.1:8080/#/register?redirect=/")
    self.driver.set_window_size(1280, 712)
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("rina")
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("rina33@gmail.com")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("rina")
    self.driver.find_element(By.ID, "passwordConfirm").click()
    self.driver.find_element(By.ID, "passwordConfirm").send_keys("rina")
    self.driver.find_element(By.CSS_SELECTOR, ".mt-3").send_keys(Keys.ENTER)
  