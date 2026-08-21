/* Jonathan Therrien, Marieville, Québec. */
#include "tebdlc_core.h"

#include <limits.h>
#include <stddef.h>
#include <string.h>

static uint64_t gcd_u64(uint64_t a, uint64_t b) { while (b != 0U) { uint64_t t = a % b; a = b; b = t; } return a; }
static uint64_t bits_u64(uint64_t x) { uint64_t bits = 0; do { ++bits; x >>= 1U; } while (x != 0U); return bits; }
static int same_text(const char *a, const char *b) { if (a == NULL || b == NULL) return a == b; return strcmp(a,b) == 0; }
static tebdlc_fractional_result result_with_status(tebdlc_status status,const tebdlc_fractional_gain *a,const tebdlc_fractional_gain *b){ tebdlc_fractional_result r={0}; r.status=status; if(a)r.left=*a; if(b)r.right=*b; return r; }

static int provenance_contains(const tebdlc_provenance *p,const char *s){ for(size_t i=0;i<p->count;i++) if(strcmp(p->items[i],s)==0) return 1; return 0; }
static void provenance_sort(tebdlc_provenance *p){ for(size_t i=0;i<p->count;i++) for(size_t j=i+1;j<p->count;j++) if(strcmp(p->items[i],p->items[j])>0){ const char *t=p->items[i]; p->items[i]=p->items[j]; p->items[j]=t; } }
static tebdlc_status provenance_merge(const tebdlc_provenance *a,const tebdlc_provenance *b,tebdlc_provenance *out,size_t *required){ out->count=0; const tebdlc_provenance *srcs[2]={a,b}; for(size_t s=0;s<2;s++){ for(size_t i=0;i<srcs[s]->count;i++){ const char *item=srcs[s]->items[i]; if(item==NULL) return TEBDLC_INVALID_REPRESENTATION; if(!provenance_contains(out,item)){ if(out->count>=TEBDLC_MAX_PROVENANCE){ if(required) *required=out->count+1U; return TEBDLC_PROVENANCE_CAPACITY_REQUIRED; } out->items[out->count++]=item; } } } provenance_sort(out); return TEBDLC_OK; }

tebdlc_status tebdlc_fractional_validate(const tebdlc_fractional_gain *gain){ if(!gain||gain->denominator==0U||gain->numerator==0U||gain->numerator>=gain->denominator) return TEBDLC_INVALID_REPRESENTATION; if(!gain->typing.domain||!gain->typing.dimension||!gain->typing.unit||!gain->typing.reference||!gain->typing.context||gain->typing.provenance.count>TEBDLC_MAX_PROVENANCE) return TEBDLC_INVALID_REPRESENTATION; for(size_t i=0;i<gain->typing.provenance.count;i++) if(!gain->typing.provenance.items[i]) return TEBDLC_INVALID_REPRESENTATION; return TEBDLC_OK; }
int tebdlc_fractional_composable(const tebdlc_fractional_gain *a,const tebdlc_fractional_gain *b){ if(tebdlc_fractional_validate(a)!=TEBDLC_OK||tebdlc_fractional_validate(b)!=TEBDLC_OK)return 0; return same_text(a->typing.domain,b->typing.domain)&&same_text(a->typing.dimension,b->typing.dimension)&&same_text(a->typing.unit,b->typing.unit)&&same_text(a->typing.reference,b->typing.reference)&&same_text(a->typing.context,b->typing.context); }

tebdlc_fractional_result tebdlc_fractional_multiply(const tebdlc_fractional_gain *a,const tebdlc_fractional_gain *b){
    if(tebdlc_fractional_validate(a)!=TEBDLC_OK||tebdlc_fractional_validate(b)!=TEBDLC_OK) return result_with_status(TEBDLC_INVALID_REPRESENTATION,a,b);
    if(!tebdlc_fractional_composable(a,b)) return result_with_status(TEBDLC_INCOMPATIBLE_CONTEXT,a,b);
    uint64_t an=a->numerator,ad=a->denominator,bn=b->numerator,bd=b->denominator;
    uint64_t g1=gcd_u64(an,bd); an/=g1; bd/=g1; uint64_t g2=gcd_u64(bn,ad); bn/=g2; ad/=g2;
    tebdlc_fractional_result r=result_with_status(TEBDLC_OK,a,b);
    if(an!=0U&&bn>UINT64_MAX/an){ r.status=TEBDLC_CAPACITY_EXPANSION_REQUIRED; r.required_num_bits=bits_u64(an)+bits_u64(bn); r.required_den_bits=bits_u64(ad)+bits_u64(bd); return r; }
    if(ad!=0U&&bd>UINT64_MAX/ad){ r.status=TEBDLC_CAPACITY_EXPANSION_REQUIRED; r.required_num_bits=bits_u64(an)+bits_u64(bn); r.required_den_bits=bits_u64(ad)+bits_u64(bd); return r; }
    uint64_t numerator=an*bn,denominator=ad*bd; if(numerator==0U||denominator==0U||numerator>=denominator){ r.status=TEBDLC_INVALID_REPRESENTATION; return r; }
    uint64_t g=gcd_u64(numerator,denominator); numerator/=g; denominator/=g;
    r.value.numerator=numerator; r.value.denominator=denominator; r.value.typing=a->typing;
    tebdlc_status ps=provenance_merge(&a->typing.provenance,&b->typing.provenance,&r.value.typing.provenance,&r.required_provenance_capacity); if(ps!=TEBDLC_OK){ r.status=ps; return r; }
    return r;
}
tebdlc_status tebdlc_fractional_add_forbidden(void){return TEBDLC_FORBIDDEN_OPERATION;}
tebdlc_status tebdlc_fractional_sub_forbidden(void){return TEBDLC_FORBIDDEN_OPERATION;}
tebdlc_status tebdlc_fractional_div_forbidden(void){return TEBDLC_FORBIDDEN_OPERATION;}
