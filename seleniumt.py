from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.add_argument("--headless")

servico = Service(GeckoDriverManager().install())

navegador = webdriver.Firefox(service=servico)

navegador.get('https://select-quiz.vercel.app')

navegador.find_element(
    'xpath', '/html/body/div/div/div[1]/div/a[5]').click()

time.sleep(2)

navegador.find_element(
    'xpath', '/html/body/div/div/div[1]/section/div/form/div/input').send_keys('Pseudomusk')

time.sleep(2)

navegador.find_element(
    'xpath', '/html/body/div/div/div[1]/section/div/form/button').click()

navegador.quit()
