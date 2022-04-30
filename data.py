from zipfile import ZipFile 
  
file = "./data/ser.zip"
  
# open the zip file in read mode
with ZipFile(file, 'r') as zip: 
    # list all the contents of the zip file
    zip.printdir() 
  
    # extract all files
    print('extraction...') 
    zip.extractall("./data/") 
    print('Done!')