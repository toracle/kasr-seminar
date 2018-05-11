# -*- coding: utf-8 -*-

from kasr.sermons.crawlers.base import ArticleList
from kasr.sermons.crawlers.base import Article
from kasr.sermons.crawlers.base import parse_query_params
from kasr import exceptions as exc


class NewsnJoyArticle(Article):
    def __init__(self, url):
        super(NewsnJoyArticle, self).__init__(url)
        self.article_src = 'newsnjoy'

    def get_uid(self, url):
        query_params = self.parse_query_params(url)
        return query_params.get('idxno')

    def parse_text(self, soup):
        elements = soup.select('#articleBody')
        if not elements:
            raise exc.NoContent()
        element = elements[0]
        return element.text.strip()


class NewsnJoyArticleList(ArticleList):
    def __init__(self):
        self.src = 'newsnjoy'
        self.domain = 'http://www.newsnjoy.or.kr'
        self.base_url = self.domain + '/news/articleList.html?page={}&view_type=tm'
        self.page = 1

    def get_page_url(self):
        url = self.base_url.format(self.page)
        self.page += 1
        return url

    def has_next(self, soup):
        current_selected = soup.select('.page-nav > .wb > a.on')[0]
        current_page = int(current_selected.text)

        next_link = soup.select('.page-nav .next-btn')[0]
        query_params = parse_query_params(next_link['href'])
        next_page = int(query_params['page'])

        if current_page == next_page:
            return False
        return True

    def parse(self, soup):
        tags = soup.select('#aticle-list-tm .aticle-list > a')
        for tag in tags:
            yield '{}{}'.format(self.domain, tag.get('href'))

    def get_article(self, url):
        return NewsnJoyArticle(url)
