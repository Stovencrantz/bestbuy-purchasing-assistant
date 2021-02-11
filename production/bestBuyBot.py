from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# driver.get('https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442');

# Prompt the user for some information, before initializing the webDriver, this prevents python from bugging out when it tries to prompt the user for info and also laod the driver at the same time
productURL = input("Please enter the link to your desired product: ")
print("Enter your login info")
username = input("Please enter your username: ")
password = input("Please enter your password: ")
print("Enter your shipping info")
firstName = input("First Name: ")
lastName = input("Last Name: ")
address = input("Shipping Address: ")
city = input("City: ")
state = input("State (Ex. NY): ").upper()
zipCode = input("ZIP Code: ")

# try/except to pass ad
PATH = 'C:\webdrivers\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('https://www.bestbuy.com/')

# grabs the advertisement that pops up on initial page load,  and closes out of it
try:
    advertisement = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "widgets-view-email-modal-mount"))
    )
    advertClose = advertisement.find_element_by_class_name("c-modal-close-icon")
    advertClose.click()
    print("advertisement has been closed")

    # grabs first utility-navigation-list-item, which in our case is the account button
    accountButton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "utility-navigation-list-item"))
    )
    accountButton.click()

    # Try/except to open account dropdown and click signIn button
    try:
        # signInMenu = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.ID, "account-menu-container"))
        # )
        signInButton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "lam-signIn__button"))
        )
        # signInButton = signInMenu.find_element_by_class_name("lam-signIn__button")
        signInButton.click()
        # Try/except to fill out signin info and click SignIn button
        try: 
            signInForm = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "cia-main-container"))
            )
            emailForm = signInForm.find_element_by_id("fld-e")
            emailForm.send_keys(username)

            passwordForm = signInForm.find_element_by_id("fld-p1")
            passwordForm.send_keys(password)

            signInButtonFinal = signInForm.find_element_by_class_name("cia-form__controls__submit")
            signInButtonFinal.click()

            # Try/except to certify that the user is signed in
            try:
                loggedIn = WebDriverWait(driver, 10).until(
                 EC.presence_of_element_located((By.CLASS_NAME, "logged_user_name"))
            )
                # time.sleep(2)
                print("COngrats! You are logged in")
                # driver.get('https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442');
                driver.get(productURL);


                # time.sleep(2)

                # Try/except to certify that the item is in stock, and if so to add it to the cart
                try:
                    addToCartButton = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'add-to-cart-button'))
                )
                # set addToCartButtonStatus to hold initial boolean to enter our while loop. If it is false, we will loop, otherwise we pass the loop
                    addToCartButtonStatus = addToCartButton.is_enabled()

                    while(addToCartButtonStatus == False):
                        # If the add to cart button is present, meaning the item is IN STOCK, click the button and proceed to check out
                        # time.sleep(2)
                        # driver.get('https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442');
                        driver.get(productURL); 
                        
                        # locate the addToCart Button after the page refreshed to check if button status updated
                        try:
                            addToCartButton = WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located((By.CLASS_NAME, 'add-to-cart-button'))
                            )
                            # If the button is now enabled and the item can be checked out, we will break from this loop 
                            if (addToCartButton.is_enabled()): 
                                print("Looks like the item is now in stock, We have added your item to the cart")
                                # print("addToCartButton is enabled")
                                print(addToCartButton.is_enabled())
                                break 
            

                            # If the add to cart button is NOT present, meaning the item is OUT OF STOCK, refresh the page
                            # This else is unnecessary, its just being used to show we are continuously looping through in the console
                            else:
                                # print(addToCartButton.is_enabled())
                                # print("addToCartButton is disabled")
                                print("Looks like our Item is out of stock, check back later!")
                        
                        except Exception as e: print("Could not locate the Add-to-cart button \n" + str(e))


                    # Once an items add-to-cart button becomes active, we exit our loop and add the item to our cart
                    addToCartButton.click()                
                    try:
                        goToCartButton = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.CLASS_NAME, "go-to-cart-button"))
                        )
                        goToCartButton.click()                
                        print("Navigating to our cart")

                        #Ensure that the radio button for shipping to your address is clicked before purchase, will click the button whether the availabilti__list container is in either location
                        try:
                            radioContainer = WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located((By.CLASS_NAME, "availability__list"))
                            )
                            shippingBtn = radioContainer.find_element_by_xpath("//input[(@id='fulfillment-order-shipping') or contains(@id,'fulfillment-shipping')]")
                            shippingBtn.click()

                            checkoutBtn = driver.find_element_by_class_name("checkout-buttons__checkout").find_element_by_xpath("*")
                            checkoutBtn.click()
                            print('Navigating to checkout page')

                            # Locate the shipping info form and fill in all of the field swith the users billing info that they entered
                            try:
                                shippingForm = WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located((By.CLASS_NAME, "streamlined__shipping--body"))
                            )
                                firstNameForm = shippingForm.find_element_by_id("consolidatedAddresses.ui_address_2.firstName")
                                firstNameForm.send_keys(firstName)

                                lastNameForm = shippingForm.find_element_by_id("consolidatedAddresses.ui_address_2.lastName")
                                lastNameForm.send_keys(lastName)

                                addressForm = shippingForm.find_element_by_id("consolidatedAddresses.ui_address_2.street")
                                addressForm.send_keys(address)

                                cityForm = shippingForm.find_element_by_id("consolidatedAddresses.ui_address_2.city")
                                cityForm.send_keys(city)

                                zipCodeForm = shippingForm.find_element_by_id("consolidatedAddresses.ui_address_2.zipcode")
                                zipCodeForm.send_keys(zipCode)

                                stateForm = shippingForm.find_element_by_id("consolidatedAddresses.ui_address_2.state")
                                stateBtn = stateForm.find_element_by_css_selector("option[value="+state+"]") 
                                stateBtn.click()
                                # stateBtn.send_keys(Keys.RETURN)

                                try:
                                    paymentContinueField = WebDriverWait(driver, 10).until(
                                    EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='button--continue']"))
                                )
                                    paymentContinueBtn = paymentContinueField.find_element_by_xpath("*")
                                    paymentContinueBtn.click()
                                    # driver.execute_script("arguments[0].click();", paymentContinueBtn)

                                    try: 
                                        placeOrderBtn = WebDriverWait(driver, 10).until(
                                        EC.presence_of_element_located((By.XPATH, "//button[contains(@data-track,'Place your Order - Contact Card')]"))
                                    )
                                        placeOrderBtn.click()

                                        try: 
                                            orderSuccessMsg = WebDriverWait(driver, 10).until(
                                            EC.presence_of_element_located((By.CLASS_NAME, "//span[@text, 'Thanks for shopping with us!']"))
                                        )           
                                            print("Your Item was ordered successfully")

                                        except Exception as e: print("Could not locate the order Success message \n" + str(e))

                                    except Exception as e: print("Could not locate the finalize purchase button \n" + str(e))

                                except Exception as e: print("Exception trying to find the continue to payment button \n" + str(e))

                            except Exception as e: print("Could not identify the form for entering the users shipping info \n" + str(e))

                        except Exception as e: print("Could not identify the radio button container for shipping to the users address \n" + str(e))

                    except Exception as e: print("Could not locate the go-to-cart button \n" + str(e))

                except Exception as e: print("There was an exception checking that the user was logged in \n" + str(e))
            
            except Exception as e: print("There was an exception getting the sign in form \n" + str(e))

        except Exception as e: print("There was an exception trying to sign in button \n" + str(e))

    except Exception as e: print("An exception occured trying to click Sign In dropdown menu \n" + str(e))           

except Exception as e: print("an exception occured trying to access the advertisement \n" + str(e))




time.sleep(20)

# driver.quit()