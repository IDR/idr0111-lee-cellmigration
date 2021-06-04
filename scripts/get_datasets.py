import csv

"""
Print out the dataset to which an image file belongs.
In the same order as it appears in the filePaths.tsv
"""

filepaths = open("../experimentA/idr0111-experimentA-filePaths.tsv", 'r').readlines()
for filepath in filepaths:
  tmp = filepath.split("/")
  filename = tmp[len(tmp)-1].strip()
  dataset = None
  annos = csv.DictReader(open("../experimentA/idr0111-experimentA-annotation.csv"))
  for anno in annos:
    tmp = anno["Image File"].split("/")
    anno_filename = tmp[len(tmp)-1].strip()
    if anno_filename == filename:
      if dataset == None:
        dataset = anno["Dataset Name"]
      else:
        print("Image file name not unique!")
        dataset = None
        break
  if dataset is not None:
    print(f"Dataset:name:{dataset}")
  else:
    print(f"{filename} not found!")
