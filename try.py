import base64
with open('8.txt') as fh:
	c=fh.read()

c_array=[ i.decode('hex') for i in c.splitlines()];

#ciphertext = [bytes.fromhex(line.strip()) for line in open('8.txt')]
size=16
count=0;
for i in c_array:
	count+=1;
	chunks=[ i[j:j+size] for j in range(0,len(i),size)]
	if((len(chunks) - len(set(chunks))) != 0):
		print count
#line no 133 have repeated chunks