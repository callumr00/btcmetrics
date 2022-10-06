# Import modules

import time

from btcrpc import rpc
from blockchainInfo import getBlockHeight
from blockchainInfo import getBlockDifficulty

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

print('Difficulty           :')

fileName = 'coinbase.csv'
filePath = Path('data/' + fileName)

fileName2 = 'blockInfo.csv'
filePath2 = Path('data/' + fileName2)

# load data frame
df = pd.read_csv(filePath)
df2 = pd.read_csv(filePath2)

# print stats
print('adjustment change    :')

# Show data frame
print(df)
# --------------------------------------------------------------------------------------
# Save data
# dfData = df[['Block Height', 'Difficulty']]
# dfData.to_csv('data/blockInfo Split/Block Difficulty.csv', mode='w', index=False, header=True)

# print(dfData)
# --------------------------------------------------------------------------------------
# Create chart

# variables
x = df['Block Height']
# y = df['Coinbase'] # coinbase
# y = (df['Coinbase'] - df['Block Reward']) / df2['nTx'] # avg tx fee
y = df['Coinbase'] - df['Block Reward'] # total tx fees
# y = 1 - (df['Block Reward'] - df['Coinbase']) # % tx fees


axcol = 'orange'

# functions
# replace 1000 with 1
def thousands (x, pos):
    return '%1.0f' % (x * 1e-3)

# general
fig, ax = plt.subplots()
plt.scatter(x,y, color = axcol, s = 1, alpha = 0.2)
# plt.plot(df['Coinbase'].rolling(2016).mean(), color = 'k', alpha = 0.6, linewidth = 1)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.grid(True, which = 'major', axis = 'both', alpha = 0.4)
plt.title("Difficulty Per Block",pad = 30)

# x
ax.set_xlabel("Block Height (thousands)", labelpad = 20)
ax.xaxis.set_major_formatter(FuncFormatter(thousands))
plt.xticks(np.arange(0,maxHeight,step = 210000))
plt.xlim([0, maxHeight])

# y
ax.set_ylabel('Difficulty', labelpad = 20)
# plt.ylim([1, 10**14])
plt.yscale('log')
# --------------------------------------------------------------------------------------
# Stop timer

executionTime = (time.time() - startTime)
print()
print('Execution time: ' + str(round(executionTime,3)) + 's')
# --------------------------------------------------------------------------------------
# Show chart

plt.show()