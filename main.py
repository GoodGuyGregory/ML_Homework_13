import random


def gradientDescent(eta, xVal, yVal):
    calculatedValues = []
    xSubT = xVal - eta * (-4 + (4 * (xVal)))
    ySubT = yVal - eta * (24 + (6 * (yVal)))
    calculatedValues.append(xSubT)
    calculatedValues.append(ySubT)
    return calculatedValues

def determinePerformance(xVal, yVal):
    performanceMetric = {}
    xValBest = (-4 + (4 * (xVal)))
    yValBest = 24 + (6 * (yVal))
    performanceMetric[xVal] = round(xValBest,4)
    performanceMetric[yVal] = round(yValBest,4)
#   returns trial values for xVal, yVal
    return performanceMetric



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
            trialList.append(determinePerformance(xValue, yValue))
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
