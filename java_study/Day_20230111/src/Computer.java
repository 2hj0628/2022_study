
public class Computer extends Calculator {

	@Override
	double areaCircle(double r) {
		// TODO Auto-generated method stub
		System.out.println("원의 넓이 계산 - Computer의 areaCircle()");
		return Math.PI*r*r;
		//return super.areaCircle(r);
	}

	
}
