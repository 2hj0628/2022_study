
public class Ex_20230105_01 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] scores = { 95, 70, 88, 69, 99, 100, 45, 60};
		int sum = 0;
		
		for(int score : scores) {
			sum += score;
		}
		System.out.println("sum : "+ sum);
		
		double avg = (double)sum / scores.length;
		
		System.out.println("avg : "+avg);
		
	}

}
