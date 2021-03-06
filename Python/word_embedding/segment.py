# -*- coding: utf-8 -*-

import jieba
import logging

STOPWORD_EXCULDE = False


def main():

    logging.basicConfig(
        format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    # jieba custom setting.
    jieba.set_dictionary('Python/word_embedding/jieba_dict/dict.txt.big')

    # load stopwords set
    stopwordset = set()
    with open('Python/word_embedding/jieba_dict/stopwords.txt', 'r', encoding='utf-8') as sw:
        for line in sw:
            stopwordset.add(line.strip('\n'))

    texts_num = 0

    output = open('wiki_seg.txt', 'w')
    with open('Python/word_embedding/wiki_zh_tw.txt', 'r') as content:
        for line in content:
            line = line.strip('\n')
            words = jieba.cut(line, cut_all=False)
            for word in words:
                if (STOPWORD_EXCULDE and word not in stopwordset) or not STOPWORD_EXCULDE:
                    output.write(word + ' ')

            texts_num += 1
            if texts_num % 10000 == 0:
                logging.info("已完成前 %d 行的斷詞" % texts_num)
    output.close()


if __name__ == '__main__':
    main()
