import random


def gradientDescent(eta, xVal, yVal):
    calculatedValues = []
    xSubT = xVal - eta * (-4 + (4 * (xVal)))
    ySubT = yVal - eta * (24 + (6 * (yVal)))
    calculatedValues.append(xSubT)
    calculatedValues.append(ySubT)
    return calculatedValues

def determinePerformanceForMinimum(xVal, yVal):
    performanceMetric = {}
    xValBest = (-4 + (4 * (xVal)))
    yValBest = 24 + (6 * (yVal))
    performanceMetric[xVal] = round(xValBest,4)
    performanceMetric[yVal] = round(yValBest,4)
#   returns trial values for xVal, yVal
    return performanceMetric

def determineGlobalPerformance(xVal, yVal):
    return 52 - (4 * xVal) + (2 * (xVal ** 2)) + (24 * yVal) + (3 * (yVal**2))



def main():
    # rates for each trial
    eta = [.1, .01, .001]

    # create dictionary for corresponding trails and values of x and y for performance metrics
    etaTrials = {}

    # build the initial
    for etaRates in eta:
        # initialize an empty list for performance metrics per the 10 trails
        etaTrials[etaRates] = []

    # initialize random inputs.
    #  iterate through each trial.
    for rate in eta:
        # calculated based on partial derivates
        # trials list
        trialList = []
        for i in range(10):
            # generate a random starting point
            xValue = random.randint(-10, 10)
            yValue = random.randint(-10, 10)

            for i in range(500):
                xYDeltas = gradientDescent(rate, xValue, yValue)
                xValue = xYDeltas[0]
                yValue = xYDeltas[1]

        # plug them back in and determine the best performance.
            trialList.append(determinePerformanceForMinimum(xValue, yValue))
        # determine the best performaning trial and record the results in the dictionary.
        etaTrials[rate].append(trialList)

    #  print each trial for analysis:
    for k,v in etaTrials.items():
        print('Eta:' + str(k))
        print("======================================")
        print("Trial Results:")
        for trial in range(len(v)):
            print(v)

    # append the best one to the list of etaTrails map.

    # perform GD 500 times



main()

def evaluate():
    eta = [.1, .01, .001]
    for i in range(len(eta)):
        # find and supply the best value:
        print("supply the best trial results for " + str(eta[i]))
        print("==============================================")
        xVal = input("provide best X: ")
        yVal = input("provide best Y: ")
        print("Performance to Global min of 2")
        print(determineGlobalPerformance(float(xVal), float(yVal)))


evaluate()


# Comments the higher the eta value the results were able to be closer and more refined to an approximate minimum as each trial
# was executed. first time time around each of the trials ranged the smaller the eta the more unpredictable the resulting minumim value.
# the program runs and produces key value pairs for x and y <x: <minum with respect to its derivative> and <y: <with respect to it's derivative>
# to see the results of the best performance execute the code and supply the best x and y keys based on their values with respect their global mins



