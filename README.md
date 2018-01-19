

```python
import sqlite3
br_db = sqlite3.connect('bitrate_db')

cursor = br_db.cursor()
# cursor.execute('CREATE TABLE bitrate(Velocity INTEGER, Angle INTEGER, Result TEXT, MSE INTEGER )')
# br_db.commit()


```


```python
import random
import pandas as pd

angle_list = [random.randint(1, 90) for k in range(9999)]
velocity_list = [random.uniform(0, 1) for k in range(9999)]
moo=pd.DataFrame({'Angles' : angle_list,'Velocity' : velocity_list,}, columns=['Angles','Velocity', 'Result','MSE'])
                  

moo.to_sql("Kikoken", br_db, if_exists="append")

br_db.commit()
br_db.close()
```


```python
moo.head(10)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Angles</th>
      <th>Velocity</th>
      <th>Result</th>
      <th>MSE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>41</td>
      <td>0.759689</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>18</td>
      <td>0.241323</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>64</td>
      <td>0.200562</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>0.126473</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>32</td>
      <td>0.445323</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>12</td>
      <td>0.617033</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>78</td>
      <td>0.089850</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>0.407637</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>53</td>
      <td>0.214619</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>75</td>
      <td>0.069660</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
