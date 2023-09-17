import java.util.Scanner;

public class KaKaoSchool {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		boolean run = true;
		int studentNo = 0;
		int[] scores = null;
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("카카오 대학교 파이썬 성적 관리 프로그램(ver 1.0)");
		
		while(run) {
			System.out.println("----------------------------------------");
			System.out.println("1.학생수 2.점수입력 3.점수리스트 4.분석 5.종료");
			System.out.println("----------------------------------------");
			System.out.print("선택>");
			
			int num = sc.nextInt();
			
			switch(num) {
				case 1 :
					//학생 수 등록
					System.out.print("등록할 학생수 : ");
					int std_num = sc.nextInt(); 
					scores = new int[std_num];
					break;
				case 2 :
					//점수 입력
					System.out.print("1번째 학생 점수 :");
					scores[0] = sc.nextInt();
					break;
				case 3 :
					//점수 리스트 표시
					System.out.println("1번 학생 : " + scores[0]);
					break;
				case 4 :
					//분석 - 최고점수, 최저점수, 평균
					System.out.println("최고점수 : " + scores[0]);
					System.out.println("최저점수 : " + scores[0]);
					System.out.println("평균 : " + scores[0]);
					break;
				case 5 :
					//종료
					run = false;
					break;
				default :
					System.out.println("잘못 선택하셨습니다.");
			}			
		}
		
		System.out.println("프로그램 종료");
		
		
	}

}
