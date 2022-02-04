import matplotlib.pyplot as plt
from PIL import Image
from AImages import *
from Ordenamiento import * 
import time
import sys
import numpy as np



def open_image(im):

        tiempoIni = time.time()

        route = (im)
        im = Image.open(route)
        im.show()
        
        tiempoFin= time.time()
        print("Pocessed in ", tiempoFin - tiempoIni, "seconds")

#----------------------------------------------------------------------------------------------------------------------------

def binarization(im):
      tiempoIni = time.time()

      route = (im)

      im = Image.open(route)
      im.show()


      im_weidth = im.size[0]
      im_heigth = im.size[1]
      final_image = Image.new("L",(im_weidth,im_heigth))

      umbral = 50
      i = 0
      j = 0

      while i < im_weidth:
         while j < im_heigth:

            colors = im.getpixel( (i,j) )  
            #gray = (colors[0] + colors[1] + colors[2])/3
            gray = colors[0] * 299/1000 + colors[1] * 587/1000 + colors[2] * 114/1000
            gray= int(gray)
            if gray <= umbral:
              final_image.putpixel( (i,j),0 )
            else:
              final_image.putpixel( (i,j),255 )
            j=j+1
         i=i+1
         j=0

      #final_image.show()
      final_image.save("Nueva.png")

      tiempoFin= time.time()
      print("Processed in ", tiempoFin - tiempoIni, "seconds")
      return"Nueva.png"

#----------------------------------------------------------------------------------------------------------------------------

def gray_scale(im):

      tiempoIni = time.time()
      route = (im)
      im = Image.open(route)
      im.show()

      im_weidth = im.size[0]
      im_heigth = im.size[1]
      final_image = Image.new("L",(im_weidth,im_heigth))

      i=0
      j=0

      while i < im_weidth:
         while j < im_heigth:
            colors = im.getpixel( (i,j) )
            gray = colors[0] * 299/1000 + colors[1] * 587/1000 + colors[2] * 114/1000
            gray = int(gray)
            final_image.putpixel((i,j), gray)
            j = j+1
         i = i+1
         j = 0


      final_image.show()

      tiempoFin = time.time()
      print("Processed in: ", tiempoFin + tiempoIni, " seconds")

#----------------------------------------------------------------------------------------------------------------------------

def histogram(im):

      tiempoIni = time.time()
      route = (im)
      im = Image.open(route)
      #im.show()
      mapping_list = []
      i = 0

      while i <=255:
         mapping_list.append(i)     #Create the list to create a diccionary for mapping the values
         i = i+1 

      mapping_dic = dict.fromkeys(mapping_list ,0) #dicctionary to graphic the histogram

      im_weidth = im.size[0]
      im_heigth = im.size[1]

      i = 0
      j = 0

      while i < im_weidth:
         while j < im_heigth:
            colors = im.getpixel( (i,j) )
            if type(colors) == int:
               gray = int(colors)
            else:
               gray = ((colors[0] * 299)/1000) + ((colors[1] * 587)/1000) + ((colors[2] * 114)/1000)
               gray = int(gray)
            mapping_dic[gray] = mapping_dic.get(gray)  + 1
            j = j+1
         i = i+1
         j=0

      tiempoFin = time.time()
      print("Processed in: ",tiempoFin - tiempoIni, " seconds")

      return mapping_dic

#----------------------------------------------------------------------------------------------------------------------------

def graph_histogram(my_dic):

      #y_values = my_dic.values()
      y_values = list(my_dic.values())
      #x_values = my_dic.keys()

      #plt.stem(x_values,y_values,use_line_collection=True)    //lo comentado es la forma que tabien funciona pero son rayitas
      #plt.show()
      plt.plot(y_values)
      plt.show()


#----------------------------------------------------------------------------------------------------------------------------

