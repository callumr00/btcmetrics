# Import modules
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from btcrpc import rpc
from blockchainInfo import getBlockHeight

import numpy  as np
import pandas as pd

from pathlib import Path
from tqdm import tqdm

# Get the current block height
maxHeight           = getBlockHeight()

# Get the block reward for each block until current block height
def blockreward(height):
    halvings = 0
    blockrewards = []

    print('\n> getting block rewards...')

    for i in tqdm(range(height)):
        blockreward = 50/2**halvings
        blockrewards.append(blockreward)
        if i >= 210000 and i % 210000 == 0: halvings +=1

    return(blockrewards)

# Get the value of the coinbase transaction for each block until current block height
def coinbase(height):
    coinbases = []

    print('\n> getting coinbase transactions...\n')

    for i in tqdm(range(height)):
        if i == 0: continue
        blockHash = rpc.getblockhash(i)
        blockInfo = rpc.getblock(blockHash)
        coinbase  = blockInfo['tx'][0]
        encodedtx = rpc.getrawtransaction(coinbase)
        decodedtx = rpc.decoderawtransaction(encodedtx)
        coinbases.append(float(decodedtx['vout'][0]['value']))

    coinbases.insert(0, "null")
    return(coinbases)

# Save data to a data frame
df = pd.DataFrame(
    {
        'Block Height'  : np.arange(0,maxHeight,step = 1),
        'Block Reward'  : blockreward(maxHeight),
        'Coinbase'      : coinbase(maxHeight)
    }
)

print(df)

# Save data to a .csv file
fileName = 'coinbase.csv'
filePath = Path('data/' + fileName)

print('\n>writing data...')
df.to_csv(filePath, mode='w', index=False, header=True)
print('\n>complete\n')