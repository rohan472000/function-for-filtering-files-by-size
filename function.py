import os

def unique_files():
  fin = []
  dirname='drive/My Drive/multiple-file-sizes/'       # directory of source
  directory = "drive/My Drive/rhn/"                   # directory to save 
  i=0
  for fname in os.listdir(dirname):
      file_size = os.path.getsize(os.path.join(dirname, fname))
      # print((int)(file_size/1024))
      sze = (int)(file_size/1024)
      if(fin.count(sze)):
        pass
      else:
        fin.insert(i,sze)
        #print(sze)
        filepath = directory + fname
        with open(filepath, 'w+') as fp:
          pass
      i = i + 1

      
unique_files()     ## calling the function      
