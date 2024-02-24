from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://secure-retreat-92358.herokuapp.com/")

fName = driver.find_element(By.NAME, value="fName")
fName.send_keys("Aman")

lName = driver.find_element(By.NAME, value="lName")
lName.send_keys("Raza")

email = driver.find_element(By.NAME, value="email")
email.send_keys("amanraza1010@gmail.com")

button = driver.find_element(By.CSS_SELECTOR, value=".btn-block")
button.click()


# driver.close()
# driver.quit()
