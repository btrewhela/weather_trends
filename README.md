# Weather Trends: Santiago Case
In this project, I analyze local and global yearly average temperature data and compare Santiago (Chile) temprature trends to overall global temperature trends.

## Installation Instructions
In order to use this code, you will need to install the following Python Libraries:
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
```
In addition, you will have to download the two datasets *"extract_global_data.csv"* and *"extract_santiago.csv"*.

These datasets contains global yearly average temperatures and Santiago's yearly average temperatures respectively.

## Considerations and Limitations

1. The code calculates moving averages with a window of 10 years. This can be modified in the *ma_window* variable.

2. Null values are treated during the data gathering process. In this case, both datasets contain the same years.

3. The plot *x_ticks* is calculated for this particular time series and is not generalized.
