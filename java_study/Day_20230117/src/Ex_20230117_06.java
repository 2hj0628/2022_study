
public class Ex_20230117_06 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		try {
			String data = null;
			System.out.println(data.toString());
			
			int[] num = {10,20,30};
			for(int i=0; i<5; i++) {
				System.out.println(num[i]);
			}
			
			String data1 = "100";
			String data2 = "a100";
			
			int num1 = Integer.parseInt(data1);
			int num2 = Integer.parseInt(data2);
		
		} catch (NullPointerException e) {
			System.out.println("NullPointerException 예외 발생");
		} catch (ArrayIndexOutOfBoundsException e) {
			System.out.println("ArrayIndexOutOfBoundsException 예외 발생");
		} catch (NumberFormatException e) {
			System.out.println("NumberFormatException 예외 발생");
		} catch (Exception e) {
			System.out.println("Exception 예외 발생");
		} finally {
			System.out.println("finally 구문 실행");
		}
	}

}
