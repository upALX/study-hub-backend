import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;
import java.math.BigInteger;



public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String n = bufferedReader.readLine();
        
        BigInteger value = new BigInteger(n);
        
        boolean isPrime = value.isProbablePrime(1);

        System.out.print(isPrime ? "prime" : "not prime");

        bufferedReader.close();
    }
}
