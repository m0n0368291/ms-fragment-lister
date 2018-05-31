# -*- coding: utf-8 -*-
# !C:/Program Files (x86)/Python 3.5/python.exe

import glob
import pandas as pd

def masses_to_csv(file):
	df = pd.read_csv(file, sep="\t", header=6)
	df = df.round({"Mass":0,"Relative Intensities":0}) # round values
	#print(df)
	df2 = df[["Mass","Relative Intensities"]].loc[df["Relative Intensities"] > 4] # select only values above 4% rel. intensity
	df2["Mass"] = pd.to_numeric(df2["Mass"],downcast="integer") # remove trailing zero
	df2["Relative Intensities"] = pd.to_numeric(df2["Relative Intensities"],downcast="integer") # remove trailing zero
	df2["Relative Intensities"] = df2["Relative Intensities"].astype(str, copy=False) # convert back to string
	df2["Relative Intensities"] = df2["Relative Intensities"].str.replace("(\d+)", r"(\1)") # add parentheses to second column
	output_csv = str(file+".csv")
	df2.to_csv(path_or_buf=output_csv, columns=None, header=False, index=False, sep=" ", line_terminator=", ") # write values to csv file

files = glob.glob("*.D.txt")
for file in files:
	#print(file)
	masses_to_csv(file)