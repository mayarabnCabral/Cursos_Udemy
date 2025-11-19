/*
    Operadores Aritméticos
        + -> Soma

        - -> Subtração

        * -> Multiplicação

        / -> Divisão

        % -> Resto da Divisão (Módulo
*/

using System;

namespace CursoCSharp.Fundamentos
{
    class OperadoresAritimeticos
    {
        public static void Executar()
        {
            //Preço desconto
                var preco = 1000.0;
                var imposto = 355;
                var desconto = 0.1;

                double total = preco + imposto;
                var totalComDesconto = total - (total * desconto);
                Console.WriteLine("O preço final é {0}",
                totalComDesconto);

             //Calculo IMC
                double peso = 90.0;
                double altura = 1.82;
                double imc = peso / Math.Pow(altura, 2); //No C# não existe o operador ˆ para potenciação, utiliza-se a função Math.Pow
                Console.WriteLine($"O IMC é {imc}");

                //Número par ou ímpar
                int par = 24;
                int impar = 55;
                Console.WriteLine($"O Numero {par} tem resto {par % 2}, ele é par? {par % 2 == 0}");
                Console.WriteLine($"O Numero {impar} tem resto {impar % 2}, ele é impar? {impar % 2 == 1}");
        }
    }
}