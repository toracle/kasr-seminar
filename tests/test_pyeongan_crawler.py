# -*- coding: utf-8 -*-

from kasr.sermons.crawlers.pyeongan import PyeonganArticleList
from kasr.sermons.crawlers.pyeongan import PyeonganArticle
from bs4 import BeautifulSoup


def test_article_list_get_page_url():
    al = PyeonganArticleList()
    url = al.get_page_url()
    assert url == 'http://pyeong-an.com/설교-말씀-원고/?pageid=1'

    url = al.get_page_url()
    assert url == 'http://pyeong-an.com/설교-말씀-원고/?pageid=2'


def test_article_list_has_next():
    with open('tests/fixtures/pyeongan-list.txt') as fin:
        content = fin.read()
        soup = BeautifulSoup(content, 'html5lib')
        al = PyeonganArticleList()
        assert al.has_next(soup) is True


def test_article_list_parse():
    with open('tests/fixtures/pyeongan-list.txt') as fin:
        content = fin.read()
        soup = BeautifulSoup(content, 'html5lib')
        al = PyeonganArticleList()
        links = [e for e in al.parse(soup)]
        assert len(links) == 10


def test_article_get_uid():
    url = 'http://pyeong-an.com/설교-말씀-원고/?pageid=1&mod=document&uid=693'
    article = PyeonganArticle(url)
    assert article.uid == '693'


def test_article_parse_text():
    with open('tests/fixtures/pyeongan-article.txt') as fin:
        url = 'http://pyeong-an.com/설교-말씀-원고/?pageid=1&mod=document&uid=693'
        content = fin.read()
        soup = BeautifulSoup(content, 'html5lib')
        article = PyeonganArticle(url)
        assert article.parse_text(soup).startswith('종려주일입니다')
        assert article.parse_text(soup).endswith('축복합니다, 할렐루야!')
