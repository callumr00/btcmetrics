# Import modules

import time

from btcrpc import rpc
from blockchainInfo import getBlockHeight

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

import numpy  as np
import pandas as pd

from pathlib import Path
# --------------------------------------------------------------------------------------
# Start timer

startTime           = time.time()
# --------------------------------------------------------------------------------------
# Variables

# set max block height
maxHeight           = getBlockHeight()
# --------------------------------------------------------------------------------------
# Main
print('Block Length         :')

fileName = 'blockInfo.csv'
filePath = Path('data/' + fileName)

# load data frame
df = pd.read_csv(filePath)

# print stats
print('shortest block       : ' + str(df['Time'].diff().min()) + 's')
print('longest block        : ' + str(df['Time'].diff().max()) + 's')

# show data frame
print(df)
# --------------------------------------------------------------------------------------
# Save data
dfData = df[['Block Height', 'Time']]
dfData.to_csv('data/blockInfo Split/Block Time.csv', mode='w', index=False, header=True)

print(dfData)
# --------------------------------------------------------------------------------------
# Create chart

# variables
x = df['Block Height']
y = df['Time'].diff()

axcol = 'orange'

# functions
# replace 1000 with 1
def thousands (x, pos):
    return '%1.0f' % (x * 1e-3)

def minutes (x, pos):
    return '%1.0f' % (x / 60)

# general
fig, ax = plt.subplots()
plt.scatter(x,y, color = axcol, s = 1, alpha = 0.2)
plt.plot(df['Time'].diff().rolling(2016).mean(), color = 'k', alpha = 0.6, linewidth = 1)
plt.axhline(y = 600, color = 'k', linestyle='--')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.grid(True, which = 'major', axis = 'both', alpha = 0.4)
plt.title("Block Length ",pad = 30)

# x
ax.set_xlabel("Block Height (thousands)", labelpad = 20)
ax.xaxis.set_major_formatter(FuncFormatter(thousands))
plt.xticks(np.arange(0,maxHeight,step = 210000))
plt.xlim([0, maxHeight])

# # y
ax.set_ylabel('Time to Mine (minutes)', labelpad = 20)
ax.yaxis.set_major_formatter(FuncFormatter(minutes))
plt.yticks(np.arange(0,7201,step = 600))
plt.ylim([1,7200])
# --------------------------------------------------------------------------------------
# Stop timer

executionTime = (time.time() - startTime)
print()
print('Execution time: ' + str(round(executionTime,3)) + 's')
# --------------------------------------------------------------------------------------
# Show chart

plt.show()