def brighter_log(im):
      
      tiempoIni = time.time()
      route = (im)
      im = Image.open(route)  #Open the image to work with
      im.show()   #showing the original image
      final_image = Image.new("L",(im.size[0] ,im.size[1])) #Create the final image wihtout values
      sum_im = 0       #sum of gray scale values to know the brightness level for the entire original image
      sum_final_image = 0 #sum of gray sacale values to kow the brightness level for the entira final image
      im_weidth = im.size[0]  #
      im_heigth = im.size[1]  #
      i=0
      j=0
      delta = 0.5    #value to change the brightness of the image

      while i < im_weidth:
         while j < im_heigth:
            colors = im.getpixel( (i,j) )   #getting the RGB value of the pixel (i,j)
            gray = (colors[0] + colors[1] + colors[2]) / 3  #calculating the brightness level fo the pixel (i,j)
            sum_im = sum_im + gray           #adding up all the gray values for the original images
            A =  255/ np.log( (0.5*255)+1)     #calculating A with a logarithmic function
            new_r = A * np.log((delta*colors[0])+1) #calculating the new red values for the new image using a logarithmic function 
            new_g = A * np.log((delta*colors[1])+1) #calculating the new green values for the new image using a logarithmic function
            new_b = A * np.log((delta*colors[2])+1) #calculating the new blue values for the new image using a logarithmic function
            new_gray = (new_r + new_g + new_b )/3  #calculating the new gray values
            sum_final_image = sum_final_image + new_gray #adding up all the gray values with brightness level increased
            new_gray = int(new_gray)  #transform the float new values into int 
            final_image.putpixel((i,j), new_gray) #set the new values to the final image
            j = j+1
         i = i+1
         j = 0

      brighness_im = sum_im/(im_weidth * im_heigth) #Calculating the brightness level for the entire original image
      brighness_final_image = sum_final_image / (im_weidth * im_heigth) #Calculating the brightness levelfor the entire new image
      print(brighness_im)        #showing the brightness level of the original image
      print(brighness_final_image) #showing brightness level of the original image

      final_image.show()      #showing the new imagen with brightness level increased

      tiempoFin = time.time()
      print("Processed in ", tiempoFin - tiempoIni, " seconds") #estimating time process 
      return "Nueva.png"

#----------------------------------------------------------------------------------------------------------------------------

def brighter_exp(im):
      
      tiempoIni = time.time()
      route = (im)
      im = Image.open(route)
      im.show()
      im_weidth = im.size[0]
      im_heigth = im.size[1]
      final_image = Image.new("L", (im_weidth, im_heigth) )
      sum_im = 0
      sum_final_image = 0
      delta1 = 10 # greather than zero
      i = 0
      j = 0
      delta = -delta1

      while i < im_weidth:
         while j < im_heigth:
            colors = im.getpixel((i,j))
            gray = (colors[0] + colors[1] + colors[2]) / 3
            sum_im = sum_im + gray
            A = 255/(1 - np.exp(delta))
            new_r =  A * (1 - np.exp(  (colors[0] * delta) /255  ) )
            new_g =  A * (1 - np.exp(  (colors[1] * delta) /255  ) )
            new_b =  A * (1 - np.exp(  (colors[2] * delta) /255  ) )
            new_gray = (new_r + new_g + new_b)/3
            sum_final_image = sum_final_image + new_gray
            new_gray = int(new_gray)
            final_image.putpixel((i,j), new_gray)
            j = j+1
         i = i+1
         j = 0

      brighness_im = sum_im/(im_weidth * im_heigth)
      brighness_final_image = sum_final_image / (im_weidth * im_heigth)
      print(brighness_im)
      print(brighness_final_image)

      final_image.show()

      tiempoFin = time.time()
      print("Processed in ", tiempoFin - tiempoIni, " seconds")

#----------------------------------------------------------------------------------------------------------------------------

def darkest_exp(im):
      
      tiempoIni = time.time()
      route = (im)
      im = Image.open(route)
      im.show()
      im_weidth = im.size[0]
      im_heigth = im.size[1]
      final_image = Image.new("L", (im_weidth, im_heigth))
      sum_im = 0
      sum_final_image = 0
      delta = 10
      i = 0
      j = 0

      while i < im_weidth:
         while j < im_heigth:
            colors = im.getpixel((i,j))
            gray = (colors[0] + colors[1] + colors[2])/3
            sum_im = sum_im + gray
            A = 255 / ( np.exp(delta) - 1)
            new_r = A * ( np.exp((delta * colors[0])/255) - 1)
            new_g = A * ( np.exp((delta * colors[1])/255) - 1)
            new_b = A * ( np.exp((delta * colors[2])/255) - 1)
            new_gray = (new_r + new_g + new_b) / 3
            sum_final_image = sum_final_image + new_gray
            new_gray = int(new_gray)
            final_image.putpixel((i,j), new_gray)
            j = j+1
         i = i+1
         j=0

      darkness_im = sum_im / (im_weidth* im_heigth)
      darkness_final_image = sum_final_image / (im_heigth*im_weidth)
      print(darkness_im)
      print(darkness_final_image)

      final_image.show()

      tiempoFin = time.time()
      print("Processed in ", tiempoFin - tiempoIni, " seconds")

#----------------------------------------------------------------------------------------------------------------------------

