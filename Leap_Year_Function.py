def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

test_data = [1900, 2000, 2016, 1987, 2021]
test_result = [False, True, True, False, True]
for i in range(len(test_data)):
    yr = test_data[i]
    print (yr, "->",end="")
    result = is_year_leap (yr)
    if result == test_result[i]:
        print("ok")
    else:
        print("Failed")