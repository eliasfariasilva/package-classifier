def classifier(width, height, length, mass):
    
    # Getting info
    volume = height * length * width    
    bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    heavy = mass >= 20
    
    #Geting result
    if bulky and heavy:
        result = "REJECTED"   
    elif bulky or heavy:
        result = "SPECIAL"
    else:
        result = "STANDARD"

    return result