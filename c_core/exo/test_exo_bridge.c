/* Jonathan Therrien, Marieville, Québec. */
#include "tebdlc_exo_bridge.h"
#include <assert.h>
#include <stdio.h>
#include <string.h>

static tebdlc_poly_big_gain mk(unsigned long n,unsigned long d,uint64_t id,const char *ctx){
    tebdlc_poly_big_gain g; tebdlc_poly_big_init(&g); mpz_set_ui(g.numerator,n); mpz_set_ui(g.denominator,d);
    g.typing.domain="integrity"; g.typing.dimension="coverage"; g.typing.unit="ratio"; g.typing.reference="EXO-361"; g.typing.context=ctx;
    g.node_id=id; return g;
}
int main(void){
    tebdlc_poly_big_gain a=mk(300,361,1,"C-origin"), b=mk(300,361,2,"C-origin");
    tebdlc_imp_set set={.members={&a,&b},.count=2,.integration_model="U1-model",.target_unit="U1"};
    tebdlc_imp_assessment as; tebdlc_imp_assessment_init(&as); assert(tebdlc_imp_describe_mass(&set,&as)==TEBDLC_IMP_OK);
    assert(as.relation_to_one==TEBDLC_IMP_MASS_GT_ONE); assert(as.unitary_attained==0); assert(as.integrability_proven==0);

    tebdlc_st_archive sa,sb; tebdlc_st_archive_init(&sa); tebdlc_st_archive_init(&sb);
    assert(tebdlc_st_stagnate_gain(&a,&sa)==TEBDLC_ST_OK); assert(tebdlc_st_stagnate_gain(&b,&sb)==TEBDLC_ST_OK);
    assert(tebdlc_st_compress(&sa)==TEBDLC_ST_OK); assert(tebdlc_st_compress(&sb)==TEBDLC_ST_OK);
    assert(tebdlc_st_decompress_verify(&sa)==TEBDLC_ST_OK); assert(tebdlc_st_decompress_verify(&sb)==TEBDLC_ST_OK);
    assert(tebdlc_st_reactivate(&sa,"C-call-new")==TEBDLC_ST_REVALIDATION_REQUIRED);
    assert(tebdlc_st_reactivate(&sb,"C-call-new")==TEBDLC_ST_REVALIDATION_REQUIRED);
    assert(strcmp(sa.origin_context,"C-origin")==0 && strcmp(sb.origin_context,"C-origin")==0);
    assert(strcmp(sa.call_context,"C-call-new")==0 && strcmp(sb.call_context,"C-call-new")==0);

    tebdlc_exo_reactivation r; tebdlc_exo_reactivation_init(&r);
    assert(tebdlc_exo_capture_impotent_origin(&set,&as,&r)==TEBDLC_EXO_OK);
    assert(tebdlc_exo_origin_still_impotent(&r)); assert(mpq_cmp(r.origin.mass,as.mass)==0);

    assert(tebdlc_exo_reactivate_for_unit(&r,"U2-model","U2","C-call-new")==TEBDLC_EXO_REVALIDATION_REQUIRED);
    assert(r.call_unitary_attained==0); assert(tebdlc_exo_origin_still_impotent(&r));
    assert(strcmp(r.origin.origin_target_unit,"U1")==0); assert(strcmp(r.call_target_unit,"U2")==0);

    assert(tebdlc_exo_revalidate_new_unit(&r,1,1,0,1)==TEBDLC_EXO_PROOF_REJECTED);
    assert(r.call_unitary_attained==0); assert(tebdlc_exo_origin_still_impotent(&r));

    assert(tebdlc_exo_revalidate_new_unit(&r,1,1,1,1)==TEBDLC_EXO_OK);
    assert(r.call_unitary_attained==1); assert(r.call_integrability_proven==1);
    assert(tebdlc_exo_origin_still_impotent(&r));
    assert(r.origin.original_unitary_attained==0); assert(r.origin.original_integrability_proven==0);
    gmp_printf("origin_mass=%Qd origin_U1_unitary=%d call_U2_unitary=%d preserved=%d\n",r.origin.mass,r.origin.original_unitary_attained,r.call_unitary_attained,r.historical_origin_preserved);

    tebdlc_st_archive_clear(&sa); tebdlc_st_archive_clear(&sb); tebdlc_exo_reactivation_clear(&r); tebdlc_imp_assessment_clear(&as); tebdlc_poly_big_clear(&a); tebdlc_poly_big_clear(&b);
    puts("TEBDLC impotent-stagnation recontextualization: PASS"); return 0;
}
