
public class ComputerMain {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int r = 10;
		
		Calculator c1 = new Calculator();
		System.out.println("원의 넓이 : " +c1.areaCircle(r));
		
		Computer c2 = new Computer();
		System.out.println("원의 넓이 : " +c2.areaCircle(r));
	}

}
