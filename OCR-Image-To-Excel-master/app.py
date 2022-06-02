#for tesseract
from PIL import Image
import pytesseract

#for path
import glob
import os

#for excel
import xlwt
from xlwt import Workbook

#for performance
import time

#time using for performance test
print("Process Starting")
start_time = time.time()

#Check out the README
#You will need download Tesseract if you dont have
#Specify path if available Tesseract
#Otherwise you will need download before specifying the path
path = '/usr/bin/tesseract'
pytesseract.pytesseract.tesseract_cmd = path

#test image folder 
#file_path_array = glob.glob("test/*.jpg")
file_path_array = glob.glob("test/*.png")

#create excel wordbook and adding sheet
wb = Workbook()
sheet = wb.add_sheet('Sheet')

#header
header_style = xlwt.easyxf('font: bold 1, color red;')
sheet.write(0, 0, 'Path', header_style)
sheet.write(0, 1, 'Name', header_style)
sheet.write(0, 2, 'Text', header_style)    

#if you want to use another language change lang parameter
#tur=Turkish
for idx, val in enumerate(file_path_array):
    print(".")
    sheet.write(idx + 1, 0, val)
    sheet.write(idx + 1, 1, os.path.basename(val))
    #sheet.write(idx + 1, 2, pytesseract.image_to_string(Image.open(val), lang="tur"))
    sheet.write(idx + 1, 2, pytesseract.image_to_string(Image.open(val), lang="eng"))


#if file does not exist creates new xls
#else overwrites exists file
wb.save('result.xls')


#this region using for process time 
#if u dont need this area
#don't worry you can delete
end_time = time.time()
cycle_time = end_time-start_time
print(len(file_path_array), "data processing took", format(cycle_time, '.2f'), "sec")
score = cycle_time/len(file_path_array)
print("performance score per proccess: ", format(score, '.2f'), "sec")
print("Process Done!")

