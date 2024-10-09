//Complete this code or write your own from scratch
import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        HashMap<String, String> numberString = new HashMap<String, String>();
        ArrayList<String> namesSearch = new ArrayList<>();
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        for(int i = 0; i < n; i++){
            String name = in.next();
            String phone = in.next();
            numberString.put(name, phone);
        }
        while(in.hasNext()){
            String nameSearch = in.next();
            namesSearch.add(nameSearch);
        }
        for(int inc = 0; inc < namesSearch.size(); inc++){
            if(numberString.containsKey(namesSearch.get(inc))){
                System.out.println(namesSearch.get(inc) + "=" + numberString.get(namesSearch.get(inc)));
            }else{
                System.out.println("Not found");
            }
        }
        in.close();
    }
}
