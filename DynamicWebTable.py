import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service()
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(3)

# Login
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(3)

# Admin-->User Management--> users
driver.find_element(By.XPATH, "//li[1]//a[1]//span[1]").click()
time.sleep(4)
driver.find_element(By.XPATH,
                    "//span[normalize-space()='User Management']//i[@class='oxd-icon bi-chevron-down']").click()
driver.find_element(By.XPATH, "//ul[@role='menu']//li").click()
time.sleep(5)

# **********************************************************************************************************************************
# 1) To Find Total Number of Enabled Users
noOfRows = len(driver.find_elements(By.XPATH,
                                    "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div"))
print("total no of rows:", noOfRows)

count = 0
for r in range(1, noOfRows + 1):
    status = driver.find_element(By.XPATH,
                                 "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[" + str(
                                     r) + "]//div[5]").text
    if status == "Enabled":
        count = count + 1
print("Number of Enabled Users:", count)
print("Number of  Users:", noOfRows)
print("Number of Disabled Users:", (noOfRows - count))

# **********************************************************************************************************************************
# 2) Print the username along with the UserRole if the Role is Ess

for value in range(1, noOfRows + 1):
    Username = driver.find_element(By.XPATH,
                                   "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div["
                                   "2]/div[" + str(
                                       value) + "]/div/div[2]").text
    role = driver.find_element(By.XPATH,
                               "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[" + str(
                                   value) + "]/div/div[3]").text
    if role == "ESS":
        print("UserName:", Username, "    ", "UserRole:", role)

time.sleep(5)
driver.close()

# **********************************************************************************************************************************
# Record Found
#driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div["
 #                             "1]/div[5] | /html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div["
 #

# note
# /html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/div[5] ---># only select all Rows of status values
# "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[5]" -----> # 5th column of header "status"
# "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div" -------># capture all the rows


# Username = [driver.find_elements(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div["
# "1]/div[1]/div[1]/div[2] | /html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[" "1]/div[2]/div[3]/div[1]/div[
# 2]/div/div/div[2]")]
#
# UserRole = [driver.find_elements(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div["
# "1]/div[1]/div[1]/div[3] | /html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[" "1]/div[2]/div[3]/div[1]/div[
# 2]/div/div/div[3]")]
