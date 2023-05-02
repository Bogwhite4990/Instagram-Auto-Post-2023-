from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os
import datetime
import time


def accept_cookies():
    try:
        cookies_btn = driver.find_element_by_xpath(
            '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]')
        cookies_btn.click()
    except:
        pass


def login(username, password):
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_css_selector('._acap > div:nth-child(1)').click()


def create_post(day):
    driver.find_element_by_css_selector(
        'div.x1iyjqo2:nth-child(2) > div:nth-child(7) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1)').click()
    time.sleep(2)

    folder_path = f"photos/{day}/"
    file_paths = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".jpg") or file_name.endswith(".png"):
            photo_path = os.path.abspath(os.path.join(folder_path, file_name))
            file_paths.append(photo_path)

    file_paths_str = "\n".join(file_paths)

    element = driver.find_element_by_xpath("//input[@type='file']")
    element.send_keys(file_paths_str)
    time.sleep(1)

    driver.find_element_by_css_selector('.xyamay9 > div:nth-child(1)').click()
    time.sleep(1)
    driver.find_element_by_css_selector('.xyamay9 > div:nth-child(1)').click()
    time.sleep(1)

    file_name_text = f"{current_day}.txt"

    file_path = f"{folder_path}/{file_name_text}"

    with open(file_path, "r", encoding='utf-8') as f:
        caption_text = f.read()

    caption_input = driver.find_element_by_css_selector('div.xw2csxc:nth-child(1)')
    # actions = ActionChains(driver)
    # actions.move_to_element(caption_input)
    # actions.click()
    caption_input.click()
    for char in caption_text:
        caption_input.send_keys(char)
        time.sleep(0.05)

    time.sleep(3)
    driver.find_element_by_css_selector('.xyamay9 > div:nth-child(1)').click()


if __name__ == '__main__':
    current_day = datetime.datetime.today().day
    username = ""
    password = ""
    day = current_day
    driver = webdriver.Firefox()
    driver.get("https://www.instagram.com/")
    time.sleep(2)

    accept_cookies()
    time.sleep(3)
    login(username, password)
    time.sleep(8)
    create_post(day)
