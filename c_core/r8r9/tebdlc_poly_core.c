/* Jonathan Therrien, Marieville, Québec. */
#include "tebdlc_poly_core.h"

#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static uint64_t gcd_u64(uint64_t a, uint64_t b) {
    while (b != 0U) { uint64_t t = a % b; a = b; b = t; }
    return a;
}
static uint64_t bits_u64(uint64_t x) {
    uint64_t bits = 0U;
    do { ++bits; x >>= 1U; } while (x != 0U);
    return bits;
}
static int same_text(const char *a, const char *b) {
    if (a == NULL || b == NULL) return a == b;
    return strcmp(a, b) == 0;
}
static int contexts_equal(const tebdlc_poly_context *a, const tebdlc_poly_context *b) {
    return same_text(a->domain,b->domain) && same_text(a->dimension,b->dimension) &&
           same_text(a->unit,b->unit) && same_text(a->reference,b->reference) &&
           same_text(a->context,b->context);
}
static int provenance_contains(const tebdlc_poly_provenance *p, const char *s) {
    for (size_t i=0; i<p->count; ++i) if (strcmp(p->items[i],s)==0) return 1;
    return 0;
}
static void provenance_sort(tebdlc_poly_provenance *p) {
    for (size_t i=0; i<p->count; ++i) for (size_t j=i+1; j<p->count; ++j)
        if (strcmp(p->items[i],p->items[j])>0) { const char *t=p->items[i]; p->items[i]=p->items[j]; p->items[j]=t; }
}
static tebdlc_poly_status provenance_merge(const tebdlc_poly_provenance *a, const tebdlc_poly_provenance *b, tebdlc_poly_provenance *out) {
    memset(out,0,sizeof(*out));
    const tebdlc_poly_provenance *src[2]={a,b};
    for (size_t s=0;s<2;++s) for (size_t i=0;i<src[s]->count;++i) {
        const char *item=src[s]->items[i]; if (!item) return TEBDLC_POLY_INVALID_REPRESENTATION;
        if (!provenance_contains(out,item)) {
            if (out->count>=TEBDLC_POLY_MAX_PROVENANCE) return TEBDLC_POLY_PROVENANCE_CAPACITY_REQUIRED;
            out->items[out->count++]=item;
        }
    }
    provenance_sort(out); return TEBDLC_POLY_OK;
}
static int genealogy_contains(const tebdlc_poly_genealogy *g, uint64_t id) {
    for (size_t i=0;i<g->count;++i) if (g->node_ids[i]==id) return 1;
    return 0;
}
static tebdlc_poly_status genealogy_merge(const tebdlc_poly_genealogy *a, uint64_t aid, const tebdlc_poly_genealogy *b, uint64_t bid, uint64_t result_id, tebdlc_poly_genealogy *out) {
    memset(out,0,sizeof(*out));
    const tebdlc_poly_genealogy *src[2]={a,b};
    uint64_t roots[2]={aid,bid};
    for(size_t s=0;s<2;++s){
        for(size_t i=0;i<src[s]->count;++i){ uint64_t id=src[s]->node_ids[i]; if(!genealogy_contains(out,id)){ if(out->count>=TEBDLC_POLY_MAX_GENEALOGY)return TEBDLC_POLY_GENEALOGY_CAPACITY_REQUIRED; out->node_ids[out->count++]=id; }}
        if(roots[s]!=0U && !genealogy_contains(out,roots[s])){ if(out->count>=TEBDLC_POLY_MAX_GENEALOGY)return TEBDLC_POLY_GENEALOGY_CAPACITY_REQUIRED; out->node_ids[out->count++]=roots[s]; }
    }
    if(result_id!=0U && !genealogy_contains(out,result_id)){ if(out->count>=TEBDLC_POLY_MAX_GENEALOGY)return TEBDLC_POLY_GENEALOGY_CAPACITY_REQUIRED; out->node_ids[out->count++]=result_id; }
    return TEBDLC_POLY_OK;
}
static tebdlc_poly_status validate_u64(const tebdlc_poly_u64_gain *g){
    if(!g || g->denominator==0U || g->numerator==0U || g->numerator>=g->denominator) return TEBDLC_POLY_INVALID_REPRESENTATION;
    if(!g->typing.domain||!g->typing.dimension||!g->typing.unit||!g->typing.reference||!g->typing.context) return TEBDLC_POLY_INVALID_REPRESENTATION;
    if(g->typing.provenance.count>TEBDLC_POLY_MAX_PROVENANCE || g->genealogy.count>TEBDLC_POLY_MAX_GENEALOGY) return TEBDLC_POLY_INVALID_REPRESENTATION;
    return TEBDLC_POLY_OK;
}

