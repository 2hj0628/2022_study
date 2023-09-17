# 실습 5 - 백제의 왕 맞추기

name=''
while name!='근초고왕':
    try:
        name=str(input('백제의 제 13대 왕으로, 백제의 전성기를 이끌었고 마한과 대방을 합병한 왕은? '))
    except:
        print('다시 입력하세요.')
    else:
        if name=='근초고왕':
            break