import numpy as np
import math
import statistics

def generate_list(mu, sigma):
    s = np.random.normal(mu, sigma, 100)
    s = list(s)
    s.sort()

    removes = []

    for i in range(len(s)):
        if s[i] < 0 or s[i] > 100:
            removes.append(i)
            
    removes.reverse()
    for i in removes:
        s.pop(i)
    return s
    
def get_best(percentList):
    winners = []
    for i in range(len(percentList)-2):
        for j in range(i+1,len(percentList)-1):
            for k in range(j+1,len(percentList)):
                iwins = i / 100
                jwins = (1-(i/100))*(j/100)
                kwins = (1-(i/100))*(1-(j/100))*(k/100)
                if iwins >= jwins and iwins >= kwins:
                    winners.append(i)
                if jwins >= iwins and jwins >= kwins:
                    winners.append(j)
                if kwins >= jwins and kwins >= iwins:
                    winners.append(k)
    return winners
    
winners = []

for i in range(101):
    mu = i
    print(i)
    for j in range(31):
        sigma = j
        s = generate_list(mu, sigma)
        best = get_best(s)
        for k in best:
            winners.append(k)
    print("Winners length: " + str(len(winners)))
        
mean = sum(winners) / float(len(winners))
print("Mean: " + str(mean))
mode = statistics.mode(winners)
print("Mode: " + str(mode))