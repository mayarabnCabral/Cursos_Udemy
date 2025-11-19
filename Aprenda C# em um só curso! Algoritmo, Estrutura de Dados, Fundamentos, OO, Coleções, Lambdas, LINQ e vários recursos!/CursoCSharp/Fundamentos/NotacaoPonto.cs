using System;

namespace CursoCSharp.Funddamentos
{
    class NotacaoPonto
    {
        public static void Executar()
        {
            var saudacao = "Olá".ToUpper() // Converte a string para maiúsculas
                                .Insert(3, " World!") // Insere " World!" na posição 3
                                .Replace("World!", "Mundo!");// Substitui "World!" por "Mundo!" 
            Console.WriteLine(saudacao);

            System.Console.WriteLine("Teste".Length); // Retorna o tamanho da string

            string valorImportante = null;
            System.Console.WriteLine(valorImportante?.Length); // O ? evita o erro de referência nula, executando apenas se a variável não for nula

        }
    }
}