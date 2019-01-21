import time
from datetime import datetime

from easygui import *
from selenium import webdriver


def fill_survey():
    x = 1
    if x:
        usr = enterbox("Enter Your Email / Phone no", 'Phone no / Email')
        print("Got your Email as : " + usr)
        pas = passwordbox("Enter Your Password:", "Enter Your password")
        print("Got your pass....")
        startTime = datetime.now()
        driver = webdriver.Chrome(executable_path='chromedriver.exe')
        driver.get("http://accounts.google.com")
        time.sleep(3)
        username = driver.find_element_by_id("identifierId")
        username.send_keys(usr)

        nexts = driver.find_element_by_id("identifierNext")
        nexts.click()

        time.sleep(3)
        password = driver.find_element_by_name("password")
        password.send_keys(pas)

        nextss = driver.find_element_by_id("passwordNext")
        nextss.click()

        time.sleep(3)

        driver.get(
            "https://docs.google.com/forms/d/e/1FAIpQLSeGXUs17bUWilur6cWyNNco_XOHZJQB-sea4BwE0egphWENzg/viewform?vc=0&c=0&w=1")
        section = driver.find_elements_by_xpath("//*[@role='radio']")[1]
        section.click()

        button = driver.find_element_by_xpath("//*[@role='button']")
        button.click()
        for i in range(0, 8):
            final = 61
            # if i == 7: final = 56
            for j in range(0, final, 5):
                field = driver.find_elements_by_xpath("//*[@role='radio']")[j]
                field.click()
                time.sleep(0.2)
            if i == 7:
                self_response = driver.find_element_by_xpath("//*[@role='checkbox']")
                self_response.click()
                time.sleep(2)

            button = driver.find_elements_by_xpath("//*[@role='button']")[1]
            button.click()

        print("Done")
        print("\nTime taken: " + str(datetime.now() - startTime))
    print("Good Bye")


if __name__ == '__main__':
    print("------------------------------")
    print("Gmail Form filler")
    print("Opening Login page...\nPlease Wait")
    print("------------------------------")
    time.sleep(3)
    fill_survey()