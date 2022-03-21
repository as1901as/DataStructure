class Student:
    university="Dong-A"
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"name: {self.name}age: {self.age}"
    
s=Student("Jimin\n", "26")
print(s)

# self 의미
# 자신의 인스턴스를 나타내는 변수"
# __init__ 의미
# 초기화 메소드 (첫번째 인자로 self를 지정)
# __str__
# 문자열로 반환하는 기능