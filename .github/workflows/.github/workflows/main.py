import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


STORE_URL = "https://store.wizardry.info/"
FREE_GEMS_SKU = "jp.co.drecom.wizardry.daphne.X_gem900010"


def main():
    if len(sys.argv) <= 1:
        print("USER_ID needed. Usage: python main.py [USER_ID]")
        sys.exit(1)

    user_id = sys.argv[1]

    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 15)
    actions = ActionChains(driver)

    try:
        print("Opening Wizardry store...")
        driver.get(STORE_URL)

        print("Handling GDPR popup...")
        try:
            gdpr_button = wait.until(
                EC.element_to_be_clickable((By.ID, "reject-button"))
            )
            gdpr_button.click()
        except Exception:
            print("GDPR popup not found or already dismissed.")

        print("Finding login field...")
        user_id_field = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@placeholder='Enter your user ID']")
            )
        )

        login_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@data-testid='fast-login-button-authorization-user-id']")
            )
        )

        print("Entering user ID...")
        user_id_field.clear()
        user_id_field.send_keys(user_id)

        print("Logging in...")
        actions.move_to_element(login_button).perform()
        login_button.click()

        time.sleep(3)

        print("Finding free gems button...")
        free_gems_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, f"//button[@data-sku='{FREE_GEMS_SKU}']")
            )
        )

        if not free_gems_button.is_enabled():
            print("Free gems button is not enabled.")
            return

        print("Clicking free gems button...")
        actions.move_to_element(free_gems_button).perform()
        free_gems_button.click()

        time.sleep(3)

        print("Free gems collection completed.")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
