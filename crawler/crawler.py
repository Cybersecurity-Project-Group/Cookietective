from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# provide path to browser driver
PATH = "chromedriver"

# set up options for browser
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
opts.add_argument("--incognito")

# initiate browser driver
chromeExecutable = webdriver.chrome.service.Service(executable_path=PATH)
driver = webdriver.Chrome(service=chromeExecutable, options=opts)

# send request to URL
url = input("Enter URL: ")
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
        if href:
            print(href)
except:
    # raise exception if error
    raise("error locating link")

finally:
    # terminate browser
    print("\ndone")
    driver.quit()
