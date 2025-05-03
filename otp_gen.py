import secrets 

def getOtp(length=6):
    """ DESCRIPTION: function to generate random otp code
    arg: length -> length of the otp(default:6)
    how it works:
    first generates numbers using secrets.randbelow() that's below 10. then stringfy the list of numbers and the make a string with them
    """
    return "".join(str(secrets.randbelow(10)) for _ in range(length))
    
print(getOtp(8))