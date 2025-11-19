/*
    * O C# é uma linguagem fortemente tipada, ou seja, todas as variáveis devem ser declaradas com um tipo específico.
*/

using System;

namespace CursoCSharp.Fundamentos
{
    class VariaveisEConstantes
    {
        public static void Executar()
        {
            // Área de circunferencia 

            double raio = 4.5; // Variavel do tipo double, identificada como raio
            const double PI = 3.14; // Constante do tipo double, identificada como PI
                                    // uma constante não pode ter seu valor alterado durante a execução do programa
            
            raio = 5.5;
           // PI = 3.1415; Isso gerará um erro de compilação, pois PI é uma constante

           double area = PI * raio * raio; // Cálculo da área da circunferência

            Console.WriteLine("Área da circunferência com raio " + raio + " é: " + area);
            Console.WriteLine("Valor de PI é: " + PI);

            // Tipos internos 

            bool estachovendo = true; // Tipo booleano, pode ser true ou false
            Console.WriteLine("Está chovendo? " + estachovendo);

            byte idade = 45; // Tipo byte, armazena valores inteiros de 0 a 255
            Console.WriteLine("Idade: " + idade);

            sbyte saldoDeGols = sbyte.MinValue; // Tipo sbyte, armazena valores inteiros de -128 a 127
            Console.WriteLine("Saldo de Gols: " + saldoDeGols);

            short salario = short.MaxValue; // Tipo short, armazena valores inteiros de -32.768 a 32.767
            Console.WriteLine("Salário: " + salario);

            int menorValorInt = int.MinValue; // Tipo int, armazena valores inteiros de -2.147.483.648 a 2.147.483.647
            Console.WriteLine("Menor valor int: " + menorValorInt);

            uint populacaoBrasileira = 207_600_000; // Tipo uint, armazena valores inteiros positivos de 0 a 4.294.967.295
            Console.WriteLine("População Brasileira: " + populacaoBrasileira);
            
            long menorValorLong = long.MinValue; // Tipo long, armazena valores inteiros muito grandes
            Console.WriteLine("Menor valor long: " + menorValorLong);

            ulong populacaoMundial = 7_600_000_000; // Tipo ulong, armazena valores inteiros positivos muito grandes
            Console.WriteLine("População Mundial: " + populacaoMundial);    

            float precoComputador = 1299.99f; // Tipo float, armazena números de ponto flutuante (decimais) com precisão simple
            Console.WriteLine("Preço do Computador: " + precoComputador);

            double valorDeMercadoDaApple = 1_000_000_000_000.00; // Tipo double, o dobro de numeros que o float, com precisão dupla
            Console.WriteLine("Valor de Mercado da Apple: " + valorDeMercadoDaApple);

            decimal distanciaEntreEstrelas = decimal.MaxValue; // Tipo decimal, usado para valores financeiros e alta precisão
            Console.WriteLine("Distância entre Estrelas: " + distanciaEntreEstrelas);

            char letra = 'm'; // Tipo char, armazena um único caractere
            Console.WriteLine("Letra: " + letra);   

            string texto = "Seja bem vindo ao Curso de C#"; // Tipo string, armazena uma sequência de caracteres
            Console.WriteLine(texto);

        }


    }
}