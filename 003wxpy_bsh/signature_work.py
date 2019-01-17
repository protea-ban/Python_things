import re
import jieba
import numpy
import pandas as pd
import matplotlib.pyplot as plt
from scipy.misc import imread
from wordcloud import WordCloud, ImageColorGenerator
import codecs
def read_txt_file(path):
    '''
    读取txt文本
    :param path:
    :return:
    '''
    with open(path, 'r', encoding='utf-8-sig', newline='') as f:
        return f.read()


txt_filename = 'signature.txt'
content = read_txt_file(txt_filename)
segment = jieba.lcut(content)
words_df = pd.DataFrame({'segment':segment})
stopwords = pd.read_csv("stopwords.txt", index_col=False, quoting=3, sep=" ", names=['stopword'], encoding='utf-8')
words_df = words_df[~words_df.segment.isin(stopwords.stopword)]

words_stat = words_df.groupby(by=['segment'])['segment'].agg({"计数":numpy.size})
words_stat = words_stat.reset_index().sort_values(by=["计数"], ascending=False)

# 设置词云属性
color_mask = imread('background.jpg')
wordcloud = WordCloud(font_path="simhei.ttf",
                      background_color="white",
                      max_words=100,
                      mask=color_mask,
                      max_font_size=100,
                      random_state=42,
                      width=1000,height=860,margin=2,
                      )

word_frequence = {x[0]:x[1] for x in words_stat.head(100).values}
print(word_frequence)
word_frequence_dict = {}
for key in word_frequence:
    word_frequence_dict[key] = word_frequence[key]

wordcloud.generate_from_frequencies(word_frequence_dict)
# 从背景图片生成颜色值
image_colors = ImageColorGenerator(color_mask)
# 重新上色
wordcloud.recolor(color_func=image_colors)
# 保存图片
wordcloud.to_file('output.png')
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
