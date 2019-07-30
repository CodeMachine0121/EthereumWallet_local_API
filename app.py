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
        return make_response( jsonify({'response' : str(wt.Address())}) , 200)
    else: #401 Unauthorized
        return make_response( jsonify({'error':'something wrong'}) , 401)


@app.route('/showPrivatekey')
def showPrivatekey():
    ep.privatekey()
    return make_response( jsonify({'response':"successful"} ) ,200)
@app.route('/privatekey')
def PrivateKey():
    return  make_response( jsonify({'response' : wt.Mnemonics() }) , 200)

@app.route('/showPublickey')
def showPublickey():
    ep.publickey()
    return make_response( jsonify({'response':"successful"} ) ,200)
@app.route('/publickey')
def Publickey():
    return make_response( jsonify({'response': str(wt.PublicKey()) }),200)

@app.route('/showAddress')
def showAddress():
    ep.address()
    return make_response( jsonify({'response':"successful"} ) ,200)
@app.route('/address')
def Address():
    return make_response( jsonify({'response' : str(wt.Address())}) , 200)

@app.route('/ethertxn',methods=['POST']) #to_Address ,value , nonce ,gasPrice,gas
def Ethertxn():
    data = request.values['data'].split(',')
    print(data)
    tmp = mk.EtherTxn(data[0],int(data[1]), int(data[2]),int(data[3]),int(data[4]))
    tmp =  hex(int.from_bytes(tmp,byteorder='big'))
    return make_response( jsonify({'response' : str(tmp)}), 200)

@app.route('/priv_hash')
def Get_Priv_hash():
    priv_hash = wt.Get_priv_hash()
    return make_response(jsonify({'response':str(priv_hash)}) ,200)
app.run(host='127.0.0.1', port=5000,debug=True)
