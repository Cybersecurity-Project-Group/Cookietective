from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.request import urlopen
import sys
import logging
import time
import sqlite3

# set up logging config
logging.basicConfig(level=logging.INFO, format="%(levelname)s (%(asctime)s): %(message)s")

# manage command-line args
file = open(sys.argv[1])
urls = file.readlines()

url_start_index = int(sys.argv[2])
url_end_index = int(sys.argv[3])

# set up request interval
sleepTime = 1

# provide path to browser driver
PATH = "chromedriver"

# set up options for browser
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
opts.add_argument("--incognito")

# initiate browser driver
chromeExecutable = webdriver.chrome.service.Service(executable_path=PATH)
driver = webdriver.Chrome(service=chromeExecutable, options=opts)

# connect to SQLite database
conn = sqlite3.connect("scraped_urls.db")
cursor = conn.cursor()

# create table for scraped urls
cursor.execute(
    "CREATE TABLE IF NOT EXISTS scraped_urls (url TEXT PRIMARY KEY)"
)
conn.commit()

def scrape_links(url):

    # check URL if already scraped
    cursor.execute("SELECT * FROM scraped_urls WHERE url = ?", (url,))
    if cursor.fetchone():
        logging.info("Skipping: %s", url)
        return 
    
    logging.info("Scraping: %s", url)

    # add URL to scraped_urls table
    cursor.execute("INSERT INTO scraped_urls VALUES (?)", (url,))
    conn.commit()

    # send request to URL
    driver.get(url)

    try:
        # wait for HTML element with anchor tag to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "a"))
        )

        # locate HTML anchor tags
        links = driver.find_elements(By.TAG_NAME, "a")
        for link in links:
            # obtain links
            href = link.get_attribute("href")
            if href and href.startswith("http"):
                scrape_links(href)
                
    except Exception as e:
        # log error and continue scraping
        logging.debug("Error scraping %s: %s", url, e)

    finally:
        logging.debug("Done scraping: %s", url)


# prompt user for initial URL to scrape
for i in range(url_start_index, url_end_index):
    scrape_links("https://" + urls[i])

# terminate browser
driver.quit()