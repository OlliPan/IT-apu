import socket                   

            
port = 60000                    # portin varaus


def laheta():
    s = socket.socket() 
    s.connect(("192.168.1.106", port))
    while True:
     
        filename="vika.txt"
        f = open(filename,"rb")
        l = f.read(1024)
        while (l):
           s.send(l)
           #print("Sent ",repr(l))
           l = f.read(1024)

        f.close()
        #print('Successfully get the file')
        s.close()
        #print('connection closed')
