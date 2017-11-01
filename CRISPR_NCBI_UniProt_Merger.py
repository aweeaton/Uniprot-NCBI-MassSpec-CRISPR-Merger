#Important note: Need to have pandas, bioservices, xlrd, and biopython pre-downloaded

#Importing all of the necessary libraries
#Library that allows us to accress UniProt
from bioservices import UniProt

#Library that allows us to access NCBI
from Bio import Entrez

#Library allowing for data frame manipulation/analysis
import pandas as pd
import xlrd
from io import StringIO

#Library allowing us to write files to Excel
import xlsxwriter

#Library allowing us to set up command-line interface
import argparse

#Sets up the argument parser and help on running the script
parser = argparse.ArgumentParser(description = """Welcome to the CRISPR screen/UniProt merging script.
                                                Inputting a CRISPR screen file is required. Connection to WiFi also required.""")

#Sets up -i to store the input CRISPR screen files
parser.add_argument("-i", help = "Input CRISPR screen file", required = True, type = argparse.FileType('r'))

args = parser.parse_args()

input_file = args.i.name


df_input = pd.read_excel(input_file)

#Storing UniProt as an easier to type variable 'u'
u = UniProt()

#Using a built-in UniProt method to create a data frame containg everything in UniProt
df_uniprot = u.get_df("organism:9606+and+reviewed:yes")

#Rename the common column to match the inputted column
df_uniprot.rename(columns={'Gene names  (primary )':'Gene Symbol', 'Entry':'UniProt Symbol',
                            'Proteomes':'Chromosome Number', 'Length':'Protein Length'}, inplace = True)

#Selecting columns I think are interesting
df1_uniprot = df_uniprot[['UniProt Symbol', 'Gene names', 'Gene Symbol', 'Protein names',
        'Chromosome Number', 'Sequence', 'Protein Length', 'Function [CC]', 'Gene ontology (GO)',
        'Gene ontology (biological process)', 'Gene ontology (molecular function)',
        'Gene ontology (cellular component)', 'Protein families']]

#Converting the NCBI gene list to a pandas data frame
df_ncbi = pd.read_table('NCBI_GeneID_File.txt')

#Merge the data frames on the UniProt
df_merged = df_input.merge(df1_uniprot, how='outer', on = 'Gene Symbol')
df_merged2 = df_merged.merge(df_ncbi, how = 'outer', on = 'Gene Symbol')


#Writing the data frame to an Excel file
out_file = pd.ExcelWriter('CRISPR_Uniprot_NCBI_DataFrame3.xlsx', engine = 'xlsxwriter')
df_merged2.to_excel(out_file)
out_file.close()
