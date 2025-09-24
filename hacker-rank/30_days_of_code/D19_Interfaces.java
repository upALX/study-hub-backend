import java.io.*;
import java.util.*;

interface AdvancedArithmetic{
   int divisorSum(int n);
}
class Calculator implements AdvancedArithmetic {
    public int divisorSum(int n) {
        
        ArrayList<Integer> list = new ArrayList<>();
        
        for(int counter = 0; counter <= n; counter++){
            if(counter !=0){
                if (n % counter == 0){
                list.add(counter);
            } 
            }
            
        }
        
        return list.stream().mapToInt(Integer::intValue).sum();
    }
}

class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        scan.close();
        
      	AdvancedArithmetic myCalculator = new Calculator(); 
        int sum = myCalculator.divisorSum(n);
        System.out.println("I implemented: " + myCalculator.getClass().getInterfaces()[0].getName() );
        System.out.println(sum);
    }
}
