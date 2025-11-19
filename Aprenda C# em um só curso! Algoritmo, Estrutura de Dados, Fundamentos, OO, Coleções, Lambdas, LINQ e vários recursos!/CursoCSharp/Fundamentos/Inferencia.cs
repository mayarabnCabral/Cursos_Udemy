using System;

namespace CursoCSharp.Fundamentos
{
    class Inferencia
    {
        /*
            * Inferência é a capacidade do compilador de deduzir o tipo de uma variável com base no valor atribuído a ela.
            * Em C#, a inferência de tipos é realizada usando a palavra-chave 'var'.
            * Isso permite que o desenvolvedor escreva código mais conciso, sem a necessidade de declarar explicitamente o tipo da variável.
         */
        public static void Executar()
        {
            var nome = "Mayara"; // O compilador infere que 'nome' é do tipo string
            var idade = 23;     // O compilador infere que 'idade' é do tipo int
            var altura = 1.68;  // O compilador infere que 'altura' é do tipo double
            var ativo = true;   // O compilador infere que 'ativo' é do tipo bool

            Console.WriteLine($"Nome: {nome}, Idade: {idade}, Altura: {altura}, Ativo: {ativo}");
        }
    }
}