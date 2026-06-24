import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        
        Scanner leitor = new Scanner(System.in);
        
        System.out.println("Digite a primeira nota:"); 
        float nota1 = leitor.nextFloat();
        
        System.out.println("Digite a segunda nota:");
        float nota2 = leitor.nextFloat();
        
        float media = (nota1 + nota2) / 2;
        
        if (media >= 7) {
            System.out.println("O aluno foi aprovado!");
        } else {
            System.out.println("O aluno foi reprovado!");
        }
        
        leitor.close();
    } 
} 