from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox() # Some versions are incompatible with selenium, try https://ftp.mozilla.org/pub/firefox/releases/30.0/win32/en-US/

# Request Dominos
driver.get("https://www.dominos.com/en/pages/order/?locations=1#/locations/")
driver.implicitly_wait(5) # Allow page loading

# Enter Address Information (Type: Apartment)
Type = driver.find_element_by_id("Address_Type_Select")
for option in Type.find_elements_by_tag_name("option"):
    if option.text == "Apartment":
        option.click()
        break
                                                                         # Fill information out prior to use
driver.find_element_by_id("Street").send_keys("[STREET]")                # <--- Street
driver.find_element_by_id("Address_Line_2").send_keys("[APARTMENT]")     # <--- Apartment 
driver.find_element_by_id("City").send_keys("[CITY]")                    # <--- City
driver.find_element_by_id("Postal_Code").send_keys("[ZIP]")              # <--- Zip

State = driver.find_element_by_id("Region")                              
for option in State.find_elements_by_tag_name("option"):
    if option.text == "[STATE]":                                         # <--- State (Ex. MA, NJ, NY)
        option.click()
        break

# Search for locations
driver.find_element(By.XPATH, ".//*[@id='locationsSearchPage']/form/div/div[2]/div/button").click()
driver.implicitly_wait(5) # Allow page loading

# Click the first option (closest delivery)
driver.find_element(By.XPATH, ".//*[@id='locationsResultsPage']/div[1]/div[2]/div[4]/div[2]/a").click()
driver.implicitly_wait(5) # Allow page loading

# Click Popular Items
driver.find_element(By.XPATH, ".//*[@id='entreesPage']/div[1]/div[3]/a/div[2]/h2").click()

# Click Large Cheese Pizza
driver.find_element(By.XPATH, ".//*[@id='entreesPage']/div[1]/div[3]/div/div/div[2]/div[1]/ul/li[1]/a/h5").click()
driver.implicitly_wait(5) # Allow page loading

# Straight to checkout
driver.get("https://www.dominos.com/en/pages/order/payment.jsp")

# Enter contact information                                              # Fill information out prior to use
driver.find_element_by_id("First_Name").send_keys("[FIRST NAME]")        # <--- First Name
driver.find_element_by_id("Last_Name").send_keys("[LAST NAME]")          # <--- Last Name 
driver.find_element_by_id("Email").send_keys("[EMAIL]")                  # <--- Email
driver.find_element_by_id("Callback_Phone").send_keys("[PHONE]")         # <--- Phone
driver.find_element_by_id("Email_Opt_In").click()                        # Opt in is preselected, click again to Opt out

# Pay with cash upon delivery
driver.find_element(By.XPATH, ".//*[@id='orderPaymentPage']/form/div[5]/div/div[2]/div/div[3]/label/input").click()

# Place order
# driver.find_element(By.XPATH, ".//*[@id='orderPaymentPage']/form/div[6]/div[4]/button").click()
# Last step is commented for your safety ;)
# Only uncomment after you've tested the rest of the program first
