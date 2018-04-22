import random
import json

inputDataFile = 'data.json'
lastDataFile = 'last.json'

with open(inputDataFile, 'r', encoding='utf-8') as inf :
	inputData = json.load(inf)
place = inputData['place']
ghost = inputData['ghost']

lastData = None
try :
	f = open(lastDataFile, 'r')
	lastData = json.load(f)
except:
	lastData = {}
	lastData['place'] = random.choice(place)
	lastData['ghost'] = []
	for i in range(0, 5) :
		lastData['ghost'].append(random.choice(ghost))

lastBonus = 0.5

delta = lastBonus / len(ghost)
weight = [1.0+i*delta for i in range(0, len(ghost))]
wsum = sum(weight)

def chooseIndex() :
	r = random.random() * wsum
	ws = 1.0
	i = 0
	while ws < r :
		i += 1
		ws += weight[i]
	return i

def chooseGhost() :
	return ghost[chooseIndex()]

curPlace = random.choice(place)
while curPlace == lastData['place'] :
	curPlace = random.choice(place)

curGhost = chooseGhost()
while curGhost in lastData['ghost'] :
	curGhost = chooseGhost()

lastData['place'] = curPlace
lastData['ghost'] = lastData['ghost'][1:5]
lastData['ghost'].append(curGhost)

with open(lastDataFile, 'w') as outfile:
    json.dump(lastData, outfile)

print('')
print('{}에 {}'.format(curPlace, curGhost))