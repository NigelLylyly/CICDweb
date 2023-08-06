from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    # Initialize the WebDriver (Make sure you have the appropriate WebDriver executable in your PATH)
    driver = webdriver.Chrome()

    # Navigate to the website
    driver.get("https://www.google.com")

    try:
        # Wait for the username input element to be present
        username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "userid")))

        # Type the username
        username_input.send_keys("my_username")

        # Wait for the password input element to be present
        password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))

        # Type the password
        password_input.send_keys("my_password")

        # Find and click the login button
        login_button = driver.find_element_by_id("btnK")
        login_button.click()

        # Wait for the page to load and perform some assertions or further actions
        # ...

    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        # Close the browser window and end the WebDriver session
        driver.quit()


if __name__ == "__main__":
    main()

