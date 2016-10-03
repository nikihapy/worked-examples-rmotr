def return_float(minutes):
    result = minutes * 100 / 60
    rounded_result = "{0:.1f}".format(result)
    return float(rounded_result)
