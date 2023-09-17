
public class Ex_20230102_04 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String position="과장";
		
		if(position== "부장")
			System.out.println("보너스 500만원");
		else if(position== "차장" | position== "과장")
			System.out.println("보너스 300만원");
//		else if(position== "차장")
//			System.out.println("보너스 300만원");
//		else if(position== "과장")
//			System.out.println("보너스 300만원");
		else
			System.out.println("보너스 100만원");
		
	}

}
