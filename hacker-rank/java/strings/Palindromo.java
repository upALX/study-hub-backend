import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A =sc.next();
        sc.close();
        
        String B = new StringBuilder(A).reverse().toString();
        
        if(A.equals(B)){
            System.out.print("Yes");
        }else{
            System.out.print("No");
        }
        
    }
}



