
from selenium import webdriver
from selenium.webdriver.common.by import By


# 5. Test case: Verify that the user can book a flight on expedia.com
# Steps:
# Launch the browser and navigate to https://www.expedia.com
def visit_website(url):
    driver.get(url)

# Locate the flights tab and click on it
def locate_flights_tab_and_click():
    driver.find_element(By.XPATH, "//*[@id='multi-product-search-form-1']/div/div/div[1]/ul/li[2]/a/span").click() # flights tab

# Locate the origin field and enter a valid departure city or airport "New York"
def enter_city_departure():
    driver.find_element(By.XPATH, "//button[@aria-label='Leaving from']").click() # leaving from

    input_from = driver.find_element(By.XPATH, "//input[@id='location-field-leg1-origin']")
    input_from.send_keys("New York")
    input_from.submit()

# Locate the destination field and enter a valid arrival city or airport "London"
def enter_city_destination():
    driver.find_element(By.XPATH, "//button[@aria-label='Going to']").click()  # going to

    input_to = driver.find_element(By.XPATH, "//input[@id='location-field-leg1-destination']")
    input_to.send_keys("London")
    input_to.submit()

# Locate the departure date field and select a valid date from the calendar "May 20"
# Locate the return date field and select a valid date from the calendar "May 27"
def dates_for_flight():
    driver.find_element(By.XPATH, "//button[@id='d1-btn']").click() # for dates
    driver.find_element(By.XPATH, "//button[@data-day='29'][1]").click()
    driver.find_element(By.XPATH, "//button[@data-day='30'][1]").click()

    driver.find_element(By.XPATH, "//button[@data-stid='apply-date-picker']").click() # done button

# Click on the search button or press enter
def search():
    driver.find_element(By.XPATH, "//button[@data-testid='submit-button']").click()

    captcha_frame = driver.find_element(By.XPATH, "(//div[@id='app'])[2]")
    driver.switch_to.frame(captcha_frame)
    driver.find_element(By.XPATH, "//button[@id='home_children_button']").click()

    driver.execute_script("document.getElementById('app').style.display = 'none';")

# Verify that the results page contains available flights matching the search criteria
def verify():
    verify_text = driver.find_element(By.XPATH, "(//span[@class='is-visually-hidden'])[7]")
    verify_text = verify_text.text
    assert verify_text.__contains__("New York") and verify_text.__contains__("London")



if __name__ == '__main__':
    url = "https://www.expedia.com"

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    visit_website(url)
    locate_flights_tab_and_click()
    enter_city_departure()
    enter_city_destination()
    dates_for_flight()
    search()
    verify()

# Its not working properly
