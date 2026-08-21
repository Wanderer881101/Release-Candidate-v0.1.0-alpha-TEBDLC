/* Jonathan Therrien, Marieville, Québec. */
#include "tebdlc_behavior.h"
#include "../exo/tebdlc_exo_bridge.h"
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static tebdlc_poly_big_gain mk(unsigned long n,unsigned long d,uint64_t id,const char *ctx){
    tebdlc_poly_big_gain g; tebdlc_poly_big_init(&g); mpz_set_ui(g.numerator,n); mpz_set_ui(g.denominator,d);
    g.typing.domain="integrity"; g.typing.dimension="coverage"; g.typing.unit="ratio"; g.typing.reference="BH-361"; g.typing.context=ctx; g.node_id=id; return g;
}
static tebdlc_bh_observation *snapshot_history(const tebdlc_bh_history *h){
    tebdlc_bh_observation *s=(tebdlc_bh_observation*)calloc(h->count,sizeof(*s)); assert(s);
    for(size_t i=0;i<h->count;++i){ s[i]=h->observations[i]; }
    return s;
}
int main(void){
    tebdlc_poly_big_gain a=mk(300,361,1,"C-origin"),b=mk(300,361,2,"C-origin");
    tebdlc_imp_set set={.members={&a,&b},.count=2,.integration_model="U1-model",.target_unit="U1"};
    tebdlc_imp_assessment as; tebdlc_imp_assessment_init(&as); assert(tebdlc_imp_describe_mass(&set,&as)==TEBDLC_IMP_OK); assert(as.relation_to_one==TEBDLC_IMP_MASS_GT_ONE);
    tebdlc_exo_reactivation r; tebdlc_exo_reactivation_init(&r); assert(tebdlc_exo_capture_impotent_origin(&set,&as,&r)==TEBDLC_EXO_OK);
    tebdlc_bh_history h; tebdlc_bh_history_init(&h);

    assert(tebdlc_bh_record(&h,1,"C-origin","U1-model","U1",TEBDLC_BH_STAGNATED,1,0,1,0)==TEBDLC_BH_OK);
    assert(tebdlc_exo_reactivate_for_unit(&r,"U2-model","U2","C-call-2")==TEBDLC_EXO_REVALIDATION_REQUIRED);
    assert(tebdlc_exo_revalidate_new_unit(&r,1,1,0,1)==TEBDLC_EXO_PROOF_REJECTED);
    assert(tebdlc_bh_record(&h,2,"C-call-2","U2-model","U2",TEBDLC_BH_PROOF_REJECTED,1,1,0,1)==TEBDLC_BH_OK);
    assert(tebdlc_exo_reactivate_for_unit(&r,"U3-model","U3","C-call-3")==TEBDLC_EXO_REVALIDATION_REQUIRED);
    assert(tebdlc_exo_revalidate_new_unit(&r,1,0,1,1)==TEBDLC_EXO_PROOF_REJECTED);
    assert(tebdlc_bh_record(&h,3,"C-call-3","U3-model","U3",TEBDLC_BH_PROOF_REJECTED,1,0,1,1)==TEBDLC_BH_OK);
    assert(tebdlc_exo_reactivate_for_unit(&r,"U4-model","U4","C-call-4")==TEBDLC_EXO_REVALIDATION_REQUIRED);
    assert(tebdlc_exo_revalidate_new_unit(&r,1,1,1,1)==TEBDLC_EXO_OK);
    assert(tebdlc_bh_record(&h,4,"C-call-4","U4-model","U4",TEBDLC_BH_INTEGRABLE,1,1,1,1)==TEBDLC_BH_OK);
    assert(tebdlc_exo_origin_still_impotent(&r));

    tebdlc_bh_observation *snap=snapshot_history(&h); size_t snap_n=h.count;
    tebdlc_bh_model m; assert(tebdlc_bh_assimilate(&h,&m)==TEBDLC_BH_OK);
    assert(m.source_observation_count==4U); assert(m.integrable_count==1U); assert(m.rejected_count==2U); assert(m.stagnated_count==1U);
    assert(m.all_integrable_observations_had_complete_proof==1); assert(m.incomplete_proof_never_promoted_unit==1); assert(m.identity_inference_permitted==0);
    assert(h.count==snap_n); assert(tebdlc_bh_history_equal_prefix(&h,snap,snap_n));
    assert(tebdlc_bh_record(&h,5,"C-call-5","U5-model","U5",TEBDLC_BH_INTEGRABLE,1,0,1,1)==TEBDLC_BH_CONTRADICTORY);
    assert(h.count==4U); assert(tebdlc_bh_history_equal_prefix(&h,snap,snap_n));

    printf("observations=%zu integrable=%zu rejected=%zu stagnated=%zu origin_U1_impotent=%d identity_inference=%d\n",h.count,m.integrable_count,m.rejected_count,m.stagnated_count,tebdlc_exo_origin_still_impotent(&r),m.identity_inference_permitted);
    free(snap); tebdlc_bh_history_clear(&h); tebdlc_exo_reactivation_clear(&r); tebdlc_imp_assessment_clear(&as); tebdlc_poly_big_clear(&a); tebdlc_poly_big_clear(&b);
    puts("TEBDLC behavioral assimilation: PASS"); return 0;
}
