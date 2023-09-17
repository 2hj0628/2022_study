
public interface RemoteControl {
	//상수
	public int MAX_TEMP = 30;
	public int MIN_TEMP = 16;
	
	//추상 메서드
	public void turnOn();
	public void turnOff();
	public void setTemp(int temp);
	
}
