import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int numberOfStrings = scanner.nextInt();
        scanner.nextLine();  
        
        for (int inc = 0; inc < numberOfStrings; inc++) {
            String s = scanner.nextLine(); 
            
            StringBuilder evenIndexedChars = new StringBuilder();
            StringBuilder oddIndexedChars = new StringBuilder();
            
            for (int index = 0; index < s.length(); index++) {
                if (index % 2 == 0) {
                    evenIndexedChars.append(s.charAt(index));
                } else {
                    oddIndexedChars.append(s.charAt(index));
                }
            }
            
            System.out.println(evenIndexedChars + " " + oddIndexedChars);
        }
        
        scanner.close();
    }
}
