import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from faker import Faker
fake = Faker()

options = Options()
options.add_experimental_option("detach", True)
# 1. Launch browser
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.maximize_window()
# 2. Navigate to url 'http://automationexercise.com'
url = "http://automationexercise.com"
driver.get(url)

# 3. Verify that home page is visible successfully
expectedTitle = "Automation Exercise"
actualTitle = driver.title.title()
print("Actual Title is : {}".format(actualTitle))
assert actualTitle.__contains__(expectedTitle)

# 4. Click on 'Signup / Login' button
signupButton = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[4]")
signupButton.click()

# 5. Verify 'New User Signup!' is visible
newUserSignupText = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[3]/div/h2")
assert newUserSignupText.is_displayed()

# 6. Enter name and email address
fakeName = fake.name()
fakeEmailAddress = f"{fake.name().lower().replace(' ', '.')}@{fake.domain_name()}"

signUpNameBox = driver.find_element(By.XPATH, "//*[@*='signup-name']")
signUpNameBox.send_keys(fakeName)
signUpEmailBox = driver.find_element(By.XPATH, "//*[@*='signup-email']")
signUpEmailBox.send_keys(fakeEmailAddress)

# 7. Click 'Signup' button
driver.find_element(By.XPATH, "//*[@*='signup-button']").click()

# 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
expectedText = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div/div/h2/b")
assert expectedText.is_displayed()

# 9. Fill details: Title, Name, Email, Password, Date of birth
# 10. Select checkbox 'Sign up for our newsletter!'
# 11. Select checkbox 'Receive special offers from our partners!'
# 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
# 13. Click 'Create Account button'
genderRadioButton = driver.find_element(By.ID, "id_gender1")
fakePassword = fake.password()
actions = ActionChains(driver)
actions.move_to_element(genderRadioButton).click().send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(fakePassword).perform()
actions.send_keys(Keys.TAB).send_keys(Keys.ARROW_DOWN).send_keys(Keys.TAB).send_keys(Keys.ARROW_DOWN).send_keys(Keys.TAB).perform()
actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).perform()
actions.send_keys(Keys.TAB).send_keys(fake.name()).send_keys(Keys.TAB).send_keys(fake.address()).send_keys(Keys.TAB).perform()
actions.send_keys(fakeName).send_keys(Keys.TAB).send_keys(fakeName).send_keys(Keys.TAB).send_keys(Keys.ARROW_DOWN).perform()
actions.send_keys(Keys.TAB).send_keys(fake.city()).send_keys(Keys.TAB).send_keys(fake.city()).send_keys(Keys.TAB).perform()
actions.send_keys("1234").send_keys(Keys.TAB).send_keys("+905555555555").send_keys(Keys.TAB).click().perform()

#There is some problem in actions section, Maybe its about chrome options

# 14. Verify that 'ACCOUNT CREATED!' is visible
# 15. Click 'Continue' button
# 16. Verify that 'Logged in as username' is visible
# 17. Click 'Delete Account' button
# 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button