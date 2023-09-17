
public class Ex_20230117_05 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] num = {10,20,30};
		
		try {
			for(int i=0; i<5; i++) {
				System.out.println(num[i]);
			}
		} catch (ArrayIndexOutOfBoundsException e) {
			System.out.println("ArrayIndexOutOfBoundsException 예외 발생");
		}
		
	}

}
