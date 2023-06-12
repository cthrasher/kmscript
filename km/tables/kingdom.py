import numpy as np
import pandas as pd

kingdom_size = pd.DataFrame(
  [[ 1, 9, 'Territory', 'd4', 0, 4 ],
  [ 10, 24, 'Province', 'd6', 1, 8 ],
  [ 25, 49, 'State', 'd8', 2, 12 ],
  [ 50, 99, 'Country', 'd10', 3, 16 ],
  [ 100, np.nan, 'Dominion', 'd12', 4, 20 ]],
  columns=('Size_Low','Size_High','Type of Nation','Resource Die','Control DC Modifier','Commodity Storage')
)
