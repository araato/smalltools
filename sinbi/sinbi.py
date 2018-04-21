
place = ['안방', '침대방', '서재', '놀이방']
ghost = ['벽수귀', '흑진귀', '팬텀토르소', '모주귀',\
        '이드라', '무면귀', '마리오네트 퀸', '치돈귀',\
        '환마귀', '키클라스', '호문쿨루스', '망부화',\
        '골묘귀', '어둑시니', '불가살이', '라바나브',
        '헤론', '객귀', '마고할망', '그슨새','지하국대적',\
        '림 샤이코스', '이안', '시온', '요하임',\
        '혈안귀', '살음귀', '벨라', '백의귀',\
        '인큐버스', '케르베로스', '만티코어', '시두스',\
        '슬렌더맨', '바알제붑', '손각시', '네비로스', \
        '장도한', '홍콩할매', '강시', '외눈우산',\
        '구미호', '팔척귀신', '발록', '장산범',\
	'망태할아버지', '조마구', '네코마타']

import random
import json
datafile = 'last.json'

lastData = None
try :
	f = open(datafile, 'r')
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

with open(datafile, 'w') as outfile:
    json.dump(lastData, outfile)

print('')
print('{}에 {}'.format(curPlace, curGhost))