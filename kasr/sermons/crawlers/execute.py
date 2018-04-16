# -*- coding: utf-8 -*-


from .base import Crawler
from .pyeongan import PyeonganArticleList
from .buksuwon import BuksuwonArticleList


if __name__ == '__main__':
    # article_list_class = [PyeonganArticleList]
    article_list_class = [BuksuwonArticleList] 

    for list_class in article_list_class:
        crawler = Crawler(list_class)
        crawler.fetch()
