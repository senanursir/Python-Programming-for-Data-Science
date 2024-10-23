# JOIN

import pandas as pd
import numpy as np
m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99

pd.concat([df1, df2])    # merged(with indexes.)

# indexes also need to be updated:
pd.concat([df1, df2], ignore_index=True)


df1 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering','hr']})

df2 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                   'start_date': [2010, 2009, 2014,2019]})

pd.merge(df1, df2)   # merged by according to employees.

pd.merge(df1, df2, on="employees")


# we want to reach to every employees' manager.
df3 = pd.merge(df1, df2)

df4 = pd.DataFrame({'group': ['accounting', 'engineering', 'hr'],
                    'manager': ['Caner', 'Mustafa', 'Berkcan']})
#
pd.merge(df3, df4)
