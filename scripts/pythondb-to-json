import os
import json

dirs_trad = os.listdir("ChineseSimplified")
dirs_simp = os.listdir("ChineseTraditional")
dirs_en = os.listdir("English")

dirs = list(set(dirs_trad) & set(dirs_simp) & set(dirs_en))

dirs.sort()


tlist = []
for dirname in dirs:
    files = os.listdir(f'English/{dirname}')
    files.sort()
    
    for filename in files:
        trios = [
            f'{lang}/{dirname}/{filename}' 
            for lang 
            in ["ChineseSimplified", "ChineseTraditional", "English"]
        ]
        tlist.append(trios)
    


translations = []
errors = []
for triofilepath in tlist:
    trio = []
    for filepath in triofilepath:
        with open(file=filepath, mode='r') as file:
            content = json.load(file)
            try:
                trio.append(content['name'])
            except:
                errors.append(filepath)
                
    translations.append(trio)

    
outputdict = {}
for simplified, traditional, english in translations:
    outputdict[simplified] = english
    outputdict[traditional] = english

output = []
for x in outputdict:
    tempdict = {'en':outputdict[x], 'zhCN':x}
    output.append(tempdict)
    

with open(file='output.json', mode='w') as file:
    json.dump(output, file, ensure_ascii=False)
