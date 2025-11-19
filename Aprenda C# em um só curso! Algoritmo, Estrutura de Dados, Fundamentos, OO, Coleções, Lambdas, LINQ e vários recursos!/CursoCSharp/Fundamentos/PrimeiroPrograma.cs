// Digitando cw + TAB dentro do Main, o Visual Studio completa com Console.WriteLine();
// Textos em azul são palavras reservadas da linguagem C#
// Texto com a cor "meio apagada" são "partes" que não são obrigatórias ou que não estão sendo utilizadas

using System;


namespace CursoCSharp.Fundamentos // Por padrão, colocamos o nome da pasta/localização como namespace, mas não é algo obrigatório podemos colocar o nome que quisermos 
{
    class PrimeiroPrograma
    {
        public static void Executar()
        {
            Console.Write("Primeiro "); //Write não pula linha
            System.Console.WriteLine("Programa"); //WriteLine pula linha
            Console.WriteLine("Terminou!");
        
        }
    }
};