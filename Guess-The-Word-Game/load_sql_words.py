import mysql.connector

# 连接到数据库
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="140526",
    database="words"
)

cursor = connection.cursor()

file_path=r"D:\_Project\Guess_The_Word\Guess-The-Word-Game-Using-Python-master\test.txt"
# 打开文本文件并逐行读取内容
with open(file_path, "r",encoding='utf-8') as file:
    for line in file:
        parts = line.strip().split()  # 假设词汇和定义以空格分隔
        if len(parts) >= 2:
            word = parts[0]
            definition = " ".join(parts[1])
            translate=" ".join(parts[2:])

            print (parts)
            # 将数据插入到数据库
            #将一条新的记录插入到 "word_files" 表格(***)列名称
            cursor.execute("INSERT INTO word_files (word,attribute,chinese) VALUES (%s, %s, %s)", (word, definition,translate))
            connection.commit()
            
print("插入成功")
# 关闭数据库连接
cursor.close()
connection.close()
