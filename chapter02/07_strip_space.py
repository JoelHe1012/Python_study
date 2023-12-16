# 删除人命中的空白
# 用变量表示一个人的名字，并在其开头和结尾都包含一些空白字符，务必至少使用字符组合'\t'和'\n'各一次
name = '\tJoel He\n'
print(name)     # 前面一个制表符，后面包含一个空行
print(name.rstrip().lstrip())   # 删除前面的制表符和后面的空行
print(name.rstrip())    # 删除右边的空行
print(name.lstrip())    # 删除左边的制表符
print(name.strip())     # 删除两边的空白
# strip()相关指令是删除任意类型的空白，
