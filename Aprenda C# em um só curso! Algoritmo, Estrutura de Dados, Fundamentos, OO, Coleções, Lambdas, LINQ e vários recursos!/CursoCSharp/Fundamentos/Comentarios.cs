using System;

namespace CursoCSharp.Fundamentos
{
        class Comentarios
    {

        /// <summary>
        /// XML Comments (Como se fosse o Java Doc)
        /// É apenas colocar três barras antes do comentário
        /// </summary>
        public static void Executar()
        {
            System.Console.WriteLine("Código claro é sempre melhor!"); // Comentário de uma linha

            System.Console.WriteLine("O C# tem o XML comments");
            
            /*
             * Esse é um comentário
             * de múltiplas linhas
             */
        }
    }
}

