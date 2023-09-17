# 복잡한 객체를 정렬할 때 활용

students=[
    ('어피치','A',15),
    ('라이언','B',16),
    ('무지','C',10),
]

print(sorted(students))         #이름순
print(sorted(students,key=lambda x:x[1]))   #성적순
print(sorted(students,key=lambda x:x[2]))   #나이순(오름차순)