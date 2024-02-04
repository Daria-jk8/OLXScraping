from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


class OLXScraping:
    def __init__(self, url, options):
        self.url = url
        self.options = options
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.options)

    def scrape_data(self):
        self.driver.get(self.url)
        advs = self.driver.find_elements(By.CLASS_NAME, "css-1sw7q4x")

        advs_list = []
        for adv in advs:
            try:
                id = (
                    WebDriverWait(adv, 10)
                    .until(
                        EC.presence_of_element_located(
                            (By.XPATH, './/div[@data-testid="l-card"]')
                        )
                    )
                    .get_attribute("id")
                    .strip()
                )
                price = (
                    WebDriverWait(adv, 10)
                    .until(
                        EC.presence_of_element_located(
                            (By.XPATH, ".//a/div/div/div[2]/div[1]/p")
                        )
                    )
                    .text.strip()
                )
                location_and_time = (
                    WebDriverWait(adv, 10)
                    .until(
                        EC.presence_of_element_located(
                            (By.XPATH, ".//a/div/div/div[2]/div[3]/p")
                        )
                    )
                    .text.strip()
                )

                location_parts = location_and_time.split(" - ")
                location = location_parts[0].strip()
                publish_time = location_parts[1].strip()

                area = (
                    WebDriverWait(adv, 10)
                    .until(
                        EC.presence_of_element_located(
                            (By.XPATH, ".//a/div/div/div[2]/div[3]/div")
                        )
                    )
                    .text.strip()
                )
                adv_item = {
                    "ID": id,
                    "Price": price,
                    "Location": location,
                    "Publish_time": publish_time,
                    "Area": area,
                }
                advs_list.append(adv_item)
            except Exception as e:
                print(f"Error: {e}")

        return pd.DataFrame(advs_list)

    def quit_driver(self):
        self.driver.quit()
