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

# number of halvings displayed
global maxHalvingShown
maxHalvingShown         = 14
maxHalving              = 33

global blocksPerHalving
blocksPerHalving        = 210000
global maxCoins
maxCoins                = 21000000

currentHeight           = getBlockHeight()
blockHeight             = np.arange(0,(maxHalvingShown * blocksPerHalving) + 1,step = 1)
# --------------------------------------------------------------------------------------
# Functions
def getInflation():
    print('> getting data...')
    blockReward         = 50
    blocksPerYear       = 52560

    existingCoins       = 0
    localHeight         = 0
    halvingHeight       = 0
    halving             = 0

    coins               = []
    inflation           = []

    # data data for specified blocks
    while localHeight          <= (maxHalvingShown * blocksPerHalving):
        # every n blocks, enact halving
        if halvingHeight       == blocksPerHalving:
            halvingHeight      = 0
            halving            = halving + 1
            blockReward        = blockReward / 2

        existingCoins          = existingCoins + blockReward
        inflationRate          = (blockReward * blocksPerYear) / existingCoins
        halvingHeight          = halvingHeight + 1
        localHeight            = localHeight + 1

        coins.append(existingCoins)
        inflation.append(round(inflationRate,6))
    
    print('> complete')
    print('> writing data...')

    # combine lists into data frame
    df = pd.DataFrame(
        {
            'Block Height'     : blockHeight,
            'Existing Coins'   : coins,
            'Inflation Rate'   : inflation,
        }
    )

    # export data frame to csv
    df.to_csv(filePath, mode='w', index=False, header=True)

    print('> complete')
    print()
# --------------------------------------------------------------------------------------
# Main
print('Inflation            :') 

fileName = 'inflation.csv'
filePath = Path('data/' + fileName)

# create csv
if not filePath.is_file():
    print('> ' + fileName + ' not found; creating file...')
    open(filePath, 'x')
    print('> file created')
    getInflation()

# load data frame
df = pd.read_csv(filePath)

# print stats
print('max coins            : ' + str(maxCoins))
print('existing coins       : ' + str(df.iloc[currentHeight]['Existing Coins']))
print('inflation rate       : ' + str(round(df.iloc[currentHeight]['Inflation Rate'] * 100,4)) + '%')
print('remaining inflation  : ' + str(round(((maxCoins / df.iloc[currentHeight]['Existing Coins']) - 1) * 100,4)) + '%')
print()  

# show data frame
print(df.head(maxHalvingShown * blocksPerHalving))
# --------------------------------------------------------------------------------------
# Chart
# variables
x = np.linspace(0,(maxHalvingShown * blocksPerHalving)+1,(maxHalvingShown * blocksPerHalving)+1)
y1 = df['Existing Coins']
y2 = df['Inflation Rate'] * 100

ax1col = 'black'
ax2col = 'orange'

# functions
# replace 1000000 with 1
def millions (x, pos):
    return '%1.0f' % (x * 1e-6)

# replace 1000 with 1
def thousands (x, pos):
    return '%1.0f' % (x * 1e-3)

# create chart
fig, ax1 = plt.subplots()

# x
ax1.set_xlabel("Block Height (thousands)", labelpad = 20)
ax1.xaxis.set_major_formatter(FuncFormatter(thousands))
plt.xlim([0, (maxHalvingShown * blocksPerHalving)])
plt.xticks(np.arange(0,(maxHalvingShown * blocksPerHalving),step = blocksPerHalving))

# y1
ax1.set_ylabel('Existing Coins (millions)', color = ax1col, labelpad = 20)
ax1.plot(x, y1, color = ax1col)
ax1.tick_params(axis = 'y', labelcolor = ax1col, color = 'white')
ax1.yaxis.set_major_formatter(FuncFormatter(millions))
plt.ylim([0, maxCoins])
plt.yticks(np.arange(0, maxCoins + 1,step = maxCoins / 7))
plt.grid(True, which = 'major', axis = 'both', alpha = 0.4)

# y2
ax2 = ax1.twinx()

ax2.set_ylabel('% Inflation Rate', color = ax2col, labelpad = 20)
ax2.plot(x, y2, color = ax2col)
ax2.tick_params(axis = 'y', labelcolor = ax2col, color = 'white')
plt.ylim([0.0001, 1000])
plt.yscale('log')
plt.minorticks_off()

# hide spines
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

# set title
plt.title("Bitcoin Supply Inflation",pad = 30)

# set line at current block height
plt.axvline(x = currentHeight, color = ax1col, linestyle='--')
# --------------------------------------------------------------------------------------
# Stop timer

executionTime = (time.time() - startTime)
print()
print('Execution time: ' + str(round(executionTime,3)) + 's')
# --------------------------------------------------------------------------------------
# Show chart

plt.show()