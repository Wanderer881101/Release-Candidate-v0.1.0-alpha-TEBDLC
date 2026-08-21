/* Jonathan Therrien, Marieville, Québec. */
#include "tebdlc_omega_st.h"
#include <limits.h>
#include <string.h>
static int add_u64(uint64_t a,uint64_t b,uint64_t *out){if(UINT64_MAX-a<b)return 0;*out=a+b;return 1;}
uint64_t tebdlc_omega_uleb128_bits(uint64_t value){uint64_t bytes=1U;while(value>=128U){value>>=7U;++bytes;}return bytes*8U;}
uint64_t tebdlc_omega_string_bits(const char *s){if(!s)return 0U;size_t n=strlen(s);if(n>UINT64_MAX/8U)return UINT64_MAX;uint64_t payload=(uint64_t)n*8U, r=0U;if(!add_u64(tebdlc_omega_uleb128_bits((uint64_t)n),payload,&r))return UINT64_MAX;return r;}
uint64_t tebdlc_omega_factor_structural_bits(const tebdlc_px_factor *f){
    if(!f||!f->context||!f->integration_model||!f->target_unit)return UINT64_MAX;
    uint64_t r=0U,t=0U;
    const uint64_t fields[]={tebdlc_omega_string_bits(f->context),tebdlc_omega_string_bits(f->integration_model),tebdlc_omega_string_bits(f->target_unit),8U,8U};
    for(size_t i=0;i<5U;++i){if(fields[i]==UINT64_MAX||!add_u64(r,fields[i],&t))return UINT64_MAX;r=t;}
    return r;
}
uint64_t tebdlc_omega_factor_occurrence_bits(const tebdlc_px_factor *f){
    if(!f||f->occurrence_count==0U)return UINT64_MAX;
    uint64_t r=tebdlc_omega_uleb128_bits((uint64_t)f->occurrence_count),t=0U,prev=0U;
    for(size_t i=0;i<f->occurrence_count;++i){
        uint64_t seq=f->sequences[i]; if(seq==0U||seq<=prev)return UINT64_MAX;
        uint64_t delta=seq-prev; uint64_t bits=tebdlc_omega_uleb128_bits(delta);
        if(!add_u64(r,bits,&t)) return UINT64_MAX;
        r=t;
        prev=seq;
    }
    return r;
}
int tebdlc_omega_measure(const tebdlc_px_ledger *ledger,tebdlc_omega_st_measure *out){
    if(!ledger||!out) return 0;
    memset(out,0,sizeof(*out));
    out->exact_reconstructibility_required=1;
    uint64_t structural=0U,occ=0U,t=0U;size_t sum_occ=0U;
    for(size_t i=0;i<ledger->factor_count;++i){
        const tebdlc_px_factor *f=&ledger->factors[i];
        uint64_t sb=tebdlc_omega_factor_structural_bits(f),ob=tebdlc_omega_factor_occurrence_bits(f);
        if(sb==UINT64_MAX||ob==UINT64_MAX)return 0;
        if(!add_u64(structural,sb,&t)) return 0;
        structural=t;
        if(!add_u64(occ,ob,&t)) return 0;
        occ=t;
        if(SIZE_MAX-sum_occ<f->occurrence_count) return 0;
        sum_occ+=f->occurrence_count;
    }
    if(sum_occ!=ledger->total_occurrences)return 0;
    if(!add_u64(structural,occ,&t))return 0;
    out->factor_count=ledger->factor_count;out->total_occurrences=ledger->total_occurrences;
    out->factorized_repetition_count=ledger->total_occurrences>=ledger->factor_count?ledger->total_occurrences-ledger->factor_count:0U;
    out->structural_bits=structural;out->occurrence_bits=occ;out->omega_st_bits=t;return 1;
}
