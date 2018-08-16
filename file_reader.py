# -*- coding: utf-8 -*-
"""
@author: mcreng
"""
import gzip
import os

class FileReader:
     def __init__(self, filename):
          self.filename = filename
          if not os.path.exists(self.filename):
               open(filename, 'w')
          
     def read_countries(self):
         with gzip.open(self.filename, 'rb') as f:
              return [s.decode('utf-8').strip() for s in list(f)]
    
     def write_countries(self, countries):
          with gzip.open(self.filename, 'wb') as f:
               for country in countries:
                    f.write(bytes(country + '\n', 'utf-8'))
