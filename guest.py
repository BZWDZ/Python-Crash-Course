guestslist = ['王文龙','王乙凡','云中君']
a = guestslist[0] + '先生是否愿意与我共用晚餐？'
b = guestslist[1] + '先生是否愿意与我共用晚餐？'
c = guestslist[2] + '先生是否愿意与我共用晚餐？'
print(a)
print(b)
print(c)
print(a,b,c)
guests = guestslist.pop(0)
print(guests)
guestslist = ['王勇','王乙凡','云中君']
print(guestslist)
guestslist.insert(0,'张大大')
print(guestslist)
guestslist.insert(2,"萨顶顶")
guestslist.append('宋丹丹')
print(guestslist)

a = guestslist.pop()
print(a + "我很抱歉，请不要来了")
b = guestslist.pop()
c = guestslist.pop()
d = guestslist.pop()
print(guestslist)
print(guestslist[0] + "你在受邀请之列")
print(guestslist[1] + "你在受邀请之列")
del guestslist[0:2]
print(guestslist)


