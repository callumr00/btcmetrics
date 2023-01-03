import os
from pathlib import Path

from ChartSettings import ( 
                            FormatThousands,
                            FormatMillions,
                            FormatMinutes,
                            ChartBlockTimeToMine,
                            ChartBlockSize,
                            ChartBlockWeight,
                            ChartBlockDifficulty,
                            ChartTxPerBlock,
                            ChartTxTotal,
                            ChartIssuanceSchedule,
                            ChartSupplyInflation,
                            ChartBlockAvgTxFee,
                            ChartBlockSumTxFees,
                            ChartBlockSumTxFeesPctCoinbase,
                            ChartBlockCoinbase,
                            )

project = os.path.basename(os.path.dirname(os.path.dirname(__file__)))
script, _ = os.path.splitext(os.path.basename(__file__))
print('\n', f'{project} | {script}'.center(os.get_terminal_size().columns, ' '))

# Print chart options
print('''
    [1] Block Time\n
    [2] Block Size\n
    [3] Block Weight\n
    [4] Block Difficulty\n
    [5] Tx Per Block\n
    [6] Tx Total\n
    [7] Issuance Schedule\n
    [8] Supply Inflation\n
    [9] Average Tx Fee\n
    [10] Total Tx Fees\n
    [11] Tx Fees as a % of Coinbase\n
    [12] Block Coinbase\n
    ''')

def SelectChart():
    '''Show chart based on user input option'''
    
    chart = str(input(f'Select Chart: '))

    if chart == "1":
        ChartBlockTimeToMine()
    elif chart == "2":
        ChartBlockSize()
    elif chart == "3":
        ChartBlockWeight()
    elif chart == "4":
        ChartBlockDifficulty()
    elif chart == "5":
        ChartTxPerBlock()
    elif chart == "6":
        ChartTxTotal()
    elif chart == "7":
        ChartIssuanceSchedule()
    elif chart == "8":
        ChartSupplyInflation()
    elif chart == "9":
        ChartBlockAvgTxFee()
    elif chart == "10":
        ChartBlockSumTxFees()
    elif chart == "11":
        ChartBlockSumTxFeesPctCoinbase()
    elif chart == "12":
        ChartBlockCoinbase()
    else: 
        print(f'\n"{chart}" is not a valid input.\nE.g. "3" for Block Weight.\n')
        SelectChart()

SelectChart()