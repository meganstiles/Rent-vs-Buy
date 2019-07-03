
def getPaymentPrinciple(payment_amount, principle_balance, interest_rate):

    '''
    Inputs:
    payment_amount = monthly mortgage payment
    principle_balance = remaining principle on loan
    interest_rate = interest rate on mortgage

    Returns
    Amount of payment applied to principle
    '''

    interest_payment = principle_balance * (interest_rate/12)
    principle_payment = payment_amount - interest_payment

    return principle_payment

def getInterestPayment (payment_amount, principle_balance, interest_rate):


    '''
    Inputs:
    payment_amount = monthly mortgage payment
    principle_balance = remaining principle on loan
    interest_rate = interest rate on mortgage

    Returns
    Amount of payment applied to interest
    '''

    interest_payment = principle_balance * (interest_rate/12)

    return interest_payment
