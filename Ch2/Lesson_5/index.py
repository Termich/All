import re
import requests
from bs4 import BeautifulSoup as BS
from wiki_requests import get_topic_page
from wiki_requests import get_link



def get_topic_words(topic):
    html_content = get_topic_page(topic)
    words = re.findall("[а-яА-Я\-\']{3,}", html_content)
    return words

def get_common_words(topic):
    words_list = get_topic_words(topic)
    rate = {}
    for word in words_list:
        if word in rate:
            rate[word] += 1
        else:
            rate[word] = 1
    rate_list = list(rate.items())
    rate_list.sort(key = lambda x: -x[1])
    return rate_list

def visualize_common_words(topic):
    words = get_common_words(topic)
    for w in words[3:6]:
        print(w[0])
    return words

def main():
    topic = input("Topic: ")
    visualize_common_words(topic)


def get_http(topic):
    html_content = get_topic_page(topic)
    text = requests.get(html_content).text
    data = BS(text,"html.parser")
    result = data.find_all("div id",class_="mw-parser-output",text="/wiki/")
    return result



#Fink = print(visualize_common_words(input("ВВедите значение")))
print(get_http(input("ВВедите значение")))


# li = re.findall('<p><a href="/wiki/([\d\s]+)"></a></p>',Fink)
# print(li)
#
# with open (get_link,encoding='utf-8') as f:
#     s = f.read()
# soup = BS(s,"html.parser")
# print(soup)

# t= soup.find_all("div id",class_="mw-parser-output",text="/wiki/")
# print(t)





