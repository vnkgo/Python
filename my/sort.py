my_list = [["c", 123], ["b", 124], ["a", 134]]

# 基于带名函数
def choose_sort_key(element):
    return element[1]

# 基于匿名函数
# my_list.sort(key=lambda element: element[1], reverse=True)

my_list.sort(key=choose_sort_key,reverse=True)
print(my_list)
