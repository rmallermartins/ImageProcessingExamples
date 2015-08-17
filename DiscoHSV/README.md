# DiscoHSV
Primeiro trabalho, gerar um disco cromático utilizando o sistema de cores HSV

## Sistemas de Cores HSV
É um sistema de cores composto por 3 componentes _**H**ue_ (Matiz), _**S**aturation_ (Saturação) e _**V**alue_ (Valor), onde temos que:
* **Hue**: é a tonalidade (tipo) de cor, abrange todas as cores do spectro. Seu valor vai de 0 a 360;
* **Saturation**: é a pureza da cor, quanto menor, mais "cinza" fica a cor, quanto maior, mais pura ela é. Seu valor vai de 0 a 100%;
* **Value**: é o brilho da cor, do escuro para o claro. Seu valor vai de 0 a 100%.

Esse sistema geralmente é representado por um circulo, nesse o valor do _Hue_ é alterado em relação ao angulo e a _Saturation_ em relação a distância do centro. Para representar o _Value_, precisariamos de uma visualização em 3 dimensões, pois seria necessário um Cone para sua representação. Portanto, usamos o _Value_ com o valor máximo (1 - 100%), para nossa representação.

## Gerando o Disco
Para a geração do disco foi utilizada uma função chamada `geraDisco` que recebe como parâmetro o tamanho da imagem a ser exibida e o raio do disco a ser gerado (para visuzalização completa do disco, o tamanho da imagem deve ser maior ou igual o dobro do raio):
```python
def geraDisco(tamImagem, raioDisco) :
```

Começamos então criando um array de 3 dimensões, com todos valores igual a 1,  que será a base para nossa imagem a ser gerada (`DISCO`). As 2 primeiras dimensões representam a altura (X) e a largura (Y) da nossa imagem, já a terceira representa cada um dos valores HSV que temos em um ponto (pixel) da imagem. Depois, a partir dessa imagem, criamos 2 vetores que representam os indices dessa matriz em X (`vetorX`) e Y (`vetorY`) e definimos o centro da imagem (`centroImg`).
```python
DISCO = np.zeros((tamImagem, tamImagem, 3), np.float32)
    
vetorX, vetorY = np.ogrid[:tamImagem, :tamImagem]
    
centroImg = tamImagem/2
```

Se pedirmos para o programa mostrar a imagem nesse ponto, teremos uma imagem toda branca pois `DISCO` foi inicializada com uns:

![disco1](https://github.com/rmallermartins/ProcImagens/blob/master/DiscoHSV/Imagens/disco1.png)

Porém, já temos o suficiente para criar nosso valores para _Hue_. Isso é feito primeiramente utilizando a função `arctang2(x1, x2)` do numpy, ela é uma função que retorna o arc tangente de `x1/x2` escolhendo o quadrante correto, assim sempre retornando um valor positivo do ângulo em radianos. Aplicamos essa função ao `vetorX` e ao `vetorY` ambos com seus valores subtraídos do `centroImg`. E por final, transformamos de radianos para graus com a função `degrees(x)`.

```python
H = np.arctan2(vetorX.astype(np.float32) - centroImg, vetorY.astype(np.float32) - centroImg)
H = np.degrees(H)
```

Com isso temos nosso _Hue_ definido, para podermos mostrar a nossa imagem apenas com o _Hue_, temos que atribuí-lo a sua primeira posição (0) da terceira dimensão e depois converter a imagem de HSV para RGB, pois é esse o sistema de cores que nossos monitores usam, podemos fazer isso através das seguintes linhas de código:

```python
DISCO[:, :, 0] = H

DISCO = cv2.svtColor(DISCO, cv2.COLOR_HSV2BGR)
```

E temos como resultado:

![disco2](https://github.com/rmallermartins/ProcImagens/blob/master/DiscoHSV/Imagens/disco2.png)

Agora vamos criar nossa matriz para a _Saturation_, precisamos que essa matriz faça um degradê do centro da imagem até o raio do nosso disco, de forma que no centro o valor da _Saturation_ seja 0 e vá crescendo conforme se distância do centro. Começamos criando o disco que representará nossos valores em relação ao centro da imagem, para isso fazemos a soma entre os vetores `vetorX` e `vetorY` subtraídos do `centroImg` (coloca 0 no centro) elevando cada um ao quadrado para retirar números negativos. A nossa _Saturation_ recebe esse disco nomalizado em relação ao raio, fazendo os valores irem de 0 até 1, do centro até a borda:

```python
discoSat = ((vetorX - centroImg) ** 2) + ((vetorY - centroImg) ** 2)

S = discoSat.astype(np.float32)/(raioDisco ** 2)
```

A imagem produzida pela _Saturation_ seria:

![disco3](https://github.com/rmallermartins/ProcImagens/blob/master/DiscoHSV/Imagens/disco3.png)

E se aplicarmos ela a nossa imagem de saída antes da conversão para RGB:

```python
DISCO[:, :, 1] = S
```

Temos:

![disco4](https://github.com/rmallermartins/ProcImagens/blob/master/DiscoHSV/Imagens/disco4.png)

Para nosso caso, o _Value_ teria todos valores em 1 (100%) e nossa Imagem já foi toda inicializada com 1, assim não havendo necessidade de cria-lo e coloca-lo em nossa imagem.

Nossa imagem ainda é apresentada em forma de quadrado, temos agora que delimitar nossa imagem para o disco de raio que foi passado como parâmetro. Para isso, usamos o disco que foi criado para a _Saturation_ e comparamos seus valores com o raio de entrada `discoSat > raioDisco ** 2`, todas as posições da nossa imagem de saída que satisfazerem a comparação, recebem o valor 0 (preto) em cada uma das posições da terceira dimensão.

```python
DISCO[discoSat > raioDisco ** 2] = [0, 0, 0]
```

Assim temos nossa imagem final:

![disco5](https://github.com/rmallermartins/ProcImagens/blob/master/DiscoHSV/Imagens/disco5.png)
