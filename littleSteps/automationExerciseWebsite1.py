from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from faker import Faker
fake = Faker()


# 1. Launch browser
driver = webdriver.Chrome()
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




# 7. Click 'Signup' button
# 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
# 9. Fill details: Title, Name, Email, Password, Date of birth
# 10. Select checkbox 'Sign up for our newsletter!'
# 11. Select checkbox 'Receive special offers from our partners!'
# 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
# 13. Click 'Create Account button'
# 14. Verify that 'ACCOUNT CREATED!' is visible
# 15. Click 'Continue' button
# 16. Verify that 'Logged in as username' is visible
# 17. Click 'Delete Account' button
# 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button