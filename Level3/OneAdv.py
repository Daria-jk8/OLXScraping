from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


url = "https://www.olx.ua/d/uk/obyavlenie/prodazh-abo-obmn-1-km-kvartiri-r-n-kazbet-IDUmRNs.html"
driver = webdriver.Chrome()
driver.get(url)

try:
    link = driver.find_element(By.XPATH, "//link[@rel='canonical']").get_attribute('href')
    title = driver.title
    price = driver.find_element(By.CLASS_NAME, 'css-12vqlj3').text.strip()
    floor1 = driver.find_element(By.XPATH, "//*[contains(text(), 'Поверх')]").text.split(':')[-1].strip() 
    floor2 = driver.find_element(By.XPATH, "//*[contains(text(), 'Поверховість')]").text.split(':')[-1].strip() 
    area = driver.find_element(By.XPATH, "//*[contains(text(), 'Загальна площа')]").text.split(':')[-1].strip() 
    city = driver.find_element(By.CLASS_NAME, 'css-1cju8pu.er34gjf0').text.strip().replace(',', '')
   
    print(f"Посилання: {link}")
    print(f'Оголошення: {title}')
    print(f"Ціна: {price}")
    print(f"Номер поверху: {floor1}")
    print(f'Поверховість: {floor2}')
    print(f'Загальна площа: {area}')
    print(f'Місцезнаходження: {city}')

    data = {'Посилання': [link],
            'Оголошення': [title],
            'Ціна': [price], 
            'Номер поверху': [floor1], 
            'Поверховість': [floor2], 
            'Загальна площа': [area], 
            'Місцезнаходження': [city]}
    
    df = pd.DataFrame(data)
    df.to_csv('OneAdv.csv', index=False, encoding='utf-8')

    print("Дані успішно записано в CSV-файл") 
 
finally:
    driver.quit()
