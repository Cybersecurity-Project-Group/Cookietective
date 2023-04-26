from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import logging
import datetime

# set up logging config
logging.basicConfig(level=logging.INFO, format="%(levelname)s (%(asctime)s): %(message)s")
logging.info("start")

# manage command-line args
file = open(sys.argv[1])
urls = file.readlines()

url_start_index = int(sys.argv[2])
url_end_index = int(sys.argv[3])

# set up scan time
scan_time = 15
driver_wait_time = 5

# set up options for browser
opts = webdriver.FirefoxOptions()
opts.add_argument("--private")
opts.add_argument("--headless")
opts.set_preference('javascript.enabled', False)
opts.set_preference('network.trr.mode', 5)

# initiate browser driver
driver = webdriver.Firefox(options=opts)

# data structures for BFS
visited = set()
queue = []

def scrape_links(url, current_time, stop_time):
    # check timer
    if current_time >= stop_time:
        return
    
    # visit first node
    visited.add(url)
    queue.append(url)
    
    while not queue.empty():
        h = queue.pop(0)
        logging.info(f"Scanning: {h}")

        # send request to URL
        driver.get(h)

        try:
            # wait for HTML element with anchor tag to load
            WebDriverWait(driver, driver_wait_time).until(
                EC.presence_of_element_located((By.TAG_NAME, "a"))
            )

            # locate HTML anchor tags
            links = driver.find_elements(By.TAG_NAME, "a")
            for neighbor in links:
                # obtain links
                href = neighbor.get_attribute("href")
                if href and href.startswith("http"):
                    queue.append(neighbor)
        
        except Exception as e:
            # log error and continue scraping
            logging.debug(f"Error scraping {url}: {e}")
            return

    logging.debug(f"Done scanning: {url}")


# iterate thorugh list of URLs to scrape
for i in range(url_start_index, url_end_index):
    logging.debug(f"start time for {urls[i]}: {datetime.datetime.now()}")

    link = "http://" + urls[i]
    scrape_links(link, datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(seconds=scan_time))

    logging.debug(f"end time for {urls[i]}: {datetime.datetime.now()}")

# terminate browser
driver.quit()