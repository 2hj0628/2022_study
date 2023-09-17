import java.util.Scanner;

public class Ex_20221230_01 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		System.out.print("아이디 입력 : ");
		String id = sc.nextLine();
		
		//System.out.println("id : " + id);
	
		System.out.print("패스워드 입력 : ");
		String pwd = sc.nextLine();
		
		int pwd2 = Integer.parseInt(pwd);
		//System.out.println("pwd2 : " + pwd2);
		
		//mysql 접속 프로그램
		if(id.equals("root") && pwd2==1234) {
			System.out.println("관리자님 환영합니다.");
		} else {
			System.out.println("아이디 또는 패스워드가 틀렸습니다.");
		}
		
	}

}
