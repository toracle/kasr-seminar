# -*- coding: utf-8 -*-

import os
import gensim
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

from konlpy.tag import Twitter, Hannanum, Kkma
from sklearn.manifold import TSNE


matplotlib.rc('font', family='Noto Sans CJK KR')


def ensure_dir(path, parent=False):
    _path = os.path.dirname(path) if parent else path

    if not os.path.isdir(_path):
        os.makedirs(_path)


class SentenceReader(object):
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        with open(self.path, encoding='utf8') as fin:
            for line in fin:
                _line = line.strip()
                if not _line:
                    continue
                yield _line.split()


class SermonVoca(object):
    def __init__(self, name):
        self.name = name

    def make(self):
        ensure_dir('outputs')
        ensure_dir('models')
        ensure_dir('words')

        self.make_corpus()
        self.make_model()

    def make_corpus(self):
        processor = Hannanum()
        with open('outputs/sermon-{}-corpus.txt'.format(self.name), 'w') as fout:
            data_dir = 'data/{}'.format(self.name)
            for filename in os.listdir(data_dir):
                if not filename.endswith('txt'):
                    continue

                path = os.path.join(data_dir, filename)
                with open(path) as fin:
                    print(path)
                    for line in fin:
                        _line = self.clean_punctuation(line)
                        if not _line:
                            continue

                        _lines = _line.split('.')

                        for l in _lines:
                            _l = self.clean_punctuation(l)
                            if not _l:
                                continue
                            sentence = ['{}/{}'.format(word, tag) for word, tag in processor.pos(_l) if self.filter_tag(tag) and self.filter_word(word)]
                            if len(sentence) > 2:
                                fout.write(' '.join(sentence) + '\n')

    def make_model(self):
        sentences_vocab = SentenceReader('outputs/sermon-{}-corpus.txt'.format(self.name))
        sentences_train = SentenceReader('outputs/sermon-{}-corpus.txt'.format(self.name))

        self.model = gensim.models.Word2Vec(sg=1, window=15, min_count=50)
        self.model.build_vocab(sentences_vocab)
        self.model.train(sentences_train, total_examples=self.model.corpus_count, epochs=self.model.epochs)
        self.model.save('models/{}'.format(self.name))
        self.save_words(self.model, 'words/{}'.format(self.name))

    def filter_tag(self, tag):
        return tag not in set(['J', 'E', 'X', 'S'])

    def filter_word(self, word):
        try:
            float(word)
            return False
        except ValueError:
            if len(word) > 1:
                return True
            return False

    def clean_punctuation(self, line):
        return line.replace('"', '').replace("'", '').replace(',', '').\
            replace('....', '').replace('...', '').replace('..', '').\
            replace('(', ' ').replace(')', ' ').replace('?', '').replace('!', '').\
            replace('“', '').replace('”', '').replace(chr(8216), '').replace(chr(8217), '').\
            replace('…', '').\
            strip()

    def load(self):
        self.model = gensim.models.Word2Vec.load('models/{}'.format(self.name))
        return self

    def most_similar(self, positive=None, negative=None, topn=10):
        return self.model.wv.most_similar(positive=positive, negative=negative, topn=topn)

    def save_words(self, model, path):
        with open(path, 'w') as fout:
            for word in model.wv.vocab:
                fout.write('{}\n'.format(word))

    def tsne_plot(self):
        labels = []
        tokens = []

        for word in self.model.wv.vocab:
            tokens.append(self.model[word])
            labels.append(word)

        tsne_model = TSNE(perplexity=40, n_components=2, n_iter=5000, random_state=23)
        new_values = tsne_model.fit_transform(tokens)

        x = []
        y = []
        for value in new_values:
            x.append(value[0])
            y.append(value[1])

        plt.figure(figsize=(16, 16))

        for i, _ in enumerate(x):
            plt.scatter(x[i], y[i])
            plt.annotate(labels[i],
                         xy=(x[i], y[i]),
                         xytext=(5, 2),
                         textcoords='offset points',
                         ha='right',
                         va='bottom')
        return plt
