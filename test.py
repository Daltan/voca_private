import pandas as pd
import numpy as np
from random import sample
import os
voc=pd.read_csv("./data1.csv",encoding='utf8',header=None)
voc.columns=['单词','解释']
n=int(input("比例(1-100)"))
# n=30
print()

nums=int(n/100*voc.shape[0])
textprompt="""
-----------
\033[1;32;41m
回车继续
按[1]查看答案
按[2]修改比例
按 # 退出
\033[0m
"""
inp=''
while inp !='#':
    test=voc.sample(nums)
    os.system('cls')
    for i in test.单词:
        print(i)
    inp=input(textprompt)
    if inp=='':
        continue
    elif inp=='1':
        os.system('cls')
        print("\n---- 测试表-----")
        print(test)
        print("\n----------------")
        input("任意键继续")
    elif inp=='2':
        n=int(input("比例(1-100)"))
        print()
        # n=30
        nums=int(n/100*voc.shape[0])