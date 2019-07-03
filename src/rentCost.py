
def getTotalRent( starting_rent, annual_increase_rate, num_payments):

    rent_total = 0
    monthly_rent = starting_rent
    extra_months = num_payments % 12

    for i in range (0, num_payments //12):
        yearly_rent = monthly_rent * 12
        new_rent = monthly_rent * (1 + (annual_increase_rate /100))
        rent_total = yearly_rent + rent_total
        monthly_rent = new_rent

    if extra_months == 0:
        total = rent_total / num_payments
    else:
        extra_rent = monthly_rent * extra_months
        rent_total = rent_total + extra_rent
        total = rent_total / num_payments

    return total
