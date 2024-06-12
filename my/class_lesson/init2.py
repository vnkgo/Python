class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

# 创建一个空字典来存储学生信息
students = {}

# 使用 for 循环录入 10 位学生的信息
for i in range(1, 11):
    print(f"当前录入第 {i} 位学生信息，总共需要录入 10 位学生信息")
    name = input("请输入学生的姓名：")
    age = int(input("请输入学生的年龄："))  # 注意将输入的年龄转换为整数
    address = input("请输入学生的地址：")
    students[i] = Student(name, age, address)#字典每个key存储了一个student的实例对象
    print(f"学生{i}信息录入完成，信息为：姓名：{students[i].name}，年龄：{students[i].age}，地址：{students[i].address}")#所以调用需要.xxx

# 输出所有学生的信息
for i in range(1, 11):
    print(f"学生{i}信息：姓名：{students[i].name}，年龄：{students[i].age}，地址：{students[i].address}")
