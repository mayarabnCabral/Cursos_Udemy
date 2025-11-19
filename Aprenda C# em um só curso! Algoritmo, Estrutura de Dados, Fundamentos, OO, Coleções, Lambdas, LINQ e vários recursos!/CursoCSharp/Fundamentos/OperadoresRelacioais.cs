/*
    Operadores Relacionais
    >  -> Maior

    <  -> Menor

    >= -> Maior ou igual

    <= -> Menor ou igual  

    == -> Igual

    != -> Diferente
*/


using System;

namespace CursoCSharp.Fundamentos
{
    class OperadoresRelacionais
    {
        public static void Executar()
        {
            Console.WriteLine("Digite a nota do aluno:");
            double.TryParse(Console.ReadLine(), out double nota);


            double notaDeCorte = 6.0;

            Console.WriteLine($"Nota inválida: {nota > 10.0 && nota < 0.0}"); // Verifica se a nota é maior que 10 e menor que 0
            Console.WriteLine($"Reprovado: {nota < notaDeCorte}"); // Verifica se a nota é menor que a nota de corte
            Console.WriteLine($"Perfeito: {nota == 10.0}"); // Verifica se a nota é igual a 10
            Console.WriteLine($"Tem como melhorar? {nota != 10.0}"); // Verifica se a nota é diferente de 10
            Console.WriteLine($"Passou por média? {nota >= notaDeCorte}"); // Verifica se a nota é maior ou igual a nota de corte
            Console.WriteLine($"Recuperação? {nota < notaDeCorte}"); //  Verifica se a nota é menor que a nota de corte
            Console.WriteLine($"Reprovado? {nota <= 3.0}"); // Verifica se a nota é menor ou igual a 3
        }
    }
}