/* Jonathan Therrien, Marieville, Québec. */
#include "tebdlc_impotent.h"
#include <string.h>
static int same_text(const char *a,const char *b){ if(!a||!b) return a==b; return strcmp(a,b)==0; }
static int same_measure_reference(const tebdlc_poly_big_gain *a,const tebdlc_poly_big_gain *b){ return same_text(a->typing.domain,b->typing.domain)&&same_text(a->typing.dimension,b->typing.dimension)&&same_text(a->typing.unit,b->typing.unit)&&same_text(a->typing.reference,b->typing.reference)&&same_text(a->typing.context,b->typing.context); }
void tebdlc_imp_assessment_init(tebdlc_imp_assessment *a){ if(!a)return; memset(a,0,sizeof(*a)); mpq_init(a->mass); a->initialized=1; }
void tebdlc_imp_assessment_clear(tebdlc_imp_assessment *a){ if(a&&a->initialized){mpq_clear(a->mass);a->initialized=0;} }
tebdlc_imp_status tebdlc_imp_describe_mass(const tebdlc_imp_set *set,tebdlc_imp_assessment *out){
    if(!set||!out||!out->initialized||set->count==0U||set->count>TEBDLC_IMP_MAX_MEMBERS||!set->integration_model||!set->target_unit) return TEBDLC_IMP_INVALID;
    mpq_set_ui(out->mass,0U,1U); out->unitary_attained=0; out->integrability_proven=0; out->member_count=set->count;
    const tebdlc_poly_big_gain *first=set->members[0]; if(tebdlc_poly_big_validate(first)!=TEBDLC_POLY_OK) return TEBDLC_IMP_INVALID;
    for(size_t i=0;i<set->count;++i){ const tebdlc_poly_big_gain *g=set->members[i]; if(tebdlc_poly_big_validate(g)!=TEBDLC_POLY_OK) return TEBDLC_IMP_INVALID; if(!same_measure_reference(first,g)) return TEBDLC_IMP_INCOMPATIBLE_REFERENCE; mpq_t q; mpq_init(q); mpq_set_num(q,g->numerator); mpq_set_den(q,g->denominator); mpq_canonicalize(q); mpq_add(out->mass,out->mass,q); mpq_clear(q); }
    int cmp=mpq_cmp_ui(out->mass,1U,1U); out->relation_to_one=cmp<0?TEBDLC_IMP_MASS_LT_ONE:(cmp>0?TEBDLC_IMP_MASS_GT_ONE:TEBDLC_IMP_MASS_EQ_ONE); return TEBDLC_IMP_OK;
}
tebdlc_imp_status tebdlc_imp_apply_integrability_proof(tebdlc_imp_assessment *assessment,int coherent,int coverage_complete,int compatible,int completeness_proven){ if(!assessment||!assessment->initialized) return TEBDLC_IMP_INVALID; if(!(coherent&&coverage_complete&&compatible&&completeness_proven)) return TEBDLC_IMP_PROOF_REQUIRED; assessment->integrability_proven=1; assessment->unitary_attained=1; return TEBDLC_IMP_OK; }
