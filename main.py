import random
import np

def gradientDescent(eta, xVal, yVal):
    calculatedValues = []
    xSubT = xVal - eta * (-4 + 4(xVal))
    ySubT = yVal - eta * (24 + 6(yVal))
    calculatedValues.append(xSubT)
    calculatedValues.append(ySubT)
    return calculatedValues

    def main():
        # rates for each trial
        eta = [.1, .01, .001]



        # initialize random inputs.
        #  iterate through each trial.
        for rate in eta:
            # calculated based on partial derivates
            bestX = 1
            bestY = -4
            for i in range(10):
                # generate a random starting point
                xValue = random.randint(-10, 10)
                yValue = random.randint(-10, 10)

                for i in range(500):
                    xYDeltas = gradientDescent(rate, xValue, yValue)
                    xValue = xYDeltas[0]
                    yValue = xYDeltas[1]

    #              plug them back in and determine best performance.




    # perform GD 500 times


main()
