# coding=utf-8
from random import randint

import jieba
from matplotlib import pyplot
from matplotlib.image import imread
from wordcloud import WordCloud


def read_txt(sorce_path, dest_path):
    with open(sorce_path, "r") as file:
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
    mask = imread("./image/love.png")
    with open(file_path, "r") as file:
        txt = file.read()
    word = WordCloud(background_color="yellow", width=800, height=800,
                     font_path="simhei.ttf", mask=mask,
                     color_func=random_color_func,
                     collocations=False, max_font_size=50,
                     random_state=30).generate(txt)
    word.to_file("11.png")
    print("词条图片完成")
    pyplot.imshow(word)
    pyplot.axis("off")
    pyplot.show()


def random_color_func(word=None, font_size=None, position=None, orientation=None,
                      font_path=None, random_state=None):
    return "hsl(%d, 100%%, 50%%)" % randint(0, 255)


if __name__ == "__main__":
    read_txt("./lidazhao.txt", "./lidazhaoafter.txt")
    generate_image("./lidazhaoafter.txt")
