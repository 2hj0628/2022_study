
public class Ex_20230102_03 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String position="차장";
		
		switch(position) {
		case "부장":
			System.out.println("보너스 500만원");
			break;
		case "차장": //브레이크가 없으므로 차장도 300
		case "과장":
			System.out.println("보너스 300만원");
			break;
		default:
			System.out.println("보너스 100만원");
		}
	}

}
