# -*- coding: utf-8 -*-
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
f=open('正向.txt','r',encoding='gb18030')
font = r'C:\Windows\Fonts\FZSTK.TTF'        #电脑自带的字体
txt=f.read()
img_array=np.array(Image.open(r'img.png'))          #将图片转化为数组
wd=WordCloud(
    width=1400,height=2200,
    background_color='white',
    mode='RGB',
    mask=img_array,     #添加模板,生成指定形状的词云，并且词云图的颜色从模板中提取
    font_path=font,
    max_font_size=150,
    relative_scaling=0.1,       #设置字体大小与词频的关键程度为0.6
    random_state=50,
    scale=2
).generate(txt)
image_color=ImageColorGenerator(img_array)      #词云颜色
wd.recolor(color_func=image_color)

plt.imshow(wd)          #显示词云
plt.axis('off')         #关闭x，y轴
plt.show()          #显示
wd.to_file('词云图.jpg')

