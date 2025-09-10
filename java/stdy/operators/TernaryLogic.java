package operators;

public class TernaryLogic {

    public static void main(String[] args) {
        //expression ? true : false
        String name = "Iza";
        final int MAIOR_IDADE = 17;

        boolean value1 = true;
        boolean value2 = 1+1 >= 3;

        String maiorIdadeExpression = name + (MAIOR_IDADE >= 18 ? " é maior de idade\n" : " não é maior de idade\n");

        System.out.print(maiorIdadeExpression);

        //LOGICOS
        if (value1 == value2 || value1 != value2){
            System.out.print("Deu bom!");
        }

    }
}
