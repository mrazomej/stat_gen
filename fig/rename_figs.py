#!/usr/bin/python

#%%
import os
import glob
import pandas as pd

# %%

# Read list of images
xl = pd.ExcelFile('./fig_names.xlsx')

# Define chapters given by sheet names
chapters = xl.sheet_names

# %%

# Loop through chapters
for chap in chapters:
    # Read figures in chapter
    figs = xl.parse(chap)
    # Loop through figures and rename them
    for idx, f in figs.iterrows():
        ## FIGURES ##
        # Find figures with name
        fig_path = glob.glob(f'./{chap}/*{f.fig_name}*')
        # Loop through files with filename (can have multiple versions)
        for p in fig_path:
            # Find extesion of figure
            extension = p.split(f.fig_name)[-1]
            # Set new path for file
            new_fig = f'./{chap}/{f.chapter:02d}_{f.section:02d}_' + \
                    f'{f.number:02d}_{f.fig_name}{extension}'
            # Move file to new location
            print(f'{p} -> {new_fig}')
            os.rename(p, new_fig)
                    ## SCRIPTS ##
        # Find scripts with name
        script_path = glob.glob(f'../code/{chap}/*{f.fig_name}*')
        # Check that script exist
        if len(script_path) > 0:
            # Loop through files with filename (can have multiple versions)
            for q in script_path:
                # Find extesion of figure
                extension = q.split(f.fig_name)[-1]
                # Set new path for file
                new_script = f'../code/{chap}/{f.chapter:02d}_' + \
                            f'{f.section:02d}_{f.number:02d}_' + \
                            f'{f.fig_name}{extension}'
                # Move file to new location
                print(f'{q} -> {new_script}')
                os.rename(q, new_script)

# %%
