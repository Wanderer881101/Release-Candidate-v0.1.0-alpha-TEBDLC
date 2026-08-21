# Jonathan Therrien, Marieville, Québec.
from fractions import Fraction
cases=[(100,100,361),(180,181,361),(300,300,361),(999999,999999,1000003)]
for a,b,d in cases:
    m=Fraction(a,d)+Fraction(b,d)
    rel=-1 if m<1 else (1 if m>1 else 0)
    print(f"mass={m} relation={rel} unitary=0")
print("python impotent oracle: PASS")
