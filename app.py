from flask import Flask,jsonify , request , make_response
from Wallet import  wallet
from Wallet import makeTxn
from paper import Epaper as ep
from web3.auto import w3
import os
from os import path

global wt,mk


app = Flask(__name__)
wt = wallet("")


status =  False


@app.route('/login',methods=['POST'])
def login():
    passwd = request.values['data'].split(',')[1]
    if not path.exists('/home/pi/EthereumWallet_local_API/wallet/keystore'):
        return make_response( jsonify({'response' :"Address not exists"}))
    if wt.PrivateKey(passwd):
        status = True
        return make_response( jsonify({'response' :'Login success'}))
    else:
        return make_response( jsonify({'response' :'Password error'}))

#按鈕 key1 觸控############
@app.route('/signup')
def signup():
    result = "no reaponse"
    if wt.newAccount():
        ep.privatekey(wt.Mnemonics(),wt.password)
        result = "Sign up Success"
    return make_response(jsonify({'response':result}),200)
###################

@app.route('/showPrivatekey')
def showPrivatekey():

    if not path.exists('/home/pi/EthereumWallet_local_API/wallet/keystore'):
        return make_response( jsonify({'response' :"Address not exists"}))
    
    ep.privatekey(wt.Mnemonics())
    return make_response( jsonify({'response':"successful"} ) ,200)
@app.route('/privatekey')
def PrivateKey():
    
    if not path.exists('/home/pi/EthereumWallet_local_API/wallet/keystore'):
        return make_response( jsonify({'response' :"Address not exists"}))
    return  make_response( jsonify({'response' : wt.Mnemonics() }) , 200)

@app.route('/showPublickey')
def showPublickey():
 
    if not path.exists('/home/pi/EthereumWallet_local_API/wallet/keystore'):
        return make_response( jsonify({'response' :"Address not exists"}))
    ep.publickey(str(wt.PublicKey(wt.private) ))
    return make_response( jsonify({'response':"successful"} ) ,200)

@app.route('/publickey')
def Publickey():
 
    if not path.exists('/home/pi/EthereumWallet_local_API/wallet/keystore'):
        return make_response( jsonify({'response' :"Address not exists"}))
    return make_response( jsonify({'response': str(wt.PublicKey(wt.private)) }),200)

@app.route('/showAddress')
def showAddress():
    if not path.exists('/home/pi/EthereumWallet_local_API/wallet/keystore'):
        return make_response( jsonify({'response' :"Address not exists"}))
    ep.address( str(wt.Address()))
    return make_response( jsonify({'response':"successful"} ) ,200)

@app.route('/address')
def Address():
    
    if not path.exists('/home/pi/EthereumWallet_local_API/wallet/keystore'):
        return make_response( jsonify({'response' :"Address not exists"}))
    return make_response( jsonify({'response' : str(wt.Address()) }) , 200)

@app.route('/setBalance',methods=['POST'])
def setBalance():
    bal = request.values['data'].split(',')[1]
    ep.setBalance("%.2f" %(float(bal)))
    return make_response(jsonify({'response':'successful'}))

@app.route('/yourBalance',methods=['POST'])
def yourBalance():
    bal = request.values['data'].split(',')[1].strip('\b').strip(" ")
    ep.yourBalance("%.2f" %(float(bal)))
    return make_response(jsonify({'response':'successful'}))

@app.route('/ethertxn',methods=['POST']) #password,to_Address ,value , nonce ,gasPrice,gas
def Ethertxn():
    
    if not path.exists('/home/pi/EthereumWallet_local_API/wallet/keystore'):
        return make_response( jsonify({'response' :"Address not exists"}))
    
    data = request.values['data'].split(',')
    print(data)
    nonce = int(data[3].split("\b")[0])
    password = data[0]
    mk = makeTxn(password)
    print('mktxn: ',mk.password)
    if not w3.isAddress(data[1]):
        return make_response(jsonify({'response':"Address Error"}))
   
    try:
        tmp = mk.EtherTxn(data[1],float(data[2]), nonce ,int(data[4]),int(data[5]))
    #tmp = hex(int.from_bytes(tmp,byteorder='big'))
    except:
        return make_response(jsonify({'response':"Value Error"}))
    return make_response( jsonify({'response' : str(tmp)}), 200)

@app.route('/priv_hash')
def Get_Priv_hash():
    if not path.exists('/home/pi/EthereumWallet_local_API/wallet/keystore'):
        return make_response( jsonify({'response' :"Address not exists"}))
    priv_hash = wt.Get_priv_hash()
    return make_response(jsonify({'response':str(priv_hash)}) ,200)


app.run(host='127.0.0.1', port=6000,debug=True)







