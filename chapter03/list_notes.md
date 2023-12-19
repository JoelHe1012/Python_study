# 列表(list)
## 1.列表的创建
-`list = []`

## 2.列表的访问与使用
- `list[index]` 索引从0开始

## 3.修改、添加和删除元素

### 修改元素
- `list[index] = 'new'`

### 添加元素
- `list.append('new')` 在列表末尾添加元素，追加元素，改变列表，一次只能加一个元素,
- `list.insert(index, 'new')` 在索引处添加元素，即插入一个元素

### 删除元素
- `del list[index]` 直接将列表中索引为index的值删除，变量的值发生改变
- `list.pop(index)`  删除(弹出)一个值，默认为列表的最后一个，返回被删除的值，原列表改变，每执行一次，弹出一个元素
- `list.remove(value)` 根据值来删除元素，只删除第一个值，返回值为被删除的值

### 管理列表
- list.sort() 方法永久排序
- sorted(list) 函数临时排序
- list.reverse() 反转列表的排列顺序,返回值为None,是一种操作