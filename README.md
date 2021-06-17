# TRISTAN-hesp

Reading data from Tristan on Hesperides in xlsx files.

## IMPORTANT!

To read output.json file, use the `convert_axes` *kwarg*:
```python
import pandas as pd
data_frame = pd.read_json("./hesp_rafaelhermida_2019/TristanHespData.json", convert_axes=False)
```
to read data correctly, since the index column has the format `DOYHHMMSS` where
- `DOY`: Day Of the Year
- `HH`: Hours
- `MM`: Minutes
- `SS`: Seconds
is not the expected format for `read_json` method

#### Notes:

Military timezone codes [here](https://en.wikipedia.org/wiki/List_of_military_time_zones)
