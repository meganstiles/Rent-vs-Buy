
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

def getTotalPrincipleInterest(payment_amount, principle_balance, interest_rate, num_payments):

    total_principle = 0
    total_interest = 0

    for i in range (0, num_payments):

        principle = get_payment_principle(payment_amount, principle_balance, interest_rate)

        interest = get_interest_payment(payment_amount, principle_balance, interest_rate)

        total_principle = total_principle + principle

        total_interest = total_interest + interest

        principle_balance = principle_balance - principle

    return total_principle, total_interest
