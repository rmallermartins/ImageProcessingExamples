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

Começamos então criando um array de 3 dimensões, com todos valores igual a 0,  que será a base para nossa imagem a ser gerada (`DISCO`). As 2 primeiras dimensões representam a altura (X) e a largura (Y) da nossa imagem, já a terceira representa cada um dos valores HSV que temos em um ponto (pixel) da imagem. Depois, a partir dessa imagem, criamos 2 vetores que representam os indices dessa matriz em X (`vetorX`) e Y (`vetorY`) e definimos o centro da imagem (`centroImg`).
```python
    DISCO = np.zeros((tamImagem, tamImagem, 3), np.float32)
    
    vetorX, vetorY = np.ogrid[:tamImagem, :tamImagem]
    
    centroImg = tamImagem/2
```

Se pedirmos para o programa mostrar a imagem nesse ponto, teremos uma imagem toda preta pois `DISCO` foi inicializada com zeros:

![alt tag](https://github.com/rmallermartins/ProcImagens/blob/master/DiscoHSV/Imagens/disco1.png)

Nesse ponto, já temos o suficiente para criar nosso valores para _Hue_.
