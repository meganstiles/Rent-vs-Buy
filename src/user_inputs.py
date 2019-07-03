def getPurchasePrice(price):

    #Inputs: price of home you are buying

    #Returns price of home, removing symbols,commas, etc.

    price = price.replace(",", "")
    price = price.replace("$", "")
    price = int(price)
    return price

def getDownPayment(down_payment):

    #Inputs: amount of down_payment in dollars

    #Returns price of home, removing symbols,commas, etc.

    down_payment = down_payment.replace(",", "")
    down_payment = down_payment.replace("$", "")
    down_payment = int(down_payment)
    return down_payment

def getInterestRate(int_rate):

    #Inputs: interest rate of mortgage (format 5.5%)

    #Returns interest rate in decimal format

    int_rate = int_rate.replace("%", "")
    int_rate = float(int_rate)
    int_rate = int_rate/100
    return int_rate

def getTermLength(term_length):

    #Inputs: mortgage term length in years

    #Returns: term term_length

    term_length = int(term_length)
    return term_length
