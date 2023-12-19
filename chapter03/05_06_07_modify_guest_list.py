# 有位嘉宾临时无法赴约，因此你需邀请另一位嘉宾
guest_list = ['胖哥','大师姐','詹姐','朱姐']
# print(guest_list[0],'，请你吃饭')
# print(guest_list[1],'，请你吃饭')
# print(guest_list[2],'，请你吃饭')
# print(guest_list[3],'，请你吃饭')
# 改用for循环
for i in range(len(guest_list)):
    print(guest_list[i], '请你吃饭')
# 朱姐临时有事，无法赴约
# del_guest = guest_list.pop(3)
# print(f'{del_guest}因为临时有事，无法参加这次聚会')
# 修改嘉宾名单，将无法赴约的嘉宾替换为新邀请的嘉宾
guest_list[3] = '陈天浩'
for i in range(len(guest_list)):
    print(guest_list[i], '请你吃饭')

# 添加嘉宾
# 你找到了一个更大的餐桌，可以容纳更多的嘉宾就卓，你可以再邀请三位嘉宾
guest_list.insert(0,'威哥')
print(guest_list)
guest_list.insert(2,'周姐')
print(guest_list)
guest_list.append('唐扬')
for i in range(len(guest_list)):
    print(guest_list[i], '请你吃饭')
print(f'一共邀请了{len(guest_list)}位嘉宾吃饭')

# 缩短名单
# 你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾
print('各位，不好意思，钱不够了，只能请两位同学')
print(guest_list)
print(f'{guest_list.pop()},不好意思，这次不能请你吃饭了')
print(f'{guest_list.pop()},不好意思，这次不能请你吃饭了')
print(f'{guest_list.pop()},不好意思，这次不能请你吃饭了')
print(f'{guest_list.pop()},不好意思，这次不能请你吃饭了')
print(f'{guest_list.pop()},不好意思，这次不能请你吃饭了')
print(guest_list)
for i in range(len(guest_list)):
    print(guest_list[i], '请你吃饭')
del guest_list[0]
del guest_list[0]
print(guest_list)