void tebdlc_poly_big_init(tebdlc_poly_big_gain *g){
    if (!g) return;
    memset(g,0,sizeof(*g));
    mpz_init(g->numerator);
    mpz_init(g->denominator);
    g->initialized=1;
}
void tebdlc_poly_big_clear(tebdlc_poly_big_gain *g){
    if(g && g->initialized){ mpz_clear(g->numerator); mpz_clear(g->denominator); g->initialized=0; }
}

tebdlc_poly_status tebdlc_poly_promote_u64(const tebdlc_poly_u64_gain *src, tebdlc_poly_big_gain *dst){
    if(validate_u64(src)!=TEBDLC_POLY_OK || !dst || !dst->initialized) return TEBDLC_POLY_INVALID_REPRESENTATION;
    mpz_set_ui(dst->numerator,src->numerator); mpz_set_ui(dst->denominator,src->denominator);
    dst->typing=src->typing; dst->genealogy=src->genealogy; dst->node_id=src->node_id; return TEBDLC_POLY_OK;
}

tebdlc_poly_u64_result tebdlc_poly_u64_multiply(const tebdlc_poly_u64_gain *a,const tebdlc_poly_u64_gain *b,uint64_t result_node_id){
    tebdlc_poly_u64_result r; memset(&r,0,sizeof(r));
    if (a) r.left=*a;
    if (b) r.right=*b;
    if(validate_u64(a)!=TEBDLC_POLY_OK||validate_u64(b)!=TEBDLC_POLY_OK){r.status=TEBDLC_POLY_INVALID_REPRESENTATION;return r;}
    if(!contexts_equal(&a->typing,&b->typing)){r.status=TEBDLC_POLY_INCOMPATIBLE_CONTEXT;return r;}
    uint64_t an=a->numerator,ad=a->denominator,bn=b->numerator,bd=b->denominator;
    uint64_t g1=gcd_u64(an,bd); an/=g1; bd/=g1; uint64_t g2=gcd_u64(bn,ad); bn/=g2; ad/=g2;
    if(an!=0U&&bn>UINT64_MAX/an){r.status=TEBDLC_POLY_CAPACITY_EXPANSION_REQUIRED;r.required_num_bits_upper_bound=bits_u64(an)+bits_u64(bn);r.required_den_bits_upper_bound=bits_u64(ad)+bits_u64(bd);return r;}
    if(ad!=0U&&bd>UINT64_MAX/ad){r.status=TEBDLC_POLY_CAPACITY_EXPANSION_REQUIRED;r.required_num_bits_upper_bound=bits_u64(an)+bits_u64(bn);r.required_den_bits_upper_bound=bits_u64(ad)+bits_u64(bd);return r;}
    uint64_t n=an*bn,d=ad*bd; if(n==0U||d==0U||n>=d){r.status=TEBDLC_POLY_INVALID_REPRESENTATION;return r;}
    uint64_t g=gcd_u64(n,d); n/=g; d/=g;
    r.value.numerator=n;r.value.denominator=d;r.value.typing=a->typing;r.value.node_id=result_node_id;
    tebdlc_poly_status ps=provenance_merge(&a->typing.provenance,&b->typing.provenance,&r.value.typing.provenance); if(ps!=TEBDLC_POLY_OK){r.status=ps;return r;}
    tebdlc_poly_status gs=genealogy_merge(&a->genealogy,a->node_id,&b->genealogy,b->node_id,result_node_id,&r.value.genealogy); if(gs!=TEBDLC_POLY_OK){r.status=gs;return r;}
    r.status=TEBDLC_POLY_OK;return r;
}

tebdlc_poly_status tebdlc_poly_big_validate(const tebdlc_poly_big_gain *g){
    if(!g||!g->initialized) return TEBDLC_POLY_INVALID_REPRESENTATION;
    if(mpz_sgn(g->numerator)<=0||mpz_sgn(g->denominator)<=0||mpz_cmp(g->numerator,g->denominator)>=0) return TEBDLC_POLY_INVALID_REPRESENTATION;
    if(!g->typing.domain||!g->typing.dimension||!g->typing.unit||!g->typing.reference||!g->typing.context) return TEBDLC_POLY_INVALID_REPRESENTATION;
    return TEBDLC_POLY_OK;
}

