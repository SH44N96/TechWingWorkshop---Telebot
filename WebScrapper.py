
import requests
from bs4 import BeautifulSoup

def get_description(sign):
    url = 'https://www.ganeshaspeaks.com/horoscopes/daily-horoscope/' + sign
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    results = soup.find(id = 'daily')
    paragraph = results.find(class_ = 'margin-top-xs-0')
    return paragraph.get_text()
