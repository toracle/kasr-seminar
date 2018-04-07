# -*- coding: utf-8 -*-


from .base import Crawler
from .pyeongan import PyeonganArticleList


if __name__ == '__main__':
    article_list_class = [PyeonganArticleList]

    for list_class in article_list_class:
        crawler = Crawler(list_class)
        crawler.fetch()
