# -*- coding: utf-8 -*-

import os
import gensim
from konlpy.tag import Twitter, Hannanum, Kkma


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
        if not os.path.isdir('outputs'):
            os.makedirs('outputs')

        if not os.path.isdir('models'):
            os.makedirs('models')

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
                            sentence = ['{}/{}'.format(word, tag) for word, tag in processor.pos(_l) if self.filter_tag(tag)]
                            fout.write(' '.join(sentence) + '\n')

    def make_model(self):
        sentences_vocab = SentenceReader('outputs/sermon-{}-corpus.txt'.format(self.name))
        sentences_train = SentenceReader('outputs/sermon-{}-corpus.txt'.format(self.name))

        self.model = gensim.models.Word2Vec(sg=1)
        self.model.build_vocab(sentences_vocab)
        self.model.train(sentences_train, total_examples=self.model.corpus_count, epochs=self.model.epochs)
        self.model.save('models/{}'.format(self.name))

    def reduce_model(self):
        vectors = []
        labels = []
        for word in self.model.wv.vocab:
            w, pos = word.split('/')
            vectors.append(self.model.wv[word])
            labels.append(word)

    def filter_tag(self, tag):
        return tag not in set(['J', 'E', 'X'])

    def clean_punctuation(self, line):
        return line.replace('"', '').replace("'", '').replace(',', '').\
            replace('....', '').replace('...', '').replace('..', '').\
            replace('(', ' ').replace(')', ' ').replace('?', '').replace('!', '').\
            replace('“', '').replace('”', '').replace(chr(8216), '').replace(chr(8217), '').\
            strip()

    def load(self):
        self.model = gensim.models.Word2Vec.load('models/{}'.format(self.name))
        return self

    def most_similar(self, positive=None, negative=None, topn=10):
        return self.model.wv.most_similar(positive=positive, negative=negative, topn=topn)
