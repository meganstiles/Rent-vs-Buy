
def getPaymentAmount(term_length, interest_rate, purchase_price, down_payment):

    '''
    Inputs:
    term_length = length of mortgage in years
    interest_rate = mortgage interest rate
    purchase_price = final purchase price of home
    down_payment = amount of down payment in dollars

    Returns:
    monthy mortgage payment amount
    '''

    #Amount of original loan amount
    principal = purchase_price - down_payment

    #Montlhy interest amount (assumes interest compounded monthly)
    monthly_interest = (interest_rate/12)

    #Total Number of payments over the entire term length
    n_payments = int(term_length * 12)

    #Amount for each payment
    payment = principal * ((monthly_interest*(1 + monthly_interest)**n_payments))/(((1+ monthly_interest)**n_payments) - 1)

    return payment
