# -*- coding: utf-8 -*-

import os
import requests
from bs4 import BeautifulSoup


class ArticleList(object):
    def get_article_links(self):
        while True:
            url = self.get_page_url()
            self.next()
            response = requests.get(url)
            content = response.content
            soup = BeautifulSoup(content, 'html5lib')
            if not self.has_next(soup):
                return
            for link in self.parse(soup):
                yield link

    def __iter__(self):
        for link in self.get_article_links():
            print(link)
            yield self.get_article(link)


class Article(object):
    def __init__(self, url):
        self.url = url
        self.uid = self.get_uid(url)

    def get_content(self):
        response = requests.get(self.url)
        content = response.content
        soup = BeautifulSoup(content, 'html5lib')
        text = self.parse_text(soup)
        return text

    def get_local_path(self):
        return os.path.join('data', self.article_src, '{}.txt'.format(self.uid))


class Crawler(object):
    def __init__(self, list_class):
        self.list_class = list_class

    def fetch(self):
        article_list = self.list_class()
        for article in article_list:
            local_path = article.get_local_path()
            dirname = os.path.dirname(local_path)
            if not os.path.isdir(dirname):
                os.makedirs(dirname)

            if os.path.isfile(local_path):
                continue

            content = article.get_content()
            with open(local_path, 'w') as fout:
                fout.write(content)
