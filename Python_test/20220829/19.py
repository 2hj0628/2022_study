# 오버로딩
class A:
    def func(self,a):
        return 'hello'
    def func(self):
        return 'bye'    #같은 이름이라 덮어씀

a=A()
print(a.func())
# print(a.func(1))