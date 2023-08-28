from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

import time
import pandas as pd
import random
import urllib.request
import re
import datetime


class Scrapper():
    def __init__(self):

        # set driver as class var

        self.options_driver = Options()
        self.options_driver.add_argument(
            "app-version=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62")
        self.driver = webdriver.Chrome(executable_path='.\chromedriver.exe', options=self.options_driver)

        self.db = db_connector.Database()

    # 함수목록: get_elem by css, 및 xpath 함수
    # 함수 내 에러처리기능 포함(elem 없을경우 null 반환 및 일정 횟수만큼 access 해주기
    # 필요 함수목록(glb) : set driver, quit_driver, find_elem(css, xpath) & click() or send_keys() & text, sleep(rand)
    # set.document, set_savepoint - 날짜? 페이지 num , 주소, + 각 사이트에 따른 세이브 포인트로 이동하는 시퀀스 필요
    # driver.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys("webElement") - 태그 내 attr 선택 예제
    # driver.find_element(By.NAME, "q").send_keys("webdriver" + Keys.ENTER) - send key 예

    # 1.0에서 지원할것 - JSON 파일 받아 원하는 뉴스 사이트 및 element, 동작 순서 입력받아 그대로 파싱하게 하기


    def set_driver(self, link):
        # self.driver = self.webdriver.Chrome(executable_path='C:\dev\crawling\chromedriver.exe',
        #                                     options=self.options_driver)
        self.driver.implicitly_wait(10)
        self.driver.get(link)

    def quit_driver(self):
        self.driver.quit()

    def driver_action(self,
             method,
             scr_form,
             scr_form_param,
             action,
             action_param
             ):

        """
        method :
             - 0 (element)- get an element
             - 1 (elements) - will be supported at version 1.0

        scr_form :
            - 0 (id)  find element by element id
            - 1 (class) : find element by element class
            - 2 (tag name) : find element by tag name
            - 3 (xpath) : find element by xpath
            - 4 (css selector) : find element by css selector

        scr_form_param : parameters using at each 'find_element' method
            - ex) find by tag name <p> -> 'p'

        action :
            - 0 (click) : click() method's parameter
            - 1 (send_key) : use [send keys()] method's parameter
            - 2 (mouse) : will be supported with version 1.0
            - 3 (wheel) : will be supported with version 1.0
            - 4 (get text) : return current element's text
            - 5 (get_attribute) : return current element's attribute

        action_param : parameters using at each action
            - ex) using [action = 2] and [action_param = Keys.ENTER] will be [send_keys(Keys.ENTER)]

        action_options : will be supported at version 1.0

        return:
        """

        wait = WebDriverWait(self.driver, 3)
        # fluent wait
        # wait = WebDriverWait(self.driver, 10, poll_frequency=1,
        #                      ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        # element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div")))

        if(method == 0):
            if(scr_form == 0):
                element = wait.until(EC.presence_of_element_located((By.ID, scr_form_param)))
            elif(scr_form == 1):
                # element = driver.find_element(By.CLASS_NAME, scr_form_param)
                element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, scr_form_param)))
            elif(scr_form == 2):
                # element = driver.find_element(By.TAG_NAME, scr_form_param)
                element = wait.until(EC.presence_of_element_located((By.TAG_NAME, scr_form_param)))
            elif(scr_form == 3):
                # element = driver.find_element(By.XPATH, scr_form_param)
                print('waiting for...')
                element = wait.until(EC.presence_of_element_located((By.XPATH, scr_form_param)))
            elif(scr_form == 4):
                # element = driver.find_element(By.CSS_SELECTOR, scr_form_param)
                print('waiting for...')
                element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, scr_form_param)))
            else:
                raise Exception("Param Error: scr_form")
        else:
            raise Exception("Param Error : method")
        try:
            if(action == 0):
                # WebDriverWait(self.driver, 10).until(element_to_be_clickable(element))
                element.click()
            elif(action == 1):
                # WebDriverWait(self.driver, 10).until(element_to_be_selected(element))
                element.send_keys(action_param)
            elif(action == 2):
                pass
            elif(action == 3):
                pass
            elif(action == 4):
                # WebDriverWait(self.driver, 10).until(EC.element_to_be_selected((element)))
                return str(element.text)
            elif(action== 5):
                # WebDriverWait(self.driver, 10).until(EC.element_to_be_selected((element)))
                return str(element.get_attribute(action_param))
            else:
                raise Exception("Param Error: action, action_param")
        except:
            raise Exception("Param Error: action, element")


    def pattern_chicago(self):

        ret_val = {}

        ret_val['wheat'] = self.driver_action(
            method=0,
            scr_form=3,
            scr_form_param='/html/body/form/div[6]/div/div[1]/div[5]/div/div[1]/table/tbody/tr[2]/td[2]',
            action=4,
            action_param='')

        ret_val['coffee'] = self.driver_action(
            method=0,
            scr_form=3,
            scr_form_param='/html/body/form/div[6]/div/div[1]/div[5]/div/div[1]/table/tbody/tr[11]/td[2]',
            action=4,
            action_param='')

#/html/body/form/div[6]/div/div[1]/div[5]/div/div[2]

        self.driver_action(
            method=0,
            scr_form=3,
            scr_form_param='/html/body/form/div[6]/div/div[1]/div[5]/div/div[2]',
            action=0,
            action_param='')

        ret_val['sugar'] = self.driver_action(
            method=0,
            scr_form=3,
            scr_form_param='/html/body/form/div[6]/div/div[1]/div[5]/div/div[1]/table/tbody/tr[16]/td[2]',
            action=4,
            action_param='')

        return ret_val


def main():
    crawler = Scrapper()
    try:
        crawler.set_driver(link = "https://tradingeconomics.com/commodity/wheat")
        #https://tradingeconomics.com/commodity/wheat

        print(crawler.pattern_chicago())
    except Exception as e:
        print(e)
        crawler.quit_driver()

