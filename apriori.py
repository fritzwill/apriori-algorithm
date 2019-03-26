
def createCandidateSet(data):
	cand = []
	for row in data:
		for itm in row:
			if [itm] not in cand:
				cand.append([itm])
	cand.sort()
	return list(map(frozenset,cand))

def scanData(data, candidateSet, minSupport):
	subsetCount = {}
	for curSet in data:
		for cand in candidateSet:
			if cand.issubset(curSet):
				if not cand in subsetCount:
					subsetCount[cand] = 1
				else:
					subsetCount[cand] += 1
	n = float(len(data))
	valid = []
	for key in subsetCount:
		sup = subsetCount[key]
		if sup >= minSupport:
			valid.insert(0,key)
	return valid, subsetCount

def genApriori(freqSets, k):
	valid = []
	nFreqSets = len(freqSets)
	for i in range(nFreqSets):
		for j in range(i+1, nFreqSets):
			lstCands1 = list(freqSets[i])[:k-2]
			lstCands2 = list(freqSets[j])[:k-2]
			lstCands1.sort()
			lstCands2.sort()
			# if first k-2 elements are equal
			if lstCands1 == lstCands2:
				valid.append(freqSets[i]|freqSets[j]) # union 
	return valid

def apriori(data, minSupport):
	candSet = createCandidateSet(data)
	setData = list(map(set,data))
	lstCands, subsetCounts = scanData(setData,candSet,minSupport)
	lstCands = [lstCands]
	k = 2
	while(len(lstCands[k-2]) > 0):
		candSetX = genApriori(lstCands[k-2],k)
		lstCandsX, subsetCountsX = scanData(setData,candSetX, minSupport)
		subsetCounts.update(subsetCountsX)
		lstCands.append(candSetX)
		k += 1
	return lstCands, subsetCounts

# read in data
data = []
dataSetFilename = 'Dataset-apriori.txt'
with open(dataSetFilename,'r') as file:
	for line in file:
		data.append(line.strip().split(','))


print("What min. support do you want to use? ")
minSupp = raw_input()
minSupp = int(minSupp)

print("\n**** Apriori with minSupport = {} ****".format(minSupp))

# call apriori
sets, counts = apriori(data,minSupp)
print("\nSets:\n")
for x in sets:
	for y in x:
		print(y)

print("\nCounts:\n")
for k,v in counts.items():
	print(k, v)
