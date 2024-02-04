from web_scrap import OLXScraping
from selenium import webdriver

url = "https://www.olx.ua/uk/nedvizhimost/kvartiry/"
options = webdriver.ChromeOptions()

olx_scraper = OLXScraping(url, options=options)
df = olx_scraper.scrape_data()
print(df)

filename = "data.csv"
df.to_csv(filename, index=False)

olx_scraper.quit_driver()
