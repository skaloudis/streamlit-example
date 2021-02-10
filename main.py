import pandas as pd
import numpy as np
import plotly.graph_objects as go


df = pd.read_excel('corn.xlsx', index_col=0)
#print (df.head())
#
arr = df.to_numpy()
data = arr.reshape(30, 12) 

rows = data.shape[0]
cols = data.shape[1]

data_new = np.copy(data)
for x in range(0, rows):
    for y in range(0, cols):
        data_new[x,y] = data[x,y] - data[x,0]
        #print(x,y,data[x,y],data_new[x,y])

month_avg = np.average(data_new, axis=0)
print(month_avg)

x = np.arange(12)
fig = go.Figure(data=go.Scatter(x=x, y=month_avg))
fig.show()

