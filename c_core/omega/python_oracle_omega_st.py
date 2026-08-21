# Jonathan Therrien, Marieville, Québec.
def uleb_bits(v):
    b=1
    while v>=128:
        v >>= 7; b += 1
    return b*8
def s_bits(s): return uleb_bits(len(s))+8*len(s)
def factor(ctx,model,unit,outcome,seqs):
    structural=s_bits(ctx)+s_bits(model)+s_bits(unit)+8+8
    prev=0; occ=uleb_bits(len(seqs))
    for x in seqs:
        assert x>prev
        occ += uleb_bits(x-prev); prev=x
    return structural+occ
r1=factor("C-loop","U2-model","U2",2,[1])
r100=factor("C-loop","U2-model","U2",2,list(range(1,101)))
d10=sum(factor(f"C-{i}",f"M-{i}",f"U-{i}",2,[i+1]) for i in range(10))
d20=sum(factor(f"C-{i}",f"M-{i}",f"U-{i}",2,[i+1]) for i in range(20))
assert r100>r1 and r100-r1<99*64 and d20>d10
print(f"repeat_1={r1} repeat_100={r100} distinct_10={d10} distinct_20={d20} repetitions_factorized=99")
print("TEBDLC OmegaSt Python oracle: PASS")
