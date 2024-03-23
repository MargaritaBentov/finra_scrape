import random
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Constants
URL = "https://www.finra.org/finra-data/browse-catalog/short-sale-volume-data/daily-short-sale-volume-files"
VIEW_CONTENT_CLASS = 'view-content'
YEAR_DROPDOWN_SELECTOR = "[data-drupal-selector='edit-custom-year-wrapper']"
MONTH_DROPDOWN_SELECTOR = "[data-drupal-selector='edit-custom-month-wrapper']"
CHOSEN_RESULTS_CLASS = 'chosen-results'
LINKS_FILE = 'links.txt'


def initialize_driver():
    options = Options()
    options.headless = True
    profile = webdriver.FirefoxProfile()
    options.profile = profile
    driver = webdriver.Firefox(options=options)
    return driver


def scrape_links(driver, url):
    driver.get(url)
    for year in range(2023, 2011-1, -1):  # Loop from 2023 to 2011
        select_year(driver, str(year))
        start_month = 1 if year != 2011 else 3  # Start from March for 2011
        for month in range(start_month, 12+1):  # Loop from January to December
            select_month(driver, month)
            extract_and_write_links(driver)
            time.sleep(random.randint(1, 5))  # Random sleep to avoid being blocked


def extract_and_write_links(driver):
    time.sleep(random.uniform(1.2, 2.7))
    view_content = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, VIEW_CONTENT_CLASS)))
    links = view_content.find_elements(By.TAG_NAME, 'a')
    hrefs = [link.get_attribute('href') for link in links]
    with open(LINKS_FILE, 'a') as file:
        for href in hrefs:
            file.write(href + '\n')


def select_year(driver, year):
    time.sleep(random.uniform(1.2, 2.7))
    year_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, YEAR_DROPDOWN_SELECTOR))
    )
    # driver.execute_script("arguments[0].scrollIntoView(true);", year_dropdown)
    year_dropdown.click()
    year_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//ul[@class='{CHOSEN_RESULTS_CLASS}']/li[normalize-space()='{year}']"))
    )
    # driver.execute_script("arguments[0].scrollIntoView(true);", year_option)
    time.sleep(random.uniform(1.2, 2.7))
    year_option.click()


def select_month(driver, month):
    time.sleep(random.uniform(1.2, 2.7))
    month_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, MONTH_DROPDOWN_SELECTOR))
    )
    # driver.execute_script("arguments[0].scrollIntoView(true);", month_dropdown)
    month_dropdown.click()
    month_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//ul[@class='{CHOSEN_RESULTS_CLASS}']/li[normalize-space()='{month_name(month)}']"))
    )
    # driver.execute_script("arguments[0].scrollIntoView(true);", month_option)
    time.sleep(random.uniform(1.2, 2.7))
    month_option.click()


def month_name(month_number):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return months[month_number - 1]
