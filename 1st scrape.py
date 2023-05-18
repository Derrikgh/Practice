from bs4 import BeautifulSoup
import requests
import csv
from tkinter import *
from tkinter import ttk

window=Tk()

scrape = requests.get('https://freekidsbooks.org/')
soup = BeautifulSoup(scrape.text, 'html.parser')

books = soup.findAll('div', attrs={'class':'book_header'})

len(books)

file = open('1st_scrape.csv', 'w')
writer = csv.writer(file)
writer.writerow(['books'])

for book in books:
 print(book)
 writer.writerow([book.text])
file.close()

window.mainloop
