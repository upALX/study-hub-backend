import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;
import java.util.Scanner;


public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        Scanner scan = new Scanner(System.in);
        String S = scan.next();
        
        try{
            
            int value = Integer.parseInt(S);
            
            System.out.println(value);
                        
        }catch(NumberFormatException e){
            System.out.print("Bad String");
        }
        
        scan.close();
    }
}
