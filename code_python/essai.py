def knapSack(totalWeight, objects):

    currentWeight = 0

    subSet = []

    for counter in range(len(objects)):

        if (currentWeight + objects[counter][-1]) <= totalWeight:
            currentWeight += objects[counter][-1]
            subSet.append(objects[counter])

        return subSet


b=[[1, 20, 2], [1, 20, 4], [1, 30, 1], [1, 100, 8]]
a=sorted(b, key=lambda bb: bb[2]/bb[1])
print(a)