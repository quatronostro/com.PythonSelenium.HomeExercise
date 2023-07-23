import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


# Test Case 4:
# Website: www.booking.com
# Objective: Perform a hotel search, select a hotel, and verify the booking details.

# Steps:

# Launch the browser and navigate to www.booking.com.
def launch_browser_navigate_website(url):
    driver.get(url)

# Enter a specific location and travel dates in the search bar.
# Click on the "Search" button.
def search_travel():
    driver.find_element(By.XPATH, "//*[@aria-label='Dismiss sign-in info.']").click()

    destination = driver.find_element(By.XPATH, "//*[@id=':Ra9:']")
    actions = ActionChains(driver)
    actions.click(destination).send_keys("Paris").send_keys(Keys.TAB).perform()
    time.sleep(5)

# Verify that the search results display available hotels.
def verify_search():
    pass

# Select a specific hotel from the search results.
# Verify that the hotel details page is displayed.
def select_hotel_and_verify():
    pass

# Check the booking options, such as room types and prices.
# Verify that the booking details match the selected options.
def check_and_verify_booking_options():
    pass


if __name__ == '__main__':
    url = "https://www.booking.com"

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    launch_browser_navigate_website(url)
    search_travel()
    verify_search()
    select_hotel_and_verify()
    check_and_verify_booking_options()

