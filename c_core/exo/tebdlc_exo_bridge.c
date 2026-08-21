/* Jonathan Therrien, Marieville, Québec. */
#include "tebdlc_exo_bridge.h"
#include <stdlib.h>
#include <string.h>

static char *dupstr(const char *s){ if(!s)return NULL; size_t n=strlen(s)+1U; char *p=(char*)malloc(n); if(p)memcpy(p,s,n); return p; }

void tebdlc_exo_reactivation_init(tebdlc_exo_reactivation *r){
    if(!r) return;
    memset(r,0,sizeof(*r));
    mpq_init(r->origin.mass);
    r->origin.initialized=1;
}
void tebdlc_exo_reactivation_clear(tebdlc_exo_reactivation *r){
    if(!r) return;
    if(r->origin.initialized) mpq_clear(r->origin.mass);
    free(r->origin.origin_integration_model); free(r->origin.origin_target_unit); free(r->origin.origin_context);
    free(r->call_integration_model); free(r->call_target_unit); free(r->call_context); memset(r,0,sizeof(*r));
}
tebdlc_exo_status tebdlc_exo_capture_impotent_origin(const tebdlc_imp_set *set,const tebdlc_imp_assessment *a,tebdlc_exo_reactivation *out){
    if(!set||!a||!a->initialized||!out||!out->origin.initialized||set->count==0U||!set->members[0]) return TEBDLC_EXO_INVALID;
    if(a->unitary_attained||a->integrability_proven) return TEBDLC_EXO_INVALID;
    mpq_set(out->origin.mass,a->mass); out->origin.relation_to_one=a->relation_to_one;
    out->origin.original_unitary_attained=a->unitary_attained; out->origin.original_integrability_proven=a->integrability_proven;
    out->origin.origin_integration_model=dupstr(set->integration_model); out->origin.origin_target_unit=dupstr(set->target_unit); out->origin.origin_context=dupstr(set->members[0]->typing.context);
    if(!out->origin.origin_integration_model||!out->origin.origin_target_unit||!out->origin.origin_context) return TEBDLC_EXO_INVALID;
    out->historical_origin_preserved=1; return TEBDLC_EXO_OK;
}
tebdlc_exo_status tebdlc_exo_reactivate_for_unit(tebdlc_exo_reactivation *r,const char *m,const char *u,const char *c){
    if(!r||!r->origin.initialized||!r->historical_origin_preserved||!m||!u||!c) return TEBDLC_EXO_INVALID;
    free(r->call_integration_model); free(r->call_target_unit); free(r->call_context);
    r->call_integration_model=dupstr(m); r->call_target_unit=dupstr(u); r->call_context=dupstr(c);
    if(!r->call_integration_model||!r->call_target_unit||!r->call_context) return TEBDLC_EXO_INVALID;
    r->call_integrability_proven=0; r->call_unitary_attained=0;
    return TEBDLC_EXO_REVALIDATION_REQUIRED;
}
tebdlc_exo_status tebdlc_exo_revalidate_new_unit(tebdlc_exo_reactivation *r,int coherent,int coverage_complete,int compatible,int completeness_proven){
    if(!r||!r->call_integration_model||!r->call_target_unit||!r->call_context) return TEBDLC_EXO_INVALID;
    if(!(coherent&&coverage_complete&&compatible&&completeness_proven)){ r->call_integrability_proven=0; r->call_unitary_attained=0; return TEBDLC_EXO_PROOF_REJECTED; }
    r->call_integrability_proven=1; r->call_unitary_attained=1; return TEBDLC_EXO_OK;
}
int tebdlc_exo_origin_still_impotent(const tebdlc_exo_reactivation *r){
    if(!r||!r->historical_origin_preserved) return 0;
    return r->origin.original_unitary_attained==0 && r->origin.original_integrability_proven==0;
}
