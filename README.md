## Level 3_Web Scraping with Selenium & Python

[source] [Квартири: ціни на квартири в Україні на OLX.ua](https://www.olx.ua/uk/nedvizhimost/kvartiry/)

![t1](https://github.com/Daria-jk8/OLXScraping/assets/92945302/bfafa712-df5c-4216-bffc-dd0129fa3a51)


```bash
Level3/  
│   ├─requirements.txt             # packages & libraries needed to work
│   ├─ main.py  
│   ├─ web_scrap.py                 # class OLXScraping  
│   ├─ savetogoogle.py  
│   ├─ credentials.json
```
## SUMMARY

- create: token.json, data.csv, 'OLXScrap' spreadsheets.

<u>PROS</u>

- [x] отримана часткова інформація, включаючи ID, ціну, місце розташування, час публікації та площу.

<u>CONS</u>

- [ ] парсинг лише 52 оголошень на одній сторінці; не реалізовано циклічість для переходу через кілька сторінок;
- [ ] перехід із каталогу на nextpage(оголошення) за доп click();
- [ ] не отримано дані: поверх, поверховість;
- [ ] не зроблено Exploratory Data Analysis(EDA).

GitHub Repository [OLXScraping](https://github.com/Daria-jk8/OLXScraping)

Google Sheet [OLXScrap](https://docs.google.com/spreadsheets/d/1qg6A6ySbRXOs3RpkUGOKezYwbRKeQ6fHFLFgt2IgZBk/edit?usp=sharing)