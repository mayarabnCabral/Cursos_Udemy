/* 
    += -> Atribuição de adição
        -> Seria, num1 = num1 + num2

    -= -> Atribuição de subtração
        -> Seria, num1 = num1 - num2  
*/

using System;

namespace CursoCSharp.Fundamentos
{
    class OperadoresDeAtribuicao
    {
        public static void Executar()
        {
            var num1 = 3;

            num1 += 5; // num1 = num1 + 5 (atribuição aditiva)
            num1 -= 3; // num1 = num1 - 3 (atribuição subtrativa)
            num1 *= 2; // num1 = num1 * 2  (atribuição multiplicativa)
            num1 /= 4; // num1 = num1 / 4 (atribuição divisiva)
            num1 %= 2; // num1 = num1 % 2 (atribuição modular)

            System.Console.WriteLine(num1);


            int a = 1;

            int b = a; // b recebe o valor de a (atribuição simples)

            a++; // a = a + 1 (incremento)
            b--; // b = b - 1 (decremento)
            System.Console.WriteLine($"{a} {b}");
        }
    }
}