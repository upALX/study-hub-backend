import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        String value1 = scan.next();
        String value2 = scan.next();

        try{
            
            long valueLong1;
            long valueLong2;
            
            try {
                valueLong1 = Long.parseLong(value1);
                valueLong2 = Long.parseLong(value2);
            } catch (NumberFormatException e) {
                throw new InputMismatchException();
            }
            
            if (valueLong1 < Integer.MIN_VALUE || valueLong1 > Integer.MAX_VALUE ||
    valueLong2 < Integer.MIN_VALUE || valueLong2 > Integer.MAX_VALUE) {
    throw new InputMismatchException();
}
            
            long result = valueLong1 / valueLong2;
            
            System.out.println(result);
            
        }catch(InputMismatchException e){
            System.out.print(e);
            
        }catch(ArithmeticException e){
            System.out.print(e);
        }catch(NumberFormatException e){
            System.out.print(e);
        }
        
                
    }
}
