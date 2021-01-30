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
        signInMenu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "account-menu-container"))
        )
        # signInButton = signInMenu.find_element_by_class_name("lam-signIn__button")
        signInButton = signInMenu.find_element_by_class_name("lam-signIn__button")
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

            try:
                loggedIn = WebDriverWait(driver, 10).until(
                 EC.presence_of_element_located((By.CLASS_NAME, "logged_user_name"))
            )
                time.sleep(2)
                print("COngrats! You are logged in")
                time.sleep(2)
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