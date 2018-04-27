# -*- coding: utf-8 -*-

import argparse
from kasr.sermons.core import SermonVoca


def gather_common_words():
    datasets = ['buksuwon', 'pyeongan']
    wordset_per_dataset = {}
    for dataset in datasets:
        voca = SermonVoca(dataset)
        voca.load()
        wordset = set(voca.model.wv.vocab)
        wordset_per_dataset[dataset] = wordset

    common_wordset = set.intersection(*wordset_per_dataset.values())
    print('Common words: {}'.format(len(common_wordset)))
    return common_wordset


def draw(dataset, common_words):
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
    draw(args.dataset, common_words)
