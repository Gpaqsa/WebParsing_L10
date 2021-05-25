from random import randint
from time import sleep

import requests
from bs4 import BeautifulSoup

file = open('Moves.csv', 'w',  encoding="utf-8",  newline='\n')
file.write('Title, Title_En, year\n')

ind = 1
while ind < 60:
    url = "https://geo.saitebi.ge/genre/26/1/Music.html" + str(ind)
    conn = requests.get(url)
    print(conn.status_code)

    content = conn.text

    soup = BeautifulSoup(content, 'html.parser')

    all_movies_block = soup.find('div', {'id': 'content'})
    # print(all_movies_block)
    all_movies = all_movies_block.find_all('div', class_='movie-items-wraper')
    # print(all_movies)

    for one in all_movies:
        title = one.a.h4.text
        en_title = one.find('h4', class_='b').text
        year = one.a.span.text
        print(title + ', ', en_title, year)
        file.write(title + ',' + en_title + ',' + year + '\n')
    ind += 15
    sleep(randint(22, 30))
