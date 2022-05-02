import os,sys
from ROOT import TH1D,TH2D,TFile,TTree,TCanvas
import sys
import array
import numpy as np

## MAIN FUNCTION ##
def main(FileName,datafile):
    
    inFileName = os.path.join(datafile,FileName) #Not relevant for the branches selection
    inFile=TFile(inFileName)
    intree = inFile.Get("DecayTree")

# New cutted file                                                                                                    
    cutted_sample_path = '/panfs/mleydier/Python_training/Project/MC_Cutted_files/' 
#    cutted_sample_path = '/panfs/mleydier/Python_training/Project/Cutted_files/' 
    cutted_sample_name = 'Cut_' + FileName

    newfile = TFile(cutted_sample_path + cutted_sample_name,"RECREATE")

#Branches to keep 
    
    intree.SetBranchStatus("*",0)
    branches_to_keep = ["K_PIDK","JPsi_MM","muplus_TRACK_GhostProb","muplus_ProbNNghost","muminus_ProbNNghost",
    "muminus_TRACK_GhostProb","K_ProbNNghost","K_TRACK_GhostProb","B_L0MuonDecision_TOS","B_L0DiMuonDecision_TOS",
    "B_DIRA_OWNPV","B_IPCHI2_OWNPV","B_DTF_PVandJpsi_CHI2NDOF","B_ENDVERTEX_CHI2","B_PT", "K1_1270_ENDVERTEX_CHI2",
    "JPsi_FDCHI2_OWNPV","K_PT","muplus_PT","muminus_PT","JPsi_P","JPsi_PT","JPsi_CosTheta","B_MM", "piminus_PT", "piplus_PT"]

    for keepbranch in branches_to_keep:
        intree.SetBranchStatus(keepbranch, 1) # activate branches of interest 

# Apply Sonia's cut : 
    LooseCut = "K_PIDK>-2 && muplus_TRACK_GhostProb<0.3 && muminus_TRACK_GhostProb<0.3  && K_TRACK_GhostProb<0.3 && (B_L0MuonDecision_TOS || B_L0DiMuonDe\
cision_TOS) && B_DIRA_OWNPV > 0.9999"
# && B_LOKI_DTF_CHI2NDOF<5               


    newtree  = intree.CopyTree(LooseCut)

    # pseudorapity eta = -ln() with JPsi_costheta
    #Cos_Theta = intree.AsMatrix(["JPsi_CosTheta"])
    eta_arrqy = array.array('d',[0])
    phi_pt_qrray = array.array('d',[0])
    b_dtf_array = array.array('d',[0])
    kpipi_vtx_array = array.array('d',[0])
    jpsi_fd_array = array.array('d',[0])
    mu_plus_array = array.array('d',[0])
    mu_minus_array = array.array('d',[0])
    kaon_array = array.array('d',[0])


    #define all qrrqys for the brqnches to rename
    #define all newtree.Branch for those branches

    #JPsi_eta = -1*np.log(np.tan(0.5*Cos_Theta))
    newtree.Branch("Jpsi_ETA", eta_arrqy , "Jpsi_ETA/D")
    newtree.Branch("phi_PT", phi_pt_qrray , "phi_PT/D")
    newtree.Branch("B_LOKI_DTF_CHI2NDOF", b_dtf_array, "B_LOKI_DTF_CHI2NDOF/D")
    newtree.Branch("B_VtxChi2_234", kpipi_vtx_array, "B_VtxChi2_234/D")
    newtree.Branch("Jpsi_FDCHI2_OWNPV", jpsi_fd_array, "Jpsi_FDCHI2_OWNPV/D")
    newtree.Branch("mu1_PT", mu_plus_array, "mu1_PT/D")
    newtree.Branch("mu2_PT", mu_minus_array, "mu2_PT/D")
    newtree.Branch("Kaon_PT", kaon_array, "Kaon_PT/D")


    for i in range(newtree.GetEntries()):
        newtree.GetEntry(i)
        eta_arrqy[0] = -1*np.log(np.tan(0.5*newtree.JPsi_CosTheta))
        phi_pt_qrray[0] = newtree.piplus_PT + newtree.piminus_PT
        #print(eta_arrqy[0])
        #copy the value from old brqnch to array of new branch (element 0)
        b_dtf_array[0] = newtree.B_DTF_PVandJpsi_CHI2NDOF
        kpipi_vtx_array[0] = newtree.K1_1270_ENDVERTEX_CHI2
        jpsi_fd_array[0] = newtree.JPsi_FDCHI2_OWNPV
        mu_plus_array[0] = newtree.muplus_PT
        mu_minus_array[0] = newtree.muminus_PT
        kaon_array[0] = newtree.K_PT



        newtree.Fill()


    list_branches = [key.GetName() for key in intree.GetListOfBranches()]
    for branch in list_branches:
        if branch in branches_to_keep:   
            print(branch)


# Writing in the new tree 
    print("Tree written with ", newtree.GetEntries(), " entries copied")
    print("File saved at location: ", cutted_sample_path+cutted_sample_name)
    newtree.Write()

    inFile.Close()
    print("File closed")
#end function 
if(__name__=='__main__'):
    sys.exit(main(sys.argv[1]))
