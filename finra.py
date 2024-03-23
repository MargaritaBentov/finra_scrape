from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select


# Set up headless option for Firefox
options = Options()
options.headless = True

# Initialize the Firefox driver with the specified options

# Create a new Firefox Profile
profile = webdriver.FirefoxProfile()
options.profile = profile
driver = webdriver.Firefox(options=options)


# Now you can use the driver to navigate and interact with web pages
driver.get("https://www.finra.org/finra-data/browse-catalog/short-sale-volume-data/daily-short-sale-volume-files")

view_content = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'view-content')))

# ... perform your tasks ...
# print(driver.page_source)

# Find all <a> elements within this element
links = view_content.find_elements(By.TAG_NAME, 'a')
# Extract href attributes
hrefs = [link.get_attribute('href') for link in links]

# Write hrefs to a text file
with open('links.txt', 'w') as file:
    for href in hrefs:
        file.write(href + '\n')

# Wait until the dropdown is clickable and then click it
year_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-drupal-selector='edit-custom-year-wrapper']"))
)
year_dropdown.click()

# Find the list item for year 2023 and click it
year_2023 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//ul[@class='chosen-results']/li[normalize-space()='2023']"))
)
year_2023.click()

view_content = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'view-content')))
# Find all <a> elements within this element
links = view_content.find_elements(By.TAG_NAME, 'a')
# Extract href attributes
hrefs = [link.get_attribute('href') for link in links]
print(hrefs)

# Remember to close the driver after your tasks are done
driver.quit()
