# 加载所有模块
import tkinter
from tkinter import *
import random
from tkinter import messagebox
import mysql.connector

"""
0.基础GUI界面，以及游戏功能

可增加功能
1.可以增删单词库，可选择单词库
2.对于猜错单词频率出现
3.登陆系统，用户拥有得分系统
4.数据库处理单词库,接入mysql
6.提示功能
7.可选择难度
8.用dearpygui增加启动界面
"""
def shuffle_word(str):
    str_list=list(str)
    random.shuffle(str_list)
    return "".join(str_list)



# 创建数据库连接
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="140526",
    database="words"
)

# 创建一个游标对象
cursor = connection.cursor()

# 执行SQL查询
"""
TODO: 
"""
query = "SELECT * FROM word_files"
cursor.execute(query)

# 获取查询结果 result为列表；每个元素为是一行的数据，为元组
result = cursor.fetchall()

# 关闭游标和数据库连接
cursor.close()
connection.close()



#加载单词文件
file_path=r"D:\_Project\Guess_The_Word\Guess-The-Word-Game-Using-Python-master\CET6.txt"
#file_path = r"D:\_Project\Guess_The_Word\Guess-The-Word-Game-Using-Python-master\test.txt"
with open(file_path, 'r',encoding='utf-8') as file:
    lines = file.readlines()

answers = []   
hint_list = []

for line in lines:
    line = line.strip()  # 去除行末尾的换行符和空白字符
    parts = line.split('\t')  # 使用制表符分割行，前面的部分为单词，后面的部分为其他内容
    # 确保行至少包含两部分：单词和提示
    if len(parts) >= 2:
        word = parts[0]  
        hint = parts[1]
        answers.append(word)
        hint_list.append(hint)

words= []  
#生成打乱后单词库
for item in answers:
    words.append(shuffle_word(item))



# 获取随机数索引
num=random.randrange(0,len(answers),1)
# function 配置label中对应随机单词
def working():
    global words,answers,num
    lbl.config(text=words[num])
# function 检查输入是否正确
def checkans():
    global words,answers,num
    var = e1.get() # 获取输入框值
    if var == answers[num]:
        messagebox.showinfo("CORRECT","This is correct answer")
        res()
    else:
        messagebox.showerror("ERROR","This is not a correct answer")
        e1.delete(0,END)
# function 重置随机索引 当 回答正确 or 当 点击重置按钮
def res():
    global words,answers,num
    num=random.randrange(0,len(answers),1)
    lbl.config(text=words[num])
    e1.delete(0,END)


# 定义 tkinter窗体 并且提供其属性
root = tkinter.Tk()
root.geometry("400x600")
root.title("GUESS THE WORDS")
root.configure(background="#000000")


# 定义 label，展示问题
lbl= Label(
    root,
    text="Shivam Yadav",
    font=("verdana",18),
    bg="#000000",
    fg="#ffffff",
)
lbl.pack(pady=30,ipady=10,ipadx=10)



ans1= StringVar()

# 定义 输入框，用于输入玩家答案
e1=Entry(
    root,
    font=("verdana",16),
    textvariable=ans1,
)
e1.pack()

# button 提交答案
checkbutton=Button(
    root,
    text="Check",
    font=("Comic sans ms",16),
    width=16,
    bg="#2F363F",
    fg="#FFF222",
    relief= GROOVE,
    command=checkans,
)
checkbutton.pack(pady=30)

# button 重置随机索引
resetbutton=Button(
    root,
    text="Reset",
    font=("Comic sans ms",16),
    width=16,
    bg="#2F363F",
    fg="#FFF222",
    relief= GROOVE,
    command=res,

)
resetbutton.pack()

# # 定义 label，显示提示
# hint= Label(
#     root,
#     text="Shivam Yadav",
#     font=("楷体",18,"bold"),
#     bg="#000000",
#     fg="#ffffff",
# )
# hint.pack(pady=30,ipady=10,ipadx=10)

# 初始化 加载主循环
working()
root.mainloop()
