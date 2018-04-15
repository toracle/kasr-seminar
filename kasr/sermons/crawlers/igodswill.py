# -*- coding: utf-8 -*-

from kasr.sermons.crawlers.base import ArticleList
from kasr.sermons.crawlers.base import Article


class GodsWillArticle(Article):
    def __init__(self, url):
        super(GodsWillArticle, self).__init__(url)
        self.article_src = 'igodswill'

    def get_uid(self, url):
        params = url[url.find('?'):]
        kv_list = params.split('&')
        for kv in kv_list:
            k, v = kv.split('=')
            if k == 'document_srl':
                return v

    def parse_text(self, soup):
        element = soup.select('.xe_content')[0]
        return element.text.strip()


class GodsWillArticlelist(ArticleList):
    def __init__(self):
        self.domain = 'http://www.godswill.or.kr'
        self.base_url = self.domain + 'index.php?mid=media_{}&page={}'
        self.year = 2003
        self.page = 1

    def get_page_url(self):
        url = self.base_url.format(self.year, self.page)
        return url

    def next(self):
        self.page += 1

    def has_next(self, soup):
        tags = soup.select()
