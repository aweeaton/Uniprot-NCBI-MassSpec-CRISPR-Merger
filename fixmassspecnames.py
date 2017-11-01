#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 17:46:43 2017

@author: eatonaw
"""

import pandas as pd
import xlsxwriter

df = pd.read_excel(r'/Users/eatonaw/Desktop/Atom_Files/Jim/Merger/NewMassSpecFiles/Workbook2.xlsx')
gene_df = df[['Gene Symbol']]
official_gene_df = df[['Gene Symbol Master']]

all_gene_rows = []
for genes in gene_df['Gene Symbol']:
    one_gene_row = []
    for gene in str(genes).split(';'):
        if gene in official_gene_df['Gene Symbol Master'].values:
            one_gene_row.append(gene)
            break
    all_gene_rows.append(one_gene_row)

len(all_gene_rows)

df['updated_gene'] = all_gene_rows

out_file = pd.ExcelWriter('FixedMassSpecNames.xlsx', engine='xlsxwriter')
df.to_excel(out_file)
out_file.close()


### 1. strip potenital extra space around official_gene_df genes

### 2. determine a way to stop once there are no more genes in gene_df
###    e.g. don't convert the nan
