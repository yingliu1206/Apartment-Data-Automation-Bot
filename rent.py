import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Rent:

    def __init__(self, url, header, chrome_options):
        self.url = url
        self.header = header
        self.prices = []
        self.addresses = []
        self.links = []
        self.driver = webdriver.Chrome(options=chrome_options)

    def scrape_web(self):
        # scrape the website
        response = requests.get(self.url, headers=self.header)
        website_html = response.text

        soup = BeautifulSoup(website_html, 'html.parser')

        # price
        # Clean up the strings, by removing any "+" symbols and other information so that you are only left with a dollar price.
        price_pattern = r'\$([\d,]+)'
        self.prices = [re.search(price_pattern, price.getText()).group(0) for price in soup.find_all('span', {'data-test': 'property-card-price'})]

        # address
        # Clean up the address data as well. Remove any newlines, pipe symbols |, and unnecessary whitespace.
        for address in soup.find_all('address', {'data-test': 'property-card-addr'}):
            address_text = address.text.strip()
            cleaned_address = address_text.replace('|', ',')
            cleaned_address = re.sub(r'\s+', ' ', cleaned_address)
            cleaned_address = cleaned_address.strip()
            self.addresses.append(cleaned_address)

        # links
        self.links = [link['href'] for link in soup.find_all('a', {'data-test': 'property-card-link'})]

        return self.prices, self.addresses, self.links

    def input_survey(self, url, address_lst, price_lst, link_lst):

        self.driver.get(url)

        time.sleep(3)
        for address, price, link in zip(address_lst, price_lst, link_lst):

            # input address
            address_input = self.driver.find_element(By.XPATH,
                                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address_input.send_keys(address)

            # input price
            price_input = self.driver.find_element(By.XPATH,
                                                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_input.send_keys(price)

            # input link
            link_input = self.driver.find_element(By.XPATH,
                                                  '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_input.send_keys(link)

            # click submit
            self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()

            # submit another response
            self.driver.find_element(By.XPATH,
                                     '/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()

    def create_sheet(self, url):

        self.driver.get(url)

        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/span/span[2]').click()









