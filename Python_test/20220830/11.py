num=0.0

try:
    print(1.0/num)
except ZeroDivisionError as msg:
# except Exception as msg:
    print(msg)
    print('ZeroDivisionError')

# print(msg)        #구문안에서만 써야함