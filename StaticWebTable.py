from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service()
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 1) count number of rows and columns
noOfRows = len(driver.find_elements(By.XPATH, "(//tbody)[1]//tr"))
noOfColumns = len(driver.find_elements(By.XPATH, "(//tbody)[1]//tr/th"))
print("noOfRows:", noOfRows)  # 7
print("noOfColumns:", noOfColumns)  # 4

# 2) Read specific row and column data- master in java

data = driver.find_element(By.XPATH, "(//tbody)[1]//tr[6]/td[1]").text
print(data)

# 3) Read all the rows & columns data
print("***********printing all the rows and columns data**************")

for r in range(2, noOfRows + 1):
    for c in range(1, noOfColumns + 1):
        data1 = driver.find_element(By.XPATH, "(//tbody)[1]//tr[" + str(r) + "]/td[" + str(c) + "]").text
        print(data1, end="    ")
    print()

# 4) Read data based on Condition (List books name whose author is Amit)
print("********************printing data based on Condition (List books name whose author is Amit)**************")
for row in range(2, noOfRows + 1):
    author = driver.find_element(By.XPATH, "(//tbody)[1]//tr[" + str(row) + "]/td[2]").text
    if author == "Amit":
        bookname = driver.find_element(By.XPATH, "(//tbody)[1]//tr[" + str(row) + "]/td[1]").text
        print(bookname + "   " + author)

# 5) sum of price columns
print("********************sum of price columns **************")
total=0
for price in range(2, noOfRows + 1):
    value_Price = driver.find_element(By.XPATH, "(//tbody)[1]//tr[" + str(price) + "]/td[4]").text
    total+= int(value_Price)
print("total price of all the books:",total)

driver.close()
