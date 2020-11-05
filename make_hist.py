#%%

import pandas as pd 
import numpy as np
from functools import partial, reduce
import glob 
import os
import itertools as it

#%%
path = "data"

all_files = glob.glob(os.path.join(path, "*.csv"))

df_list = []

print(f"Processing {len(all_files)} repos data:\n")

for f in all_files:
    path_list = f.split("\\")
    f_name = path_list[-1]
    f_name2 = f_name.split("stargazers_")[1]
    repo_name = f_name2.split(".csv")[0] 
    print(repo_name) 
    df_from_file = pd.read_csv(f)
    df_from_file['repo_name'] = repo_name
    df_list.append(df_from_file)



df_concat = pd.concat(df_list, ignore_index=True)



df_concat.to_csv("all_data_concatenated.csv")

# %%
