
"""""
name = "My Name is Duanwangyi"
age = 35
phone=1801600810
# 输出包含姓名、年龄和电话号码的信息，使用不同的姓名格式化方式
print(name.lower() + "\n" + str(age) + "\n" + str(phone))
# 同上，但姓名转换为大写
print(name.upper() + "\n" + str(age) + "\n" + str(phone))
# 同上，但姓名首字母大写
print(name.title() + "\n" + str(age) + "\n" + str(phone))
"""""

#!/usr/bin/python3
"""  
str='123456789'
 
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[-1])              # 输出字符串第一个字符
print(str[2:5] + "\n")            # 输出从第三个开始到第六个的字符（不包含）
print(str[2:])             # 输出从第三个开始后的所有字符
print('------------------------------')
print(str[1:5:2] + "\n")          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)             # 输出字符串两次
print(str + '你好')         # 连接字符串
 
print('------------------------------')
 
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义 """



if(n:=10)>5:
    print(bool(n))

