from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Инициализация WebDriver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Открытие страницы
driver.get('https://www.youtube.com/results?search_query=radeon+rx+580+8gb')

# Получение содержимого страницы после загрузки JavaScript
page_source = driver.page_source

# Здесь вы можете использовать BeautifulSoup для парсинга содержимого страницы
soup = BeautifulSoup(page_source, 'html.parser')
# products = soup.find_all('meta',attrs={'itemprop':'price'})

links = soup.find_all('a',id=('video-title'),limit=5)
for link in links:
    print('Link:', link.get('href'))


# # Извлечение текста из элемента
# paragraph = soup.find_all('p')
# for p in paragraph:
#     print('Paragraph:', p.text)

# weather_li = soup.find_all(class_='style_scope')
# for w in weather_li:
#     print(w.text, end='\n')

# Закрытие WebDriver
driver.quit()

