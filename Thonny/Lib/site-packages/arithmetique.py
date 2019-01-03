
def pgcd(a,b):
    """Renvoie le Plus Grand Diviseur Communs  des entiers ``a`` et ``b``.
    
    Arguments:
        a (int) : un nombre entier
        b (int) : un nombre entier
    """
    if a<0 or b<0:
        return pgcd(abs(a),abs(b))
    if b==0:
        if a==0:
            raise DivisionByZeroError("Le PGCD de deux nombres nuls n'existe pas")
        else:
            return a
    else:
        return pgcd(b,a%b)

def reste(a,b):
    """Renvoie le reste de la division de ``a`` par ``b``.

    Arguments:
        a (int): Un nombre entier.
        b (int): Un nombre entier non nul.
    """
    r=a%b
    if r<0 : r=r+abs(b)
    return r

def quotient(a,b):
    """Le quotient de la division de ``a`` par ``b``.

    Arguments:
        a (int): Un nombre entier.
        b (int): Un nombre entier non nul.
    """
    return a//b
