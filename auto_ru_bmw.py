
#парсер тру бмв


from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium import webdriver
import json


def get_bmw(url):
    driver = webdriver.Chrome(
        # путь до драйвера селениум
        executable_path=""
    )
    driver.maximize_window()
    try:
        driver.get(url=url)
        time.sleep(5)

        with open("auto_ru.html","w") as file:
            file.write(driver.page_source)
  
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

    #после скачки html на стр коммент. код запроса
    #открываем html файл
with open("") as file:
    src = file.read()

    result_list = []
    soup = BeautifulSoup(src, "lxml")
    item_title = soup.find_all("h3",class_="ListingItemTitle")
    for item in item_title:
        item_url = item.find("a").get("href")


    item_name = soup.find_all("h3",class_="ListingItemTitle")
    for item in item_name:
        item_name = item.get_text()



        result_list.append(
            {
                "auto_name":item_name,
                "auto_url":item_url      
            }
        )



    with open("auto_ru_bmw.json", 'w') as file:
        json.dump(result_list, file, indent=4, ensure_ascii=False)




get_bmw("")

