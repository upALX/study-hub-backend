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
    private List<Transacions> history;

    public CurrentAccount(int accountNumber, int agencyNumber, String clientName, LocalDate birthDate, double accountBalance) {
        this.accountBalance = accountBalance;
        this.accountNumber = accountNumber;
        this.clientName = clientName;
        this.birthDate = birthDate;
        this.agencyNumber = agencyNumber;
        this.accounts = new ArrayList<>();
        this.history = new ArrayList<>();
    }

    public void getAmount(){
        String.format("Saldo total: %.2f", this.accountBalance);
    }

    public void getValue(double value){

        if (value <= accountBalance){
            this.accountBalance -= value;
            String.format("Você sacou %.2f. Saldo atual: %.2f", value, this.accountBalance);
        }else{
            String.format("Seu saldo é insuficiente para o saque. Deposite. Melhore. Saldo atual: %.2f", this.accountBalance);
        }

    }

    private boolean validateAccount(int account){
        return this.accounts.contains(account);
    }

    public void removeAccount(int account){
        boolean isValidAccount = this.validateAccount(account);

        if(isValidAccount){
            this.accounts.remove(Integer.valueOf(account));
            String.format("Conta %i removida.", this.accountNumber);
        }else{
            String.format("Conta %i não existe.", this.accountNumber);
        }
    }

    public List<Transacions> getHistory() {
        return history;
    }

//    public List<Transacions> getHistory(LocalDate start, LocalDate end) {
//        List<Transacions> filtered = new ArrayList<>();
//        for (Transacions transaction : history) {
//            LocalDate date = transaction.getDate().toLocalDate();
//            if ((date.isEqual(start) || date.isAfter(start)) &&
//                    (date.isEqual(end)   || date.isBefore(end))) {
//                filtered.add(transaction);
//            }
//        }
//        return filtered;
//    }
}