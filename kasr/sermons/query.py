# -*- coding: utf-8 -*-

from prompt_toolkit import prompt
from kasr.sermons.core import SermonVoca


def run():
    voca_list = {'pyeongan': SermonVoca('pyeongan').load()}
    topn = 10

    while True:
        try:
            line = prompt('Sim> ')
            if not line:
                continue

            if line.startswith('/set'):
                cols = line.split()
                print(cols)
                key = cols[1]
                value = cols[2]
                if key == 'topn':
                    topn = int(value)
                continue

            params = parse_query(line)
            params['topn'] = topn
            print(params)

            for voca_name, voca_model in voca_list.items():
                target_words = voca_model.most_similar(**params)
                print(voca_name, target_words)

        except (EOFError, KeyboardInterrupt):
            break

        except KeyError:
            continue


def parse_query(line):
    words = line.split()
    positive_words = [word for word in words if not word.startswith('-')]
    negative_words = [word[1:] for word in words if word.startswith('-')]

    return {'positive': ['{}/N'.format(word) for word in positive_words], 'negative': ['{}/N'.format(word) for word in negative_words]}


if __name__ == '__main__':
    run()
