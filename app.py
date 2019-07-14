from flask import Flask,jsonify , request , make_response
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
        return make_response( jsonify({'response' : str(wt.PublicKey())}) , 200)
    else: #401 Unauthorized
        return make_response( jsonify({'error':'something wrong'}) , 401)

@app.route('/privatekey')
def PrivateKey():
    ep.privatekey(wt.Mnemonics())

    return  make_response( jsonify({'response' : wt.Mnemonics() }) , 200)
    

@app.route('/publickey')
def Publickey():
    ep.publickey()
    return make_response( jsonify({'response' : str(wt.PublicKey())}) , 200)

@app.route('/ethertxn',methods=['POST']) #to_Address ,value , nonce ,gasPrice,gas
def Ethertxn():
    data = request.values['data'].split(',')
    print(data)
    tmp = mk.EtherTxn(data[0],int(data[1]), int(data[2]),int(data[3]),int(data[4]))
    tmp =  hex(int.from_bytes(tmp,byteorder='big'))
    return make_response( jsonify({'response' : str(tmp)}), 200)
    
app.run(host='127.0.0.1', port=5000,debug=True)
