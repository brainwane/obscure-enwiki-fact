#/usr/bin/python
# GPL'd; see LICENSE.
# Copyright 2013 Sumana Harihareswara
# For a Wikipedia article: find the most obscure fact.

import requests
import random

def choosephrase():
    a = raw_input("What topic do you want to know about? ")
    return a

def APIcall(topic):
    headers =  {'User-Agent': 'obscure-fact project (https://github.com/brainwane/), using Python requests library'}
    URI = "http://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&explaintext=&titles=%s&redirects=" % topic
    r = requests.get(URI, headers=headers)
    return r.json()

def findsentence(response):
    for elem in response["query"]["pages"]:
        pagetext = response["query"]["pages"][elem]["extract"]
    sectionlist = pagetext.split("==\n==")
    section = random.choice(sectionlist)
    sentencelist = section.split(". ")
    sentence = random.choice(sentencelist)
    return sentence

def run():
    # take a string
    # Do the API call
    # Find a sentence in the longest section
    # spit out sentence
    topic = choosephrase()
    page = APIcall(topic)
    result = findsentence(page)
    print(result)

if __name__ == "__main__":
    run()
