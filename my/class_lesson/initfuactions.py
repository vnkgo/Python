class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
student1={}
# 创建一个Student类的实例对象
for i in range(10):
    name=input("mz")
    age=int(input("nn"))
    address=input("dz")
    student1[i]=Student(name,age,address)
    print(student1[i])



# 访问实例对象的属性


