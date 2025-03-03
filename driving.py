age = 20
has_driving_license = True
licence_country = "EE"

if age >= 18 and has_driving_license and (licence_country in ["LV", "CA", "EE", "LT"]):
    print("You can drive a car")
else:
    print("You can not drive a car")
