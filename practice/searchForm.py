
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = 'C:\webdrivers\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get("https://www.techwithtim.net/")
print('Web Page title: ' + driver.title)

# search the html page for an element with the name = 's', in this case, a text field
search = driver.find_element_by_name('s')
# enter the phrase 'test' into the text field
search.send_keys("test");
# act as if the user presser enter/return key to submit the search
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles = main.find_elements_by_tag_name("article")
    myWord = input("enter your word: ")
    print(myWord)
    for article in articles:
        # header = article.find_element_by_class_name("entry-summary")
        # print(header.text)
        header = article.find_element_by_class_name("entry-title").find_elements_by_tag_name("a")
        print(header.text)

except:
    driver.quit()

# main = driver.find_elements_by_id("main")

# tells the program to wait 5 seconds before moving onto the next task, allows us to visual see the changes happenning
time.sleep(5)

driver.quit()
