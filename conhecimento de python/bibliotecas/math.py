"""Funções teóricas dos números e de representação
math.ceil(x)
Retorna o limite máximo de x, o menor inteiro maior ou igual que x. Se x não é um float, delega para x.__ceil__, cujo qual deve retornar um valor do tipo Integral.

math.comb(n, k)
Retorna o número de maneiras de escolher k itens de n itens sem repetição e sem ordem.

Avalia para n! / (k! * (n - k)!) quando k <= n e avalia para zero quando k > n.

Também conhecido como coeficiente binomial pois é equivalente ao coeficiente do k-ésimo termo na expansão polionomial (1 + x)ⁿ

Levanta TypeError se algum dos argumentos não for inteiro. Levanta ValueError se algum dos argumentos for negativo.

Adicionado na versão 3.8.

math.copysign(x, y)
Retorna um ponto flutuante com a magnitude (valor absoluto) de x, mas o sinal de y. Em plataformas que suportam zeros sem sinal, copysign(1.0, -0.0) retorna -1.0.

math.fabs(x)
Retorna o valor absoluto de x.

math.factorial(n)
Retorna o fatorial de n como um inteiro. Levanta ValueError se n não for um inteiro ou for negativo.

Obsoleto desde a versão 3.9: Aceitar pontos flutuantes com valores integrais (como 5.0) foi descontinuado.

math.floor(x)
Retorna o limite mínimo de x, o maior inteiro menor ou igual a x. Se x não é um ponto flutuante, delega para x.__floor__, cujo qual deve retornar um valor do tipo Integral

math.fmod(x, y)
Retorna fmod(x, y), conforme definido pela biblioteca C da plataforma. Observe que a expressão Python x % y pode não retornar o mesmo resultado. A intenção do padrão C é que fmod(x, y) seja exatamente (matematicamente; com precisão infinita) igual a x - n*y para algum inteiro n de modo que o resultado tenha o mesmo sinal que x e magnitude menor que abs(y). O x % y do Python retorna um resultado com o sinal de y, e pode não ser exatamente computável para argumentos de ponto flutuante. Por exemplo, fmod(-1e-100, 1e100) é -1e-100, mas o resultado de -1e-100 % 1e100 do Python é 1e100-1e-100, que não pode ser representado exatamente como um ponto flutuante, e é arredondado para o surpreendente 1e100. Por esta razão, a função fmod() é geralmente preferida ao trabalhar com pontos flutuantes, enquanto o x % y do Python é preferido ao trabalhar com inteiros.

math.frexp(x)
Retorna a mantissa e o expoente de x como o par (m, e). m é um ponto flutuante e e é um inteiro tal que x == m * 2**e exatamente. Se x for zero, retorna (0.0, 0), caso contrário, 0.5 <= abs(m) < 1. Isso é usado para “separar” a representação interna de um ponto flutuante de forma portátil.

math.fsum(iterable)
Retorna uma soma de valores de ponto flutuante precisa no iterável. Evita perda de precisão rastreando várias somas parciais intermediárias.

A precisão do algoritmo depende das garantias aritméticas IEEE-754 e do caso típico em que o modo de arredondamento é meio par. Em algumas compilações que não são do Windows, a biblioteca C subjacente usa adição de precisão estendida e pode ocasionalmente arredondar uma soma intermediária fazendo com que ela fique fora do bit menos significativo.

For further discussion and two alternative approaches, see the ASPN cookbook recipes for accurate floating point summation.

math.gcd(*integers)
Retorna o maior divisor comum dos argumentos inteiros especificados. Se algum dos argumentos for diferente de zero, o valor retornado será o maior inteiro positivo que é um divisor de todos os argumentos. Se todos os argumentos forem zero, o valor retornado será 0. gcd() sem argumentos retorna 0.

Adicionado na versão 3.5.

Alterado na versão 3.9: Adicionado suporte para um número arbitrário de argumentos. Anteriormente, apenas dois argumentos eram suportados.

math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
Retorna True se os valores a e b estiverem próximos e False caso contrário.

Se dois valores são ou não considerados próximos, é determinado de acordo com as tolerâncias absolutas e relativas fornecidas.

rel_tol é a tolerância relativa – é a diferença máxima permitida entre a e b, em relação ao maior valor absoluto de a e b. Por exemplo, para definir uma tolerância de 5%, passe rel_tol=0.05. A tolerância padrão é 1e-09, o que garante que os dois valores sejam iguais em cerca de 9 dígitos decimais. rel_tol deve ser maior que zero.

abs_tol é a tolerância absoluta mínima – útil para comparações próximas a zero. abs_tol deve ser pelo menos zero.

Se nenhum erro ocorrer, o resultado será: abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol).

Os valores especiais do IEEE 754 de NaN, inf e -inf serão tratados de acordo com as regras do IEEE. Especificamente, NaN não é considerado próximo a qualquer outro valor, incluindo NaN. inf e -inf são considerados apenas próximos a si mesmos.

Adicionado na versão 3.5.

Ver também PEP 485 – Uma função para testar igualdade aproximada
math.isfinite(x)
Retorna True se x não for um infinito nem um NaN, e False caso contrário. (Observe que 0.0 é considerado finito.)

Adicionado na versão 3.2.

math.isinf(x)
Retorna True se x for um infinito positivo ou negativo, e False caso contrário.

math.isnan(x)
Retorna True se x for um NaN (não um número), e False caso contrário.

math.isqrt(n)
Retorna a raiz quadrada inteira do inteiro não negativo n. Este é o piso da raiz quadrada exata de n, ou equivalentemente o maior inteiro a tal que a² ≤ n.

Para algumas aplicações, pode ser mais conveniente ter o menor número inteiro a tal que n ≤ a² ou, em outras palavras, o teto da raiz quadrada exata de n. Para n positivo, isso pode ser calculado usando a = 1 + isqrt(n - 1).

Adicionado na versão 3.8.

math.lcm(*integers)
Retorna o mínimo múltiplo comum dos argumentos inteiros especificados. Se todos os argumentos forem diferentes de zero, o valor retornado será o menor inteiro positivo que é um múltiplo de todos os argumentos. Se algum dos argumentos for zero, o valor retornado será 0. lcm() sem argumentos retorna 1.

Adicionado na versão 3.9.

math.ldexp(x, i)
Retorna x * (2**i). Este é essencialmente o inverso da função frexp().

math.modf(x)
Retorna as partes fracionárias e inteiras de x. Ambos os resultados carregam o sinal de x e são pontos flutuantes.

math.nextafter(x, y, steps=1)
Retorna o valor de ponto flutuante com steps passos após x em direção a y.

Se x for igual a y, retorna y, a menos que steps seja zero.

Exemplos:

math.nextafter(x, math.inf) sobe: em direção ao infinito positivo.

math.nextafter(x, -math.inf) desce: em direção ao menos infinito.

math.nextafter(x, 0.0) vai em direção a zero.

math.nextafter(x, math.copysign(math.inf, x)) se afasta do zero.

Veja também math.ulp.()

Adicionado na versão 3.9.

Alterado na versão 3.12: Adicionado o argumento steps.

math.perm(n, k=None)
Retorna o número de maneiras de escolher k itens de n itens sem repetição e com ordem.

Avalia para n! / (n - k)! quando k <= n e avalia para zero quando k > n.

If k is not specified or is None, then k defaults to n and the function returns n!.

Levanta TypeError se algum dos argumentos não for inteiro. Levanta ValueError se algum dos argumentos for negativo.

Adicionado na versão 3.8.

math.prod(iterable, *, start=1)
Calcula o produto de todos os elementos na entrada iterable. O valor start padrão para o produto é 1.

Quando o iterável estiver vazio, retorna o valor de start. Esta função deve ser usada especificamente com valores numéricos e pode rejeitar tipos não numéricos.

Adicionado na versão 3.8.

math.remainder(x, y)
Retorna o resto no estilo IEEE 754 de x em relação a y. Para o finito x e o finito diferente de zero y, esta é a diferença x - n*y, onde n é o número inteiro mais próximo do valor exato do quociente x / y . Se x / y está exatamente no meio do caminho entre dois inteiros consecutivos, o inteiro par mais próximo é usado para n. O resto r = remainder(x, y) assim sempre satisfaz abs(r) <= 0.5 * abs(y).

Casos especiais seguem IEEE 754: em particular, remainder(x, math.inf) é x para qualquer x finito, e remainder(x, 0) e remainder(math.inf, x) levantam ValueError para qualquer x não NaN. Se o resultado da operação remainder for zero, esse zero terá o mesmo sinal de x.

Em plataformas que usam ponto flutuante binário do IEEE 754, o resultado dessa operação é sempre exatamente representável: nenhum erro de arredondamento é introduzido.

Adicionado na versão 3.7.

math.sumprod(p, q)
Retorna a soma dos produtos dos valores de dois iteráveis p e q.

Levanta ValueError se as entradas não tiverem o mesmo comprimento.

Aproximadamente equivalente a:

sum(itertools.starmap(operator.mul, zip(p, q, strict=True)))
Para entradas float e mistas int/float, os produtos intermediários e as somas são calculados com precisão estendida.

Adicionado na versão 3.12.

math.trunc(x)
Retorna x com a parte fracionária removida, deixando a parte inteira. Isso arredonda para 0: trunc() é equivalente a floor() para x positivos, e equivalentes a ceil() para x negativos. Se x não é um ponto flutuante, então delega para x.__trunc__, cujo qual deve retornar um valor do tipo Integral.

math.ulp(x)
Retorna o valor do bit menos significativo do ponto flutuante x:

Se x for um NaN (não um número), retorna x.

Se x for negativo, retorna ulp(-x).

Se x for um infinito positivo, retorna x.

Se x for igual a zero, retorna o menor valor flutuante positivo desnormalizado representável (menor que o ponto flutuante de valor mínimo positivo normalizado, sys.float_info.min).

Se x for igual ao maior ponto flutuante positivo representável, retorna o valor do bit menos significativo de x, tal que o primeiro ponto flutuante menor que x seja x - ulp(x).

Caso contrário (x é um número finito positivo), retorna o valor do bit menos significativo de x, de modo que o primeiro ponto flutuante maior que x seja x + ulp(x).

ULP significa “Unit in the Last Place” ou, em português, unidade na última posição.

Veja também math.nextafter() e sys.float_info.epsilon.

Adicionado na versão 3.9.

Observe que frexp() e modf() têm um padrão de chamada/retorno diferente de seus equivalentes C: elas pegam um único argumento e retornam um par de valores, ao invés de retornar seu segundo valor de retorno por meio de um “parâmetro de saída” (não existe tal coisa em Python).

Para as funções ceil(), floor() e modf(), observe que todos os números de ponto flutuante de magnitude suficientemente grande são inteiros exatos. Os pontos flutuantes do Python normalmente não carregam mais do que 53 bits de precisão (o mesmo que o tipo duplo da plataforma C), caso em que qualquer ponto flutuante x com abs(x) >= 2**52 necessariamente não tem bits fracionários.

Funções de potência e logarítmicas
math.cbrt(x)
Retorna a raiz cúbica de x.

Adicionado na versão 3.11.

math.exp(x)
Retorna e elevado à potência x, onde e = 2.718281… é a base dos logaritmos naturais. Isso geralmente é mais preciso do que math.e ** x ou pow(math.e, x).

math.exp2(x)
Retorna 2 elevado a x

Adicionado na versão 3.11.

math.expm1(x)
Retorna e elevado à potência x, menos 1. Aqui e é a base dos logaritmos naturais. Para pequenos pontos flutuantes x, a subtração em exp(x) - 1 pode resultar em uma perda significativa de precisão; a função expm1() fornece uma maneira de calcular essa quantidade com precisão total:

>>>
from math import exp, expm1
exp(1e-5) - 1  # gives result accurate to 11 places
1.0000050000069649e-05
expm1(1e-5)    # result accurate to full precision
1.0000050000166668e-05
Adicionado na versão 3.2.

math.log(x[, base])
Com um argumento, retorna o logaritmo natural de x (para base e).

Com dois argumentos, retorna o logaritmo de x para a base fornecida, calculada como log(x)/log(base).

math.log1p(x)
Retorna o logaritmo natural de 1+x (base e). O resultado é calculado de forma precisa para x próximo a zero.

math.log2(x)
Retorna o logaritmo de base 2 de x. Isso geralmente é mais preciso do que log(x, 2).

Adicionado na versão 3.3.

Ver também int.bit_length() retorna o número de bits necessários para representar um inteiro em binário, excluindo o sinal e os zeros à esquerda.
math.log10(x)
Retorna o logaritmo de base 10 de x. Isso geralmente é mais preciso do que log(x, 10).

math.pow(x, y)
Retorna x elevado a potência de y. Exceções seguem o padrão IEEE 754 o máximo possível. pow(1.0, x) e pow(x, 0.0) em particular sempre retornam 1.0, mesmo quando x é ZERO ou NaN. Se ambos x e y são números finitos, x é negativo, e y não é um inteiro então pow(x, y) é indefinido e levanta ValueError.

Ao contrário do operador embutido **, math.pow() converte ambos os seus argumentos para o tipo float. Use ** ou a função embutida pow() para calcular potências inteiras exatas.

Alterado na versão 3.11: Os casos especiais pow(0.0, -inf) e pow(-0.0, -inf) foram alterados para retornar inf ao invés de retornarem ValueError, para ter consistencia com a IEEE 754.

math.sqrt(x)
Retorna a raiz quadrada de x.

Funções trigonométricas
math.acos(x)
Retorna o arco cosseno de x, em radianos. O resultado está entre 0 e pi.

math.asin(x)
Retorna o arco seno de x, em radianos. O resultado está entre -pi/2 e pi/2.

math.atan(x)
Retorna o arco tangente de x, em radianos. O resultado está entre -pi/2 e pi/2.

math.atan2(y, x)
Retorna atan(y / x), em radianos. O resultado está entre -pi e pi. O vetor no plano da origem ao ponto (x, y) faz este ângulo com o eixo X positivo. O ponto de atan2() é que os sinais de ambas as entradas são conhecidos por ele, então ele pode calcular o quadrante correto para o ângulo. Por exemplo, atan(1) e atan2(1, 1) são ambos pi/4, mas atan2(-1, -1) é -3*pi/4.

math.cos(x)
Retorna o cosseno de x radianos.

math.dist(p, q)
Retorna a distância euclidiana entre dois pontos p e q, cada um dado como uma sequência (ou iterável) de coordenadas. Os dois pontos devem ter a mesma dimensão.

Aproximadamente equivalente a:

sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))
Adicionado na versão 3.8.

math.hypot(*coordinates)
Retorna a norma euclidiana, sqrt(sum(x**2 for x in coordinates)). Este é o comprimento do vetor da origem até o ponto dado pelas coordenadas.

Para um ponto bidimensional (x, y), isso é equivalente a calcular a hipotenusa de um triângulo retângulo usando o teorema de Pitágoras, sqrt(x*x + y*y).

Alterado na versão 3.8: Adicionado suporte para pontos n-dimensionais. Anteriormente, apenas o caso bidimensional era suportado.

Alterado na versão 3.10: Melhorou a precisão do algoritmo para que o erro máximo seja inferior a 1 ulp (unidade no último lugar). Mais tipicamente, o resultado é quase sempre arredondado corretamente para 1/2 ulp.

math.sin(x)
Retorna o seno de x radianos.

math.tan(x)
Retorna o tangente de x radianos.

Conversão angular
math.degrees(x)
Converte o ângulo x de radianos para graus.

math.radians(x)
Converte o ângulo x de graus para radianos.

Funções hiperbólicas
Funções hiperbólicas são análogas às funções trigonométricas baseadas em hipérboles em vez de círculos.

math.acosh(x)
Retorna o cosseno hiperbólico inverso de x.

math.asinh(x)
Retorna o seno hiperbólico inverso de x.

math.atanh(x)
Retorna a tangente hiperbólica inversa de x.

math.cosh(x)
Retorna o cosseno hiperbólico de x.

math.sinh(x)
Retorna o seno hiperbólico de x.

math.tanh(x)
Retorna a tangente hiperbólica de x.

Funções especiais
math.erf(x)
Retorna a função erro em x.

A função erf() pode ser usada para calcular funções estatísticas tradicionais, como a distribuição normal padrão cumulativa:

def phi(x):
    'Cumulative distribution function for the standard normal distribution'
    return (1.0 + erf(x / sqrt(2.0))) / 2.0
Adicionado na versão 3.2.

math.erfc(x)
Retorna a função erro complementar em x. A função erro complementar é definida como 1.0 - erf(x). É usado para grandes valores de x onde uma subtração de um causaria uma perda de significância.

Adicionado na versão 3.2.

math.gamma(x)
Retorna a função gama em x.

Adicionado na versão 3.2.

math.lgamma(x)
Retorna o logaritmo natural do valor absoluto da função gama em x.

Adicionado na versão 3.2.

Constantes
math.pi
A constante matemática π = 3.141592…, para a precisão disponível.

math.e
A constante matemática e = 2.718281…, para a precisão disponível.

math.tau
A constante matemática τ = 6.283185…, para a precisão disponível. Tau é uma constante de círculo igual a 2π, a razão entre a circunferência de um círculo e seu raio. Para saber mais sobre Tau, confira o vídeo Pi is (still) Wrong de Vi Hart, e comece a comemorar o dia do Tau comendo duas vezes mais torta!

Adicionado na versão 3.6.

math.inf
Um infinito positivo de ponto flutuante. (Para infinito negativo, use -math.inf.) Equivalente à saída de float('inf').

Adicionado na versão 3.5.

math.nan
Um valor de ponto flutuante “não é um número” (NaN). Equivalente à saída de float('nan'). Devido aos requisitos do padrão IEEE-754, math.nan e float('nan') não são considerados para ser igual a qualquer outro valor numérico, incluindo eles próprios. Para verificar se um número é NaN, use a função isnan() para testar NaNs em vez de is ou ==. Exemplo:

>>>
import math
math.nan == math.nan
False
float('nan') == float('nan')
False
math.isnan(math.nan)
True
math.isnan(float('nan'))
True


"""

print("BY LABAXURIAS")

