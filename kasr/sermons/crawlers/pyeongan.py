# -*- coding: utf-8 -*-

from kasr.sermons.crawlers.base import ArticleList
from kasr.sermons.crawlers.base import Article


class PyeonganArticle(Article):
    def __init__(self, url):
        super(PyeonganArticle, self).__init__(url)
        self.article_src = 'pyeongan'

    def get_uid(self, url):
        query_params = self.parse_query_params(url)
        return query_params.get('uid')

    def parse_text(self, soup):
        element = soup.select('.content-view')[0]
        return element.text.strip()


class PyeonganArticleList(ArticleList):
    def __init__(self):
        self.src = 'pyeongan'
        self.domain = 'http://pyeong-an.com'
        self.base_url = self.domain + '/설교-말씀-원고/?pageid={}'
        self.page = 1

    def get_page_url(self):
        url = self.base_url.format(self.page)
        self.page += 1
        return url

    def has_next(self, soup):
        tags = soup.select('.last-page')
        return len(tags) > 0

    def parse(self, soup):
        tags = soup.select('.kboard-list-title > a')
        for tag in tags:
            yield '{}{}'.format(self.domain, tag.get('href'))

    def get_article(self, url):
        return PyeonganArticle(url)
