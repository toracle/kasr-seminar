# -*- coding: utf-8 -*-

from kasr.sermons.core import SermonVoca


def train():
    voca = SermonVoca('pyeongan')
    voca.make()


if __name__ == '__main__':
    train()
