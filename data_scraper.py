import requests
from bs4 import BeautifulSoup
import pprint


res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def filter(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'links': href, 'votes': points})
    return sort_by_votes(hn)



pprint.pprint(filter(mega_links, mega_subtext))



# '.' = class   <css selectors
# '#' = id 