from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from timeit import default_timer as timer
from time import sleep
from termcolor import colored, cprint
import time
from time import sleep
import onetimepass as otp

# Created by Nelson Orellana (Nels2 @ GitHub), 2022.05.11
# About
#
# Selenium powered bot that goes through ConnectWise tickets and adds little support documents to make troubleshooting/diagnosing quicker.

print_blue = lambda x: cprint(x, 'white', attrs=['bold'])
print_yellow = lambda x: cprint(x, 'yellow')
print_alt_yellow = lambda x: cprint(x, 'yellow', attrs=['underline'])
print_red = lambda x: cprint(x, 'red', attrs=['blink'])
print_green = lambda x: cprint(x, 'green')
url = ""#your IT Glue login site
options = webdriver.FirefoxOptions()
options.headless = False
driver = webdriver.Firefox(options=options)
driver.get(url)

def ITGlogind():
    useremail = ''
    paswrd = ''

    usrEnter = driver.find_element(by=By.NAME, value='username')
    usrEnter.send_keys(useremail)
    passEnter = driver.find_element(by=By.NAME, value='password')
    passEnter.send_keys(paswrd)
    passEnter.send_keys(Keys.RETURN)
    # MFA junk....
    time.sleep(3)
    secret = ''
    mfacode = otp.get_totp(secret)
    print_blue("MFA Code: " + str(mfacode))
    mfa_e = driver.find_element(By.NAME, "mfa")
    mfa_e.send_keys(mfacode)
    mfa_e.send_keys(Keys.RETURN)
ITGlogind()
while True:
    try:
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label.form-label:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')))
        print_green("#### -- Logged in! -- ####")
        pass
        break
    except ValueError:
        print_red("#### -- Unable to login. -- #####")
        pass 
#driver.quit()
