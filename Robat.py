import re
import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Robo:
    counter = 1
    speed = 0

    def __init__(self):
        a = input('Enter the speed limit :')
        while True:
            try:
                a = int(a)
            except:
                pass
            if type(a) == int and a >= 0:
                self.speed = a
                break
            a = input('Enter the speed limit :')
        self.driver = webdriver.Firefox()
        # login insta
        self.driver.get('https://www.instagram.com/accounts/login/')
        sleep(2)
        # self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(
        #     'navaiiymohaahmd38')
        # self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(
        #     'gV33vmaAcxCyacr')
        sdf = input('Enter to login to Instagram :')

        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]/button/div').click()  # submit
        sleep(5)
        self.driver.get('https://getlike.io/login/')
        sleep(2)
        # login
       
        sdf = input('Enter to login to Getlike :')
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="formLogin"]/input').click()  # btn_login
        print("login")
        sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[6]/nav/div/div[2]/ul[1]/li[2]/a').click()  # Quest Exchange
        sleep(1)

    def follow(self):
        self.driver.find_element_by_xpath('//*[@id="list-3-3"]/span[2]').click()  # part flower
        sleep(2)
        id_text = self.driver.find_element_by_xpath('//*[@id="task_list"]/div/div[2]').get_attribute('innerHTML')
        ids = list()

        for sublist in [c[14:] for c in re.findall(r'data-task-id="[\d]+', id_text)]:
            if sublist not in ids:
                ids.append(sublist)
        for i, id in enumerate(ids):
            t = time.time()
            try:
                print('========================================================')
                print(self.counter, end=' > ')
                self.counter += 1
                # WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH,
                #                                                                     f'/html/body/div[6]/div[1]/div/div[2]/div/div[2]/article[{i + 1}]/div/div/div/div[4]/a')))
                sleep(3)
                self.driver.find_element_by_xpath(
                    f'/html/body/div[6]/div[1]/div/div[2]/div/div[2]/article[{i + 1}]/div/div/div/div[4]/a').click()
                sleep(1)
                try:
                    self.driver.find_element_by_xpath(
                        f"/html/body/div[6]/div[1]/div/div[2]/div/div[2]/article[{i + 1}]/div/div/div/div[4]/span/i").get_attribute(
                        'class')
                except:
                    sleep(10 + self.speed)

                self.driver.switch_to.window(self.driver.window_handles[1])
                self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]').click()
                print(self.driver.title.split('•')[0], end=' > ')

                #
                # self.driver.find_element_by_css_selector(
                #     '#react-root > section > main > div > header > section > div.nZSzR > div.Igw0E.IwRSH.eGOV_.ybXk5._4EzTm.bPdm3 > div > div > div > span > span.vBF20._1OSdk > button').click()

                sleep(1)
                print('flow', end=' > ')
                self.driver.close()
                sleep(1)
                self.driver.switch_to.window(self.driver.window_handles[0])
                # WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH,
                #                                                                     f'/html/body/div[6]/div[1]/div/div[2]/div/div[2]/article[{i + 1}]/div/div/div/div[4]/a')))

                sleep(2)
                self.driver.find_element_by_xpath(
                    f'/html/body/div[6]/div[1]/div/div[2]/div/div[2]/article[{i + 1}]/div/div/div/div[4]/a').click()
                print('ok', end='   ')
            except Exception as e:
                print('error', end='   ')
                try:
                    self.driver.switch_to.window(self.driver.window_handles[1])
                    self.driver.close()
                    self.driver.switch_to.window(self.driver.window_handles[0])
                    self.driver.find_element_by_css_selector(
                        f'#task-item-{id} > div > div > div > div.media-right.media-middle.task-btn > a').click()  # Quest Exchange

                except:
                    pass

            print(f'time = {int(time.time() - t)}')

    def like(self):
        self.driver.find_element_by_xpath('//*[@id="list-3-1"]').click()  # part flower
        sleep(2)
        id_text = self.driver.find_element_by_xpath('//*[@id="task_list"]/div/div[2]').get_attribute('innerHTML')
        ids = list()
        for sublist in [c[14:] for c in re.findall(r'data-task-id="[\d]+', id_text)]:
            if sublist not in ids:
                ids.append(sublist)

        for i, id in enumerate(ids):
            t = time.time()
            try:
                print('========================================================')
                print(self.counter, end=' > ')
                self.counter += 1
                # WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[6]/div[1]/div/div[2]/div/div[2]/article[{i+1}]/div/div/div/div[4]/a')))
                sleep(3)
                self.driver.find_element_by_xpath(
                    f'/html/body/div[6]/div[1]/div/div[2]/div/div[2]/article[{i + 1}]/div/div/div/div[4]/a').click()
                sleep(1)
                try:
                    self.driver.find_element_by_xpath(
                        f"/html/body/div[6]/div[1]/div/div[2]/div/div[2]/article[{i + 1}]/div/div/div/div[4]/span/i").get_attribute(
                        'class')
                except:
                    sleep(10 + self.speed)
                self.driver.switch_to.window(self.driver.window_handles[1])
                # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                #     (By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]')))
                self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
                print(self.driver.title.split('on')[0], end=' > ')

                # self.driver.find_element_by_xpath(
                #     '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]').click()
                sleep(1)
                print('like', end=' > ')
                self.driver.close()
                sleep(1)
                self.driver.switch_to.window(self.driver.window_handles[0])
                # WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH,
                #                                                                     f'/html/body/div[6]/div[1]/div/div[2]/div/div[2]/article[{i + 1}]/div/div/div/div[4]/a')))
                sleep(2)
                self.driver.find_element_by_xpath(
                    f'/html/body/div[6]/div[1]/div/div[2]/div/div[2]/article[{i + 1}]/div/div/div/div[4]/a').click()
                print('ok', end='   ')
            except Exception as e:
                print('error', end='   ')
                try:
                    self.driver.switch_to.window(self.driver.window_handles[1])
                    self.driver.close()
                    self.driver.switch_to.window(self.driver.window_handles[0])
                    self.driver.find_element_by_css_selector(
                        f'#task-item-{id} > div > div > div > div.media-right.media-middle.task-btn > a').click()  # Quest Exchange

                except:
                    pass
            print(f'time = {int(time.time() - t)}')


now = time.localtime()  # زمان فعلی سیستم
sec = time.mktime(now)
try:
    if sec < 7624304618+172800:
        robo = Robo()
        while sec < 7624304618+172800:
            robo.follow()
            robo.follow()
            robo.like()
except Exception as e:
    print("Please run the program again\n")
    print(f'error =>{e}')
