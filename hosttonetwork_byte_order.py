import socket
def convert_integer():
    data=1234 #32-bit
    print("Original: %s => Long Host Byte Order: %s, Network Byte Order: %s" %(data, socket.ntohl(data), socket.htonl(data)))
    print("Original: %s => Short Host Byte Order: %s, Network Byte Order: %s" %(data, socket.ntohs(data), socket.htons(data)))

if __name__== '__main__':
	convert_integer()
    