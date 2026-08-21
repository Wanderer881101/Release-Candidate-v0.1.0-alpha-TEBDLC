# Jonathan Therrien, Marieville, Québec.
from collections import defaultdict
sig_loop=('C-loop','U2-model','U2','PROOF_REJECTED',(1,1,0,1))
sig_new=('C-new','U4-model','U4','INTEGRABLE',(1,1,1,1))
events=[(i,sig_loop) for i in range(1,101)]+[(101,sig_new),(102,sig_new)]
factors=defaultdict(list)
for seq,sig in events:factors[sig].append(seq)
assert len(factors)==2 and sum(map(len,factors.values()))==102
assert len(factors[sig_loop])==100 and len(factors[sig_new])==2
assert sorted(seq for v in factors.values() for seq in v)==list(range(1,103))
print('events=102 factors=2 productive=2 repeated_nonproductive=100 reconstructible=1')
print('TEBDLC reactivation productivity factorization oracle: PASS')
