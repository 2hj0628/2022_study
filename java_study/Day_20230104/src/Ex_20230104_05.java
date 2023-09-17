
public class Ex_20230104_05 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] scores = new int[3];
		int sum = 0;
		double avg = 0.0;
		
		scores[0] = 90;
		scores[1] = 80;
		scores[2] = 75;
		
		for(int i=0; i<scores.length; i++) {
			System.out.println(scores[i]);
			sum += scores[i];
		}
		
		//avg = (double)sum / 3;
		//avg = sum / 3.0;
		avg = (double)sum / 3.0;
		
		System.out.println("ÃÑÁ¡ : " + sum);
		System.out.println("Æò±Õ : " + avg);
	}

}
