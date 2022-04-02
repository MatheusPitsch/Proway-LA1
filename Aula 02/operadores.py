'''
Operadores aritimeticos

Os operadores aritimeticos são utilizados para executar as operações que a sua aplicação utilizar para gerar um resultado

Basicos:
* adição: +
*subtração: -
*divisão: /
*divisão inteira: //
*multiplicação: *
*modulo: %
*exponenciação:**


Atribuição:
    * x += 3 -> x + 3
     * x -= 3 -> x - 3
      * x /= 3 -> x / 3
       * x //= 3 -> x // 3
        * x *= 3 -> x * 3
         * x **= 3 -> x ** 3
          * x %= 3 -> x % 3

Precedencia de Operadores

    1.() -> Agrupamento
    2.** -> Exponenciação
    3.*,/,%,// -> Multiplicação, divisão, resto e divisão inteira
    4. +, - -> soma e subtrção
'''

n1, n2 = 8, 6
media = (n1 +n2)/2
teste = 8*2/3
print(media)
print(f" o valor da variavel teste é: {teste:.3f}")
