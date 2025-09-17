import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.Scanner.*;
import java.math.BigInteger;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        BigInteger value1 = scan.nextBigInteger();
        BigInteger value2 = scan.nextBigInteger();
        
        System.out.println(value1.add(value2));
        System.out.print(value1.multiply(value2));
    
    }
}
