
public class CalculatorMain {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Calculator cal1 = new Calculator();
		
		cal1.powerOn();
		
		int result1 = cal1.plus(10, 5);
		System.out.println(result1);
		
		double result2 = cal1.plus(10.2, 3.14);
		System.out.println(result2);
		
		double result3 = cal1.plus(3.14, 100);
		System.out.println(result3);
		
		double result4 = cal1.plus(10, 3.14);
		System.out.println(result4);
		
		
		cal1.powerOff();
	}

}
