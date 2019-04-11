# 列表练习二
'''放眼世界：想出至少5个你想去旅游的地方。
1、将这些地方储存在一个列表中，并确保其中的元素不是按字母顺序排列的；
2、按照原始排列顺序打印列表；
3、使用sorted()按字母顺序打印这个列表；
4、再次打印这个列表，核实排列顺序未改变；
5、使用sorted()按字母顺序相反的顺序打印这个列表，同时不要修改它；
6、再次打印这个列表，核实排列顺序未改变；
7、使用reverse()修改列表元素的排列顺序，并打印这个列表，核实排列顺序确实变了；
8、使用reverse()再次修改列表元素的排列顺序，并打印这个列表，核实列表排列顺序已恢复；
9、使用sort()修改该列表，使其元素按字母顺序排列，并打印该列表；
10、使用sort()修改该列表，使其元素按字母排列相反的顺序排列，并打印该列表。'''

# 第1题
places = ["Tokyo(东京)", "Los Angles(洛杉矶)", "New York(纽约)", "Paris(巴黎)", "London(伦敦)", "Berlin(柏林)"]
# 第2题
print(places)
# 第3题
print(sorted(places))
# 第4题
print(places)
# 第5题
print(sorted(places, reverse=True))
# 第6题
print(places)
# 第7题
places.reverse()
print(places)
# 第8题
places.reverse()
print(places)
# 第9题
places.sort()
print(places)
# 第10题
places.sort(reverse=True)
print(places)