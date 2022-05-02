import ROOT
import os,sys
from ROOT import TH1D,TH2D,TFile,TTree,TCanvas,TChain
import sys
import array

#histFileName = sys.argv [1]
plotFileName1 = sys.argv [1]
plotFileName2 = sys.argv [2]

#histFile = TFile.Open(histFileName,"READ")
#dataHisto = histFile.Get("DecayTree")

#if not dataHisto:
#    print("Failed to get data histogram")
#    sys.exit(1)

canvas1 = TCanvas("canvas1")
#canvas1.Print(plotFileName1+"[")

# Plotting #
# "B_MM"
data_files = "data_samples"
cutted_data_files = "Cutted_files"
#

#Raw data
Run1 = TChain("DecayTree")

Run1.Add(os.path.join(data_files,"Bu2KpipiMM-Data-2011-MagDown-StrippingBu2LLK_fiducialMM_preselPIDMM_selected.root"))
Run1.Add(os.path.join(data_files,"Bu2KpipiMM-Data-2011-MagUp-StrippingBu2LLK_fiducialMM_preselPIDMM_selected.root"))
Run1.Add(os.path.join(data_files,"Bu2KpipiMM-Data-2012-MagDown-StrippingBu2LLK_fiducialMM_preselPIDMM_selected.root"))
Run1.Add(os.path.join(data_files,"Bu2KpipiMM-Data-2012-MagUp-StrippingBu2LLK_fiducialMM_preselPIDMM_selected.root"))

#Cutted data
Run1_Cut = TChain("DecayTree")

Run1_Cut.Add(os.path.join(cutted_data_files,"Cut_Bu2KpipiMM-Data-2011-MagDown-StrippingBu2LLK_fiducialMM_preselPIDMM_selected.root"))
Run1_Cut.Add(os.path.join(cutted_data_files,"Cut_Bu2KpipiMM-Data-2011-MagUp-StrippingBu2LLK_fiducialMM_preselPIDMM_selected.root"))
Run1_Cut.Add(os.path.join(cutted_data_files,"Cut_Bu2KpipiMM-Data-2012-MagDown-StrippingBu2LLK_fiducialMM_preselPIDMM_selected.root"))
Run1_Cut.Add(os.path.join(cutted_data_files,"Cut_Bu2KpipiMM-Data-2012-MagUp-StrippingBu2LLK_fiducialMM_preselPIDMM_selected.root"))


 
Run1.SetLineColor(ROOT.kBlack)
Run1_Cut.SetLineColor(ROOT.kRed)

#Draw 
#N_events = Run1.Draw("B_MM>>my_histogram1(50,3700,6900)","")

Run1.Draw("B_MM>>my_histogram1(50,3700,6900)","")
Run1_Cut.Draw("B_MM>>my_histogram11(50,3700,6900)","","same")
#N_cut_events = Run1_Cut.Draw("B_MM>>my_histogram11(50,3700,6900)","B_MM<5000","same")
#print("N_events = ", N_events, "N_cut_events = ",N_cut_events)

# Retrieve the histograms
my_histogram1 = ROOT.gDirectory.Get("my_histogram1")
my_histogram11 = ROOT.gDirectory.Get("my_histogram11")

#Styling                                                                                                                                                   
my_histogram1.GetXaxis().SetTitle("Mass [MeV]")   
my_histogram1.GetYaxis().SetTitle("Number of events") 
my_histogram1.SetStats(0) 
my_histogram11.SetStats(0) 

leg1 = ROOT.TLegend(.6,.6,.9,.7)
leg1.SetBorderSize(0)
leg1.SetFillColor(0)
leg1.SetFillStyle(0)
leg1.SetTextFont(42)
leg1.SetTextSize(0.035)
leg1.AddEntry(Run1,"Raw data","L")
leg1.AddEntry(Run1_Cut,"Cutted data","L")
leg1.Draw()

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.045)
latex.DrawText(0.6,0.8,"LHCb Run 1") 
latex.SetTextSize(0.02)
#latex.DrawText(0.7,0.77,"B \rightarrow Kpipi events")

# Update the styling part
canvas1.Update()


canvas1.SaveAs(plotFileName1)

  

canvas2 = TCanvas("canvas2")

#Raw data
Run2 = TChain("DecayTree")

