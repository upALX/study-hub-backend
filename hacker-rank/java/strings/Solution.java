import java.util.Scanner;

public class Solution {

    static boolean isAnagram(String firstWord, String secondWord) {

        char[] firstWordNormalized = firstWord.toLowerCase().toCharArray();
        char[] secondWordNormalized = secondWord.toLowerCase().toCharArray();

        java.util.Arrays.sort(firstWordNormalized);
        java.util.Arrays.sort(secondWordNormalized);

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