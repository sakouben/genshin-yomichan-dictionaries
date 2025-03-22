import json
import uuid
import shutil
import os
from dragonmapper import hanzi
from langconv.converter import LanguageConverter
from langconv.language.zh import zh_tw
from datetime import date 

def dict_compile(path, 
                 title=str(uuid.uuid4()), 
                 url=str(uuid.uuid4()), 
                 description=str(uuid.uuid4()), 
                 attribution=str(uuid.uuid4()),
                 output_path=None
                 ):
  with open(path, "r") as file:
    gi_json = json.load(file)

  gi_out = []
  for x in gi_json:
    try:
      zhcn = x['zhCN']
    except:
      continue

    if "/" in zhcn:
      for y in zhcn.split("/"):
        gi_out.append(
            [y.strip(), hanzi.to_pinyin(y), "", "", 0, [x["en"]], 0, ""]
        )

    gi_out.append(
        [zhcn, hanzi.to_pinyin(zhcn), "", "", 0, [x["en"]], 0, ""]
    )

    try:
      for variant in x["variants"]["zhCN"]:
          gi_out.append(
              [variant, hanzi.to_pinyin(variant), "", "", 0, [x["en"]], 0, ""]
          )
    except:
        pass


  tempfolder = "temp-" + str(uuid.uuid4()) + "/"

  os.mkdir(tempfolder[:-1])

  with open(f"{tempfolder}term_bank_1.json", "w") as file:
    file.write(json.dumps(gi_out, ensure_ascii=False))


  index = f"""
            {{
            "title": "{title}",
            "format": 3,
            "revision": "{date.today()}",
            "sequenced": true,
            "url": "{url}",
            "description": "{description}",
            "attribution": "{attribution}"
            }}
          """
          
  with open(f"{tempfolder}index.json", "w") as file:
    file.write(index)

  if output_path == None:
    shutil.make_archive(f'GenshinDict-{str(uuid.uuid4())}', format='zip', root_dir=tempfolder[:-1])
  else:
    shutil.make_archive(output_path, format='zip', root_dir=tempfolder[:-1])
    
  shutil.rmtree(tempfolder[:-1])


