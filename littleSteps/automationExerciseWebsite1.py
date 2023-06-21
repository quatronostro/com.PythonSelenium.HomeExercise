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


def add_close_method(driver):
    close_button = driver.find_element(By.XPATH, "//*[@id='dismiss-button']")
    close_button.click()
    driver.switch_to.parent_frame()


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
time.sleep(2)
try:
    assert newUserSignupText.is_displayed()
except:
    add_close_method(driver)
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
time.sleep(2)
try:
    assert expectedText.is_displayed()
except:
    add_close_method(driver)
    assert expectedText.is_displayed()

# 9. Fill details: Title, Name, Email, Password, Date of birth
genderRadioButton = driver.find_element(By.ID, "id_gender1")
fakePassword = fake.password()
actions = ActionChains(driver)
time.sleep(3)
actions.move_to_element(genderRadioButton).click().send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(
    fakePassword).perform()
actions.send_keys(Keys.TAB).send_keys(Keys.ARROW_DOWN).send_keys(Keys.TAB).send_keys(Keys.ARROW_DOWN).send_keys(
    Keys.TAB).perform()
actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).perform()

# 10. Select checkbox 'Sign up for our newsletter!'
newsletterCheckBox = driver.find_element(By.ID, "newsletter")
newsletterCheckBox.click()

# 11. Select checkbox 'Receive special offers from our partners!'
optinCheckBox = driver.find_element(By.ID, "optin")
optinCheckBox.click()

# 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
firstNameTextBox = driver.find_element(By.XPATH, "(//*[@class='form-control'])[7]")
firstNameTextBox.send_keys(fake.first_name())

lastNameTextBox = driver.find_element(By.XPATH, "(//*[@class='form-control'])[8]")
lastNameTextBox.send_keys(fake.last_name())

companyNameTextBox = driver.find_element(By.XPATH, "(//*[@class='form-control'])[9]")
companyNameTextBox.send_keys(fake.first_name())

addressTextBox = driver.find_element(By.XPATH, "(//*[@class='form-control'])[10]")
addressTextBox.send_keys(fake.address())

countryDropDown = driver.find_element(By.XPATH, "(//*[@class='form-control'])[12]")
actions.click(countryDropDown).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

stateTextBox = driver.find_element(By.XPATH, "(//*[@class='form-control'])[13]")
stateTextBox.send_keys(fake.city())

cityTextBox = driver.find_element(By.XPATH, "(//*[@class='form-control'])[14]")
cityTextBox.send_keys(fake.city())

zipCodeTextBox = driver.find_element(By.XPATH, "(//*[@class='form-control'])[15]")
zipCodeTextBox.send_keys("12345")

mobileNumberTextBox = driver.find_element(By.XPATH, "(//*[@class='form-control'])[16]")
mobileNumberTextBox.send_keys("+905555555555")

# 13. Click 'Create Account button'
createAccountButton = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div/div/form/button")
createAccountButton.click()

# 14. Verify that 'ACCOUNT CREATED!' is visible
accountCreatedText = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div/h2/b")
print(accountCreatedText.text)
time.sleep(2)
try:
    assert accountCreatedText.is_displayed()
except:
    add_close_method(driver)
    assert accountCreatedText.is_displayed()

# 15. Click 'Continue' button
continueButton = driver.find_element(By.XPATH, "//*[@*='continue-button']")
try:
    continueButton.click()
except:
    add_close_method(driver)
    continueButton.click()

time.sleep(5)
# iframe = driver.find_element(By.XPATH, "//*[@id='mys-content']")
# driver.switch_to.frame(iframe)
# switch to parent iframe
driver.switch_to.frame(driver.find_element(By.ID, "google_esf"))
time.sleep(2)
driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='aswift_1']"))
# switch to child iframe
driver.switch_to.frame(driver.find_element(By.ID, "ad_iframe"))

close_button = driver.find_element(By.XPATH, "//*[@id='dismiss-button']")
close_button.click()
driver.switch_to.parent_frame()


# 16. Verify that 'Logged in as username' is visible
username = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[10]/a")
time.sleep(2)
try:
    assert username.is_displayed()
except:
    add_close_method(driver)
    assert username.is_displayed()

# 17. Click 'Delete Account' button
deleteButton = driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[5]/a")
deleteButton.click()

# 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
account_deleted_text = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div/h2/b")
time.sleep(2)
try:
    assert account_deleted_text.is_displayed()
except:
    add_close_method(driver)
    assert account_deleted_text.is_displayed()

continueButton.click()

time.sleep(5)



# THIS IS IMPOSSIBLE






