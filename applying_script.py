import os,sys
#from ROOT import TH1D,TH2D,TFile,TTree,TCanvas
import sys
import array

# Import the other script
directory_in_str = './data_samples/data_samples/'
directory = os.fsencode(directory_in_str)
#directory = panfs/mleydier/Python_training/Project/data_samples/data_samples

#for files in os.listdir("./data_samples/data_samples/"):
#  print( files)
    
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".root") and filename.startswith("Bu2KpipiMM"):
        print(filename)
        import Branches_name filename
#          os.system("Branches_name.py filename")
# print(os.path.join(directory, filename))
#         continue
        # import Branches_name#.py filenam
#        else:
 #       break
