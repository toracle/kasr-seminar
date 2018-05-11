# -*- coding: utf-8 -*-

from kasr.sermons.crawlers.base import ArticleList
from kasr.sermons.crawlers.base import Article


class GodtalkSisaArticle(Article):
    def __init__(self, url):
        super(GodtalkSisaArticle, self).__init__(url)
        self.article_src = 'godtalk-sisa'

    def get_uid(self, url):
        query_params = self.parse_query_params(url)
        return query_params.get('document_srl')

    def parse_text(self, soup):
        element = soup.select('.xe_content')[0]
        return element.text.strip()


class GodtalkSisaArticleList(ArticleList):
    def __init__(self):
        self.src = 'godtalk-sisa'
        self.domain = 'http://www.godntalk.com'
        self.base_url = self.domain + '/index.php?mid=sisa&page={}'
        self.page = 1

    def get_page_url(self):
        url = self.base_url.format(self.page)
        self.page += 1
        return url

    def has_next(self, soup):
        current_selected = soup.select('.pagination > strong')[0]
        current_page = int(current_selected.text)

        next_link = soup.select('.pagination > .next')[0]
        next_page = int(next_link['href'].split('=')[-1])

        if current_page == next_page:
            return False
        return True

    def parse(self, soup):
        tags = soup.select('.board_list td.title > a')
        for tag in tags:
            if tag.get('class'):
                continue
            yield '{}{}'.format(self.domain, tag.get('href'))

    def get_article(self, url):
        return GodtalkSisaArticle(url)
