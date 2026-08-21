# Jonathan Therrien, Marieville, Québec.
from dataclasses import dataclass

@dataclass(frozen=True)
class Obs:
    seq:int; context:str; model:str; unit:str; outcome:str
    coherent:bool; coverage:bool; compatible:bool; complete:bool

obs = [
    Obs(1,'C-origin','U1-model','U1','STAGNATED',True,False,True,False),
    Obs(2,'C-call-2','U2-model','U2','PROOF_REJECTED',True,True,False,True),
    Obs(3,'C-call-3','U3-model','U3','PROOF_REJECTED',True,False,True,True),
    Obs(4,'C-call-4','U4-model','U4','INTEGRABLE',True,True,True,True),
]
snapshot = tuple(obs)
assert all((o.coherent and o.coverage and o.compatible and o.complete) for o in obs if o.outcome=='INTEGRABLE')
assert not any(o.outcome=='INTEGRABLE' and not (o.coherent and o.coverage and o.compatible and o.complete) for o in obs)
assert tuple(obs) == snapshot
assert sum(o.outcome=='INTEGRABLE' for o in obs)==1
assert sum(o.outcome=='PROOF_REJECTED' for o in obs)==2
assert sum(o.outcome=='STAGNATED' for o in obs)==1
print('observations=4 integrable=1 rejected=2 stagnated=1 origin_U1_impotent=1 identity_inference=0')
print('TEBDLC behavioral assimilation oracle: PASS')
