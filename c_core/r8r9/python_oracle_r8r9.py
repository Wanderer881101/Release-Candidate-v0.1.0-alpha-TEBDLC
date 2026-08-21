# Jonathan Therrien, Marieville, Québec.
from fractions import Fraction
import json

DEPTHS = [1,2,10,100,1000]

def main():
    out=[]
    for d in DEPTHS:
        f=Fraction(3,10) ** d
        out.append({
            "depth": d,
            "numerator_bits": f.numerator.bit_length(),
            "denominator_bits": f.denominator.bit_length(),
            "positive": f > 0,
            "below_one": f < 1,
        })
    n=4294967295; den=4294967297
    cap=Fraction(n,den)*Fraction(n,den)
    result={
        "depths": out,
        "capacity_vector": {
            "numerator": str(cap.numerator),
            "denominator": str(cap.denominator),
            "numerator_bits": cap.numerator.bit_length(),
            "denominator_bits": cap.denominator.bit_length(),
        },
        "hybrid_expected_transition_depth": 20,
        "final_depth_1000": {
            "numerator_bits": (3**1000).bit_length(),
            "denominator_bits": (10**1000).bit_length(),
        }
    }
    print(json.dumps(result, sort_keys=True, separators=(",",":")))

if __name__ == "__main__":
    main()
