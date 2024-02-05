from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


class OLXScraping:
    def __init__(self, url, options):
        self.url = url
        self.options = options
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.options)

    def scrape_data(self):
        self.driver.get(self.url)
        main_link_element = self.driver.find_element(By.ID, 'ssr_canonical')
        main_link = main_link_element.get_attribute('href')

        ad_elements = self.driver.find_elements(By.XPATH, "//div[@data-cy='l-card' and @data-testid='l-card']")

        ad_data = []
        try: 
         for ad_element in ad_elements:
           ad_link = ad_element.find_element(By.TAG_NAME, 'a').get_attribute('href')
           ad_id = ad_element.get_attribute('id')
        
           ad_price = ad_element.find_element(By.XPATH, ".//p[@data-testid='ad-price']").text.strip()
    
           ad_loc = ad_element.find_element(By.XPATH, 
                                         ".//p[@data-testid='location-date']").text.strip().split(' - ')
           ad_city = ad_loc[0] # 'Район': ad_district
           ad_date_time = ad_loc[1] if len(ad_loc) == 2 else None

           ad_area = ad_element.find_element(By.XPATH, ".//span[contains(@class, 'css-643j0o')]").text.strip().split()
           ad_area_numeric = ad_area[0] if len(ad_area) == 2 else None

           ad_data.append({'Основне посилання': main_link, 
                        'ID оголошення': ad_id, 
                        'Посилання на оголошення': ad_link, 
                        'Ціна': ad_price,
                        'Місто': ad_city,
                        'Дата і час публікації': ad_date_time, 
                        'Загальна площа': ad_area_numeric})
        except Exception as e:
               print(f"Помилка: {e}") 
        
        return pd.DataFrame(ad_data)

    def quit_driver(self):
        self.driver.quit()
