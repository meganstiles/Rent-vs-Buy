
def getPropertyTaxes(house_value, tax_rate):

    taxes = (house_value * tax_rate)/12

    return taxes

def getPropertyValue(purchase_price, appreciation_rate, num_payments):

    num_years = num_payments //12

    extra_months = num_payments % 12

    property_value = purchase_price * (1 + appreciation_rate)** num_years

    if extra_months == 0:

        property_value = property_value

    else:

        extra_value = purchase_price * (1+ appreciation_rate) ** extra_months/12

    return property_value
