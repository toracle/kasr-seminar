# -*- coding: utf-8 -*-

import argparse
from kasr.sermons.core import SermonVoca


def train(dataset):
    voca = SermonVoca(dataset)
    voca.make()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dataset')
    args = parser.parse_args()
    train(args.dataset)
