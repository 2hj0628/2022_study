-- 데이터베이스 접근
use kakao_bank;

-- client 테이블 생성
-- 테이블명 뒤에 ``붙이기(생략 가능)
create table `client`(
	client_id	varchar(20),
    name		varchar(30),
    address		varchar(50),
    phone		varchar(15),
    birth_day	date
);

-- 테이블 구조 보기
describe `client`;
desc client;

-- 테이블 구조 보기(form editor 봐야 보기 편함)
show create table `client`;

-- 테이블 삭제
drop table `client`;

-- client 테이블 생성
create table `client`(
	client_id	varchar(20)		not null,
    name		varchar(30),
    address		varchar(50),
    phone		varchar(15),
    birth_day	date
);

-- 테이블 구조 보기
desc `client`;

-- 완전체 형식
-- 컬럼=attribute, Field
-- insert into 테이블명(컬럼명1, 컬럼명2, ... , 컬럼명n)
-- values(값1, 값2, ... , 컬럼명n);

-- 데이터(행) 추가하기
insert into `client`(client_id,name,address) -- ,phone,birth_day) -- 순서대로 넣기
values('ryan','라이언','서울시 강남구');

-- 단순 조회(와일드카드(*) 이용)
-- select *
-- from 테이블명

-- 데이터 조회하기
select * 
from `client`;

-- 간략형
-- insert into 테이블명
-- values(값1, 값2, ... , 값n);

-- 데이터 추가하기(잘못된 예)
-- 구조 확인하고 넣던지, 완전체로 하기
insert into `client`
values('서울시 서초구','어피치','010-1234-5678','test','2022-09-08');

-- 데이터 조회하기
select * 
from `client`;

-- 데이터 삭제하기(데이터 전부 지우기)
delete 
from `client`;

-- 데이터 조회하기
select * 
from `client`;

-- 데이터 삭제하기(한 행을 모두 지우기)
delete 
from `client`
where client_id='서울시 서초구';

-- 데이터 조회하기
select * 
from `client`;

-- 데이터 추가하기(에러 발생)
insert into `client`(name,address)
values('어피치','서울시 서초구');

















