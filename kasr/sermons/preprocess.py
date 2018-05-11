# -*- coding: utf-8 -*-

import argparse
from kasr.sermons.core import SermonVoca


def preprocess(dataset):
    voca = SermonVoca(dataset)
    voca.preprocess()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dataset')
    args = parser.parse_args()
    preprocess(args.dataset)
