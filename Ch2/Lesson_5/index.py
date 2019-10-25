import re
from wiki_requests import get_topic_page


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
    for w in words[100:110]:
        print(w[0])

def main():
    topic = input("Topic: ")
    visualize_common_words(topic)
