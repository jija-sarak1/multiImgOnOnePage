import pdf2image
from pathlib import Path

def image_conversion(inpath,image_path):
  print("converting to image")
  OUTPUT_FOLDER = None
  FIRST_PAGE = 1
  LAST_PAGE = 16
  FORMAT = 'jpg'
  USERPWD = None
  USE_CROPBOX = False
  STRICT = False

  Name = Path(inpath).stem
  pil_images = pdf2image.convert_from_path(inpath,
                                          output_folder = OUTPUT_FOLDER,
                                          first_page = FIRST_PAGE,
                                          last_page = LAST_PAGE,
                                          fmt = FORMAT,
                                          userpw = USERPWD,
                                          use_cropbox= USE_CROPBOX,
                                          strict = STRICT )

  i = 1
  for image in pil_images :
    image.save(image_path+"/"+Name+str(i)+".jpg")
    i+=1

inpath = input("enter a pdf file path") # Give a pdf file path which you want to convert into image
image_path = input("enter a output image path") # Give a output folder path where you want to store the output image
image_conversion(inpath , image_path)
