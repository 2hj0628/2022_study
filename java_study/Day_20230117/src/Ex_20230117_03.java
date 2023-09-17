
public class Ex_20230117_03 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String data1 = "100";
		String data2 = "a100";
		
		int num1 = Integer.parseInt(data1);
		int num2 = Integer.parseInt(data2); //NumberFormatException
		
		int result = num1 + num2;
		System.out.println(result);
		
		
		
	}

}
