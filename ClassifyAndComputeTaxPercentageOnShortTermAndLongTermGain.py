from DateDifferenceLibrary import compareDates
from DateDifferenceLibrary import dateDifferenceInMonths

def classifyShortTermAndLongTermGain(mutualFundCountryType, mutualFundAssetClassType, purchaseDate, sellDate):
    debtCutOffDate = "01-04-2023"
    dateDifference = dateDifferenceInMonths(purchaseDate , sellDate)
    if(mutualFundCountryType == "Domestic" and mutualFundAssetClassType == "Debt"):
        if(compareDates(purchaseDate, debtCutOffDate)):
            if(dateDifference <= 24):
                return "short-term"
            else:
                return "long-term"
        else:
            return "short-term"
    elif (mutualFundCountryType == "Domestic" and mutualFundAssetClassType == "Equity"):
        if(dateDifference <= 12):
            return "short-term"
        else:
            return "long-term"
    elif (mutualFundCountryType == "International" and mutualFundAssetClassType == "Fund of fund"):
        if(dateDifference <= 24):
            return "short-term"
        else:
            return "long-term"
    else:
#   Don't have rules for another type
        return "short-term"


def computeTaxPercentage(mutualFundCountryType, mutualFundAssetClassType, capitalGainType, slabRate, purchaseDate, sellDate):
    debtCutOffDate = "01-04-2023"
    dateDifference = dateDifferenceInMonths(purchaseDate, sellDate)
    if(mutualFundCountryType == "Domestic" and mutualFundAssetClassType == "Debt"):
        if(compareDates(purchaseDate, debtCutOffDate)):
            if(capitalGainType == "short-term"):
                return slabRate
            else:
                if(dateDifference > 36):
                    return 20
                else:
                    return 12.5
        else:
            if(capitalGainType == "short-term"):
                return slabRate
            else:
                return slabRate
    elif(mutualFundCountryType == "Domestic" and mutualFundAssetClassType == "Equity"):
        if(capitalGainType == "short-term"):
            return 20
        else:
            return 12.5
    elif(mutualFundCountryType == "International" and mutualFundAssetClassType == "Fund of fund"):
        if(capitalGainType == "short-term"):
            return slabRate
        else:
            if(dateDifference > 36):
                return slabRate
            else:
                return 12.5
    else:
        # Rules for other type are not added yet.
        return 12.5