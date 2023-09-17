
public class PhoneMain {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		LTEPhone phone1 = new LTEPhone("라이언폰", "블루", 7);
		
		System.out.println(phone1.model);
		System.out.println(phone1.color);
		System.out.println(phone1.channel);
		
		phone1.powerOn();
		phone1.bell();
		phone1.hangUp();
		phone1.turnOnDMB();
		phone1.changeChannel(9);
		phone1.turnOffDMB();
		phone1.powerOff();
	}
	

}
