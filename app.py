from flask import Flask,jsonify , request
from Wallet import  *
from paper import Epaper as ep


wt = wallet()
mk = makeTxn()
app = Flask(__name__)

@app.route('/test')
def test():
    return jsonify("hello")

@app.route('/wallet',methods = ['POST'])
def newAccount():
    passwd =  request.values['data']

    if wt.newAccount(passwd):
        return 'Successfully'
    else:
        return 'fail'

@app.route('/privatekey')
def PrivateKey():
    ep.privatekey(wt.Mnemonics())

    return  wt.Mnemonics()

@app.route('/publickey')
def Publickey():
    ep.publickey()
    return wt.PublicKey()

@app.route('/ethertxn',methods=['POST']) #to_Address ,value , nonce ,gasPrice,gas
def Ethertxn():
    data = request.values['data'].split(',')
    print(data)
    tmp = mk.EtherTxn(data[0],int(data[1]), int(data[2]),int(data[3]),int(data[4]))
    tmp =  hex(int.from_bytes(tmp,byteorder='big'))
    return str(tmp)

app.run(host='127.0.0.1', port=5000,debug=True)
