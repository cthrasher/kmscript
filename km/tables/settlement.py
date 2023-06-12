import numpy as np
import pandas as pd

settlement_types = pd.DataFrame(
  [[ 'Village', 1, 1, 2, 0, 400, 1, 1, 1, 0],
  [ 'Town', 3, 2, 5, 401, 2000, 2, 2, 1, 1],
  [ 'City', 9, 5, 10, 2001, 25000, 5, 4, 2, 2 ],
  [ 'Metropolis', 15, 10, np.nan, 25001, np.nan, 10, 6, 3, 3 ]],
  columns=('Settlement','Size_Low','Size_High','Population_Low','Population_High','Level','Consumption','Max Bonus','Influence')
)
