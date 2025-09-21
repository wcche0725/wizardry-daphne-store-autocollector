import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def main():
    load_dotenv()
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options)
    #does not appear that the code needs to emulate geolcation data to force the EN store
    #(which is necessary for the user_id_field variable)
    actions = ActionChains(driver)

    driver.implicitly_wait(1)
    driver.get('https://store.wizardry.info/')
    
    user_id_text = 'Enter your user ID'
    user_id_field = driver.find_element(By.XPATH, "(//input[@placeholder='" + user_id_text + "'])")
    login_button = driver.find_element(By.XPATH, "(//button[@data-testid='fast-login-button-authorization-user-id'])")

    actions.move_to_element(login_button).perform()
    user_id_field.send_keys(os.getenv("USER_ID"))
    login_button.click()

    #give the system time to log in
    time.sleep(2.5)

    driver.find_element(By.ID, "reject-button").click()

    free_gems_button = driver.find_element(By.XPATH, "(//button[@data-sku='jp.co.drecom.wizardry.daphne.X_gem900010'])")
    actions.move_to_element(free_gems_button).perform()
    free_gems_button.click()

    #give the system time to process the "purchase"
    time.sleep(2.5)
    driver.close()


if __name__ == '__main__':
    main()