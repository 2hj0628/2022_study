
public class Ex_20221229_09 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		/*
		int num = 5;
		if(num%2 == 0) {
			System.out.println("짝수");
		} else {
			System.out.println("홀수");
		}
		*/
		int num = 5;
		String result = null;
		
		// 파이썬 문법 : (참인 값) if 조건 else (거짓인경우 값)
		// 자바 문법 : 조건 ? 참인 값 : 거짓인경우 값
		
		// 파이썬 문법 : and or
		// 자바 문법 : && ||
		result = (num%2 == 0) ? "짝수" : "홀수";
		System.out.println(result);
		
	
		
		
		
	}

}