def darkest_cos(im):
      
      tiempoIni = time.time()
      route = (im)
      im = Image.open(route)
      im.show()
      im_weidth = im.size[0]
      im_heigth = im.size[1]
      final_image = Image.new("L", (im_weidth,im_heigth))
      sum_im = 0
      sum_final_image = 0
      i=0
      j=0
      while i < im_weidth:
         while j < im_heigth:
            colors = im.getpixel((i,j))
            gray = (colors[0] + colors[1] + colors[2]) / 3
            sum_im = sum_im + gray
            new_r = 255 * (1 - np.cos((np.pi * colors[0]) / (2*255)))
            new_g = 255 * (1 - np.cos((np.pi * colors[1]) / (2*255)))
            new_b = 255 * (1 - np.cos((np.pi * colors[2]) / (2*255)))
            new_gray = (new_r + new_g + new_b) / 3
            sum_final_image = sum_final_image + new_gray
            new_gray = int(new_gray)
            final_image.putpixel((i,j), new_gray)
            j = j+1
         i = i+1
         j = 0

      darkness_im = sum_im / (im_weidth * im_heigth)
      darkness_final_image = sum_final_image / (im_weidth * im_heigth)
      print(darkness_im)
      print(darkness_final_image)

      final_image.show()

      tiempoFin = time.time()
      print("Processed in ", tiempoFin - tiempoIni, " seconds")

#----------------------------------------------------------------------------------------------------------------------------

def negative(im):
      tiempoIni = time.time()
      route =  (im)
      im = Image.open(route)
      im.show()
      im_weidth = im.size[0]
      im_heigth = im.size[1]
      final_image = Image.new("L",(im_weidth,im_heigth))
      i = 0
      j = 0

      while i < im_weidth:
         while j < im_heigth:
            colors = im.getpixel((i,j))
            gray = (colors[0] + colors[1] + colors[2]) / 3
            gray = int(gray)
            new_value = 255 - gray
            final_image.putpixel((i,j), new_value )
            j = j+1
         i = i+1
         j = 0

      final_image.show()

      tiempoFin = time.time()
      print("Processed in ",tiempoFin - tiempoIni, " seconds")

#----------------------------------------------------------------------------------------------------------------------------

def histogram_expansion(im):

      tiempoIni = time.time()
      route = (im)
      im = Image.open(route)
      in_histogram = histogram(route)
      values = in_histogram.values()
      keys = in_histogram.keys()
      final_image = Image.new("P", (im.size[0],im.size[1]))
      mapping_list = []
      min_value = 255
      max_value = 0
      i = 0

      while i <=255:
         mapping_list.append(i)     #Create the list to create a diccionary for mapping the values
         i = i+1 

      mapping_dic = dict.fromkeys(mapping_list ,0) #dicctionary to graphic the histogram

      i = 0

      while i <= len(in_histogram):
         if in_histogram[i] > 0: #encontramos el menor nivel de intensidad en la imagen
            min_value_image = i
            break
         i = i+1

      i = len(in_histogram) - 1

      while i > 0:
         if in_histogram[i] > 0: #encontramos el mayor nivel de intensidad en la imagen
            max_value_image = i
            break
         i = i-1

      i = 0
      j = 0

      while i < im.size[0]:
         while j < im.size[1]:
            colors = im.getpixel((i,j))
            gray = (colors[0] + colors[1] + colors[2]) / 3
            gray = int(gray)
            new_value = (((gray-min_value_image)/(max_value_image-min_value_image))*(max_value-min_value))+min_value
            new_value = round(new_value)
            mapping_dic[new_value] = mapping_dic.get(new_value) + 1
            final_image.putpixel((i,j), new_value)
            j = j+1
         i = i+1
         j = 0

      final_image.show()

      tiempoFin = time.time()
      print("Expansion processed in ", tiempoFin - tiempoIni, " seconds")
      return mapping_dic

#----------------------------------------------------------------------------------------------------------------------------

