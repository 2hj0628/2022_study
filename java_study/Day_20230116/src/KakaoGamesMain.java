package KakaoGames;

import java.util.Scanner;

public class KakaoGamesMain {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		Character character = null;
		GameEngine ge = null;
		
		System.out.println("캐릭터 생성");
		System.out.println("1.라이언2.어피치3.무지");
		int num = sc.nextInt();
		
		switch(num) {
			case 1 : 
				character = new Ryan();
				break;
			case 2 :
				character = new Apeach();
				break;
			case 3 :
				character = new Muzi();
				break;
			default :
				System.out.println("잘못 입력하셨습니다s.");
		}
		
		if(character==null) {
			System.out.println("게임을 종료합니다.");
			return;
		}else {
			ge = new GameEngine(character);
		}
		
		while(true) {
			ge.printMenu(sc);
			if(ge.isExit()) {
				System.out.println("게임을 종료합니다.");
				break;
			}
		}
		
	}

}






