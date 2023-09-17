import java.util.Scanner;

public class KakaoBank {
	
	private static Account[] acArr = new Account[100];
	private static Scanner sc = new Scanner(System.in);
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		boolean run = true;
		
		while(run) {
			System.out.println("1.계좌생성2.계좌목록3.예금4.출금5.종료");
			System.out.print("선택>");
			
			int no = sc.nextInt();
			
			if(no==1)
				createAccount();
			else if(no==2)
				accountList();
			else if(no==3)
				deposit();
			else if(no==4)
				withdraw();
			else if(no==5)
				run = false;
		}
		System.out.println("프로그램 종료합니다.");
	}
	
	private static void withdraw() {
		// TODO Auto-generated method stub
		System.out.println("출금");
		System.out.print("계좌번호 : ");
		String ano = sc.next();
		System.out.print("출금액 : ");
		int money = sc.nextInt();
		
		Account ac = findAccount(ano);
		if(ac==null) {
			System.out.println("계좌가 없습니다.");
			return;
		}
		
		ac.setBalance(ac.getBalance()-money);
		System.out.println("출금이 성공했습니다.");
	}

	private static void deposit() {
		// TODO Auto-generated method stub
		System.out.println("예금");
		System.out.print("계좌번호 : ");
		String ano = sc.next();
		System.out.print("입금액 : ");
		int money = sc.nextInt();
		
		Account ac = findAccount(ano);
		if(ac==null) {
			System.out.println("계좌가 없습니다.");
			return;
		}
		
		ac.setBalance(ac.getBalance()+money);
		System.out.println("입금이 성공했습니다.");
	
	}

	private static Account findAccount(String ano) {
		// TODO Auto-generated method stub
		Account ac = null;
		
		for(int i=0; i<acArr.length; i++) {
			if(acArr[i] != null) {
				String dbano = acArr[i].getAno();
				if(dbano.equals(ano)) {
					ac = acArr[i];
					break;
				}
			}
		}
		
		return ac;
	}

	private static void accountList() {
		// TODO Auto-generated method stub
		System.out.println("계좌목록");
		for(int i=0; i<acArr.length; i++) {
			Account ac = acArr[i];
			if(ac != null) {
				System.out.print(ac.getAno()+"  ");
				System.out.print(ac.getOwner()+"  ");
				System.out.println(ac.getBalance());
			}
			
			
		}
	}


	private static void createAccount() {
		// TODO Auto-generated method stub
		System.out.println("계좌생성");
		System.out.print("계좌번호 : ");
		String ano = sc.next();
		System.out.print("계좌주 : ");
		String owner = sc.next();
		System.out.print("입금액 : ");
		int balance = sc.nextInt();
		
		Account newAccount  = new Account(ano, owner, balance);
		
		for(int i=0; i<acArr.length; i++) {
			if(acArr[i]==null) {
				acArr[i] = newAccount;
				System.out.println("계좌가 생성되었습니다.");
				break;
			}
		}
	}
	
	
	

}





