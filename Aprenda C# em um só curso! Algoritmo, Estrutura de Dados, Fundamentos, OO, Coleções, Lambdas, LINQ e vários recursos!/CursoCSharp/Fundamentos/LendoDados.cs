using System;
using System.Globalization;
using System.Runtime.InteropServices;

namespace CursoCSharp.Fundamentos
{
    class LendoDados
    {
       public static void Executar()
        {
            Console.WriteLine("Qual o seu nome? ");
            string nome = Console.ReadLine(); // Lê uma linha de texto do console

            Console.WriteLine("Qual a sua idade? ");
            int idade = int.Parse(Console.ReadLine()); // Lê uma linha do console e converte para inteiro

            Console.WriteLine("Qual a sua altura? ");
            double altura = double.Parse(Console.ReadLine()); // Lê uma linha do console e converte para double

            Console.WriteLine("Qual o seu salário? ");
            float salario = float.Parse(Console.ReadLine(), CultureInfo.InvariantCulture); // Lê uma linha do console e converte para float usando cultura invariante, ou seja, ponto como separador decimal
         
            Console.WriteLine($"Olá {nome}, você tem {idade} anos, {altura} de altura e tem o salário de R${salario}.");  

        }
    }
}