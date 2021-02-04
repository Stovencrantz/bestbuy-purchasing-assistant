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
                    # EC.presence_of_element_located((By.XPATH, "//button[contains(@class,'add-to-cart-button') and contains(@class, 'btn-leading-ficon')]"))
                    # EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'add-to-cart-button')]"))
                    EC.presence_of_element_located((By.CLASS_NAME, 'add-to-cart-button'))
                )

                    # If the add to cart button is present, meaning the item is IN STOCK, click the button and proceed to check out
                    if (addToCartButton.is_enabled()): 
                        addToCartButton.click()                
                        print("Looks like the item is in stock, We have added your item to the cart")
                        # print("addToCartButton is enabled")
                        time.sleep(2)                
                        
                        try:
                            goToCartButton = WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located((By.CLASS_NAME, "go-to-cart-button"))
                            )
                            goToCartButton.click()                
                            print("Navigating to our cart")
                            time.sleep(2)
                            
                        except Exception as e: print(e)

                    # If the add to cart button is NOT present, meaning the item is OUT OF STOCK, refresh the page
                    else:
                        # print("addToCartButton is disabled")
                        print("Looks like our Item is out of stock, check back later!")
                        # driver.get('https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442');
                        driver.get('https://www.bestbuy.com/site/logitech-z150-2-0-multimedia-speakers-2-piece-black/5326434.p?skuId=5326434');


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