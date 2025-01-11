from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome() 
driver.get("http://127.0.0.1:8080/#/register?redirect=/")
driver.set_window_size(1280, 712)

try:

    name_field = driver.find_element(By.ID, "name")
    name_field.click()
    name_field.send_keys("lara")
    

    email_field = driver.find_element(By.ID, "email")
    email_field.click()
    email_field.send_keys("lara33@gmail.com")
    

    password_field = driver.find_element(By.ID, "password")
    password_field.click()
    password_field.send_keys("lara")
    

    confirm_password_field = driver.find_element(By.ID, "passwordConfirm")
    confirm_password_field.click()
    confirm_password_field.send_keys("lara")
    
  
    register_button = driver.find_element(By.CSS_SELECTOR, ".mt-3")
    register_button.click()
    
   
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    username = driver.find_element(By.ID, "username").text
    assert username == "lara", f"Expected username 'lara', but got {username}"
    
    print("Test passed successfully!")

except Exception as e:
    print(f"Test failed: {e}")

finally:
    driver.quit()
