
import jieba
import wordcloud  # 调用两个库

def run():
    f = open("recommend.txt", "r", encoding="utf-8")
    t = f.read()
    f.close()
    ls = jieba.cut(t)
    txt = " ".join(ls)
    w = wordcloud.WordCloud(width=1000, height=700,background_color="white",font_path="SIMYOU.ttf")
    w.generate(txt)
    w.to_file("output.png")

if __name__ == '__main__':
    run()
