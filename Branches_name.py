import os,sys
from ROOT import TH1D,TH2D,TFile,TTree,TCanvas
import sys
import array

# launch script with " Branches_name.py File.root " format
if len(sys.argv) !=2:
    print("USAGE: %s <input file> <output file>"%(sys.argv[0]))
    sys.exit(1)

inFileName= sys.argv[1]
#outFileName= sys.argv[2]
#print("Reading from", inFileName, "and writing to", outFileName)
inFile=TFile(inFileName)
#inFile=TFile("Bu2KpipiMM-Data-2011-MagDown-StrippingBu2LLK_fiducialMM_preselPIDMM_selected.root")
intree = inFile.Get("DecayTree")

# Not useful 

Nentries =intree.GetEntries()
print("Nentries : ", Nentries)

#Branches to keep 
intree.SetBranchStatus("*",0)
branches_to_keep = ["K_PIDK","JPsi_MM","muplus_TRACK_GhostProb","muplus_ProbNNghost","muminus_ProbNNghost","muminus_TRACK_GhostProb","K_ProbNNghost","K_TRACK_GhostProb","B_L0MuonDecision_TOS","B_L0DiMuonDecision_TOS","B_DIRA_OWNPV","B_IPCHI2_OWNPV","B_DTF_PVandJpsi_CHI2NDOF","B_ENDVERTEX_CHI2","B_PT","JPsi_FDCHI2_OWNPV","K_PT","muplus_PT","muminus_PT","JPsi_P","JPsi_PT","JPsi_CosTheta"]

for keepbranch in branches_to_keep:
    intree.SetBranchStatus(keepbranch, 1) # activate branches of interest 

list_branches = [key.GetName() for key in intree.GetListOfBranches()]
for branch in list_branches:
    if branch in branches_to_keep:   
        print(branch)

# Apply Sonia's cut : 
LooseCut = "K_PIDK>-2 && muplus_TRACK_GhostProb<0.3 && muminus_TRACK_GhostProb<0.3  && K_TRACK_GhostProb<0.3 && (B_L0MuonDecision_TOS || B_L0DiMuonDe\
cision_TOS) && B_DIRA_OWNPV > 0.9999"
# && B_LOKI_DTF_CHI2NDOF<5               
# Jpsi_nombre > 50 truc 


## New cutted file                                                                                                    
cutted_sample_path = '/panfs/mleydier/Python_training/Project/'
cutted_sample_name = 'Cut_' + inFile.GetName()
newfile = TFile(cutted_sample_path + cutted_sample_name,"RECREATE")
newTree  = intree.CopyTree(LooseCut)

# Writing in the new tree 
print("Tree written with ", newTree.GetEntries(), " entries copied")
print("File saved at location: ", cutted_sample_path+cutted_sample_name)
newTree.Write()


inFile.Close()

