package flow_control;

public class Switch{
	static String value = "x";
	static Integer number;
	public static void main(String args[]){
	
		switch (value){
			case "x":{
				number = 1;
				break;

			}case "y":{
				number = 2;
				break;
			}
			default:{
				number = 3;
				break;
			} 
		}
		System.out.print(number);
	}

}
