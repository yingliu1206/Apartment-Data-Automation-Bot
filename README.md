# Apartment-Data-Automation-Bot

An automated web scraping tool that collects apartment data from simulated real estate websites using **Selenium** and **BeautifulSoup**, and saves the data into a Google Form for easy record-keeping. The records can be outputted into a spreadsheet, making it a useful tool for tracking apartment listings. Future improvements will include automating the output spreadsheet.

## Features

- **Class-based Architecture**:
   - The **Rent** class contains all the logic for scraping apartment data using Selenium and BeautifulSoup. It also handles submitting the scraped data to the Google Form.
- **Data Extraction with BeautifulSoup**:
   - BeautifulSoup is used to parse the HTML of the page and extract the relevant apartment data, such as price, address, link, and other details.
- **Scraping with Selenium**:
   - Selenium is used to interact with the websites, automate fill and clicks.
- **Future Plans**:
   - Automate the handling of the outputted Google Spreadsheet for further analysis or reporting.

## Getting Started

### Prerequisites

Ensure that you have the following installed:

- **Python 3.x**
- **Selenium** (for browser automation)
- **BeautifulSoup** (for web scraping)
- **WebDriver** for your preferred browser (e.g., ChromeDriver for Chrome)

## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yingliu1206/Apartment-Data-Automation-Bot.git
   cd Apartment-Data-Automation-Bot
   ```
   
2. **Configure the Scraper**:
   - In the main Python script (main.py), you can specify the apartment websites you want to scrape and configure the relevant details. 


3. **Run the program**:
   - Run the program to start scraping and saving data:

   ```bash
   python main.py
   ```

4. **Check the responses:**
   - The responses will be automatically submitted.


5. **Link the Google Spreadsheet:**
   - The scraped data will be added to your Google Spreadsheet automatically. You can view the records there.

   
## Acknowledgments
- [100 Days of Code: The Complete Python Pro Bootcamp - Udemy](https://www.udemy.com/course/100-days-of-code) for the inspiration and guidance.
