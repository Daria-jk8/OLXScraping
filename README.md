## Level 3_Web Scraping with Selenium & Python

[source] [Квартири: ціни на квартири в Україні на OLX.ua](https://www.olx.ua/uk/nedvizhimost/kvartiry/)

![t1](https://github.com/Daria-jk8/OLXScraping/assets/92945302/bfafa712-df5c-4216-bffc-dd0129fa3a51)


```bash
Level3/  
│   ├─requirements.txt             # packages & libraries needed to work
│   ├─ main.py  
│   ├─ web_scrap.py                # class OLXScraping  
│   ├─ savetogoogle.py  
│   ├─ credentials.json
│   ├─ OneAdv.py                   # for one ad
|   ├─ EDA.ipynb                   
|   ├─ EDA.py
|   ├─ Data2.csv                  # місто | район
|   ├─ Data.csv            
│
│─ README.md
```
## SUMMARY

- create: token.json, OneAdv.csv, Data.csv, 'OLXScrap' spreadsheets.

<u>PROS</u>

- [x] отримана часткова інформація: link, ID, advertising link, price, location [city, region], date and time of publication, total area of the apartment.
- [x] додані дані для одного оголошення (ціна, поверх, поверховість, населений пункт, площа),
- [x] виконано частковий Exploratory Data Analysis(EDA).

![Screenshot 2024-02-07 at 09 18 27](https://github.com/Daria-jk8/OLXScraping/assets/92945302/6d0fd012-2743-4222-9a0c-726319ebf59a)


<u>CONS</u>

- [ ] парсинг лише 52 оголошень на одній сторінці; не реалізовано циклічість для переходу через кілька сторінок;
- [ ] перехід із каталогу на nextpage(оголошення) за доп click();
- [ ] не отримано дані: поверх, поверховість.

GitHub Repository [OLXScraping](https://github.com/Daria-jk8/OLXScraping)

Google Sheet [OLXScrap](https://docs.google.com/spreadsheets/d/1qg6A6ySbRXOs3RpkUGOKezYwbRKeQ6fHFLFgt2IgZBk/edit?usp=sharing)

Tableau Public [SalesAnalysis](link)
