import java.util.Scanner;

public class KakaoBank {
	
	private static Account[] acArr = new Account[100];
	private static Scanner sc = new Scanner(System.in);
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		boolean run = true;
		
		while(run) {
			System.out.println("1.���»���2.���¸��3.����4.���5.����");
			System.out.print("����>");
			
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
		System.out.println("���α׷� �����մϴ�.");
	}
	
	private static void withdraw() {
		// TODO Auto-generated method stub
		System.out.println("���");
		System.out.print("���¹�ȣ : ");
		String ano = sc.next();
		System.out.print("��ݾ� : ");
		int money = sc.nextInt();
		
		Account ac = findAccount(ano);
		if(ac==null) {
			System.out.println("���°� �����ϴ�.");
			return;
		}
		
		ac.setBalance(ac.getBalance()-money);
		System.out.println("����� �����߽��ϴ�.");
	}

	private static void deposit() {
		// TODO Auto-generated method stub
		System.out.println("����");
		System.out.print("���¹�ȣ : ");
		String ano = sc.next();
		System.out.print("�Աݾ� : ");
		int money = sc.nextInt();
		
		Account ac = findAccount(ano);
		if(ac==null) {
			System.out.println("���°� �����ϴ�.");
			return;
		}
		
		ac.setBalance(ac.getBalance()+money);
		System.out.println("�Ա��� �����߽��ϴ�.");
	
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
		System.out.println("���¸��");
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
		System.out.println("���»���");
		System.out.print("���¹�ȣ : ");
		String ano = sc.next();
		System.out.print("������ : ");
		String owner = sc.next();
		System.out.print("�Աݾ� : ");
		int balance = sc.nextInt();
		
		Account newAccount  = new Account(ano, owner, balance);
		
		for(int i=0; i<acArr.length; i++) {
			if(acArr[i]==null) {
				acArr[i] = newAccount;
				System.out.println("���°� �����Ǿ����ϴ�.");
				break;
			}
		}
	}
	
	
	

}





