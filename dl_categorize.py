import os
import shutil
import numpy as np
from PIL import Image
from skimage import data
from sklearn.cluster import KMeans

class Color:
    BLACK     = '\033[30m'
    RED       = '\033[31m'
    GREEN     = '\033[32m'
    YELLOW    = '\033[33m'
    BLUE      = '\033[34m'
    PURPLE    = '\033[35m'
    CYAN      = '\033[36m'
    WHITE     = '\033[37m'
    END       = '\033[0m'
    BOLD      = '\038[1m'
    UNDERLINE = '\033[4m'
    INVISIBLE = '\033[08m'
    REVERCE   = '\033[07m'

for path in os.listdir('dl_mineral_origin'):
    path_c = path.replace('.jpg','').replace('.png','').replace('.gif','').replace('.webp','').replace('.jpeg','')+'.jpg'
    os.system('mv dl_mineral_origin/'+path+' dl_mineral_origin/'+path_c)

x,y = 500,500
for path in os.listdir('dl_mineral_origin'):
    img = Image.open(f'dl_mineral_origin/{path}')
    img = img.convert('RGB')
    img_resize = img.resize((x, y))
    #path = path.replace('.jpg','').replace('.png','').replace('.gif','').replace('.webp','').replace('.jpeg','')
    #print(path)
    img_resize.save(f'dl_mineral_convert/{path}')
    print(Color.GREEN+'Resize'+Color.END+' : '+f'dl_mineral_origin/{path}'+' >- '+f'dl_mineral_convert/{path}'+f' ({x}*{y})')

#print([path for path in os.listdir('dl_mineral_convert')])
os.system('rm -rf dl_mineral_convert/.DS_Store')
feature = np.array([data.imread(f'dl_mineral_convert/'+path) for path in os.listdir('dl_mineral_convert')])
feature = feature.reshape(len(feature), -1).astype(np.float64)

print(Color.YELLOW+'--------------------------------------------------------------------'+Color.END)
print(Color.YELLOW+'|                             LEARNING                             |'+Color.END)
print(Color.YELLOW+'--------------------------------------------------------------------'+Color.END)
model = KMeans(n_clusters=15).fit(feature) #k-means
print(Color.BLUE+'--------------------------------------------------------------------'+Color.END)
print(Color.BLUE+'|                              FINISH                              |'+Color.END)
print(Color.BLUE+'--------------------------------------------------------------------'+Color.END)
labels = model.labels_

for label, path in zip(labels, os.listdir('dl_mineral_convert')):
    os.makedirs(f"dl_mineral_group/{label}", exist_ok=True)
    shutil.copyfile(f"dl_mineral_origin/{path}", f"dl_mineral_group/{label}/{path}")
    #print(Color.GREEN+str(label)+Color.END,' <- '+path)
    print(Color.GREEN+'Copy'+Color.END+' : '+f'dl_mineral_origin/{path}'+' >- '+f'dl_mineral_group/{label}/{path}')

print(Color.BLUE+'--------------------------------------------------------------------'+Color.END)
print(Color.BLUE+'|                           CATEGORIZED                            |'+Color.END)
print(Color.BLUE+'--------------------------------------------------------------------'+Color.END)
