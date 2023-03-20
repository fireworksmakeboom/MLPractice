import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

print(ord('H')) #ord() gives ascii no
# Python 3+ makes all strings Unicode


# now with urllib
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    print(line.decode().strip())
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)


# Getting HTML, can scrap/parse it with BeautifulSoup4
fhand2 = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand2:
    print(line.decode().strip())