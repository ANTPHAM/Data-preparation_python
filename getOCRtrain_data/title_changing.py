#!/usr/bin/env python
# coding: utf-8

#    #        Data Preparation For Training Tasks

# Ce script permettra de travailler avec itération sur les fichiers stockés dans un répertoire nommé " train_images". 
# 
# Il s'agit des images prises sur  des cartes de différents restaurants.
# 
# Les formats de ces images peuvent être divers: .jpeg;  .png ; .pdf; Certaines cartes sont présentées par 2 images avec 2 formats différents( pdf et jpeg par example).
# 
# Collectées de différentes sources, ces  images portent des tittres qui ne respectent pour l'instant aucune règle. 
# 
# Ce scrip va permettre dans un premier temps de numéroter les titres des images pour facilliter  tout travail de modélisation.
# 
# 


import re
import os
import pandas as pd
import numpy as np

# indiquer le chemin qui va au répertoire où les textes sont stockés
get_ipython().run_line_magic('cd', 'C:\\Users\\Pham Antoine\\Desktop\\ToGit\\Data_Preparation_Python\\getOCRtrain_data\\downloads - Copy\\carte restaurant')


# Voici le code à exécuter pour collecter les données stockés dans des différents fichiers textex et les mettre sous forme d'un Data Frame

actual_dir = os.getcwd()
dir_tree = os.walk(actual_dir)
for dirpath, dirnames, filenames in dir_tree:
    print(filenames[-3:])
    pass
file2change = []
for file in filenames:
    for j in ['jpeg', 'pdf', 'jpg', 'png', 'gif', 'JPG']:
        if file.endswith(j):
            file2change.append(file)

print( " The 3 latest files :" + file2change[-3:])

print(" There are %d files in the directory" %len(file2change))

old_name=[]# original name2change of images
imf=[]# format of the images
for file in file2change:
    for fmt in ['.jpeg', '.pdf', '.jpg', '.png', '.gif', '.JPG']:
        if file.endswith(fmt):
            t="".join(re.findall(r'(.+?)%s' % fmt,file))
            f="".join(fmt)
            old_name.append(t)
            imf.append(f)
    
u_name2change=list(np.unique(old_name))# to group same images which are represented under different formats

print( "There are %d unique images in the directory" %len(u_name2change))

# assigning to each image in "old_name" the index of the same image in "u_name2change"; by the way, 2 indentical images will have the same index
num_name2change=[]
for i in range(len(old_name)):
    for j in range(len(u_name2change)):
        if old_name[i] == u_name2change[j]:
            num_name2change.append(j)

print(num_name2change[-2:])            

# create the new name of images
new_name=[str(i) + j for i,j in zip(num_name2change, imf)]

len(new_name)

print("Old names of the 2 first images in the directorey: {} and {}".format(file2change[0], file2change[1]))

print("New names of these images are: {} and {}".format(new_name[0], new_name[1]))

try:
    for file in filenames:
        if file in file2change:
            k=int(file2change.index(file))
            os.rename(file,new_name[k])
except:
    print("No file anymore as required in the directory")

