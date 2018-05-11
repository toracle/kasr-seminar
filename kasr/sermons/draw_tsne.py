# -*- coding: utf-8 -*-

import os
import argparse
from kasr.sermons.core import SermonVoca


def gather_common_words():
    datasets = os.listdir('data')
    print('datasets: {}'.format(datasets))
    wordset_per_dataset = {}
    for dataset in datasets:
        voca = SermonVoca(dataset)
        voca.load()
        wordset = set(voca.model.wv.vocab)
        wordset_per_dataset[dataset] = wordset

    common_wordset = set.intersection(*wordset_per_dataset.values())
    print('Common words: {}'.format(len(common_wordset)))
    return common_wordset


def draw_tsne(dataset, common_words):
    voca = SermonVoca(dataset)
    voca.load()
    plt = voca.tsne_plot(common_words)
    plt.savefig('{}.png'.format(dataset))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dataset')
    parser.add_argument('--common', action='store_true')

    args = parser.parse_args()

    common_words = gather_common_words() if args.common else None
    draw_tsne(args.dataset, common_words)
