
public class AirConditionerMain {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		AirConditioner ac = new AirConditioner();
		
		ac.turnOn();
		int temp = ac.getTemp();
		System.out.println("현대 온도 : " + temp);
		ac.setTemp(30);
		ac.turnOff();
	}

}
