# AreaObjetos
Segundo trabalho, encontrar, rotular e calcular a área de objetos na imagem de entrada.

## Encontrando e Rotulando Objetos
Primeiramente é necessário binarizar a imagem, para isso aplicamos um Threshold na imagem de entrada, fazemos isso usando uma função do OpenCV, onde **b** é a imagem binarizada, **a** a imagem de entrada e **127** o valor a ser utilizado para fazer o Threshold:
```python
ret, b = cv2.threshold(a, 127, 255, cv2.THRESH_BINARY)
```

Imagem de entrada:

![Entrada](https://github.com/rmallermartins/ProcImagens/blob/master/AreaObjetos/Imagens/Entrada.png)

Imagem binarizada:

![Binarizada](https://github.com/rmallermartins/ProcImagens/blob/master/AreaObjetos/Imagens/Threshold.png)

Após isso, para encontrarmos os objetos na imagem, utilizamos uma Busca em Largura, ou seja, um **BFS**. Na sua chamada passamos a imagem binarizada e um valor que será o intervalo entre os níveis de cinza dos rótulos utilizados nas imagens:
```python
bfs(b, rotuloDif)
```

Após isso, temos a propria imagem **b** agora rotulada:

![Binarizada](https://github.com/rmallermartins/ProcImagens/blob/master/AreaObjetos/Imagens/Rotulada.png)

## Calculando a Área de cada Objeto:

Para calcularmos a área (quantidade de pixels) de cada objeto os rótulos serem sempre diferentes é essêncial, com isso basta encontrarmos o **Histograma** da imagem rotulada, assim teremos a área de cada objeto observando o seu nível de cinza. Isso é feito utilizando da função criada por nós:
```python
mostraHist(b, rotuloDif)
```

E o resultado obtido é o Histograma abaixo, onde para cada rotulo no eixo X temos a quantidade de pixels no eixo Y (rotulo, área):

![Histograma](https://github.com/rmallermartins/ProcImagens/blob/master/AreaObjetos/Imagens/Hist.png)
