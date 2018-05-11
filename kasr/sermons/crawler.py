# -*- coding: utf-8 -*-

import argparse
from .crawlers.base import Crawler
from .crawlers.pyeongan import PyeonganArticleList
from .crawlers.buksuwon import BuksuwonArticleList
from .crawlers.scch import ScchArticleList
from kasr.godtalk.crawler import GodtalkSisaArticleList
from kasr.news.crawlers.chtoday import ChTodayArticleList
from kasr.news.crawlers.newsnjoy import NewsnJoyArticleList


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dataset', nargs='*')
    args = parser.parse_args()

    article_class_id_to_class = {
        'pyeongan': PyeonganArticleList,
        'buksuwon': BuksuwonArticleList,
        'scch': ScchArticleList,
        'godtalk-sisa': GodtalkSisaArticleList,
        'chtoday': ChTodayArticleList,
        'newsnjoy': NewsnJoyArticleList,
    }

    if args.dataset:
        article_list_class = [article_class_id_to_class.get(dataset_name) for dataset_name in args.dataset if dataset_name is not None]
    else:
        article_list_class = article_class_id_to_class.values()

    for list_class in article_list_class:
        crawler = Crawler(list_class)
        crawler.fetch()
