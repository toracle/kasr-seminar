# -*- coding: utf-8 -*-

from kasr.sermons.crawlers.base import ArticleList
from kasr.sermons.crawlers.base import Article


class BuksuwonArticle(Article):
    def __init__(self, url):
        super(BuksuwonArticle, self).__init__(url)
        self.article_src = 'buksuwon'

    def get_uid(self, url):
        params = url[url.find('?'):]
        kv_list = params.split('&')
        for kv in kv_list:
            k, v = kv.split('=')
            if k == 'num':
                return v

    def parse_text(self, soup):
        element = soup.select('#AB_viewContent')[0]
        return element.text.strip()


class BuksuwonArticleList(ArticleList):
    def __init__(self):
        self.domain = 'http://buksuwon.org'
        self.base_url = self.domain + '/main/sub.html?boardID=www68&page={}'
        self.page_url = self.domain + '/core/anyboard/content.html?Mode=view&boardID=www68&num={}'
        self.page = 1

    def get_page_url(self):
        url = self.base_url.format(self.page)
        print(url)
        self.page += 1
        return url

    def has_next(self, soup):
        tags = soup.select('.pageNext')
        return len(tags) > 0

    def parse(self, soup):
        tags = soup.select('.tdLeftSubject > a')
        for tag in tags:
            num = tag.get('onclick').split(',')[1][2:-1]
            yield self.page_url.format(num)

    def get_article(self, url):
        return BuksuwonArticle(url)
