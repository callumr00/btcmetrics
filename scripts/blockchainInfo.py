# Import modules
import time

import math

from btcrpc import rpc
# --------------------------------------------------------------------------------------
# Functions
def getBlockHeight():
    blockchainInfo              = rpc.getblockchaininfo()
    blockHeight                 = blockchainInfo['blocks']
    print('Block Height         : ' + str(blockHeight))
    return blockHeight
# getBlockHeight()

def getBlockDifficulty():
    blockchainInfo              = rpc.getblockchaininfo()
    blockDifficulty             = blockchainInfo['difficulty']
    print('Block Difficulty     : ' + str(blockDifficulty))
    return blockDifficulty
# getBlockDifficulty()

def getSize():
    blockchainInfo              = rpc.getblockchaininfo()
    size                        = blockchainInfo['size_on_disk']
    print('Block Size           : ' + str(round(size/(1024**3),2)) + ' GB')
    return size
# getSize()

def getHalvingCount():
    blocksPerHalving            = 210000
    blockHeight                 = getBlockHeight()
    halvingCount                = blockHeight / blocksPerHalving
    print('Halving Count        : ' + str(math.floor(halvingCount)))
    return math.floor(halvingCount)
# getHalvingCount()

def getHalvingProgress():
    blocksPerHalving            = 210000
    blockHeight                 = getBlockHeight()
    halvingProgress             = ((blockHeight % blocksPerHalving) / blocksPerHalving) * 100
    print('Halving Progress     : ' + str(round(halvingProgress,4)) + '%')
    return halvingProgress
# getHalvingProgress()

# def getNetworkHashesPS():
    # networkHashes = rpc.getnetworkhashps()
#     print('Network Hashes/s         : ' + str(networkHashes))
#     return getNetworkHashesPS
# getNetworkHashesPS()

def getMaxCoins():
    maxcoins = 0
    for i in range(0,33):
        maxcoins = maxcoins + (round(50/2**i,8)*210000)
        print('halving : '+str(i))
        print('subsidy : '+str(f'{50/2**i:.8f}'))
        print('maxcoins: '+str(maxcoins))
        print()
# getMaxCoins()