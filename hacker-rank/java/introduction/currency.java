import java.text.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();

        Locale us = Locale.US;
        Locale france = Locale.FRANCE;
        Locale china = Locale.CHINA;
        Locale india = new Locale("en", "IN");

        Map<Locale, String> labels = new LinkedHashMap<>();
        labels.put(us, "US");
        labels.put(india, "India");
        labels.put(china, "China");
        labels.put(france, "France");

        for (Locale locale : labels.keySet()) {
            NumberFormat format = NumberFormat.getCurrencyInstance(locale);

            if (locale.equals(india)) {
                DecimalFormatSymbols symbols = ((DecimalFormat) format).getDecimalFormatSymbols();
                symbols.setCurrencySymbol("Rs."); 
                ((DecimalFormat) format).setDecimalFormatSymbols(symbols);
            }

            String formatted = format.format(payment);

            if (locale.equals(france)) {
                formatted = formatted.replace("\u202F", " ");
            }

            System.out.println(labels.get(locale) + ": " + formatted);
        }
    }
}
