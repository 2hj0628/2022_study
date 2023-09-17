
public class Phone {
	//필드
	String model;  //private쓰면 자식한테 안나옴 -> protected 사용
	String color;
	
	//기본 생성자
	public Phone() {
		System.out.println("Phone() 생성자 호출");
	}
	
	//메서드
	void powerOn() {
		 System.out.println("전원을 켭니다.");
	}
	
	void powerOff() {
		System.out.println("전원을 끕니다.");
	}
	
	void bell() {
		System.out.println("전화벨이 울립니다.");
	}
	
	void hangUp() {
		System.out.println("전화를 끊습니다.");
	}
	
	
}






