# How to use

`git clone git@github.com:Daltan/voca_private.git`
`cd voca_private`
`python test.py`

1. 输入比例。如`10`，代表`data1.csv`中的10%的单词随机抽
2. 查看并描述读音与意义。 可使用`1`、`2`查看意思修改比例
3. 回车继续。`#` 退出

# How to add words

- 使用记事本打开`data1.csv`
- 一行是一组单词、汉语释义
- 单词、汉译之间用英文半角逗号`,`
- 一行只能有一个`,`

# How to develop

- `test.py` is the main program
- `data1.csv` contains the English words.
