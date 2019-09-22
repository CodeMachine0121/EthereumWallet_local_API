from web3.auto import w3
import sys
from mnemonic import *
import binascii
import subprocess
import os
from os import path
import json
import qrcode
#import qrcode.image.pil
from PIL import Image,ImageDraw,ImageFont
from eth_utils import decode_hex
from eth_keys import keys
import hashlib
from eth_account import Account
import random 
import string 
class wallet:
    # input password before start up the wallet 
    private = ""
    password = ''
   #開機第一要做            
    def __init__(self,password):#私鑰
        self.password = password
    

    def PrivateKey(self,password):
        self.password = password
        keyfile = open("/home/pi/EthereumWallet_local_API/wallet/keystore/"+os.listdir("/home/pi/EthereumWallet_local_API/wallet/keystore")[0])
        encrypted_key = eval(keyfile.read()) #Eval = stirng to dict
        try:
            self.private = w3.eth.account.decrypt(encrypted_key,self.password)
        except:
            return False
        self.private=w3.toHex(self.private)
        
        return True
        
    def PublicKey(self,privatekey):
        private_key_Bytes = decode_hex(privatekey)
        priv_key = keys.PrivateKey(private_key_Bytes)
        pub_key = priv_key.public_key
        return pub_key

    def Address(self):#位址
        return os.listdir("/home/pi/EthereumWallet_local_API/wallet/keystore")[0]
        
    #隨機生成 長度為8的亂數字串 作為Address 密碼
    def RandomString(self):
        salt = ''.join(random.sample(string.ascii_letters+string.digits, 8))
        return salt

    def newAccount(self):# 新增錢包 Only one times
        
        try:
            os.mkdir("/home/pi/EthereumWallet_local_API/wallet/keystore/")#創資料夾
        except:
            return False
        
        self.password = self.RandomString() #產生密碼
        Acc = Account.create(self.password)
        # make keyfile
        keyfile = str(w3.eth.account.privateKeyToAccount(Acc.privateKey).encrypt(self.password))
        print("new keyfile :"+keyfile)
        
        os.mknod("/home/pi/EthereumWallet_local_API/wallet/keystore/"+Acc.address)#創文件
        fp = open("/home/pi/EthereumWallet_local_API/wallet/keystore/"+Acc.address,'w')
        fp.write(str(keyfile))
        fp.close()
        self.private = Acc.privateKey.hex()
        return True

    # user input their password
    def Mnemonics(self):#轉24助憶詞
        data = binascii.unhexlify(self.private.split('x')[1])
        m = Mnemonic("english")
        return m.to_mnemonic(data)

    #get public key hash
    def Get_priv_hash(self):
        priv = str(self.PublicKey(self.private))
        hash = hashlib.sha256()
        hash.update(priv.encode('utf8'))
        return hash.hexdigest()


class makeTxn:
        import json
        from Wallet import wallet
        password = ''
        wt = wallet('')
        def __init__(self,password):
            self.password=password
            wt = wallet(self.password)
        
        def EtherTxn(self,to_Address ,value , nonce ,gasPrice,gas):#乙太幣交易
                if self.wt.PrivateKey(self.password):
                    privateKey = self.wt.private
                else:
                    return 'Password error'
                    
                address = w3.toChecksumAddress(self.wt.Address())
                try:
                    to_Address = w3.toChecksumAddress(to_Address)
                except:
                    return "Address error"
                value =int( value * 10**18)
                try: 
                    txn = {#gas * price + value really means MAXGas * price.
                    'from':address,
                    'to':to_Address,
                    'value':int(value),
                    'gas':int(gas),
                    'gasPrice':int(gasPrice),  # = gas*price+value
                    'nonce':int(nonce),
                    }
                    # 簽名 送tmp回去給手機
                    signed_txn = w3.eth.account.signTransaction(txn,private_key=privateKey)
                    tmp  =signed_txn.rawTransaction
                    print('type of tmp: ',type(tmp))
                    # 加密存下來
                    txhasg  = w3.toHex(w3.sha3(signed_txn.rawTransaction))
                except:
                    return "Value Error"
                return tmp.hex()

        def Token_Txn(self,to_addr,value,nonce):#Token交易
                ABI = json.loads('[{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"tokens","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"buy","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[],"name":"delContract","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"price","type":"uint256"}],"name":"setPrice","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"tokens","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"tokenOwner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"tokens","type":"uint256"}],"name":"Approval","type":"event"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowed","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balances","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"buyPrice","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"weiToEther","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]')
                Token = w3.eth.contract(
                    w3.toChecksumAddress('0xdaFc7DC630DD0974d6d034727cb94Af5A2287b60'),# deploy the contract /contractaddr
                    abi=ABI
                )
                to_addr = w3.toChecksumAddress(to_addr)
                privateKey = wt.PrivateKey()
                sender = w3.toChecksumAddress(wt.PublicKey())
                txn1 = {'gas':70000,'gasPrice':1,'nonce':int(nonce),'from':sender}
                txn2 = Token.functions.transfer(to_addr,int(value)).buildTransaction(txn1)
                signed_txn =  w3.eth.account.signTransaction(txn2,private_key=privateKey)
                tmp = signed_txn.rawTransaction
                return tmp






