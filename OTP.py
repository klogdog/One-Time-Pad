""" One time pad example. not cryptographically secure."""
message = "this is an ultra secret message:"
# the random library allows for random integer generation
import random
a = []
c = []
d = []
f = []
g = []
j= 0
m = 0
eofFlag = 0
messageAndExtra = len(message) + 10000


#alphabetToNumber is a dictionary that translates letters in the alphabet to numbers
alphabetToNumber = {" " : 0, "a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26, ":" : 27}
#numberToAlphabet is a dictionary that translates numbers to a letter in the alphabet
numberToAlphabet = {0 : " ", 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z',27:':'}
#change the range to change the one time pad length


for i in range(0,messageAndExtra):
 randomthing = random.randint(0,27)
 a.append(randomthing)

print "one time pad"
print a

for i in message:
  c.append(alphabetToNumber[i])
  e = c[j] + a[j]
  if e > 28:
    e = e % 28
  d.append(e)
  j = j + 1

for i in range(len(message), messageAndExtra):
    d.append(a[i])

print "message to number"
print c
print"encrypted message"
print d

j = 0

for i in d:
  e = d[j] - a[j]
  if e < 0:
    e = e + 28
  f.append(e)
  j = j + 1

print "decrypted message"
print f


lengthF = len(f)
for i in range(lengthF):
    e = f[i]
    if e == 27:
        eofFlag = 1
    if eofFlag == 0:
     g.append(numberToAlphabet[e])

x = "".join(g)
print x
