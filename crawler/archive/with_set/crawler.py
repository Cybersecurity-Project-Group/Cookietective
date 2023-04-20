from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

# set up request interval
sleepTime = 1

# set up logging config
logging.basicConfig(level=logging.INFO, format="%(levelname)s (%(asctime)s): %(message)s")

# provide path to browser driver
PATH = "chromedriver"

# set up options for browser
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
opts.add_argument("--incognito")

# initiate browser driver
chromeExecutable = webdriver.chrome.service.Service(executable_path=PATH)
driver = webdriver.Chrome(service=chromeExecutable, options=opts)

# set up set to keep track of scraped URLs
scrapedUrls = set()

def scrape_links(url):

    # recursively scrape links found on a web page -- skip URL if already scraped
    if url in scrapedUrls:
        logging.info("Skipping: %s", url)
        return

    logging.info("Scraping: %s", url)
    scrapedUrls.add(url)
    
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
url = input("Enter URL to scrape: ")
scrape_links(url)

# terminate browser
driver.quit()