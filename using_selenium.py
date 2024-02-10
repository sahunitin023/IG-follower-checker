from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to Wikipedia
driver.get("https://www.instagram.com/")
username = driver.find_element(By.NAME, "username")
username_text = input("Username: ")
username.send_keys(username_text)

password = driver.find_element(By.NAME, "password")
password_text = input("Password: ")
password.send_keys(password_text, Keys.ENTER)

# Wait until a specific element on the page is loaded
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.NAME, "verificationCode")))

try:
    security_form = driver.find_element(By.NAME, "verificationCode")
    security_code = input("Enter the Security code sent as your Two-Factor Authentication: ")
    security_form.send_keys(security_code, Keys.ENTER)

except:
    pass

profile = driver.find_element(By.LINK_TEXT, "Profile")
profile.click()
