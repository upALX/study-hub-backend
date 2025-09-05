import java.io.*;
import java.util.*;
import java.util.Scanner;


public class Solution {
    static int B;
    static int H;
    static boolean flag = true;

    static {
        Scanner scanner = new Scanner(System.in);
        B = scanner.nextInt();
        H = scanner.nextInt();
        
        if (B <= 0 || H <= 0) {
            flag = false;
            System.out.println("java.lang.Exception: Breadth and height must be positive");
        }
        scanner.close();
    }

    public static void main(String[] args) {
        
        if(flag){
            System.out.print(H *B);
        }
        
    }
}
