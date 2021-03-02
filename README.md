
# bestbuy-purchasing-assistant
![Badge](https://img.shields.io/badge/Python-v3.9-blue "Python Badge")

## Description:
<p>
This is a script built with python and selenium that will allow the user to automatically purchase an item that they direct it to, or if the item is out of stock, it will wait until the item returns into stock and then purchase it. This allows the user to let the script run and go about their day without dedicating time and attention to constantly checking the website for when an item may become available again.
<p>

# Table of Contents
- [Description](#description)
- [Installation](#installation)
- [How to use](#how-to-use) 
- [Built with](#built-with)
- [Contributing](#contributing)
- [Credits](#credits)
- [Questions](#questions)

# Installation:
- Clone the repository to your system.

- Download and Install Python v3 or newer from https://www.python.org/downloads/

- ### Install selenium through the python terminal:
``` python
$ pip install selenium
``` 
- Check that your google chrome is up to date, otherwise install Google Chrome v88

- Download ChromeDriver v88 via https://chromedriver.chromium.org/, 
  the chromedriver version must match your updated google chrome version.

- Please create a webdrivers folder in your C drive and save the      downloaded chromedriver folder in this location, ensure the file path matches the following:

```
C:/webdrivers/chromedriver_win32/chromedriver.exe
```

# How to Use:

Save the bestBuyAssistant.py file to your desktop and then double click the file to run the script, then follow the prompts.

<p>Once the program starts the first prompt you will receive is to provide the script with the link for the product you are looking to purchase.
</p>

You will then be asked to provide the following information:
- username
- password
- first name
- last name
- billing address
- city
- state
- zip code

<p>
This information will be used to automatically log you into your bestbuy account and then allow you to continually refresh a web page without having to log-in each refresh, thus saving much needed time when searching for a product to come into stock. 
</p>


# Built With:
- Python v3.9.1
- Selenium
- Chrome Browser
- Chrome Webdriver

## Contributing:
- Steve Knapp


## Questions:
Please contact me about this program or for any additional questions using the following link: 
- [GitHub Profile](https://github.com/)
<!-- - [Video](https://drive.google.com/file/d/1S7Ghxkw8DkgHQ8dZb39vRoqImev4Hydz/view) -->

