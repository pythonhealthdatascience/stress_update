import pandas as pd
import numpy as np

csv_file_path = 'PY_STRESS.csv'

df = pd.read_csv(csv_file_path, index_col='No')

df.info('Journal')

