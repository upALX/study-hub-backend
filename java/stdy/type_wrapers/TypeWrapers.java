package type_wrapers;

public class TypeWrapers {
    public static void main(String[] args) {
        Integer numberInt = 123;
        Double numberDouble = numberInt.doubleValue();
        Integer convertedValue = numberDouble.intValue();

        String.format("The final converted value is: %d ", convertedValue);
    }
}
