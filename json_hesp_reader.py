import pandas as pd
import numpy as np

data_frame = pd.read_json("./hesp_rafaelhermida_2019/TristanHespData.json", convert_axes=False)

# TODO: Interpolar a datos 10 minutales.
#  - Primero se añaden los valores nuevos a los índices
#  - Luego se interpolan los valores con pd.interpolate()



