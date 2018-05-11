# -*- coding: utf-8 -*-

from kasr.sermons.crawlers.base import ArticleList
from kasr.sermons.crawlers.base import Article


class ScchArticle(Article):
    def __init__(self, url):
        super(ScchArticle, self).__init__(url)
        self.article_src = 'scch'

    def get_uid(self, url):
        query_params = self.parse_query_params(url)
        return query_params.get('num')

    def parse_text(self, soup):
        element = soup.select('#AB_viewContent')[0]
        return element.text.strip()


class ScchArticleList(ArticleList):
    def __init__(self):
        self.src = 'scch'
        self.domain = 'http://www.scch1.kr'
        self.base_url = self.domain + '/main/sub.html?page={}&boardID=www8&keyfield=&key=&bCate='
        self.page = 1

    def get_page_url(self):
        url = self.base_url.format(self.page)
        self.page += 1
        return url

    def has_next(self, soup):
        tags = soup.select('.center_Bottom > a > img')
        for tag in tags:
            if tag.get('src', '').endswith('rightarrow1.png'):
                return True
        return False

    def parse(self, soup):
        tags = soup.select('.smListType1 > .boardList td.textLeft > a')
        for tag in tags:
            yield '{}{}'.format(self.domain, tag.get('href'))

    def get_article(self, url):
        return ScchArticle(url)
