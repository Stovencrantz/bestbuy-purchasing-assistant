from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# driver.get('https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442');

# Prompt the user for some information, before initializing the webDriver, this prevents python from bugging out when it tries to prompt the user for info and also laod the driver at the same time
username = input("Please enter your username: ")
password = input("Please enter your password: ")

# try/except to pass ad
PATH = 'C:\webdrivers\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('https://www.bestbuy.com/')

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
                time.sleep(2)
                print("COngrats! You are logged in")
                # driver.get('https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442');
                driver.get('https://www.bestbuy.com/site/logitech-z150-2-0-multimedia-speakers-2-piece-black/5326434.p?skuId=5326434');


                time.sleep(2)

                # Try/except to certify that the item is in stock, and if so to add it to the cart
                try:
                    addToCartButton = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'add-to-cart-button'))
                )
                # set addToCartButtonStatus to hold initial boolean to enter our while loop. If it is false, we will loop, otherwise we pass the loop
                    addToCartButtonStatus = addToCartButton.is_enabled()

                    while(addToCartButtonStatus == False):
                        # If the add to cart button is present, meaning the item is IN STOCK, click the button and proceed to check out
                        time.sleep(2)
                        # driver.get('https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442');
                        driver.get('https://www.bestbuy.com/site/logitech-z150-2-0-multimedia-speakers-2-piece-black/5326434.p?skuId=5326434'); 
                        
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
                        
                        except Exception as e: print(e)


                    # Once an items add-to-cart button becomes active, we exit our loop and add the item to our cart
                    addToCartButton.click()                
                    try:
                        goToCartButton = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.CLASS_NAME, "go-to-cart-button"))
                        )
                        goToCartButton.click()                
                        print("Navigating to our cart")

                        #Ensure that the radio button for shipping to your address is clicked before purchase
                        # shipping radio button ID seems to change at a particular time, generate way to find this value regardless if it changes daily or not
                        try:
                            radioContainer = WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located((By.CLASS_NAME, "availability__list"))
                                # EC.presence_of_element_located((By.ID, "fulfillment-shipping-qss2wkkutp0r-4sdob3sngievq"))
                            )
                            # radioContainer.click()
                            print(radioContainer)

                            radioList = radioContainer.find_elements_by_class_name('c-radio-brand')
                            print("Radio List: ")
                            print(radioList)

                            # Loop through all of the radio buttons on the page and check to see which one have an id that includes fulfillment-shipping within its unique id, as only the radio button for shipping to your address has this unique phrase in it
                            for radio in radioList:
                                radioBtn = radio.find_element_by_xpath("*")
                                radioBtnIdList = radioBtn.get_attribute("id").split('-')
                                shippingBtnCheck = radioBtnIdList[0] + '-' + radioBtnIdList[1]
                                if shippingBtnCheck == 'fulfillment-shipping':
                                    radioBtn.click()
                                    break
                            time.sleep(20)

                        except Exception as e: print(e)

                    except Exception as e: print(e)

                except Exception as e: print(e)

            except Exception as e: print(e)
            # except:
            #     print("Couldnt recognize logged user")
        except Exception as e: print(e)
        # except:
        #     print("There was an exception trying to sign in")
    except Exception as e: print(e)           
    # except:
    #     print("An exception occured trying to click Sign In")
except Exception as e: print(e)
# except:
#     print("an exception occured trying to click Account")



time.sleep(5)

driver.quit()