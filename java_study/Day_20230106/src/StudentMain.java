import java.util.Scanner;

public class StudentMain {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int num;
		int score;
		
		Student s1 = new Student();
		System.out.print("학번 입력 :");
		num = sc.nextInt();
		s1.setNum(num);
		//s1.setNum(sc.nextInt());  num,score 안써도됨
		System.out.print("점수 입력 :");
		score = sc.nextInt();
		s1.setScore(score);
		
		Student s2 = new Student();
		System.out.print("학번 입력 :");
		num = sc.nextInt();
		s2.setNum(num);
		System.out.print("점수 입력 :");
		score = sc.nextInt();
		s2.setScore(score);
		
		System.out.println("학생 정보");
		System.out.println(s1.getNum());
		System.out.println(s1.getScore());
		System.out.println(s2.getNum());
		System.out.println(s2.getScore());
		double avg = (s1.getScore()+s2.getScore())/2.0;
		System.out.println(avg);
		
		
	}

}
