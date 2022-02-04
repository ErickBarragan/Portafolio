import matplotlib.pyplot as plt
from PIL import Image
from AImages import *
import time
import sys
import numpy as np


im = Image.open("ImagenOriginal.jpg")
im.show()
final_image = Image.new("L",(im.size[0] ,im.size[1]))

i = 0
j = 0
delta = 1.5
data = []
suma1 = 0 
suma2 = 0

while i < im.size[0]:
	while j < im.size[1] :
		colores = im.getpixel( (i,j) )
		gray = (colores[0] + colores[1] + colores[2]) / 3
		suma1 = suma1 + gray
		Ar =  255/ np.log( (0.5*255) +1)
		Ag =  255/ np.log( (0.5*255) +1)
		Ab =  255/ np.log( (0.5*255) +1)
		new_r = Ar * np.log( (delta * colores[0] ) +1)
		new_g = Ag * np.log( (delta * colores[1] ) +1)
		new_b = Ab * np.log( (delta * colores[2] ) +1)
		new_gray = (new_r + new_g + new_b )/3
		suma2 = suma2 + new_gray
		new_gray = int(new_gray)
		final_image.putpixel( (i,j) ,new_gray)
		j = j+1

	i = i+1
	j = 0

brillo1 = suma1 / (im.size[0] * im.size[1] )
brillo1 = int(brillo1)
print(brillo1 )

brillo2 = suma2 / (im.size[0] * im.size[1] )
brillo2 = int(brillo2)
print(brillo2 )

final_image.show()