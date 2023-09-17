
public class CarMain {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Car c1 = new Car();
		System.out.println(c1.company);
		System.out.println(c1.model);
		System.out.println(c1.color);
		System.out.println(c1.maxSpeed);
		
		Car c2 = new Car("자가용");
		System.out.println(c2.company);
		System.out.println(c2.model);
		System.out.println(c2.color);
		System.out.println(c2.maxSpeed);
		
		Car c3 = new Car("자가용", "흰색");
		System.out.println(c3.company);
		System.out.println(c3.model);
		System.out.println(c3.color);
		System.out.println(c3.maxSpeed);
		
		Car c4 = new Car("택시", "빨간색", 500);
		System.out.println(c4.company);
		System.out.println(c4.model);
		System.out.println(c4.color);
		System.out.println(c4.maxSpeed);
		
		
	}

}
