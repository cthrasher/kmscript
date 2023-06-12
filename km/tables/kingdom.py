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

kingdom_advancement = pd.DataFrame(
  [[ 1, 14 ],
  [ 2, 15 ],
  [ 3, 16 ],
  [ 4, 18 ],
  [ 5, 20 ],
  [ 6, 22 ],
  [ 7, 23 ],
  [ 8, 24 ],
  [ 9, 26 ],
  [ 10, 27 ],
  [ 11, 28 ],
  [ 12, 30 ],
  [ 13, 31 ],
  [ 14, 32 ],
  [ 15, 34 ],
  [ 16, 35 ],
  [ 17, 36 ],
  [ 18, 38 ],
  [ 19, 39 ],
  [ 20, 40 ]],
  columns=('Level','Control DC')
)
