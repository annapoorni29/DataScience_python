import urllib.request, urllib.parse, urllib.error
x = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
print(type(x))
hist={}
for line in x:
    words=line.decode().split()
    for word in words:
        hist[word]=hist.get(word, 0) + 1
print(hist)