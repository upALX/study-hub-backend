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

        List<List<Integer>> arr = new ArrayList<>();

        IntStream.range(0, 6).forEach(i -> {
            try {
                arr.add(
                    Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                        .map(Integer::parseInt)
                        .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });
        
        int rows = arr.size();
        int columns = arr.get(0).size();
        
        if(rows < 3 || columns < 3){
            throw new IllegalArgumentException("The array must be min 3x3");
        }
        
        int maxSum = Integer.MIN_VALUE;
        
        for(int i = 0; i < rows - 2; i++){
            for(int j = 0; j < columns - 2; j++){
                int top = arr.get(i).get(j) + arr.get(i).get(j + 1) + arr.get(i).get(j+ 2); 
                int middle = arr.get(i+1).get(j + 1);
                int bottom = arr.get(i + 2).get(j) + arr.get(i+2).get(j+1) + arr.get(i+2).get(j+2);
            
                int currentSum = top + middle + bottom;
            
                if(maxSum < currentSum){
                    maxSum = currentSum;
                }
            
            }
        }
        
        System.out.print(maxSum);

        bufferedReader.close();
    }
}
