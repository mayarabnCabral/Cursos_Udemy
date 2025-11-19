using System;
namespace CursoCSharp.Fundamentos {
    class Interpolacao {
        public static void Executar()
         {
            string nome = "Notebook Gamer";
            string marca = "Dell";
            double preco = 5800.00;

            // Tipos de Interpolação

            System.Console.WriteLine("O " + nome + " da marca " + marca + " custa " + preco); // Une texto e variáveis manualmente

            System.Console.WriteLine("O {0} da marca {1} custa {2}", nome, marca, preco); // Substitui os números pelos valores das variáveis passadas depois da vírgula

            System.Console.WriteLine($"O {nome} da marca {marca} custa {preco}"); // Coloca o valor das variáveis diretamente dentro das chaves {} OBS>: O meu favorito!

            System.Console.WriteLine($"1 + 1 = {1 + 1}"); // Interpolação também permite fazer cálculos dentro das chaves
        }
    }
}