from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.flipkart.com/")
driver.find_element(By.CSS_SELECTOR,"[title='Login']").click()

# driver.find_element(By.XPATH,'//input[contains(@class,"c3Bd2c yXUQVt")]').send_keys("123@gmail.com")
request_otp = driver.find_element(By.XPATH,'//button[text()="Request OTP"]')
request_otp.click()
# time.sleep(2)
# driver.find_element(By.XPATH,'//button[text()="Verify"]').click()
#
# driver.find_element(By.XPATH,'//button[text()="Request OTP"]').click()
# print(driver.find_element(By.XPATH,'//span[text()="Please enter valid Email ID/Mobile number"]').text)

driver.quit()
