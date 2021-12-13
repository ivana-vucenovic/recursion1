# Write a recursive function that given a number returns the sum of integers from 1 to that number. Example: rSigma(5) = 15 (1+2+3+4+5); rSigma(2.5) = 3 (1+2); rSigma(-1) = 0.

def rSigma(startImput):
    if startImput < 1:
        return 0
    return startImput + rSigma(startImput - 1)

print(rSigma(5))

# Given num, return the product of ints from 1 up to num. If less than zero, treat as zero. If not an integer, truncate. Experts tell us 0! is 1. rFact(3) = 6 (1*2*3). Also, rFact(6.5) = 720 (1*2*3*4*5*6).

def rFact(startImput):
    if startImput > 0:
        return int(startImput) * rFact(int(startImput - 1))
    return 1

print(rFact(4.9))

#  Flood fill

def floodFill(canvas2D,startXY,newColor,column, row):
    if startXY == 3:
        startXY == newColor
        print(startXY)
        return canvas2D


canvas2D = [
    [3,2,3,4,3],
    [2,3,3,4,0],
    [7,3,3,5,3],
    [6,5,3,4,1],
    [1,2,3,3,]]

startXY = [2,2]

newColor = 1

print(floodFill(canvas2D = [
    [3,2,3,4,3],
    [2,3,3,4,0],
    [7,3,3,5,3],
    [6,5,3,4,1],
    [1,2,3,3,]]
, startXY = [2,2], newColor = 1))