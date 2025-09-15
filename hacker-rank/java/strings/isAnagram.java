import java.util.Scanner;

public class Solution {

    static boolean isAnagram(String firstWord, String secondWord) {

        char[] firstWordNormalized = firstWord.toLowerCase().toCharArray();
        char[] secondWordNormalized = secondWord.toLowerCase().toCharArray();

        java.util.Arrays.sort(firstWordNormalized);
        java.util.Arrays.sort(secondWordNormalized);
        
        int[] counter = new int[26];
        
        for(char iter : firstWordNormalized){
            counter[iter - 'a']++;
        }  
        
        for(char iter : secondWordNormalized){
            counter[iter - 'a']--;
        }        
        
        for (int count : counter) {
            if (count != 0) {
                return false;
            }
        }
        
        if (firstWordNormalized.length != secondWordNormalized.length) {
            return false;
        }else{
            return true;
        }
        
    }

    public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
