
public class Ex_20230117_07 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			String data1 = "100";
			String data2 = "a100";
			
			int num1 = Integer.parseInt(data1);
			int num2 = Integer.parseInt(data2);
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			System.out.println("finally 구문 실행");
		}
	}

}
