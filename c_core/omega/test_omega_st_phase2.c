/* Jonathan Therrien, Marieville, Québec. */
#include "tebdlc_omega_st.h"
#include <assert.h>
#include <stdio.h>
#include <string.h>

static tebdlc_bh_observation make_obs(uint64_t seq,const char *ctx,const char *model,const char *unit,tebdlc_bh_outcome out){
    tebdlc_bh_observation o={0};o.sequence=seq;o.context=(char*)ctx;o.integration_model=(char*)model;o.target_unit=(char*)unit;o.outcome=out;o.coherent=1;o.coverage_complete=1;o.compatible=(out==TEBDLC_BH_INTEGRABLE);o.completeness_proven=1;return o;
}
static void record(tebdlc_px_ledger *l,const tebdlc_bh_observation *o){tebdlc_px_record_result r;assert(tebdlc_px_record(l,o,&r)==TEBDLC_PX_OK);}
static tebdlc_px_ledger one_factor(size_t n,uint64_t step){
    tebdlc_px_ledger l;tebdlc_px_init(&l);for(size_t i=0;i<n;++i){tebdlc_bh_observation o=make_obs(1U+(uint64_t)i*step,"C-loop","M-loop","U-loop",TEBDLC_BH_PROOF_REJECTED);record(&l,&o);}return l;
}
static tebdlc_px_ledger many_factors(size_t factors,size_t each){
    tebdlc_px_ledger l;tebdlc_px_init(&l);static char ctx[TEBDLC_PX_MAX_FACTORS][24];static char model[TEBDLC_PX_MAX_FACTORS][24];static char unit[TEBDLC_PX_MAX_FACTORS][24];uint64_t seq=1U;
    for(size_t f=0;f<factors;++f){snprintf(ctx[f],sizeof(ctx[f]),"C-%zu",f);snprintf(model[f],sizeof(model[f]),"M-%zu",f);snprintf(unit[f],sizeof(unit[f]),"U-%zu",f);for(size_t j=0;j<each;++j){tebdlc_bh_observation o=make_obs(seq++,ctx[f],model[f],unit[f],TEBDLC_BH_PROOF_REJECTED);record(&l,&o);}}
    return l;
}
int main(void){
    tebdlc_px_ledger rep100=one_factor(100U,1U),rep400=one_factor(400U,1U),gap100=one_factor(100U,128U),mix10= many_factors(10U,10U),mix20=many_factors(20U,5U),dist64=many_factors(64U,1U);
    tebdlc_omega_st_measure a,b,c,d,e,f;
    assert(tebdlc_omega_measure(&rep100,&a));assert(tebdlc_omega_measure(&rep400,&b));assert(tebdlc_omega_measure(&gap100,&c));assert(tebdlc_omega_measure(&mix10,&d));assert(tebdlc_omega_measure(&mix20,&e));assert(tebdlc_omega_measure(&dist64,&f));
    assert(a.factor_count==1U&&b.factor_count==1U&&c.factor_count==1U);assert(d.total_occurrences==100U&&e.total_occurrences==100U);
    assert(b.omega_st_bits>a.omega_st_bits);assert(c.omega_st_bits>a.omega_st_bits);assert(d.omega_st_bits>a.omega_st_bits);assert(e.omega_st_bits>d.omega_st_bits);assert(f.factor_count==64U);
    assert(a.factorized_repetition_count==99U);assert(b.factorized_repetition_count==399U);assert(d.factorized_repetition_count==90U);assert(e.factorized_repetition_count==80U);
    printf("rep100=%llu rep400=%llu gap100=%llu mix10x10=%llu mix20x5=%llu distinct64=%llu\n",(unsigned long long)a.omega_st_bits,(unsigned long long)b.omega_st_bits,(unsigned long long)c.omega_st_bits,(unsigned long long)d.omega_st_bits,(unsigned long long)e.omega_st_bits,(unsigned long long)f.omega_st_bits);
    printf("same_occurrence_count_100: rep1factor=%llu mix10=%llu mix20=%llu\n",(unsigned long long)a.omega_st_bits,(unsigned long long)d.omega_st_bits,(unsigned long long)e.omega_st_bits);
    tebdlc_px_clear(&rep100);tebdlc_px_clear(&rep400);tebdlc_px_clear(&gap100);tebdlc_px_clear(&mix10);tebdlc_px_clear(&mix20);tebdlc_px_clear(&dist64);
    puts("TEBDLC OmegaSt phase2 structural stress: PASS");return 0;
}
