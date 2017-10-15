from flask import Flask
from flask import request

app = Flask(__name__ ,static_url_path='')

@app.route('/', methods=['GET'])
def index():
    #return '<h1>aaaa</h1>'
    return app.send_static_file('index.html')
  
        
@app.route('/read_data', methods=['GET'])
def read_data():
    return '''<h1>Home</h1>'''


import json
import serial
import serial.tools.list_ports

global ser

@app.route('/get_coms', methods=['GET'])
def get_coms():
    port_list = list(serial.tools.list_ports.comports())
    d = {"port": ""}
    s = []
    for v in port_list:
    	s.append(v[0])
    d["port"] = s
    return json.dumps(d)
    
@app.route('/get_bauds', methods=['GET'])
def get_bauds():
    ser = serial.Serial(request.args.get("port"))
    coms = {"bauds": (9600)}
    coms['bauds'] = ser.BAUDRATES
    return json.dumps(coms)

@app.route('/set_baud', methods=['POST'])
def set_bauds():
    if ser.isOpen():
        print("close serial port")
        ser.close()
    baud = int(request.form.get("baud"))
    ser.baudrate= baud
    ser.open()
    print("open serier port baud=%" %baud)
    return ""


@app.route('/get_data', methods=['GET'])
def get_data():
    while not dq.empty()
        return ""
    for 









if __name__ == '__main__':
    app.run()
