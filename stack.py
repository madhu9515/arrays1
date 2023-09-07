class stackk():
    def push(self,input ):
        self.data=input
        return l.append(self.data)
    def pop(self):
        return l.pop()
    def show(self):
        return l
obj=stackk()
l=[]
obj.push(1)
obj.push(2)
print(l)
print('add the value in the end 3')
obj.push(3)
print(obj.show())
print('removed value :',obj.pop())
print(obj.show())
print('removed value :',obj.pop())
print(obj.show())
