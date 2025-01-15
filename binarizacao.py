import PIL
from PIL import Image
import numpy as np

pth= r"C:\Users\mhmon\Downloads\IMG_20241220_204920719.jpg"

# carregar a imagem como um array com valores rgb
img = Image.open(pth)
img = img.resize((500,500))
# transformar em array numpy para realizar operações
array = np.array(img)

# aplica  fomula de conversão nos canais rgb do array e retorna apenas o valor em cinza
gray = array[:,:,0] * 0.299 + array[:,:,1] * 0.587 + array[:,:,2] * 0.114
gray = gray.astype(np.uint8)
gray_image = Image.fromarray(gray, mode="L")

# retorna um array onde valores maiores que 127 se tornam 255 (branco) e menores se tornam 0 
value = 120
bw = np.asarray([[255 if x > value else 0 for x in linha]for linha in gray]).astype(np.uint8)
bwi = Image.fromarray(bw,mode='L')

# retorna array com canais de cor invertidos
reverse = 255 - array
reverse_image = Image.fromarray(reverse,mode='RGB')


gray_image.show()
bwi.show()
reverse_image.show()



