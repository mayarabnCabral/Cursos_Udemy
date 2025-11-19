/*
Sempre que existe a possíbilidade de perda de informação ao converter um tipo de dado para outro, é necessário fazer uma conversão explícita (cast).
*/

using System;

namespace CursoCSharp.Fundamentos
{
    class Conversoes
    {
        public static void Executar()
        {
            int inteiro = 10;
            double quebrado = inteiro; // conversão implícita
            Console.WriteLine(quebrado);

            double nota = 9.7;
            //int notaTuncada = nota; // Dará erro de compilação, informando que é necessária uma conversão explícita (cast)
            int notaTuncada = (int)nota; // conversão explícita (cast)
            Console.WriteLine("Nota truncada " + notaTuncada);

            Console.Write("Digite sua idade: ");
            string idadeString = Console.ReadLine(); // lendo e armazenando dado do console
            int idadeInteiro = int.Parse(idadeString); // conversão explícita (cast)
            Console.WriteLine("Idade em inteiro: " + idadeInteiro);

            idadeInteiro = Convert.ToInt32(idadeString); // Outra forma de conversão explícita (cast) onde ToInt32 converte para int, por se tratar de um inteiro de 32 bits
            Console.WriteLine("Idade em inteiro: " + idadeInteiro);

            // Forma mais segura de efetuar uma conversão explícita (cast)
            Console.Write("Digite o primeiro numero: ");
            string palavra = Console.ReadLine();
            int numero;
            int.TryParse(palavra, out numero); // Tenta converter a variável palavra para int, se conseguir armazena em numero, senão armazena 0
            Console.WriteLine("Resultado: " + numero);

            Console.Write("Digite o segundo numero: ");
            int.TryParse(Console.ReadLine(), out int numero2); // Otimizando a declaração da variável numero2 (referente a linha anterior) declarando dentro do próprio método TryParse
            // out é uma palavra chave que indica que o parâmetro é de saída, ou seja, o valor será atribuído dentro do método TryParse
            Console.WriteLine("Resultado 2: " + numero2);

        }
    }
}