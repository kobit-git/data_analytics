#coding:utf-8
import csv
from janome.tokenizer import Tokenizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from bs4 import BeautifulSoup
from collections import Counter, defaultdict


#名詞だけ抽出、単語をカウント
def counter(texts):
    words_count = defaultdict(int)
    words = []
    t = Tokenizer()
    for text in texts:
        tokens = t.tokenize(text)
        for token in tokens:
            #品詞から名詞だけ抽出
            pos = token.part_of_speech.split(',')[0]
            if (pos == '名詞') or (pos == '形容詞'):
                words_count[token.base_form] += 1
                words.append(token.base_form)
    return words_count, words

with open('/Users/takahiro-nakano/github_personal/scrapy/twitter_data/text_ozawa_twitter.tsv','r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\t')
    texts = []
    for row in reader:
        text = row[0].split('http')
        texts.append(text[0])
for t in texts:
    print(type(t))
    break
words_count, words = counter(texts)

for k in sorted(words_count.values(), reverse=True):
    print(k)
text = ' '.join(words)

fpath = "~/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc"

wordcloud = WordCloud(background_color="white", font_path=fpath, width=900, height=500).generate(text)

plt.figure(figsize=(15,12))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
