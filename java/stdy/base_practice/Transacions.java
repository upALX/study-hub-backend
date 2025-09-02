package base_practice;


import java.time.LocalDateTime;

public class Transacions {
    private String type;
    private double amount;
    private LocalDateTime date;

    public Transacions(String type, double amount){
        this.type = type;
        this.amount = amount;
        this.date = LocalDateTime.now();
    }

    @Override
    public String toString() {
        return String.format("[%s] %s de R$%.2f", date, type, amount);
    }
}
