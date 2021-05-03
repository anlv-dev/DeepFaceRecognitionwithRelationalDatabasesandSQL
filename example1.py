import os
import pandas as pd
from deepface.commons import functions

from deepface import DeepFace

model = DeepFace.build_model('Facenet')
facial_img_paths = []

for root,directory, files in os.walk('dataset'):
    for file in files:
        if '.jpg' in file:
            facial_img_paths.append(root + '/' + file )


# proecess : detect and aling for each file

instance = []
for i in pd.tqdm(range(0, len(facial_img_paths))):
    facial_img_path = facial_img_paths[i]

