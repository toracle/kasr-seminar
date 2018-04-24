# -*- coding: utf-8 -*-

import argparse
from kasr.sermons.core import SermonVoca


def draw(dataset):
    voca = SermonVoca(dataset)
    voca.load()
    plt = voca.tsne_plot()
    plt.savefig('{}.png'.format(dataset))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dataset')
    args = parser.parse_args()
    draw(args.dataset)
