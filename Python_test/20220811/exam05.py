# 실습 5 - 성적 계산 프로그램

name=input('이름을 입력하세요 :')
lan_g=int(input('국어 성적을 입력하세요 :'))
math_g=int(input('수학 성적을 입력하세요 :'))
soci_g=int(input('사회 성적을 입력하세요 :'))
sci_g=int(input('과학 성적을 입력하세요 :'))
eng_g=int(input('영어 성적을 입력하세요 :'))
amount=lan_g+math_g+soci_g+sci_g+eng_g
mid=round(float(amount)/5,1)
print(name,'님의 성적은 총합',amount,'점, 평균',mid,'점입니다.')

# 풀이
amount=lan_g+math_g+soci_g+sci_g+eng_g
mid=amount/5
print(name,'님의 성적은')
print('총합',amount,'점, 평균',round(mid,1),'점입니다.')