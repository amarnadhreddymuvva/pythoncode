class raja:
    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name
    def setmarks(self,marks):
        self.marks=marks
    def getmarks(self):
        return self.marks
n=int(input("enter num of students:"))
for i in range(n):
    s=raja()
    name=input("enter name")
    s.setname(name)
    marks=int(input("enter marks"))
    s.setmarks(marks)
print(s.getname())
print(s.getmarks())
print("sucess")