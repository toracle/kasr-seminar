# -*- coding: utf-8 -*-

import os
import requests
from bs4 import BeautifulSoup
from kasr import exceptions as exc


def parse_query_params(url):
    params = url[url.find('?')+1:]
    kv_list = params.split('&')
    return dict([kv.split('=') for kv in kv_list])


class ArticleList(object):
    def read_bookmarked_page(self):
        bookmark_path = os.path.join('data', '{}.txt'.format(self.src))
        if not os.path.isfile(bookmark_path):
            return 1

        try:
            with open(bookmark_path) as fin:
                return int(fin.read())
        except Exception:
            return 1

    def write_bookmark_page(self, page):
        bookmark_path = os.path.join('data', '{}.txt'.format(self.src))
        with open(bookmark_path, 'w') as fout:
            fout.write('{}'.format(page))

    def get_article_links(self):
        self.page = self.read_bookmarked_page()
        while True:
            url = self.get_page_url()
            print('List:', url)
            response = requests.get(url)
            content = response.content
            soup = BeautifulSoup(content, 'html5lib')
            for link in self.parse(soup):
                yield link
            self.write_bookmark_page(self.page)
            if not self.has_next(soup):
                return

    def __iter__(self):
        for link in self.get_article_links():
            yield self.get_article(link)


class Article(object):
    def __init__(self, url):
        self.url = url
        self.uid = self.get_uid(url)

    def parse_query_params(self, url):
        return parse_query_params(url)

    def get_content(self):
        response = requests.get(self.url)
        content = response.content
        soup = BeautifulSoup(content, 'lxml')
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

            print('Visit article:', article.url)
            try:
                content = article.get_content()
                with open(local_path, 'w') as fout:
                    fout.write(content)
            except exc.NoContent:
                print('  No content')
