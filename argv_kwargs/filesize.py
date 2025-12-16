import os

def filesize(*args):
    sizes = []
    
    for file in args:
        if os.path.isfile(file):
            size_bytes = os.path.getsize(file)
            size_kb = size_bytes / 1024
            sizes.append(size_kb)
        else:
            print(f"The file '{file}' doesn't exist.")
    if sizes:
        avrg_size = sum(sizes) / len(sizes)
        print(f"Avg size: {avrg_size:.2f} KB")
filesize("args.py","kwargs.py","hgdvgsdv.txt")