def histogram_contraction(im):

      tiempoIni = time.time()
      route = (im)
      im = Image.open(route)
      in_histogram = histogram(route)
      values = in_histogram.values()
      keys = in_histogram.keys()
      final_image = Image.new("P", (im.size[0],im.size[1]))
      mapping_list = []
      Cmin = 255
      Cmax = 0
      i = 0

      while i <=255:
         mapping_list.append(i)     #Create the list to create a diccionary for mapping the values
         i = i+1 

      mapping_dic = dict.fromkeys(mapping_list ,0) #dicctionary to graphic the histogram

      i = 0

      while i <= len(in_histogram):
         if in_histogram[i] > 0: #encontramos el menor nivel de intensidad en la imagen
            min_value_image = i
            break
         i = i+1

      i = len(in_histogram) - 1
      while i > 0:
         if in_histogram[i] > 0: #encontramos el mayor nivel de intensidad en la imagen
            max_value_image = i
            break
         i = i-1

      i = 0
      j = 0

      while i < im.size[0]:
         while j < im.size[1]:
            colors = im.getpixel((i,j))
            gray = (colors[0] + colors[1] + colors[2]) / 3
            gray = int(gray)
            new_value = (((Cmax-Cmin)/(max_value_image-min_value_image))*(gray - min_value_image)) + Cmin
            new_value = round(new_value)
            mapping_dic[new_value] = mapping_dic.get(new_value) + 1
            final_image.putpixel((i,j), new_value)
            j = j+1
         i = i+1
         j = 0

      final_image.show()

      tiempoFin = time.time()
      print("Contraction processed in ", tiempoFin - tiempoIni, " seconds")
      return mapping_dic

#----------------------------------------------------------------------------------------------------------------------------

def histogram_equalization_uniform(im):

      tiempoIni = time.time()
      route = (im)
      im = Image.open(route)
      in_histogram = histogram(route)
      values = in_histogram.values()
      keys = in_histogram.keys()
      final_image = Image.new("P", (im.size[0],im.size[1]))
      mapping_list = []
      Gmin = 255
      Gmax = 0
      prob = []
      acumulated = []
      i = 0

      while i <=255:
         mapping_list.append(i)     #Create the list to create a diccionary for mapping the values
         i = i+1 
      mapping_dic = dict.fromkeys(mapping_list ,0) #dicctionary to graphic the histogram

      i = 0
      while i < len(in_histogram):
         aux = in_histogram.get(i)/(im.size[0]*im.size[1])     #calculando todas las probabilidadaes
         prob.append(aux)
         i = i+1 
      
      acumulated.append(prob[0])
      i = 1
      while i < len(prob):
         aux = prob[i-1] + prob[i]
         acumulated.append(aux)
         i = i+1
         

      i = 0
      j = 0
      while i < im.size[0]:
         while j < im.size[1]:
            colors = im.getpixel((i,j))
            gray = (colors[0] + colors[1] + colors[2]) / 3
            gray = int(gray)
            new_value = ((Gmax-Gmin) * acumulated[gray]) + Gmin
            new_value = round(new_value)
            mapping_dic[new_value] = mapping_dic.get(new_value) + 1
            final_image.putpixel((i,j), new_value)
            j = j+1
         i = i+1
         j = 0

      final_image.show()

      tiempoFin = time.time()
      print("Contraction processed in ", tiempoFin - tiempoIni, " seconds")
      return mapping_dic

#----------------------------------------------------------------------------------------------------------------------------

def box_filtering(im): 

      tiempoIni = time.time()
      route = (im) 
      im = Image.open(route)
      im_weidth = im.size[0]
      im_heigth = im.size[1]
      im.show()
      final_image = Image.new("P",(im_weidth,im_heigth))

      i = 1
      j = 1

      while i < im_weidth-1:
         while j < im_heigth-1:
            colors1 = im.getpixel((i-1,j-1))
            colors2 = im.getpixel((i-1,j))
            colors3 = im.getpixel((i-1,j+1))
            colors4 = im.getpixel((i,j-1))
            colors = im.getpixel((i,j))
            colors5 = im.getpixel((i,j+1))
            colors6 = im.getpixel((i+1,j-1))
            colors7 = im.getpixel((i+1,j))
            colors8 = im.getpixel((i+1,j+1))
            if type(colors)==int:
               new_value = (colors+colors1+colors2+colors3+colors4+colors5+colors6+colors7+colors8)/9
            else:
               gray =  int((colors[0] + colors[1]+ colors[2]) / 3)
               gray1 = int((colors1[0] + colors1[1]+ colors1[2]) / 3)
               gray2 = int((colors2[0] + colors2[1]+ colors2[2]) / 3)
               gray3 = int((colors3[0] + colors3[1]+ colors3[2]) / 3)
               gray4 = int((colors4[0] + colors4[1]+ colors4[2]) / 3)
               gray5 = int((colors5[0] + colors5[1]+ colors5[2]) / 3)
               gray6 = int((colors6[0] + colors6[1]+ colors6[2]) / 3)
               gray7 = int((colors7[0] + colors7[1]+ colors7[2]) / 3)
               gray8 = int((colors8[0] + colors8[1]+ colors8[2]) / 3)
               new_value = (gray+gray1+gray2+gray3+gray4+gray5+gray6+gray7+gray8)/9
            new_value = int(new_value)
            final_image.putpixel((i,j), new_value)
            j = j+1
         i = i+1
         j = 0

      final_image.show()
      final_image.save("Nueva.png")

      tiempoFin = time.time()
      print("Processed in ", tiempoFin - tiempoIni, " seconds")
      return "Nueva.png"

