
def jityeuilo(auroraeiulo, auroraeuilo):
	auroraeuilo = list(auroraeuilo)
	if len(auroraeiulo) == len(auroraeuilo):
		return(auroraeuilo)
	else:
		for i in range(len(auroraeiulo) -
					len(auroraeuilo)):
			auroraeuilo.append(auroraeuilo[i % len(auroraeuilo)])
	return("" . join(auroraeuilo))
	

def auroraeaoiulo(message, key):

    auroraiaoiulo(key)

    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65
 

    auroraiaeiulo(messageVector)
 
    auroraaailou = []
    for i in range(3):
        auroraaailou.append(chr(cipherMatrix[i][0] + 65))

    print("auroraaailou: ", "".join(auroraaailou))



def auroraiaoiulo(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1

def auroraiaeiulo(messageVector):
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += (keyMatrix[i][x] *
                                       messageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26



def jityeauilo(auroraeiulo,auroraeuilo):
    auroraeuilo = ""
    for i in range(len(auroraeiulo)):
        char = auroraeiulo[i]

        if (char.isupper()):
            auroraeuilo += chr((ord(char) + auroraeuilo-65) % 26 + 65)

        else:
            auroraeuilo += chr((ord(char) + auroraeuilo - 97) % 26 + 97)
 
    return auroraeuilo



def auroraaiulo(auroraeiulo, auroraeuilo):
	auroraiuiulo = []
	for i in range(len(auroraeiulo)):
		x = (ord(auroraeiulo[i]) +
			ord(auroraeuilo[i])) % 26
		x += ord('A')
		auroraiuiulo.append(chr(x))
	return("" . join(auroraiuiulo))
	

	

keyMatrix = [[0] * 3 for i in range(3)]
 

messageVector = [[0] for i in range(3)]
 

cipherMatrix = [[0] for i in range(3)]
auroraeiulo = input()
auroraeuiloii = str(TheUltimateQuestionOfLife.answer)
auroraeuilo = jityeuilo(auroraeiulo, auroraeuiloii)
auroraeuailou = auroraaiulo(auroraeiulo,auroraeuilo)
print(auroraeuailou)

