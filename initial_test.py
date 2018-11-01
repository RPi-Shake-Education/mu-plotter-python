import socket as s
host = ""
port = 8889
sock = s.socket(s.AF_INET, s.SOCK_DGRAM )
sock.bind((host, port))
print("Waiting for data on Port:", port)
while 1:                                # loop forever
    data, addr = sock.recvfrom(1024) # wait to receive data
    pack = data.decode('UTF-8').strip("'{}").split(', ')
    if "EHZ" in pack[0]:
        for x in pack:
            if x != "EHZ'" and float(x) < 100000 :
                print((float(x),0,0)) # zeroes in tuple added because Mu needs a Tuple!
