/* Jonathan Therrien, Marieville, Québec. */
#include "tebdlc_productivity.h"
#include <stdlib.h>
#include <string.h>
static char *dupstr(const char *s){if(!s)return NULL;size_t n=strlen(s)+1U;char *p=(char*)malloc(n);if(p)memcpy(p,s,n);return p;}
static int eqs(const char *a,const char *b){return a&&b&&strcmp(a,b)==0;}
static int same_signature(const tebdlc_px_factor *f,const tebdlc_bh_observation *o){
    return eqs(f->context,o->context)&&eqs(f->integration_model,o->integration_model)&&eqs(f->target_unit,o->target_unit)&&f->outcome==o->outcome&&f->coherent==o->coherent&&f->coverage_complete==o->coverage_complete&&f->compatible==o->compatible&&f->completeness_proven==o->completeness_proven;
}
static void factor_clear(tebdlc_px_factor *f){if(!f)return;free(f->context);free(f->integration_model);free(f->target_unit);memset(f,0,sizeof(*f));}
void tebdlc_px_init(tebdlc_px_ledger *l){if(l)memset(l,0,sizeof(*l));}
void tebdlc_px_clear(tebdlc_px_ledger *l){if(!l)return;for(size_t i=0;i<l->factor_count;++i)factor_clear(&l->factors[i]);memset(l,0,sizeof(*l));}
tebdlc_px_status tebdlc_px_record(tebdlc_px_ledger *l,const tebdlc_bh_observation *o,tebdlc_px_record_result *out){
    if(!l||!o||!o->context||!o->integration_model||!o->target_unit||o->sequence==0U)return TEBDLC_PX_INVALID;
    for(size_t i=0;i<l->factor_count;++i){
        tebdlc_px_factor *f=&l->factors[i];
        if(same_signature(f,o)){
            if(f->occurrence_count>=TEBDLC_PX_MAX_OCCURRENCES)return TEBDLC_PX_CAPACITY;
            for(size_t k=0;k<f->occurrence_count;++k)if(f->sequences[k]==o->sequence)return TEBDLC_PX_INVALID;
            f->sequences[f->occurrence_count++]=o->sequence;++l->total_occurrences;
            if(out){out->productive=0;out->factor_index=i;out->occurrence_index=f->occurrence_count-1U;}return TEBDLC_PX_OK;
        }
    }
    if(l->factor_count>=TEBDLC_PX_MAX_FACTORS)return TEBDLC_PX_CAPACITY;
    tebdlc_px_factor *f=&l->factors[l->factor_count];memset(f,0,sizeof(*f));
    f->context=dupstr(o->context);f->integration_model=dupstr(o->integration_model);f->target_unit=dupstr(o->target_unit);
    if(!f->context||!f->integration_model||!f->target_unit){factor_clear(f);return TEBDLC_PX_INVALID;}
    f->outcome=o->outcome;f->coherent=o->coherent;f->coverage_complete=o->coverage_complete;f->compatible=o->compatible;f->completeness_proven=o->completeness_proven;f->sequences[0]=o->sequence;f->occurrence_count=1U;
    if(out){out->productive=1;out->factor_index=l->factor_count;out->occurrence_index=0U;}
    ++l->factor_count;++l->total_occurrences;return TEBDLC_PX_OK;
}
const tebdlc_px_factor *tebdlc_px_find_by_sequence(const tebdlc_px_ledger *l,uint64_t sequence){if(!l||sequence==0U)return NULL;for(size_t i=0;i<l->factor_count;++i)for(size_t k=0;k<l->factors[i].occurrence_count;++k)if(l->factors[i].sequences[k]==sequence)return &l->factors[i];return NULL;}
int tebdlc_px_reconstructs_all(const tebdlc_px_ledger *l,const tebdlc_bh_observation *events,size_t n){if(!l||!events||l->total_occurrences!=n)return 0;for(size_t i=0;i<n;++i){const tebdlc_px_factor *f=tebdlc_px_find_by_sequence(l,events[i].sequence);if(!f||!same_signature(f,&events[i]))return 0;}return 1;}
