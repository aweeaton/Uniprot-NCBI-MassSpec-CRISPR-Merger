import pandas as pd
import xlsxwriter

#Read in the mass spec data
mass = pd.read_excel('/Users/eatonaw/Desktop/Atom_Files/Jim/Merger/NewMassSpecFiles/BioID_TMD8_control_L265P_FIXED.xlsx')

mass2 = pd.read_excel('/Users/eatonaw/Desktop/Atom_Files/Jim/Merger/NewMassSpecFiles/R_Young_BioID_170430_CD79_FIXED.xlsx')

mass3 = pd.read_excel('/Users/eatonaw/Desktop/Atom_Files/Jim/Merger/NewMassSpecFiles/R_Young_TLR9_BioID_170429_FIXED.xls')

mass4 = pd.read_excel('/Users/eatonaw/Desktop/Atom_Files/Jim/Merger/NewMassSpecFiles/BioID_170432_MyD88_BJAB_TO_FIXED.xlsx')

mass5 = pd.read_excel('/Users/eatonaw/Desktop/Atom_Files/Jim/Merger/NewMassSpecFiles/Sample_170168_Ly10_L265P_L265Pibru_FIXED.xlsx')

mass6 = pd.read_excel('/Users/eatonaw/Desktop/Atom_Files/Jim/Merger/NewMassSpecFiles/Sample_170174_BJAB_WT_L265P_FIXED.xlsx')

#Read in the complete gene symbol list from UniProt
df = pd.read_excel('/Users/eatonaw/Desktop/Atom_Files/Jim/Merger/NewMassSpecFiles/GeneSymbols.xlsx')

#Make a list of all the mass spec data
mass_list = [mass, mass2, mass3, mass4, mass5, mass6]

#Merge the gene symbols with the mass spec data
for i in mass_list:
    df = df.merge(i, how = 'left', on = 'Gene Symbol')

#Kill duplicates
df.drop_duplicates('Gene Symbol', inplace=True)

#Writing the data frame to an Excel file
out_file = pd.ExcelWriter('AllMassSpecData.xlsx', engine = 'xlsxwriter')
df.to_excel(out_file)
out_file.close()
