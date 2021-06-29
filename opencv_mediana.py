# Processando imagens com o OpenCV

import cv2
import numpy as np

# Abrindo a Imagem ---------------------------------------------

# img = cv2.imread('opencvteste.jpg', cv2.IMREAD_COLOR)

# cv2.namedWindow('Imagem Carregada')
# cv2.imshow('Imagem Carregada', img)
# cv2.waitKey()

# Filtro da Mediana --------------------------------------------    

img = cv2.imread('opencvteste.jpg', 0)
  
# Pegando número de colunas da imagem

m, n = img.shape
   
# Traçar a Imagem em uma Área 3x3
# Para que assim, encontremos a média
# Fazer o cálculo e mudar o valor do centro
img_nova = np.zeros([m, n])
  
for i in range(1, m-1):
    for j in range(1, n-1):
        temp = [img[i-1, j-1],
               img[i-1, j],
               img[i-1, j + 1],
               img[i, j-1],
               img[i, j],
               img[i, j + 1],
               img[i + 1, j-1],
               img[i + 1, j],
               img[i + 1, j + 1]]
          
        temp = sorted(temp)
        img_nova[i, j]= temp[4]
  
img_nova = img_nova.astype(np.uint8)
cv2.imwrite('imagemcomfiltrodamediana.png', img_nova)