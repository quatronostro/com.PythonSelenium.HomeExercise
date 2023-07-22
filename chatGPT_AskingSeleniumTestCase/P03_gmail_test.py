import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# Test Case 3:
# Website: www.gmail.com
# Objective: Log in to a Gmail account, compose an email with attachments, and send it.

# Steps:

# Launch the browser and navigate to www.gmail.com.
def launch_browser_navigate_website(url):
    driver.get(url)

# Enter valid login credentials and click on the "Sign In" button.
# Verify that the user is successfully logged in.
def user_login(email, password):
    email_box = driver.find_element(By.ID, "identifierId")
    email_box.send_keys(email)

    driver.find_element(By.XPATH, "(//*[@jsname='V67aGc'])[2]").click() # Next button
    time.sleep(5)

    password_box = driver.find_element(By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input")

    driver.find_element(By.ID, "passwordNext").click() #Next button
    time.sleep(5)

# Click on the "Compose" button to create a new email.
# Enter the recipient's email address, subject, and body of the email.
def create_compose_mail():
    pass

# Attach specific files to the email.
def attach_file():
    pass

# Click on the "Send" button.
# Verify that the email is sent successfully.
def send_mail_and_verify():
    pass

if __name__ == '__main__':
    url = "https://www.gmail.com"
    email = "b.baramuk@gmail.com"
    password = "0990.0110.Berke"

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    launch_browser_navigate_website(url)
    user_login(email, password)
    create_compose_mail()
    attach_file()
    send_mail_and_verify()

