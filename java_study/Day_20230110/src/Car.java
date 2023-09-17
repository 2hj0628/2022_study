
public class Car {

	// 필드
	String company =  "테슬라";
	String model;
	String color;
	int maxSpeed;
	
	//기본 생성자
	public Car() {
		this("자동차","은색", 250);
	}

	//매개 변수가 있는 생성자
	public Car(String model) {
		this(model, "은색", 250);
	}

	public Car(String model, String color) {
		this(model, color, 250);
	}

	public Car(String model, String color, int maxSpeed) {
		this.model = model;
		this.color = color;
		this.maxSpeed = maxSpeed;
		//this(model, color, maxSpeed);
	}
	
	
	
	
	
	
	
	
	
	
	
}
