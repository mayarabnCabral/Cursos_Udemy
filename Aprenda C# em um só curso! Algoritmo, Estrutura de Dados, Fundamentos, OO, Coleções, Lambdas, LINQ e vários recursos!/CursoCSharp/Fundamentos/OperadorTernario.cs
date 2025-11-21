using System;

namespace CursoCSharpe.Fundamentos
{
    class OperadorTernario
    {
        public static void Executar()
        {
            var nota = 7.0;
            var bomComportamento = true;
            var resultado = nota >= 7.0 && bomComportamento ? "Aprovado" : "Reprovado" ; // Operador Ternário, onde ? significa "se" e : significa "senão", então se a condição for verdadeira retorna o primeiro valor, senão o segundo valor
            // Condição ? valorSeVerdadeiro : valorSeFalso, nesse exemplo significa se a nota for maior ou igual a 7.0 e o bomComportamento for verdadeiro, então retorna "Aprovado", senão retorna "Reprovado"
            Console.WriteLine(resultado);
        }
    }
}