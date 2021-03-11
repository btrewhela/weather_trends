import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn


df_global = pd.read_csv('extract_global_data.csv', sep=',',  index_col = 'year')
df_stgo = pd.read_csv('extract_santiago.csv', sep=',',  index_col = 'year')

df_stgo['Category'] = df_stgo.city + ", " + df_stgo.country
df_global['Category'] = 'Global'

del df_stgo['city']
del df_stgo['country']

### Moving averages calculations https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rolling.html

ma_window = 10

df_global['MA_10'] = df_global.rolling(window=ma_window).mean()
df_stgo['MA_10'] = df_stgo.rolling(window=ma_window).mean()

df_global = df_global.iloc[ma_window-1:]
df_stgo = df_stgo.iloc[ma_window-1:]

seaborn.set_style("whitegrid")
(fig, ax) = plt.subplots(1, 1, figsize = (40,20))

x = df_global.index
y_global = df_global['MA_10']
y_stgo = df_stgo['MA_10']

ax.plot(np.arange(len(x)), y_global, color='blue', label = 'Global', linewidth=5.0)
ax.plot(np.arange(len(x)), y_stgo, color='red', label = 'Santiago, Chile', linewidth=5.0)

x_values = list(df_global.index)

for i in np.arange(len(x_values)):
	if x_values[i] == 1864:
		x_values[i] = '1864'
	elif x_values[i] == 1900:
		x_values[i] = '1900'
	elif x_values[i] == 1950:
		x_values[i] = '1950'
	elif x_values[i] == 2000:
		x_values[i] = '2000'
	elif x_values[i] == 2013:
		x_values[i] = '2013'
	else:
		x_values[i] = ''

plt.xticks(range(len(x_values)), x_values, rotation=0, ha='center', fontsize=30, weight = 'bold')
plt.xlabel('\n' + 'Year', weight = 'bold', size = 40)
plt.ylabel("10-Year Moving Average Yearly Temperature [°C]" + '\n', fontsize=40, fontdict=dict(weight='bold'))
ax.yaxis.set_tick_params(labelsize=30)
plt.legend(prop={'size': 30, 'weight':'bold'})
plt.yticks(weight = 'bold')
plt.savefig('figure_temp.png')
exit()