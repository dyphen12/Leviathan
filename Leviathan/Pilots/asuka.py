#This is 'Asuka' the 'McNuts' model pilot from ouroboros

import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
import pandas as pd
from keras.models import load_model

from Angels.Armisael import fusion


print('"Asuka" the pilot for the EVA_Prototype3')

print('Loading model: EVA_Prototype3')

model = load_model(r'C:\Users\Usuario\Documents\GitHub\Leviathan\Leviathan\Fortune Tellers\Models\Eva_prototype3.h5')

print('model loaded')

print('Loading data from Angel: Sachiel')

(ArmisaeltrainX,ArmisaeltestX,AngelStatus) = fusion()

    while AngelStatus = True:
        





