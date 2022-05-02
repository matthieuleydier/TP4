import os,sys
#from ROOT import TH1D,TH2D,TFile,TTree,TCanvas
import sys
import array
# Import the other script
import Branches_name
directory_in_str = './data_samples/'
directory = os.fsencode(directory_in_str)


#iterating over the files     
for file in os.listdir(directory):
    
    filename = os.fsdecode(file)
    
    if filename.endswith(".root") and filename.startswith("Bu2KpipiMM"):
        print(filename)
        
#        print(directory_in_str)

#        base_dir = os.path.Project(os.path.abspath(__file__))
 #       Branches_name.main(os.path.join(base_dir, 'data_samples', filename))
#        Branches_name.main(os.path.join("data_samples",filename))
        Branches_name.main(filename,"data_samples")
       # Branches_name.main("data_samples/{}".format(filename))
       # Branches_name.main(filename)
        print(filename)
        # os.system('Branches_name.py "filename"')        
       #import Branches_name filename