#----------------------------------------------------------------------------------------------------------------------------

def median_filtering(im): #para sal y pimienta

      tiempoIni = time.time()
      route = (im) 
      im = Image.open(route)
      im_weidth = im.size[0]
      im_heigth = im.size[1]
      name= "Nueva.png"
      im.show()
      final_image = Image.new("P",(im_weidth,im_heigth))

      i = 1
      j = 1

      while i < im_weidth-1:
         while j < im_heigth-1:
            colors1 = im.getpixel((i-1,j-1))
            colors2 = im.getpixel((i-1,j))
            colors3 = im.getpixel((i-1,j+1))
            colors4 = im.getpixel((i,j-1))
            colors = im.getpixel((i,j))
            colors5 = im.getpixel((i,j+1))
            colors6 = im.getpixel((i+1,j-1))
            colors7 = im.getpixel((i+1,j))
            colors8 = im.getpixel((i+1,j+1))
            if type(colors)==int:
               median_list = [colors, colors1,colors2,colors3,colors4,colors5,colors6,colors7,colors8]
            else:
               gray =  int((colors[0] + colors[1]+ colors[2]) / 3)
               gray1 = int((colors1[0] + colors1[1]+ colors1[2]) / 3)
               gray2 = int((colors2[0] + colors2[1]+ colors2[2]) / 3)
               gray3 = int((colors3[0] + colors3[1]+ colors3[2]) / 3)
               gray4 = int((colors4[0] + colors4[1]+ colors4[2]) / 3)
               gray5 = int((colors5[0] + colors5[1]+ colors5[2]) / 3)
               gray6 = int((colors6[0] + colors6[1]+ colors6[2]) / 3)
               gray7 = int((colors7[0] + colors7[1]+ colors7[2]) / 3)
               gray8 = int((colors8[0] + colors8[1]+ colors8[2]) / 3)
               median_list = [gray, gray, gray2, gray3, gray4, gray5, gray6, gray7, gray8]
            ordered_list = shellSort(median_list)
            median = ordered_list[4]
            new_value = int(median)
            final_image.putpixel((i,j), new_value)
            j = j+1
         i = i+1
         j = 0

      final_image.show()
      final_image.save(name)

      tiempoFin = time.time()
      print("Processed in ", tiempoFin - tiempoIni, " seconds")
      return name

#----------------------------------------------------------------------------------------------------------------------------

def calculateUmbral(im):

      route = (im)
      im = Image.open(route)
      im_weidth = im.size[0]
      im_heigth = im.size[1]
      res = 0

      i = 0
      j = 0

      while i < im_weidth:
         while j < im_heigth:
            colors = im.getpixel((i,j))
            if type(colors)==int:
               res = res + colors
            else:
               gray =  int((colors[0] + colors[1]+ colors[2]) / 3)
               res = res + gray
            j = j+1
         i = i+1
         j = 0

      nivel = res/(im_weidth * im_heigth )
      return int(nivel)
            
      

#----------------------------------------------------------------------------------------------------------------------------

def gradient(im):
      tiempoIni = time.time()
      aux = im
      route = (im)
      im = Image.open(route)
      im_weidth = im.size[0]
      im_heigth = im.size[1]
      im.show()
      final_image = Image.new("P", (im_weidth,im_heigth))
      final_image2 = Image.new("P", (im_weidth,im_heigth))

      umbral = calculateUmbral(aux)
      i = 0
      j = 0

      wfinal = im_weidth - 1
      hfinal = im_heigth - 1

      while i < wfinal :
         while j < hfinal:
            colors = im.getpixel((i,j))
            colorsx = im.getpixel((i,j+1))
            colorsy = im.getpixel((i+1,j)) 
            if type(colors)==int:
               gx = colorsx -colors
               gy = colorsy -colors

            else:
               gray =  int((colors[0] + colors[1]+ colors[2]) / 3)
               grayx = int((colorsx[0] + colorsx[1]+ colorsx[2]) / 3)
               grayy = int((colorsy[0] + colorsy[1]+ colorsy[2]) / 3)

               gx = grayx - gray
               gy = grayx -gray

            gf = abs(gx) + abs(gy)
            new_value = int(gf)
            final_image.putpixel((i,j),new_value)
            if new_value <= umbral :
               new_value = 0
            else:
               new_value = 255
            final_image2.putpixel((i,j),new_value)
            j = j+1
         i = i+1
         j = 0

      final_image.show()
      final_image2.show()


      tiempoFin = time.time()
      print("Procesed in ", tiempoFin - tiempoIni, " seconds")

