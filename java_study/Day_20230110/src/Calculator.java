
public class Calculator {

	//메서드
	void powerOn() {
		System.out.println("전원이 켜집니다.");
	}
	
	//메서드 오버로딩
	int plus(int x, int y) {
		int result = x + y;
		return result;
	}
		
	double plus(double x, double y) {
		double result = x + y;
		return result;
	}
	
	double plus(int x, double y) {
		double result = x + y;
		return result;
	}
	
	double plus(double x, int y) {
		double result = x + y;
		return result;
	}
	
	
	void powerOff() {
		System.out.println("전원이 꺼집니다.");
	}
	
}
