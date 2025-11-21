using System;

namespace CursoCSharp.Fundamentos
{
    class OperadoresUnarios
    {
        public static void Executar()
        {
            var valorNegativo = -5;
            var numero1 = 2;
            var numero2 = 3;
            var booleano = true;

            System.Console.WriteLine(-valorNegativo); // Operador Unário de Negação (inverte o sinal)

            System.Console.WriteLine(!booleano); // Operador Unário de Negação Lógica (inverte o valor booleano)

            numero1++; //  Operador de incremento pós-fixado: usa o valor primeiro e incrementa depois
            System.Console.WriteLine(numero1);

            --numero1; // Operador de decremento pré-fixado: decrementa primeiro e usa o valor depois
            System.Console.WriteLine(numero1);

            System.Console.WriteLine(numero1++ == --numero2); // Quando usamos o operador pós-fixado (++ ou -- depois da variável), o valor atual é usado primeiro e só depois a operação é aplicada. Já no operador pré-fixado (++ ou -- antes da variável), a operação é aplicada imediatamente e o valor já alterado é usado na expressãoEm uma mesma expressão, o operador pré-fixado tem precedência, por isso --numero2 é executado antes de numero1++

            System.Console.WriteLine($"{numero1} {numero2}");

        }
    }
}