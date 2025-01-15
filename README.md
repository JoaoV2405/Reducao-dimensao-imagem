# Reducao-dimensao-imagem

Esta é a resolução do desafio **Redução de Dimensão de Imagens**. O objetivo do desafio é transformar uma imagem RGB em:

1. Uma imagem em escala de cinza
2. Uma imagem em preto e branco

Além disso, realizei uma operação extra de inversão de cores por curiosidade.

Utilizei as bibliotecas **PIL** (para carregamento e exibição de imagens) e **NumPy** (para operações numéricas).

## 📌 Primeiro Passo: Preparação do Ambiente

```python
from PIL import Image
import numpy as np
```

## 📌 Carregar e Processar a Imagem

```python
pth = r"C:\Users\user\Imagens\sua_imagem.jpg"
img = Image.open(pth)
img = img.resize((500, 500))
```
Carregamos a imagem a partir do caminho fornecido em `pth` e a redimensionamos para 500x500 pixels. O redimensionamento serve apenas para padronizar as imagens.

**Imagem utilizada:**

![image](https://github.com/user-attachments/assets/2946eaa9-4782-4ccb-b48c-480a8d9a7ae5)

---

## 📌 Convertendo a Imagem para Tons de Cinza

```python
array = np.array(img)
gray = array[:, :, 0] * 0.299 + array[:, :, 1] * 0.587 + array[:, :, 2] * 0.114
# Transformar o tipo do array de float para inteiro
gray = gray.astype(np.uint8)
gray_image = Image.fromarray(gray, mode="L")
```

A fórmula utilizada considera a percepção humana da luminosidade:
- **0.299** para o canal vermelho (R)
- **0.587** para o canal verde (G)
- **0.114** para o canal azul (B)

O retorno é um array com uma dimensão a menos e com os valores na escala de cinza.

**Resultado:**

![image](https://github.com/user-attachments/assets/947f4fb5-c7dc-4684-9693-5f14506e767c)

---

## 📌 Criando uma Versão Preto e Branco

```python
value = 120
bw = np.asarray([[255 if x > value else 0 for x in linha] for linha in gray]).astype(np.uint8)
bwi = Image.fromarray(bw, mode='L')
```

Aqui transformamos a imagem em preto e branco puro. A lógica é:
- Se um pixel na escala de cinza for maior que o valor de limite (**120**), ele se torna branco (**255**).
- Caso contrário, ele se torna preto (**0**).

Utilizei compreensão de listas, mas seria igualmente efetivo usar uma função lambda.

**Resultado:**

![image](https://github.com/user-attachments/assets/71cda85c-2eda-4e62-82ba-43d8549b3e82)

---

## 📌 Invertendo as Cores da Imagem

```python
reverse = 255 - array
reverse_image = Image.fromarray(reverse, mode='RGB')
```

Nesta etapa, invertemos as cores da imagem original. Para cada pixel:
- Se o valor for preto (**0**), ele se torna branco (**255**), e vice-versa.

**Resultado:**

![image](https://github.com/user-attachments/assets/df6bdc5a-2e06-411a-b8a3-e244bd87fc1f)

---

## 📌 Exibindo as Imagens

```python
gray_image.show()
bwi.show()
reverse_image.show()
```
No final, usamos o método `show()` para exibir as versões processadas diretamente.

---

## 🚀 Ferramentas Utilizadas
- **Python**
- **Pillow (PIL)**
- **NumPy**

