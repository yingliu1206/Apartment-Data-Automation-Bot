import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from rent import Rent

# for scraping
ZILLOW_URL = 'https://appbrewery.github.io/Zillow-Clone/'
HEADER = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

# for saving scraped results
SURVEY_URL = 'https://docs.google.com/forms/d/e/1FAIpQLScmFH_kJQDCWncGMiH778bC6Ny7uxO5VWo0NSXYNSJpbR844g/viewform?usp=dialog'
SHEET_URL = 'https://docs.google.com/forms/d/16q96f2jH7OddfhDveVI6p9IdkmWKujfFIPjosCkxT74/edit#responses'

# create the driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# utilize the class
rent_class = Rent(ZILLOW_URL, HEADER, chrome_options)

# scrape the price, address, and link from the website
price_lst, address_lst, link_lst = rent_class.scrape_web()

# input all the surveys
rent_class.input_survey(SURVEY_URL, address_lst, price_lst, link_lst)

# output responses into a spreadsheet - under development
# rent_class.create_sheet(SHEET_URL)




