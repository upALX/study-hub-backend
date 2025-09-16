import java.util.Scanner;
import java.util.regex.*;
import java.util.regex.Pattern;


public class Solution
{
    
    public static boolean isValidRegex(String pattern) {
        try {
            Pattern.compile(pattern);
            return true;
        } catch (PatternSyntaxException e) {
            return false;
        }
    }
    
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
        int counter = 0;
		int testCases = Integer.parseInt(in.nextLine());
		while(testCases>0){
			String pattern = in.nextLine();
            boolean isValid = isValidRegex(pattern);
            
            System.out.println(isValid ? "Valid" : "Invalid");
            
            counter ++;
            if (counter == testCases){
                break;
            } 
		}
        in.close();
	}
}
