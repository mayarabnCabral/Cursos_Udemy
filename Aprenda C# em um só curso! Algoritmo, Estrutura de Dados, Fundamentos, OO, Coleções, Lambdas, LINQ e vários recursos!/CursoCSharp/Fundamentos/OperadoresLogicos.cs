/*  
    && -> AND (E)
        -> Todas as condições precisam ser verdadeiras

    || -> OR (OU)
        -> Apenas uma das condições precisa ser verdadeira
    
    ^  -> XOR (OU Exclusivo)
         -> Apenas uma das condições precisa ser verdadeira, se ambas forem verdadeiras o resultado será falso

    !  -> NOT (NÃO)
         -> Inverte o valor lógico 
        
*/

using System;
using System.Security.Cryptography.X509Certificates;

namespace CursoCSharp.Fundamentos {
    class OperadoresLogicos {
        public static void Executar()
        {
            var executouTrabalho1 = true;
            var executouTrabalho2 = false; 

            var comprouTv50 = executouTrabalho1 && executouTrabalho2;
            System.Console.WriteLine($"Comprou a TV 50? {comprouTv50}"); 

            var comprouSorvete = executouTrabalho1 || executouTrabalho2;
            System.Console.WriteLine($"Comprou Sorvete? {comprouSorvete}");

            var comprouTv32 = executouTrabalho1 ^ executouTrabalho2;
            System.Console.WriteLine($"Comprou a TV 32? {comprouTv32}");

            System.Console.WriteLine("Mais saudável? " + !comprouSorvete);
            
        }
    }
}