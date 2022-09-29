guestslist = ['王文龙','王乙凡','云中君']
print(len(guestslist))

#3_10
list = ['1','2','3','4']
list.append('5')
print(list)

list.pop()
print(list)
print(list.pop())
print(list)      #使用pop被弹出的元素就不再表中了
list.remove('3')       #remove()要有确定的值
print(list)

del list[0:]
print(list)

tip = ['one','two','three','four','five']
print(sorted(tip))
print(sorted(tip,reverse=True))
tip.sort()
print(tip)
tip.sort(reverse=True)
print(tip)
print(len(tip))