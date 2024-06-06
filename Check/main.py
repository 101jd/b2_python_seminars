import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

values = list(set(data['whoAmI']))
print(values)
nf = pd.DataFrame({
    values[0]:[1 if el == values[0] else 0 for el in lst],
    values[1]:[1 if el == values[1] else 0 for el in lst]
    })

print(nf)