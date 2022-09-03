import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time

# your secret credentials
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
DRIVER_PATH = os.environ.get("DRIVER_PATH")

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3243287332&f_AL=true&f_TPR=r2592000&" \
      "f_WT=2&geoId=92000000&keywords=data%20analytics%20python&location=Worldwide&refresh=true"

s = Service(DRIVER_PATH)
print("Starting driver")
driver = webdriver.Chrome(service=s)
driver.get(URL)
driver.maximize_window()

time.sleep(3)
print("Logging in")
driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]").click()
driver.find_element(By.CSS_SELECTOR, "#username").send_keys(EMAIL)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys(PASSWORD)
driver.find_element(By.CSS_SELECTOR, ".login__form_action_container ").click()

time.sleep(5)

# get a list of all the element's in the sidebar

all_list_items = driver.find_elements(By.CLASS_NAME, "occludable-update")

for job in all_list_items:
    # my_list = ""
    try:
        job.click()
        time.sleep(2)
        save_job = driver.find_element(By.CSS_SELECTOR, ".jobs-save-button")
        my_list = save_job.text.split("\n")[0]
        print(my_list)
        if my_list != "Saved":
            save_job.click()
            print("Job saved!")
            time.sleep(2)
            btn_close = driver.find_element(By.CLASS_NAME, "artdeco-button__icon")
            btn_close.click()
        else:
            continue

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(3)
# driver.quit()
