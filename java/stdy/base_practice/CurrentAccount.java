package base_practice;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class CurrentAccount{
    private int accountNumber;
    private int agencyNumber;
    private String clientName;
    private LocalDate birthDate;
    private double accountBalance = 0.0;
    private List<Integer> accounts;

    public CurrentAccount(int accountNumber, int agencyNumber, String clientName, LocalDate birthDate, double accountBalance) {
        this.accountBalance = accountBalance;
        this.accountNumber = accountNumber;
        this.clientName = clientName;
        this.birthDate = birthDate;
        this.agencyNumber = agencyNumber;
        this.accounts = new ArrayList<>();
    }

    public String getValue(double value){

        String message;

        if (value <= accountBalance){
            this.accountBalance -= value;
            message = String.format("Você sacou %.2f. Saldo atual: %.2f", value, this.accountBalance);
        }else{
            message = String.format("Seu saldo é insuficiente para o saque. Deposite. Melhore. Saldo atual: %.2f", this.accountBalance);
        }

        return message;
    }

    private boolean validateAccount(int account){
        return this.accounts.contains(account);
    }
}