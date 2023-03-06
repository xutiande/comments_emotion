import jieba
from snownlp import SnowNLP         #情感分析库
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
f=open('评论.txt','r',encoding='utf8')            #读取txt文件
txt=f.readlines()
correct=[]          #正向的列表
anti=[]             #反向的列表
for i in txt:
    comments=i.strip('\n').strip()
    fenci = jieba.lcut(comments)
    for j in fenci[2:]:
        j=j.strip('，/。：？”“ .@ ')            #去掉标点符号
        if len(j) == 0:
            continue
        else:
            s=SnowNLP(j)
        if s.sentiments >0.5:               #判断0.5以上为正向，反之为负向
            correct.append(j)
        else:
            anti.append(j)
with open('正向.txt','w')as f1:           #写入文件
    for h in correct:
        f1.write(h)
        f1.write('\n')
print('正向输出为:',correct)
print('反向输出为:',anti)

f.close()
