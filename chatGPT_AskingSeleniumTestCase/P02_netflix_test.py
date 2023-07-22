import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


# Test Case 2:
# Website: www.netflix.com
# Objective: Sign up for a new account and perform a search for a TV show.

# Steps:

# Launch the browser and navigate to www.netflix.com.
def launch_browser_navigate_website(url):
    driver.get(url)

# Click on the "Sign In" button.
# Select the "Sign Up" option.
# Enter valid information details, including name, email, and password.
# Access your profile and verify that the user is logged in.
def sign_up_action():


    driver.find_element(By.XPATH, "//button[text()='Accept']").click() #Cookies Accept button
    driver.find_element(By.XPATH, "//a[text()='Sign In']").click() #Sign In button

    emailBox = driver.find_element(By.XPATH, "//*[@for='id_userLoginId']")
    actions.click(emailBox).send_keys("mbaramuk@hotmail.com").send_keys(Keys.TAB).send_keys("Muz994599").send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()

    driver.find_element(By.XPATH, "(//li[@class='profile'])[2]").click() # profile click

    account_drop_down = driver.find_element(By.XPATH, "//div[@class='account-dropdown-button']")
    actions.move_to_element(account_drop_down).perform()

    profile_name = driver.find_element(By.XPATH, "//span[@class='profile-name']")
    profile_name = profile_name.text
    expected_name = "mbaramuk"
    assert profile_name.__contains__(expected_name)

# Perform a search for a specific TV show.
def search(tv_show_text):
    search_icon = driver.find_element(By.CLASS_NAME, "search-icon")
    actions.move_to_element(search_icon).click().send_keys(tv_show_text).perform()
    time.sleep(3)

# Verify that the search results display the TV show and relevant information.
def verify_search_result(tv_show_text):
    tv_show = driver.find_element(By.XPATH, "(//p[@class='fallback-text'])[1]")
    tv_show = tv_show.text
    expected_tv_show = tv_show_text
    assert expected_tv_show.__contains__(tv_show)


if __name__ == '__main__':
    url = "https://www.netflix.com"
    tv_show_text = "Breaking Bad"

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    actions = ActionChains(driver)

    launch_browser_navigate_website(url)
    sign_up_action()
    search(tv_show_text)
    verify_search_result(tv_show_text)
