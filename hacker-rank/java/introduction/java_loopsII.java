import java.util.*;
import java.io.*;
import java.util.Scanner;

class Solution{
    //base+(base^k)*value)
   //k é fator
    public static void main(String []argh){
        Scanner scanner = new Scanner(System.in);

        int entries=scanner.nextInt();
        for(int i=0;i<entries;i++){
            int iniValue = scanner.nextInt();
            int values = scanner.nextInt();
            int loops = scanner.nextInt();
            
            int sum = iniValue;
            int fator = 1;
            for (int j = 0; j < loops; j++) {
                sum += fator * values;
                System.out.print(sum + " ");
                fator *= 2; 
            }
            System.out.println();
        }
    scanner.close();
    }
}
