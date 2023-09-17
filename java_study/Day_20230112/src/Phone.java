
public abstract class Phone {
	
	//필드
	public String owner;
	
	//생성자 추상클래스에선 필수
	public Phone(String owner) {
		this.owner = owner;
	}
	
	//메서드
	public void powerOn() {
		 System.out.println("전원을 켭니다.");
	}
	
	public void powerOff() {
		System.out.println("전원을 끕니다.");
	}
	

}
