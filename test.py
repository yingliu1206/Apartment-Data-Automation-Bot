import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

ZILLOW_URL = 'https://appbrewery.github.io/Zillow-Clone/'
HEADER = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(ZILLOW_URL, headers=HEADER)
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')
price_pattern = r'\$([\d,]+)'
prices = [re.search(price_pattern, price.getText()).group(0) for price in soup.find_all('span', {'data-test': 'property-card-price'})]
# print(prices)

addresses = []
for address in soup.find_all('address', {'data-test': 'property-card-addr'}):

    address_text = address.text.strip()
    cleaned_address = address_text.replace('|', ',')
    cleaned_address = re.sub(r'\s+', ' ', cleaned_address)
    cleaned_address = cleaned_address.strip()
    addresses.append(cleaned_address)


links = [link['href'] for link in soup.find_all('a', {'data-test': 'property-card-link'})]
# print(links)

SURVEY_URL = 'https://docs.google.com/forms/d/e/1FAIpQLScmFH_kJQDCWncGMiH778bC6Ny7uxO5VWo0NSXYNSJpbR844g/viewform?usp=dialog'
# create the driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
# driver.get(SURVEY_URL)

# time.sleep(3)
# s = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
# s.send_keys(addresses[0])
# p = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
# p.send_keys(prices[0])
# l= driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
# l.send_keys(links[0])
# driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
# driver.find_element(By.XPATH,
#                                      '/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()

driver.get('https://docs.google.com/forms/d/16q96f2jH7OddfhDveVI6p9IdkmWKujfFIPjosCkxT74/edit#responses')

time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/span/span[2]').click()