Run2.Add(os.path.join(data_files,"Bu2KpipiMM-Data-2015-MagDown-StrippingBu2LLK_fiducialMM16_preselPIDMM16_selected.root"))
Run2.Add(os.path.join(data_files,"Bu2KpipiMM-Data-2015-MagUp-StrippingBu2LLK_fiducialMM16_preselPIDMM16_selected.root"))
Run2.Add(os.path.join(data_files,"Bu2KpipiMM-Data-2016-MagDown-StrippingBu2LLK_fiducialMM16_preselPIDMM16_selected.root"))
Run2.Add(os.path.join(data_files,"Bu2KpipiMM-Data-2016-MagUp-StrippingBu2LLK_fiducialMM16_preselPIDMM16_selected.root"))
Run2.Add(os.path.join(data_files,"Bu2KpipiMM-Data-2017-MagDown-StrippingBu2LLK_fiducialMM16_preselPIDMM16_selected.root"))
Run2.Add(os.path.join(data_files,"Bu2KpipiMM-Data-2017-MagUp-StrippingBu2LLK_fiducialMM16_preselPIDMM16_selected.root"))
Run2.Add(os.path.join(data_files,"Bu2KpipiMM-Data-2018-MagDown-StrippingBu2LLK_fiducialMM16_preselPIDMM16_selected.root"))
Run2.Add(os.path.join(data_files,"Bu2KpipiMM-Data-2018-MagUp-StrippingBu2LLK_fiducialMM16_preselPIDMM16_selected.root"))

#Cutted data
Run2_Cut = TChain("DecayTree")

Run2_Cut.Add(os.path.join(cutted_data_files,"Cut_Bu2KpipiMM-Data-2015-MagDown-StrippingBu2LLK_fiducialMM16_preselPIDMM16_selected.root"))
Run2_Cut.Add(os.path.join(cutted_data_files,"Cut_Bu2KpipiMM-Data-2015-MagUp-StrippingBu2LLK_fiducialMM16_preselPIDMM16_selected.root"))
Run2_Cut.Add(os.path.join(cutted_data_files,"Cut_Bu2KpipiMM-Data-2016-MagDown-StrippingBu2LLK_fiducialMM16_preselPIDMM16_selected.root"))
Run2_Cut.Add(os.path.join(cutted_data_files,"Cut_Bu2KpipiMM-Data-2016-MagUp-StrippingBu2LLK_fiducialMM16_preselPIDMM16_selected.root"))
Run2_Cut.Add(os.path.join(cutted_data_files,"Cut_Bu2KpipiMM-Data-2017-MagDown-StrippingBu2LLK_fiducialMM16_preselPIDMM16_selected.root"))
Run2_Cut.Add(os.path.join(cutted_data_files,"Cut_Bu2KpipiMM-Data-2017-MagUp-StrippingBu2LLK_fiducialMM16_preselPIDMM16_selected.root"))
Run2_Cut.Add(os.path.join(cutted_data_files,"Cut_Bu2KpipiMM-Data-2018-MagDown-StrippingBu2LLK_fiducialMM16_preselPIDMM16_selected.root"))
Run2_Cut.Add(os.path.join(cutted_data_files,"Cut_Bu2KpipiMM-Data-2018-MagUp-StrippingBu2LLK_fiducialMM16_preselPIDMM16_selected.root"))

#Styling 
Run2.SetLineColor(ROOT.kBlack)
Run2_Cut.SetLineColor(ROOT.kRed)

# Draw 
Run2.Draw("B_MM>>my_histogram2(50,3700,6900)")
Run2_Cut.Draw("B_MM>>my_histogram22(50,3700,6900)","","same")

# Retrieve the histograms
my_histogram2 = ROOT.gDirectory.Get("my_histogram2")
my_histogram22 = ROOT.gDirectory.Get("my_histogram22")

#Styling                                                                                                                                                   
my_histogram2.GetXaxis().SetTitle("Mass [MeV]")   
my_histogram2.GetYaxis().SetTitle("Number of events") 
my_histogram2.SetStats(0) 
my_histogram22.SetStats(0) 

leg2 = ROOT.TLegend(.6,.6,.9,.7)
leg2.SetBorderSize(0)
leg2.SetFillColor(0)
leg2.SetFillStyle(0)
leg2.SetTextFont(42)
leg2.SetTextSize(0.035)
leg2.AddEntry(Run2,"Raw data","L")
leg2.AddEntry(Run2_Cut,"Cutted data","L")
leg2.Draw()

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.045)
latex.DrawText(0.6,0.8,"LHCb Run 2") 
latex.SetTextSize(0.02)
#latex.DrawText(0.7,0.77,"B \rightarrow Kpipi events")

# Update the styling part
canvas2.Update()


canvas2.SaveAs(plotFileName2)


# End of plotting 

