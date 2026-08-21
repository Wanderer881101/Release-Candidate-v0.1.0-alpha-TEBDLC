# Jonathan Therrien, Marieville, Québec.
from fractions import Fraction
import json

def evaluate():
    origin_mass = Fraction(300,361)+Fraction(300,361)
    origin = {"unit":"U1","context":"C-origin","mass":str(origin_mass),"integrability":False,"unitary":False}
    call = {"unit":"U2","context":"C-call-new","integrability":False,"unitary":False}
    rejected = all((True,True,False,True))
    if rejected:
        call["integrability"] = True
        call["unitary"] = True
    return {"origin":origin,"call":call,"origin_preserved":origin["unitary"] is False and origin["integrability"] is False}

if __name__ == '__main__':
    print(json.dumps(evaluate(),sort_keys=True,separators=(',',':')))
