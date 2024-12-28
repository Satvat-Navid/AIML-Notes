'''
Real-World Example: Multithreading for I/O-bound Tasks
Scenario: Web Scraping
Web Scraping often involves making numerous network requests to 
fetch web pages. There tasks are I/O bound because they spend a lot of
time waiting for responses from servers. Multithreading can significantly
improve the performance by allowing multiple web pages to be fetched concurrently;
'''

'''
https://numpy.org/doc/2.1/reference/generated/numpy.median.html#numpy-median

https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html

https://seaborn.pydata.org/generated/seaborn.relplot.html
'''

import threading
import requests
from bs4 import BeautifulSoup

urls = [
'https://numpy.org/doc/2.1/reference/generated/numpy.median.html#numpy-median',

'https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html',

'https://seaborn.pydata.org/generated/seaborn.relplot.html'
]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content, 'html.parser')
    print(f'Fetched {(len(soup.text))} characters from {url}')

threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched")