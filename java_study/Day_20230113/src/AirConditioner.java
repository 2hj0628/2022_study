
public class AirConditioner implements RemoteControl {

	//필드
	private int temp;
	
	public int getTemp() {
		return temp;
	}

	@Override
	public void turnOn() {
		// TODO Auto-generated method stub
		System.out.println("에어컨을 켭니다.");
	}

	@Override
	public void turnOff() {
		// TODO Auto-generated method stub
		System.out.println("에어컨을 끕니다.");
	}

	@Override
	public void setTemp(int temp) {
		// TODO Auto-generated method stub
		if(temp > RemoteControl.MAX_TEMP) {
			this.temp = RemoteControl.MAX_TEMP;
		}else if(temp < RemoteControl.MIN_TEMP) {
			this.temp = RemoteControl.MIN_TEMP;
		}else {
			this.temp = temp;
		}
		
		System.out.println("현재 온도 : " + this.temp);
		
	}

	
	
}
