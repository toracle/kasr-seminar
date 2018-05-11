# -*- coding: utf-8 -*-

from kasr.sermons.crawlers.base import ArticleList
from kasr.sermons.crawlers.base import Article


class ChTodayArticle(Article):
    def __init__(self, url):
        super(ChTodayArticle, self).__init__(url)
        self.article_src = 'chtoday'

    def get_uid(self, url):
        return url.split('/')[-1]

    def parse_text(self, soup):
        element = soup.select('#article_body')[0]
        text = element.text.strip()
        return text[:text.find('<저작권자')]


class ChTodayArticleList(ArticleList):
    def __init__(self):
        self.src = 'chtoday'
        self.domain = 'http://www.christiantoday.co.kr'
        self.base_url = self.domain + '/archives/page{}.htm'
        self.page = 1

    def get_page_url(self):
        url = self.base_url.format(self.page)
        self.page += 1
        return url

    def has_next(self, soup):
        buttons = soup.select('.bx-page > a[onclick^=document]')
        for button in buttons:
            if button.text == '다음':
                return True
        return False

    def parse(self, soup):
        tags = soup.select('.grid-main-article4 > .list > .art-title3 > a')
        for tag in tags:
            if not tag.get('href') or tag.get('href').startswith('http'):
                continue
            yield '{}{}'.format(self.domain, tag.get('href'))

    def get_article(self, url):
        return ChTodayArticle(url)
