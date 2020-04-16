import math


def MSE(x, x_dash):
    N = len(x)
    sumVal = 0.0

    for i in range(N):
        tmpVal = (x[i] - x_dash[i])*(x[i] - x_dash[i])
        sumVal += tmpVal
        tmpVal = 0.0

    mseVal = float(sumVal) / float(N)
    return mseVal


def SNR(x, x_dash):
    N = len(x)

    numerator = 0.0
    for i in range(N):
        tmp = x[i]*x[i]
        numerator += tmp
        tmp = 0.0

    denominator = 0.0
    for i in range(N):
        tmp = (x[i] - x_dash[i])*(x[i] - x_dash[i])
        denominator += tmp
        tmp = 0.0

    if denominator == 0 or numerator == 0:
        return False, 0.0
    else:
        difference = math.log10(numerator) - math.log10(denominator)
        snrVal = 10 * difference
        return True, snrVal
    # if absFraction == 0.0:
    #     return False, 0.0
    # else:
    #     snrVal = 10 * math.log10(absFraction)
    #     return True, snrVal


def SNR2(x, x_dash):
    N = len(x)

    sum_input = 0.0
    sum_output = 0.0
    for i in range(N):
        sum_input += x[i]
        sum_output += x_dash[i]
    mean_input = float(sum_input) / float(N)
    mean_output = float(sum_output) / float(N)

    numerator_input = 0.0
    numerator_output = 0.0
    for i in range(N):
        tmpI = (x[i]-mean_input)*(x[i]-mean_input)
        tmpO = (x_dash[i]-mean_output)*(x_dash[i]-mean_output)
        numerator_input += tmpI
        numerator_output += tmpO
        tmpI = 0.0
        tmpO = 0.0

    varI = float(numerator_input) / float(N-1)
    varO = float(numerator_output) / float(N-1)

    if varI == 0 or varO == 0:
        return False, 0.0
    else:
        difference = math.log10(varI) - math.log10(varO)
        snrVal = 10 * difference
        return True, snrVal


def MD(x, x_dash):
    absDifference = []

    for i in range(len(x)):
        tmp = abs(x[i] - x_dash[i])
        absDifference.append(tmp)
        tmp = 0.0

    mdVal = max(absDifference)
    return mdVal
