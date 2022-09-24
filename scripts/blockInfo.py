# Import modules
import time

from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

from btcrpc import rpc
from blockchainInfo import getBlockHeight

import numpy  as np
import pandas as pd

from pathlib import Path

import os
# --------------------------------------------------------------------------------------
# Start timer

startTime           = time.time()
# --------------------------------------------------------------------------------------
# Variables

# set max block height
maxHeight           = getBlockHeight()

blockHeight         = np.arange(0,maxHeight,step = 1)
# --------------------------------------------------------------------------------------
# Functions

def getBlockInfo(minHeight):
    item = minHeight

    time            = []
    medianTime      = []
    difficulty      = []
    chainwork       = []
    nTx             = []
    strippedSize    = []
    size            = []
    weight          = []

    # create block height to do list
    blockHeightTDL = np.arange(minHeight,maxHeight,step = 1)

    print('> ' + str(len(blockHeightTDL)) + ' blocks required; getting data...')

    # get data from blocks in to do list
    for item in list(blockHeightTDL):

        blockHash = rpc.getblockhash(int(list(blockHeight)[item]))
        blockInfo = rpc.getblock(blockHash)

        blockTime = blockInfo['time']
        time.append(blockTime)

        blockMedianTime = blockInfo['mediantime']
        medianTime.append(blockMedianTime)

        blockDifficulty = blockInfo['difficulty']
        difficulty.append(blockDifficulty)

        blockChainwork = blockInfo['chainwork']
        chainwork.append(blockChainwork)

        blockNTx = blockInfo['nTx']
        nTx.append(blockNTx)

        blockStrippedSize = blockInfo['strippedsize']
        strippedSize.append(blockStrippedSize)

        blockSize = blockInfo['size']
        size.append(blockSize)

        blockWeight = blockInfo['weight']
        weight.append(blockWeight)

    print('> complete')
    print()

    # combine lists into data frame
    df = pd.DataFrame(
        {
            'Block Height'  : blockHeightTDL,
            'Time'          : time,
            'Median Time'   : medianTime,
            'Difficulty'    : difficulty,
            'Chainwork'     : chainwork,
            'nTx'           : nTx,
            'Stripped Size' : strippedSize,
            'Size'          : size,
            'Weight'        : weight
        }
    )

    # export data frame to csv
    if os.path.getsize(filePath) == 0:
        df.to_csv(filePath, mode='w', index=False, header=True)
    else:
        df.to_csv(filePath, mode='a', index=False, header=False)
# --------------------------------------------------------------------------------------
# Main
print('Block Info           :') 

fileName = 'blockInfo.csv'
filePath = Path('data/' + fileName)

# create csv
if not filePath.is_file():
    print('> ' + fileName + ' not found; creating file...')
    open(filePath, 'x')
    print('> file created')
    getBlockInfo(0)
else:
    # check if up to date
    if len(blockHeight) == pd.read_csv(filePath).shape[0]:
        print('> up to date')
        print()
    else:
        # update
        print('> outdated; updating...')
        getBlockInfo(pd.read_csv(filePath).shape[0])

# load data frame
df = pd.read_csv(filePath)
df.set_index('Block Height', inplace=True, drop=True)
print(df)
# --------------------------------------------------------------------------------------
# Stop timer

executionTime = (time.time() - startTime)
print()
print('Execution time: ' + str(round(executionTime,3)) + 's')