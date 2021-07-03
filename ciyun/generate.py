# coding=utf-8
from random import randint

import jieba
from matplotlib import pyplot
from matplotlib.image import imread
from wordcloud import WordCloud


def read_txt(sorce_path, dest_path):
    with open(sorce_path, "r", encoding="utf-8") as file:
        txt = file.read()
    re_move = {",", ".", ";", ":", "\n", "\xa0", "、", "，", "\"", "的", "是", "得"}
    for i in re_move:
        txt.replace(i, " ")
    word = jieba.lcut(txt)   # 精分词模式
    with open(dest_path, "w", encoding="utf-8") as file:
        for i in word:
            file.write(str(i) + " ")
    print("文本处理完成")


def generate_image(file_path):
    mask = imread("./ciyun/image/love.png")  # 生成指定形状的词云
    with open(file_path, "r", encoding="utf-8") as file:
        txt = file.read()
    # scale表示图片大小与清晰度，stopwords：不想展示的词
    word = WordCloud(font_path="./ciyun/typeface/simhei.ttf", width=800, height=800,
                     background_color="white", mask=mask, max_font_size=150,
                     scale=3, stopwords=set(['的', '啊', '得']),
                     collocations=False).generate(txt)
    word.to_file("./ciyun/11.png")
    print("词条图片完成")
    pyplot.imshow(word)
    pyplot.axis("off")
    pyplot.show()


def random_color_func(word=None, font_size=None, position=None, orientation=None,
                      font_path=None, random_state=None):
    return "hsl(%d, 100%%, 50%%)" % randint(0, 255)


if __name__ == "__main__":
    read_txt("./ciyun/lidazhao.txt", "./ciyun/lidazhaoafter.txt")
    generate_image("./ciyun/lidazhaoafter.txt")
