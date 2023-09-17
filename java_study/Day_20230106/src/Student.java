
public class Student {

	//속성 : 필드
	private int num;
	private int score;

	//기본 생성자
	public Student() {
		System.out.println("생성자가 호출되었습니다.");
	}
	
	//함수 : 메소드
	public int getNum() {
		return num;
	}

	public void setNum(int num) {
		this.num = num;
	}

	public int getScore() {
		return score;
	}

	public void setScore(int score) {
		this.score = score;
	}
	
	
	
		
}
