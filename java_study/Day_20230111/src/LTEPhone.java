
public class LTEPhone extends Phone {

	//필드
	int channel;
	
	//생성자
	public LTEPhone(String model, String color, int channel) {
		//super();  부모한테 받는 모델 컬러 자동호출 가능
		this.model = model;
		this.color = color;
		this.channel = channel;
		System.out.println("LTEPhone() 생성자 호출");
	}
	
	//메서드
	void turnOnDMB() {
		System.out.println("DMB방송을 시청합니다. - 채널 : "+
							this.channel +"번");
	}
	
	void changeChannel(int channel) {
		this.channel = channel;
		System.out.println("DMB 채널을 변경합니다. - 채널 : "+
							this.channel+"번");
	}
	
	void turnOffDMB() {
		System.out.println("DMB방송을 종료합니다.");
	}

}





