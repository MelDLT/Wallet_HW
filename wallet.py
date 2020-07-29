from constants import *
from dotenv import load_dotenv
import os
from web3 import Web3
import subprocess
import json

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
private_key = os.getenv("PRIVATE_KEY")



load_dotenv()
mnemonic = os.getenv('MNEMONIC', 'insert mnemonic here')

def derive_wallets(coin):
    command = './derive -g --mnemonic{mnemonic} --coin{coin} --numdrive=3 --fromat = json'
 
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell =True)
    (output, err) = p.communicate()
    p_status = p.wait()
    return print(output)

class coins:
        def __init__(self, ETH, BTCTEST):
            self.ETH = derive_wallets(ETH)
            self.BTCTEST = derive_wallets(BTCTEST)
