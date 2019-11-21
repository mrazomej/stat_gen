#!/usr/bin/python

#%%
import os
import glob
import pandas as pd
import re

# %%

# Read list of images
xl = pd.ExcelFile('./fig_names.xlsx')

# Define chapters given by sheet names
chapters = xl.sheet_names

# %%

print('Updating Figures and Scripts')
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

print('Done!')

# %%

print('Updating latex files')
# Loop through chapters
for chap in chapters:
    print(f'chapter: {chap}')
    # Locate tex files
    tex_files = glob.glob(f'../doc/chapters/{chap}/*tex')
    # read figures
    figs = xl.parse(chap)
    # Loop through tex files
    for tex_file in tex_files:
        print('reading:')
        print(tex_file)
        # Read lines into memory
        with open(tex_file, 'r') as tex:
            lines = tex.readlines()
        # Loop through figures
        for f_idx, f in figs.iterrows():
            # Define figure name 
            f_name = f'{f.chapter:02d}_{f.section:02d}_' + \
                     f'{f.number:02d}_{f.fig_name}'
            # Define pattern
            pattern = re.compile("{(.*)" +
                                f"{chap}(.*){f.fig_name}" + 
                                "(.*)}")
            # Loop through lines
            for i, line in enumerate(lines):
                match = re.findall(pattern, line)
                if len(match) > 0:
                    print(f.fig_name)
                    print(f'Found on line {i+1}')
                    lines[i] = '  {../fig/' + \
                    f'{chap}/{f_name}{match[-1][-1]}' + '}\n'
                    print(lines[i])
        # and write everything back
        with open(tex_file, 'w') as tex:
            tex.writelines(lines)
# %%
