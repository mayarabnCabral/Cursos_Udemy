using System;
using System.Globalization; // Necessário para usar CultureInfo 

namespace CursoCSharp.Fundamentos
{
    class FormatandoNumeros
    {
        public static void Executar()
        {
            double valor = 15.175;

            Console.WriteLine(valor.ToString("F1")); // Deixa o numero com 1 casa decimal
            Console.WriteLine(valor.ToString("C")); // Tranforma em valor monetário
            Console.WriteLine(valor.ToString("P")); // Tranforma em porcentagem
            Console.WriteLine(valor.ToString("#.##")); // Limita o numero de casas decimais

            CultureInfo Cultura = new CultureInfo("en-US"); // Define a cultura como dos EUA
            
            Console.WriteLine(valor.ToString("C3", Cultura)); // Valor monetário com cultura dos EUA

            int inteiro = 256;
            Console.WriteLine(inteiro.ToString("D10")); // Adiciona zeros a esquerda para completar 10 digitos
        }
    }
}