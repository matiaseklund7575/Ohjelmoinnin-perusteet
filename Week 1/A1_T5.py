print("Calculate the area of a wall.")
feed = input("Enter the width in meters: ")
Width = int(feed)

feed = input("Enter the height in meters: ")
Height = int(feed)

print("Width is", Width, "m and height is", Height, "m.")
Area = Width*Height
print("The wall will be", Area, "square meters.")

#int(feed) ei anna laittaa desimaaleja. float() taas sallii tämän.