#----------------------------------------------------------------------------------------------------------------------------

def Laplacian(im):
      tiempoIni = time.time()
      aux = im
      route = (im)
      im  = Image.open(route)
      im_weidth = im.size[0]
      im_heigth = im.size[1]
      #im.show()
      final_image = Image.new("P",(im_weidth,im_heigth))
      final_image2 = Image.new("P", (im_weidth,im_heigth))

      umbral = calculateUmbral(aux)
      i = 1
      j = 1

      while i < im_weidth-1:
         while j < im_heigth-1:
            colors2 = im.getpixel((i-1,j))
            colors4 = im.getpixel((i,j-1))
            colors = im.getpixel((i,j))
            colors5 = im.getpixel((i,j+1))
            colors7 = im.getpixel((i+1,j))
            if type(colors)==int:
               new_value =  (colors2*(1)) + (colors4* (1)) + (colors*-4) + (colors5*(1)) + (colors7*(1)) 
            else:
               gray =  int((colors[0] + colors[1]+ colors[2]) / 3)
               gray2 = int((colors2[0] + colors2[1]+ colors2[2]) / 3)
               gray4 = int((colors4[0] + colors4[1]+ colors4[2]) / 3)
               gray5 = int((colors5[0] + colors5[1]+ colors5[2]) / 3)
               gray7 = int((colors7[0] + colors7[1]+ colors7[2]) / 3)
               new_value = (gray2*(1)) + (gray4 * (1)) + (gray*-4) + (gray5*(1)) + (gray7*(1))
               new_value = new_value/9

            new_value = int(new_value)
            final_image.putpixel((i,j), new_value)
            if new_value <= 5:
               final_value = 0
            else:
               final_value = 255

            final_image2.putpixel((i,j), final_value)
            j = j+1
         i = i+1
         j = 0

      final_image.show()
      final_image2.show()

      tiempoFin = time.time()
      print("Processed in ", tiempoFin - tiempoIni," seconds" )

#----------------------------------------------------------------------------------------------------------------------------

