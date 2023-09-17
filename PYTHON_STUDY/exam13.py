class CustomerException(Exception):
    
    def __init__(self):
        Exception.__init__(self)
        print('내가 직접 만든 오류 메시지 입니다.')
        
    def __str__(self):
        return '오류가 발생했습니다.'

raise CustomerException