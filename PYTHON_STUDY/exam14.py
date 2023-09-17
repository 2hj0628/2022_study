class CustomerException(Exception):
    
    def __init__(self, message, value):
        Exception.__init__(self)
        self.message = message
        self.value = value
        
    def __str__(self):
        return  self.message
    
    def print(self):
        print('오류 정보 표시합니다.')
        print('메시지:',self.message)
        print('값:', self.value)


try :
    raise CustomerException("결측값 발견", 9999)
except CustomerException as e:
    #print('메시지:결측값 발생')
    #print('값:9999')
    e.print()
    

