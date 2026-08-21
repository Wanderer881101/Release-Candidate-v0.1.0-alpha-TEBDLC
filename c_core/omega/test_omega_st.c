/* Jonathan Therrien, Marieville, Québec. */
#include "tebdlc_omega_st.h"
#include <assert.h>
#include <stdio.h>
#include <string.h>
static void set_factor(tebdlc_px_factor *f,const char *ctx,const char *model,const char *unit,tebdlc_bh_outcome out,size_t n,uint64_t first){
    memset(f,0,sizeof(*f));f->context=(char*)ctx;f->integration_model=(char*)model;f->target_unit=(char*)unit;f->outcome=out;
    f->coherent=1;f->coverage_complete=1;f->compatible=(out==TEBDLC_BH_INTEGRABLE);f->completeness_proven=1;f->occurrence_count=n;
    for(size_t i=0;i<n;++i)f->sequences[i]=first+(uint64_t)i;
}
static tebdlc_px_ledger repeated(size_t n){
    tebdlc_px_ledger l;memset(&l,0,sizeof(l));l.factor_count=1U;l.total_occurrences=n;
    set_factor(&l.factors[0],"C-loop","U2-model","U2",TEBDLC_BH_PROOF_REJECTED,n,1U);return l;
}
static tebdlc_px_ledger distinct(size_t n){
    tebdlc_px_ledger l;memset(&l,0,sizeof(l));l.factor_count=n;l.total_occurrences=n;
    static char ctx[TEBDLC_PX_MAX_FACTORS][24];static char model[TEBDLC_PX_MAX_FACTORS][24];static char unit[TEBDLC_PX_MAX_FACTORS][24];
    for(size_t i=0;i<n;++i){snprintf(ctx[i],sizeof(ctx[i]),"C-%zu",i);snprintf(model[i],sizeof(model[i]),"M-%zu",i);snprintf(unit[i],sizeof(unit[i]),"U-%zu",i);set_factor(&l.factors[i],ctx[i],model[i],unit[i],TEBDLC_BH_PROOF_REJECTED,1U,(uint64_t)i+1U);}return l;
}
int main(void){
    tebdlc_omega_st_measure a,b,c,d,e;
    tebdlc_px_ledger r1=repeated(1U),r100=repeated(100U),d10=distinct(10U),d20=distinct(20U);
    assert(tebdlc_omega_measure(&r1,&a));assert(tebdlc_omega_measure(&r100,&b));assert(tebdlc_omega_measure(&d10,&c));assert(tebdlc_omega_measure(&d20,&d));
    assert(a.factor_count==1U&&b.factor_count==1U);assert(b.factorized_repetition_count==99U);assert(b.structural_bits==a.structural_bits);
    assert(b.omega_st_bits>a.omega_st_bits);assert((b.omega_st_bits-a.omega_st_bits)<(uint64_t)(99U*64U));
    assert(d.factor_count==20U&&c.factor_count==10U);assert(d.omega_st_bits>c.omega_st_bits);assert(d.structural_bits>c.structural_bits);
    tebdlc_px_ledger invalid=repeated(3U);invalid.factors[0].sequences[2]=2U;assert(!tebdlc_omega_measure(&invalid,&e));
    printf("repeat_1=%llu repeat_100=%llu distinct_10=%llu distinct_20=%llu repetitions_factorized=%zu\n",
      (unsigned long long)a.omega_st_bits,(unsigned long long)b.omega_st_bits,(unsigned long long)c.omega_st_bits,(unsigned long long)d.omega_st_bits,b.factorized_repetition_count);
    puts("TEBDLC OmegaSt candidate measurement: PASS");return 0;
}