tebdlc_poly_status tebdlc_poly_big_multiply(const tebdlc_poly_big_gain *a,const tebdlc_poly_big_gain *b,uint64_t result_node_id,tebdlc_poly_big_gain *out){
    if(tebdlc_poly_big_validate(a)!=TEBDLC_POLY_OK||tebdlc_poly_big_validate(b)!=TEBDLC_POLY_OK||!out||!out->initialized) return TEBDLC_POLY_INVALID_REPRESENTATION;
    if(!contexts_equal(&a->typing,&b->typing)) return TEBDLC_POLY_INCOMPATIBLE_CONTEXT;
    mpz_t an,ad,bn,bd,g,t; mpz_inits(an,ad,bn,bd,g,t,NULL);
    mpz_set(an,a->numerator);mpz_set(ad,a->denominator);mpz_set(bn,b->numerator);mpz_set(bd,b->denominator);
    mpz_gcd(g,an,bd);mpz_divexact(an,an,g);mpz_divexact(bd,bd,g);
    mpz_gcd(g,bn,ad);mpz_divexact(bn,bn,g);mpz_divexact(ad,ad,g);
    mpz_mul(out->numerator,an,bn);mpz_mul(out->denominator,ad,bd);
    mpz_gcd(g,out->numerator,out->denominator);mpz_divexact(out->numerator,out->numerator,g);mpz_divexact(out->denominator,out->denominator,g);
    out->typing=a->typing; out->node_id=result_node_id;
    tebdlc_poly_status ps=provenance_merge(&a->typing.provenance,&b->typing.provenance,&out->typing.provenance);
    tebdlc_poly_status gs=genealogy_merge(&a->genealogy,a->node_id,&b->genealogy,b->node_id,result_node_id,&out->genealogy);
    mpz_clears(an,ad,bn,bd,g,t,NULL);
    if (ps!=TEBDLC_POLY_OK) return ps;
    if (gs!=TEBDLC_POLY_OK) return gs;
    return tebdlc_poly_big_validate(out);
}

tebdlc_poly_status tebdlc_poly_resume_multiply_exact(const tebdlc_poly_u64_result *event,uint64_t result_node_id,tebdlc_poly_big_gain *out){
    if(!event||event->status!=TEBDLC_POLY_CAPACITY_EXPANSION_REQUIRED||!out||!out->initialized) return TEBDLC_POLY_INVALID_REPRESENTATION;
    tebdlc_poly_big_gain a,b; tebdlc_poly_big_init(&a);tebdlc_poly_big_init(&b);
    tebdlc_poly_status s1=tebdlc_poly_promote_u64(&event->left,&a),s2=tebdlc_poly_promote_u64(&event->right,&b),s=TEBDLC_POLY_INVALID_REPRESENTATION;
    if(s1==TEBDLC_POLY_OK&&s2==TEBDLC_POLY_OK) s=tebdlc_poly_big_multiply(&a,&b,result_node_id,out);
    tebdlc_poly_big_clear(&a);tebdlc_poly_big_clear(&b);return s;
}
int tebdlc_poly_big_equal_value(const tebdlc_poly_big_gain *a,const tebdlc_poly_big_gain *b){
    if(tebdlc_poly_big_validate(a)!=TEBDLC_POLY_OK||tebdlc_poly_big_validate(b)!=TEBDLC_POLY_OK)return 0;
    return mpz_cmp(a->numerator,b->numerator)==0&&mpz_cmp(a->denominator,b->denominator)==0;
}
char *tebdlc_poly_big_canonical(const tebdlc_poly_big_gain *g){
    if(tebdlc_poly_big_validate(g)!=TEBDLC_POLY_OK)return NULL;
    char *n=mpz_get_str(NULL,10,g->numerator),*d=mpz_get_str(NULL,10,g->denominator); if(!n||!d){free(n);free(d);return NULL;}
    size_t len=strlen(n)+strlen(d)+2U; char *s=(char*)malloc(len); if(s) snprintf(s,len,"%s/%s",n,d); free(n);free(d);return s;
}