def Kirsch(im):
      
      tiempoIni = time.time()
      aux = im
      route = (im)
      im  = Image.open(route)
      im_weidth = im.size[0]
      im_heigth = im.size[1]
      im.show()
      final_image = Image.new("P",(im_weidth,im_heigth))
      listaux = []
      umbral = calculateUmbral(aux)

      i = 1
      j = 1

      while i < im_weidth-1:
         while j < im_heigth-1:
            colors1 = im.getpixel((i-1,j-1))
            colors2 = im.getpixel((i-1,j))
            colors3 = im.getpixel((i-1,j+1))
            colors4 = im.getpixel((i,j-1))
            colors = im.getpixel((i,j))
            colors5 = im.getpixel((i,j+1))
            colors6 = im.getpixel((i+1,j-1))
            colors7 = im.getpixel((i+1,j))
            colors8 = im.getpixel((i+1,j+1))
            if type(colors)==int:
               k0 =  (colors1*-3) + (colors2*-3) + (colors3*5) + (colors4*-3) + (colors5*5) + (colors6*-3) + (colors7*-3) +(colors8*5)
               listaux.append(k0)
               k1 =  (colors1*-3) + (colors2*5) + (colors3*5) + (colors4*-3) + (colors5*5) + (colors6*-3) + (colors7*-3) +(colors8*-3)
               listaux.append(k1)
               k2 =  (colors1*5) + (colors2*5) + (colors3*5) + (colors4*-3) + (colors5*-3) + (colors6*-3) + (colors7*-3) +(colors8*-3)
               listaux.append(k2)
               k3 =  (colors1*5) + (colors2*5) + (colors3*-3) + (colors4*5) + (colors5*-3) + (colors6*-3) + (colors7*-3) +(colors8*-3)
               listaux.append(k3)
               k4 =  (colors1*5) + (colors2*-3) + (colors3*-3) + (colors4*5) + (colors5*-3) + (colors6*5) + (colors7*-3) +(colors8*-3)
               listaux.append(k4)
               k5 =  (colors1*-3) + (colors2*-3) + (colors3*-3) + (colors4*5) + (colors5*-3) + (colors6*5) + (colors7*5) +(colors8*-3)
               listaux.append(k5)
               k6 =  (colors1*-3) + (colors2*-3) + (colors3*-3) + (colors4*-3) + (colors5*-3) + (colors6*5) + (colors7*5) +(colors8*5)
               listaux.append(k6)
               k7 =  (colors1*-3) + (colors2*-3) + (colors3*-3) + (colors4*-3) + (colors5*5) + (colors6*-3) + (colors7*5) +(colors8*5)
               listaux.append(k7)

            else:
               gray =  int((colors[0] + colors[1]+ colors[2]) / 3)
               gray1 = int((colors1[0] + colors1[1]+ colors1[2]) / 3)
               gray2 = int((colors2[0] + colors2[1]+ colors2[2]) / 3)
               gray3 = int((colors3[0] + colors3[1]+ colors3[2]) / 3)
               gray4 = int((colors4[0] + colors4[1]+ colors4[2]) / 3)
               gray5 = int((colors5[0] + colors5[1]+ colors5[2]) / 3)
               gray6 = int((colors6[0] + colors6[1]+ colors6[2]) / 3)
               gray7 = int((colors7[0] + colors7[1]+ colors7[2]) / 3)
               gray8 = int((colors8[0] + colors8[1]+ colors8[2]) / 3)
               k0 =  (gray1*-3) + (gray2*-3) + (gray3*5) + (gray4*-3) + (gray5*5) + (gray6*-3) + (gray7*-3) +(gray8*5)
               listaux.append(k0)
               k1 =  (gray1*-3) + (gray2*5) + (gray3*5) + (gray4*-3) + (gray5*5) + (gray6*-3) + (gray7*-3) +(gray8*-3)
               listaux.append(k1)
               k2 =  (gray1*5) + (gray2*5) + (gray3*5) + (gray4*-3) + (gray5*-3) + (gray6*-3) + (gray7*-3) +(gray8*-3)
               listaux.append(k2)
               k3 =  (gray1*5) + (gray2*5) + (gray3*-3) + (gray4*5) + (gray5*-3) + (gray6*-3) + (gray7*-3) +(gray8*-3)
               listaux.append(k3)
               k4 =  (gray1*5) + (gray2*-3) + (gray3*-3) + (gray4*5) + (gray5*-3) + (gray6*5) + (gray7*-3) +(gray8*-3)
               listaux.append(k4)
               k5 =  (gray1*-3) + (gray2*-3) + (gray3*-3) + (gray4*5) + (gray5*-3) + (gray6*5) + (gray7*5) +(gray8*-3)
               listaux.append(k5)
               k6 =  (gray1*-3) + (gray2*-3) + (gray3*-3) + (gray4*-3) + (gray5*-3) + (gray6*5) + (gray7*5) +(gray8*5)
               listaux.append(k6)
               k7 =  (gray1*-3) + (gray2*-3) + (gray3*-3) + (gray4*-3) + (gray5*5) + (gray6*-3) + (gray7*5) +(gray8*5)
               listaux.append(k7)
            new_value = max(listaux)
            #if new_value <= umbral:
             #  new_value = 0
            #else:
            #   new_value = 255
            final_image.putpixel((i,j), new_value)
            listaux = []
            j = j+1
         i = i+1
         j = 0

      final_image.show()
      final_image.save("Nueva.png")


      tiempoFin = time.time()
      print("Processed in ", tiempoFin- tiempoIni," seconds")
      return"Nueva.png"

#----------------------------------------------------------------------------------------------------------------------------

