import java.io.*;
import java.util.*;

public class Solution {
    private static Deque<Character> deque = new LinkedList<>();

    public boolean isEmpty() {
        return deque.isEmpty();
    }

    public int getSize() {
        return deque.size();
    }

    public void enqueueCharacter(char c) {
        deque.addLast(c); 
    }

    public char dequeueCharacter() {
        return deque.pollFirst();
    }

    public void pushCharacter(char c) {
        deque.addLast(c); 
    }

    public char popCharacter() {
        return deque.pollLast();
    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String input = scan.nextLine();
        scan.close();

        // Convert input String to an array of characters:
        char[] s = input.toCharArray();

        // Create a Solution object:
        Solution p = new Solution();

        // Enqueue/Push all chars to their respective data structures:
        for (char c : s) {
            p.pushCharacter(c);
            p.enqueueCharacter(c);
        }

        // Pop/Dequeue the chars at the head of both data structures and compare them:
        boolean isPalindrome = true;
        for (int i = 0; i < s.length/2; i++) {
            if (p.popCharacter() != p.dequeueCharacter()) {
                isPalindrome = false;                
                break;
            }
        }

        //Finally, print whether string s is palindrome or not.
        System.out.println( "The word, " + input + ", is " 
                           + ( (!isPalindrome) ? "not a palindrome." : "a palindrome." ) );
    }
}
