import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;



public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());
        
        String strBinNumber = String.valueOf(Integer.toBinaryString(n)); 
        
        int currentSum = 0;
        int maxSum = 0;
        for(int value = 0; value < strBinNumber.length(); value++){
            char current = strBinNumber.charAt(value);
            if (current == '1'){
                currentSum++;
            }else{
                currentSum = 0;
            }
            maxSum = Math.max(maxSum, currentSum);
        }
        
        System.out.print(maxSum);

        bufferedReader.close();
    }
}
