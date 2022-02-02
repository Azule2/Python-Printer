def Print(Number, Howmanyprint):
    Check = 1
    for plus in range(Howmanyprint):
        Check = Check * Number
    return Check


print('Print successful: ', Print(3, 5))
