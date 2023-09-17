
public class SmartPhone extends Phone {
	
	//생성자 (슈퍼클래스로부터 - 기본생성자 필요X, new로 못만드므로)
	public SmartPhone(String owner) {
		super(owner);
	}
	
	//메서드
	public void searchInternet() {
		System.out.println("인터넷 검색을 수행합니다.");
	}
	
	
	

}
