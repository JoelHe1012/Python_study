# 列出你想要去的五个地方
place = ['kunming','shanghai','xian','taiyuan','chongqing']
# 打印列表
print('这是原始列表：')
print(place)
# 使用sorted()函数排序
print('这是排序后的列表：')
print(sorted(place))
print('使用sorted()函数后，原列表依旧没变：')
print(place)
print('现在按与字母顺序相反的顺序来排列：')
print(sorted(place,reverse=True))
print('再次确定原列表没有发生改变：')
print(place)
print('把原来列表的顺序反过来')
place.reverse() # 直接修改列表，返回值为None
print(place)
place.reverse()
print('确定两侧reverse后列表会还原')
print(place)
print('使用sort后的列表的顺序确实发生了改变')
place.sort() # 其返回值依旧为None
print('现在列表按字母顺序排列')
print(place)
place.sort(reverse=True)
print('现在按字母反顺序排列')
print(place)