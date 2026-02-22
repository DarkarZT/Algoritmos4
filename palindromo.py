def esPalindromo(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:        return esPalindromo(s[1:-1])
    
prueba = esPalindromo("narran")

print(prueba)