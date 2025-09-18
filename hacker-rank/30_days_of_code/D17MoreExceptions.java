import java.util.*;
import java.io.*;

//Write your code here

class Calculator{
    
    public static void main(String args[]){
        
    }
    
    public int power(int n, int p) throws Exception{
        
        if (n != Math.abs(n) || p != Math.abs(p)){
            throw new Exception("n and p should be non-negative");
        }
        
        return (int) Math.pow(n, p);
    }
}

class Solution{

    public static void main(String[] args) {
    
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        while (t-- > 0) {
        
            int n = in.nextInt();
            int p = in.nextInt();
            Calculator myCalculator = new Calculator();
            try {
                int ans = myCalculator.power(n, p);
                System.out.println(ans);
            }
            catch (Exception e) {
                System.out.println(e.getMessage());
            }
        }
        in.close();
    }
}
