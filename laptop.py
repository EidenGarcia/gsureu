import socket
import cv2
import pickle
import struct
from flask import Flask, render_template, Response

# create flask app
app = Flask(__name__)


def gen():
    # socket to receive data packets
    laptop_socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    laptop_ip = '192.168.86.20'
    laptop_port = 9985
    laptop_socket2.bind((laptop_ip, laptop_port))
    laptop_socket2.listen(5)

    # create socket to connect to jetbot to send start message
    jetbot_ip = '192.168.86.37'
    jetbot_port = 9976

    laptop_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    laptop_socket.connect((jetbot_ip, jetbot_port))
    # pickle message and send
    incoming = 'mission in progress'
    a = pickle.dumps(incoming)
    message = struct.pack("Q", len(a))+a
    laptop_socket.sendall(message)
    print('message sent')

    data = b""
    payload_size = struct.calcsize("Q")
    # unwraps data packet sent from bot
    while True:
        incoming_socket, incoming_address = laptop_socket2.accept()
        if incoming_socket:
            while True:
                while len(data) < payload_size:
                    packet = incoming_socket.recv(12*1024)  # 4K
                    if not packet:
                        break
                    data += packet
                packed_msg_size = data[:payload_size]
                data = data[payload_size:]
                msg_size = struct.unpack("Q", packed_msg_size)[0]

                while len(data) < msg_size:
                    data += incoming_socket.recv(12*1024)
                incoming_data = data[:msg_size]
                data = data[msg_size:]
                incoming = pickle.loads(incoming_data)

                # print data packet
                print("time: ", incoming['time'])
                print("object: ", incoming['object'])
                print("current_forward: ", incoming['current_forward'])
                print("hint: ", incoming['hint'])
                # hard coded for now - just for testing purposes
                #incoming['hint'] = 'east'
                # convert frame data to jpeg to display on browser
                frame = incoming['frame']
                (flag, encodedImage) = cv2.imencode(".jpg", frame)
                yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
                      bytearray(encodedImage) + b'\r\n')

                # sending hint to bot is valid hint is received
                # if len(incoming['hint'])> 0:
                a = pickle.dumps(incoming)
                message = struct.pack("Q", len(a))+a
                laptop_socket.sendall(message)
                print('hint data sent')
                list = incoming['object']
                if 'teddy bear' in list:
                    break
            break
    # closing socket connections
    laptop_socket2.close()
    laptop_socket.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)
