-- 테이블 명세(엔티티 명세)
-- 데이터베이스 선택
use kakao_bank;

-- 회원 정보 테이블 생성
create table `member`(
	id 			varchar(50),
    password	varchar(50)		not null,
    name		varchar(50)		not null,
    birth		date			not null,
    tel			varchar(20)		not null,
    email		varchar(50)		not null,
    address		varchar(100)	not null,
    primary key(id)
);

-- 회원정보 테이블 구조 보기
desc `member`;

-- 상품 테이블 생성
create table `product`(
	serial		int				auto_increment,	-- 일련번호
    name		varchar(50)		not null,		-- 상품명
    standard	varchar(50)		not null,		-- 규격
    price		int				not null,		-- 가격
    primary key(serial)
);

-- 상품 테이블 구조 보기
desc `product`;

-- 주문 내역 테이블 생성
create table `order_list`(
	serial		int			auto_increment,					-- 주문번호
    date		timestamp	default current_timestamp(),	-- 주문일
    order_id	varchar(50)	not null,						-- 회원ID
    product_id	int			not null,						-- 상품ID
    qty			int			default 1,						-- 주문수량
	primary key(serial),
    foreign key(order_id)	references`member`(id),
    foreign key(product_id)	references`product`(serial)
);

-- 주문 내역 테이블 구조 보기
desc `order_list`;
show create table `order_list`;

-- 테이블 목록 보기
show tables;



