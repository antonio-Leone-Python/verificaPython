import numpy as np
import pandas as pd



# genero delle date
date = pd.date_range(start='1/1/2022', periods=30)
#genero vendite e ore lavorative
vendite = np.random.randint(0, 8, 30)
ore_lavorative = np.random.randint(4, 10, 30)
#genero un dataframe

dizionario={"data":date,
            "vendite":vendite,
            "ore_lavorative":ore_lavorative}


df=pd.DataFrame(dizionario)

print(df)


