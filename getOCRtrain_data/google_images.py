#!/usr/bin/env python
# coding: utf-8

# This job will be using the library "google-images-dowload" to dowload images in order to buid a training set 
# 
# https://github.com/hardikvasa/google-images-download
# 
# 

# Attention: 
# 
# In order t o dowload more than 100 images, it is necessary to get installed "chromedriver" and modify the python file founded in the library as following
# 
# - install chromedriver
# 
# - set up the path to chromedriver in system variable environnement
# 
# - open the source code .py in the library google-images-download
# 
# - add the below line of code ( on the row 816 for example): 
# 
# arguments['chromedriver'] = ".\\AppData\\Local\\chromedriver.exe"
# 
# 
# See : https://github.com/hardikvasa/google-images-download/issues/110
# 
cd .\getOCRtrain_data
from google_images_download import google_images_download   #importing the library

def get_images():

	number_of_images_to_dowload= input()# put a number
	response = google_images_download.googleimagesdownload()   #class instantiation
	arguments = {"keywords":"carte restaurant","limit":number_of_images_to_dowload,"print_urls":True}   #creating list of arguments
	paths = response.download(arguments)   #passing the arguments to the function
if __name__ == '__main__':
	get_images()
