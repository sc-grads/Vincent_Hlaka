import requests
from bs4 import BeautifulSoup
import openpyxl

url = 'https://www.imdb.com/search/title?release_date=2019-01-01,2019-12-31&sort=num_votes,desc&ref_=adv_prv'
page = requests.get(url)
print(page.ok)

soup = BeautifulSoup(page.content, 'html.parser')
content = soup.find_all('div', class_='lister-item-content')
movies = list()

for item in content:
    name = item.h3.a.text
    rating = item.strong.text
    movies.append((name, rating))

print(movies)


wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'IMDB Movies'
sheet['A1'] = 'Year'
sheet['B1'] = 'Movie'

for movie in movies:
    sheet.append(movie)

wb.save('movies-2019.xlsx')