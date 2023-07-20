from selenium.webdriver.common.by import By
from selenium import webdriver


# Test Case 2:
# Website: www.netflix.com
# Objective: Sign up for a new account and perform a search for a TV show.

# Steps:

# Launch the browser and navigate to www.netflix.com.
def launch_browser_navigate_website(url):
    driver.get(url)

# Click on the "Sign In" button.
# Select the "Sign Up" option.
def sign_up_action():
    driver.find_element(By.XPATH, "//button[text()='Accept']").click() #Cookies Accept button
    driver.find_element(By.XPATH, "//a[text()='Sign In']").click() #Sign In button

    emailBox = driver.find_element(By.XPATH, "//*[@for='id_userLoginId']")
    emailBox.send_keys("mbaramuk@hotmail.com")
    passwordBox = driver.find_element(By.XPATH, "//*[@for='id_password']")
    passwordBox.send_keys("Muz994599 ")

    driver.find_element(By.XPATH, "//*[@type='submit']").click() #submit button

# Enter valid information details, including name, email, and password.
def enter_valid_info():
    pass

# Access your profile and verify that the user is logged in.
def verify_login():
    pass

# Perform a search for a specific TV show.
def search():
    pass

# Verify that the search results display the TV show and relevant information.
def verify_search_result():
    pass


if __name__ == '__main__':
    url = "https://www.netflix.com"

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    launch_browser_navigate_website(url)
    sign_up_action()