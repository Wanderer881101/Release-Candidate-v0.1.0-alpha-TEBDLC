/* Jonathan Therrien, Marieville, Québec. */
#include "tebdlc_productivity.h"
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static tebdlc_bh_observation obs(uint64_t seq,const char *ctx,const char *model,const char *unit,tebdlc_bh_outcome out,int coh,int cov,int comp,int complete){tebdlc_bh_observation o={0};o.sequence=seq;o.context=(char*)ctx;o.integration_model=(char*)model;o.target_unit=(char*)unit;o.outcome=out;o.coherent=coh;o.coverage_complete=cov;o.compatible=comp;o.completeness_proven=complete;return o;}
int main(void){
    tebdlc_bh_observation events[102];
    for(uint64_t i=1;i<=100U;++i)events[i-1U]=obs(i,"C-loop","U2-model","U2",TEBDLC_BH_PROOF_REJECTED,1,1,0,1);
    events[100]=obs(101,"C-new","U4-model","U4",TEBDLC_BH_INTEGRABLE,1,1,1,1);
    events[101]=obs(102,"C-new","U4-model","U4",TEBDLC_BH_INTEGRABLE,1,1,1,1);
    tebdlc_px_ledger l;tebdlc_px_init(&l);size_t productive=0,nonproductive=0;
    for(size_t i=0;i<102U;++i){tebdlc_px_record_result r;assert(tebdlc_px_record(&l,&events[i],&r)==TEBDLC_PX_OK);if(r.productive)++productive;else ++nonproductive;}
    assert(l.factor_count==2U);assert(l.total_occurrences==102U);assert(productive==2U);assert(nonproductive==100U);
    assert(l.factors[0].occurrence_count==100U);assert(l.factors[1].occurrence_count==2U);
    assert(tebdlc_px_reconstructs_all(&l,events,102U));
    assert(tebdlc_px_find_by_sequence(&l,1U)==&l.factors[0]);assert(tebdlc_px_find_by_sequence(&l,100U)==&l.factors[0]);assert(tebdlc_px_find_by_sequence(&l,101U)==&l.factors[1]);assert(tebdlc_px_find_by_sequence(&l,102U)==&l.factors[1]);
    tebdlc_px_record_result dup;assert(tebdlc_px_record(&l,&events[101],&dup)==TEBDLC_PX_INVALID);assert(l.total_occurrences==102U);
    printf("events=102 factors=2 productive=2 repeated_nonproductive=100 reconstructible=1\n");
    tebdlc_px_clear(&l);puts("TEBDLC reactivation productivity factorization: PASS");return 0;
}
