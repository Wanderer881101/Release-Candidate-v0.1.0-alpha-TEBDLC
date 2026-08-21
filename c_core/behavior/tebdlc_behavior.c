/* Jonathan Therrien, Marieville, Québec. */
#include "tebdlc_behavior.h"
#include <stdlib.h>
#include <string.h>

static char *dupstr(const char *s){
    if(!s) return NULL;
    size_t n=strlen(s)+1U;
    char *p=(char*)malloc(n);
    if(p) memcpy(p,s,n);
    return p;
}
static void obs_clear(tebdlc_bh_observation *o){
    if(!o) return;
    free(o->context); free(o->integration_model); free(o->target_unit);
    memset(o,0,sizeof(*o));
}
void tebdlc_bh_history_init(tebdlc_bh_history *h){ if(h) memset(h,0,sizeof(*h)); }
void tebdlc_bh_history_clear(tebdlc_bh_history *h){
    if(!h) return;
    for(size_t i=0;i<h->count;++i) obs_clear(&h->observations[i]);
    memset(h,0,sizeof(*h));
}
tebdlc_bh_status tebdlc_bh_record(tebdlc_bh_history *h,uint64_t sequence,const char *context,const char *model,const char *unit,tebdlc_bh_outcome outcome,int coherent,int coverage_complete,int compatible,int completeness_proven){
    if(!h||!context||!model||!unit||sequence==0U) return TEBDLC_BH_INVALID;
    if(h->count>=TEBDLC_BH_MAX_OBSERVATIONS) return TEBDLC_BH_CAPACITY;
    if(outcome==TEBDLC_BH_INTEGRABLE && !(coherent&&coverage_complete&&compatible&&completeness_proven)) return TEBDLC_BH_CONTRADICTORY;
    tebdlc_bh_observation *o=&h->observations[h->count];
    memset(o,0,sizeof(*o));
    o->context=dupstr(context); o->integration_model=dupstr(model); o->target_unit=dupstr(unit);
    if(!o->context||!o->integration_model||!o->target_unit){ obs_clear(o); return TEBDLC_BH_INVALID; }
    o->sequence=sequence; o->outcome=outcome; o->coherent=coherent?1:0; o->coverage_complete=coverage_complete?1:0; o->compatible=compatible?1:0; o->completeness_proven=completeness_proven?1:0;
    ++h->count; return TEBDLC_BH_OK;
}
tebdlc_bh_status tebdlc_bh_assimilate(const tebdlc_bh_history *h,tebdlc_bh_model *out){
    if(!h||!out||h->count==0U) return TEBDLC_BH_INVALID;
    memset(out,0,sizeof(*out));
    out->source_observation_count=h->count;
    out->all_integrable_observations_had_complete_proof=1;
    out->incomplete_proof_never_promoted_unit=1;
    out->observations_preserved=1;
    out->identity_inference_permitted=0;
    for(size_t i=0;i<h->count;++i){
        const tebdlc_bh_observation *o=&h->observations[i];
        int full=o->coherent&&o->coverage_complete&&o->compatible&&o->completeness_proven;
        if(o->outcome==TEBDLC_BH_INTEGRABLE){ ++out->integrable_count; if(!full) out->all_integrable_observations_had_complete_proof=0; }
        else if(o->outcome==TEBDLC_BH_PROOF_REJECTED){ ++out->rejected_count; }
        else if(o->outcome==TEBDLC_BH_STAGNATED){ ++out->stagnated_count; }
        if(!full && o->outcome==TEBDLC_BH_INTEGRABLE) out->incomplete_proof_never_promoted_unit=0;
    }
    return TEBDLC_BH_OK;
}
int tebdlc_bh_history_equal_prefix(const tebdlc_bh_history *h,const tebdlc_bh_observation *snapshot,size_t n){
    if(!h||!snapshot||n>h->count) return 0;
    for(size_t i=0;i<n;++i){
        const tebdlc_bh_observation *a=&h->observations[i], *b=&snapshot[i];
        if(a->sequence!=b->sequence||a->outcome!=b->outcome||a->coherent!=b->coherent||a->coverage_complete!=b->coverage_complete||a->compatible!=b->compatible||a->completeness_proven!=b->completeness_proven) return 0;
        if(strcmp(a->context,b->context)!=0||strcmp(a->integration_model,b->integration_model)!=0||strcmp(a->target_unit,b->target_unit)!=0) return 0;
    }
    return 1;
}