def erosion(im):
      tiempoIni = time.time()
      aux = im
      route = (im)
      im  = Image.open(route)
      im_weidth = im.size[0]
      im_heigth = im.size[1]
      #im.show()
      final_image = Image.new("P",(im_weidth,im_heigth))
      listaux = []

      i = 1
      j = 1

      while i < im_weidth-1:
         while j < im_heigth-1:
            colors1 = im.getpixel((i-1,j-1))
            colors2 = im.getpixel((i-1,j))
            colors3 = im.getpixel((i-1,j+1))
            colors4 = im.getpixel((i,j-1))
            colors = im.getpixel((i,j))
            colors5 = im.getpixel((i,j+1))
            colors6 = im.getpixel((i+1,j-1))
            colors7 = im.getpixel((i+1,j))
            colors8 = im.getpixel((i+1,j+1))
            if type(colors)==int:
               listaux.append(colors)
               listaux.append(colors1)
               listaux.append(colors2)
               listaux.append(colors3)
               listaux.append(colors4)
               listaux.append(colors5)
               listaux.append(colors6)
               listaux.append(colors7)
               listaux.append(colors8)

            else:
               gray =  int((colors[0] + colors[1]+ colors[2]) / 3)
               gray1 = int((colors1[0] + colors1[1]+ colors1[2]) / 3)
               gray2 = int((colors2[0] + colors2[1]+ colors2[2]) / 3)
               gray3 = int((colors3[0] + colors3[1]+ colors3[2]) / 3)
               gray4 = int((colors4[0] + colors4[1]+ colors4[2]) / 3)
               gray5 = int((colors5[0] + colors5[1]+ colors5[2]) / 3)
               gray6 = int((colors6[0] + colors6[1]+ colors6[2]) / 3)
               gray7 = int((colors7[0] + colors7[1]+ colors7[2]) / 3)
               gray8 = int((colors8[0] + colors8[1]+ colors8[2]) / 3)
               listaux.append(gray)
               listaux.append(gray1)
               listaux.append(gray2)
               listaux.append(gray3)
               listaux.append(gray4)
               listaux.append(gray5)
               listaux.append(gray6)
               listaux.append(gray7)
               listaux.append(gray8)
            new_value = min(listaux)
            final_image.putpixel((i,j), new_value)
            listaux = []
            j = j+1
         i = i+1
         j = 0

      final_image.show()
      final_image.save("Nueva.bmp")



      tiempoFin = time.time()
      print("Processed in ", tiempoFin- tiempoIni," seconds")
      return "Nueva.png"

#----------------------------------------------------------------------------------------------------------------------------

def dilatacion(im):
      tiempoIni = time.time()
      aux = im
      route = (im)
      im  = Image.open(route)
      im_weidth = im.size[0]
      im_heigth = im.size[1]
      #im.show()
      final_image = Image.new("P",(im_weidth,im_heigth))
      listaux = []

      i = 1
      j = 1

      while i < im_weidth-1:
         while j < im_heigth-1:
            colors1 = im.getpixel((i-1,j-1))
            colors2 = im.getpixel((i-1,j))
            colors3 = im.getpixel((i-1,j+1))
            colors4 = im.getpixel((i,j-1))
            colors = im.getpixel((i,j))
            colors5 = im.getpixel((i,j+1))
            colors6 = im.getpixel((i+1,j-1))
            colors7 = im.getpixel((i+1,j))
            colors8 = im.getpixel((i+1,j+1))
            if type(colors)==int:
               listaux.append(colors)
               listaux.append(colors1)
               listaux.append(colors2)
               listaux.append(colors3)
               listaux.append(colors4)
               listaux.append(colors5)
               listaux.append(colors6)
               listaux.append(colors7)
               listaux.append(colors8)

            else:
               gray =  int((colors[0] + colors[1]+ colors[2]) / 3)
               gray1 = int((colors1[0] + colors1[1]+ colors1[2]) / 3)
               gray2 = int((colors2[0] + colors2[1]+ colors2[2]) / 3)
               gray3 = int((colors3[0] + colors3[1]+ colors3[2]) / 3)
               gray4 = int((colors4[0] + colors4[1]+ colors4[2]) / 3)
               gray5 = int((colors5[0] + colors5[1]+ colors5[2]) / 3)
               gray6 = int((colors6[0] + colors6[1]+ colors6[2]) / 3)
               gray7 = int((colors7[0] + colors7[1]+ colors7[2]) / 3)
               gray8 = int((colors8[0] + colors8[1]+ colors8[2]) / 3)
               listaux.append(gray)
               listaux.append(gray1)
               listaux.append(gray2)
               listaux.append(gray3)
               listaux.append(gray4)
               listaux.append(gray5)
               listaux.append(gray6)
               listaux.append(gray7)
               listaux.append(gray8)
            new_value = max(listaux)
            final_image.putpixel((i,j), new_value)
            listaux = []
            j = j+1
         i = i+1
         j = 0

      final_image.show()
      final_image.save("Nueva1.bmp")



      tiempoFin = time.time()
      print("Processed in ", tiempoFin- tiempoIni," seconds")
      return "Nueva.png"

#----------------------------------------------------------------------------------------------------------------------------

def apertura(im):
      im_aux = erosion(im)
      dilatacion(im_aux)

#----------------------------------------------------------------------------------------------------------------------------
def  cierre(im):
      im_aux = dilatacion(im)
      erosion(im_aux)
