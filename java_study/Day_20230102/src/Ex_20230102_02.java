
public class Ex_20230102_02 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int num=(int)(Math.random()*6)+1; // 1-6
		
		switch(num) {
			case 1:
				System.out.println(num);
				break;
			case 2:
				System.out.println(num);
				break;
			case 3:
				System.out.println(num);
				break;
			case 4:
				System.out.println(num);
				break;
			case 5:
				System.out.println(num);
				break;
			default:
				System.out.println(num); //6 default는 브레이크X
			
		}
	}

}
