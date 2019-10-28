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
    rate_list.sort(key=lambda x: -x[1])
    return rate_list


def visualize_common_words(topic):
    words = get_common_words(topic)
    for w in words[3:6]:
        print(w[0])
    return words


def main():
    topic = input("Topic: ")
    visualize_common_words(topic)

#Получаю ссылки на соседние страницы.
def get_http(topic):
    html_content = get_topic_page(topic)
    soup = BS(html_content, "html.parser")
    result = soup.find_all("a", class_=None, href=re.compile("^/wiki/"))
    result = [link.get("href") for link in result]
    result = [re.sub("/wiki/", "", link) for link in result]
    return result


topics = get_http(input("ВВедите значение"))[:10]
# Получение списка слов из ссылок 
li=[]
for topic in topics:
    li.append(get_common_words(topic)[:3])
    # for word in li:                            # Альтернативное решение(Добавления слов,в список)
    #     li2.append(word[0])





print(li)
print(len(li))
