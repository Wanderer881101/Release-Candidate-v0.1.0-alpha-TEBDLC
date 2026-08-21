# Jonathan Therrien, Marieville, Québec.
def uleb(v):
    b=1
    while v>=128:v>>=7;b+=1
    return 8*b
def sb(s):return uleb(len(s))+8*len(s)
def factor(ctx,model,unit,seqs):
    structural=sb(ctx)+sb(model)+sb(unit)+16
    prev=0;occ=uleb(len(seqs))
    for x in seqs:
        assert x>prev
        occ+=uleb(x-prev);prev=x
    return structural+occ
def one(n,step=1):return factor('C-loop','M-loop','U-loop',[1+i*step for i in range(n)])
def many(factors,each):
    total=0;seq=1
    for f in range(factors):
        seqs=list(range(seq,seq+each));seq+=each
        total+=factor(f'C-{f}',f'M-{f}',f'U-{f}',seqs)
    return total
vals={'rep100':one(100),'rep400':one(400),'gap100':one(100,128),'mix10x10':many(10,10),'mix20x5':many(20,5),'distinct64':many(64,1)}
assert vals['rep400']>vals['rep100'];assert vals['gap100']>vals['rep100'];assert vals['mix10x10']>vals['rep100'];assert vals['mix20x5']>vals['mix10x10']
print(' '.join(f'{k}={v}' for k,v in vals.items()))
print('TEBDLC OmegaSt phase2 Python oracle: PASS')
