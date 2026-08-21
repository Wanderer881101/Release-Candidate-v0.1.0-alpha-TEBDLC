/* Jonathan Therrien, Marieville, Québec. */
#include "tebdlc_poly_core.h"
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static tebdlc_poly_u64_gain ugain(uint64_t n,uint64_t d,const char *ctx,const char *prov,uint64_t node){
    tebdlc_poly_u64_gain g; memset(&g,0,sizeof(g));
    g.numerator=n;g.denominator=d;g.node_id=node;
    g.typing.domain="integrity";g.typing.dimension="coverage";g.typing.unit="ratio";g.typing.reference="R9-poly";g.typing.context=ctx;
    if(prov){g.typing.provenance.items[0]=prov;g.typing.provenance.count=1;}
    return g;
}
static void test_r8_capacity_resume_exact(void){
    const uint64_t n=UINT64_C(4294967295),d=UINT64_C(4294967297);
    tebdlc_poly_u64_gain a=ugain(n,d,"C","A",1),b=ugain(n,d,"C","B",2);
    tebdlc_poly_u64_result ev=tebdlc_poly_u64_multiply(&a,&b,3);
    assert(ev.status==TEBDLC_POLY_CAPACITY_EXPANSION_REQUIRED);
    tebdlc_poly_big_gain out;tebdlc_poly_big_init(&out);
    assert(tebdlc_poly_resume_multiply_exact(&ev,3,&out)==TEBDLC_POLY_OK);
    assert(mpz_cmp_ui(out.numerator,1U)>0); assert(mpz_cmp(out.numerator,out.denominator)<0);
    mpz_t en,ed;mpz_inits(en,ed,NULL);mpz_set_ui(en,n);mpz_mul(en,en,en);mpz_set_ui(ed,d);mpz_mul(ed,ed,ed);
    assert(mpz_cmp(out.numerator,en)==0&&mpz_cmp(out.denominator,ed)==0);
    assert(out.typing.provenance.count==2U);
    assert(out.genealogy.count==3U);
    mpz_clears(en,ed,NULL);tebdlc_poly_big_clear(&out);
}

static void test_r9_same_value_distinct_genealogy(void){
    tebdlc_poly_u64_gain a=ugain(1,2,"C","A",11),b=ugain(1,3,"C","B",12),c=ugain(1,3,"C","C",21),d=ugain(1,2,"C","D",22);
    tebdlc_poly_u64_result r1=tebdlc_poly_u64_multiply(&a,&b,13),r2=tebdlc_poly_u64_multiply(&c,&d,23);
    assert(r1.status==TEBDLC_POLY_OK&&r2.status==TEBDLC_POLY_OK);
    assert(r1.value.numerator==r2.value.numerator&&r1.value.denominator==r2.value.denominator);
    assert(r1.value.genealogy.count==3U&&r2.value.genealogy.count==3U);
    assert(r1.value.genealogy.node_ids[0]!=r2.value.genealogy.node_ids[0]);
    assert(strcmp(r1.value.typing.provenance.items[0],r2.value.typing.provenance.items[0])!=0);
}

static void test_r9_context_boundary(void){
    tebdlc_poly_u64_gain a=ugain(3,10,"A","A",30),b=ugain(3,10,"B","B",31);
    assert(tebdlc_poly_u64_multiply(&a,&b,32).status==TEBDLC_POLY_INCOMPATIBLE_CONTEXT);
}

static void test_fracto_recursive_3_10_depths(void){
    const int depths[]={1,2,10,100,1000};
    for(size_t di=0;di<sizeof(depths)/sizeof(depths[0]);++di){
        int depth=depths[di];
        tebdlc_poly_big_gain base,cur,next;tebdlc_poly_big_init(&base);tebdlc_poly_big_init(&cur);tebdlc_poly_big_init(&next);
        tebdlc_poly_u64_gain ub=ugain(3,10,"recursive","root",1000);
        assert(tebdlc_poly_promote_u64(&ub,&base)==TEBDLC_POLY_OK);
        assert(tebdlc_poly_promote_u64(&ub,&cur)==TEBDLC_POLY_OK);
        for(int k=2;k<=depth;k++){
            assert(tebdlc_poly_big_multiply(&cur,&base,(uint64_t)(1000+k),&next)==TEBDLC_POLY_OK);
            mpz_set(cur.numerator,next.numerator);mpz_set(cur.denominator,next.denominator);cur.typing=next.typing;cur.genealogy=next.genealogy;cur.node_id=next.node_id;
        }
        mpz_t pn,pd;mpz_inits(pn,pd,NULL);mpz_ui_pow_ui(pn,3U,(unsigned long)depth);mpz_ui_pow_ui(pd,10U,(unsigned long)depth);
        assert(mpz_cmp(cur.numerator,pn)==0&&mpz_cmp(cur.denominator,pd)==0);
        assert(mpz_sgn(cur.numerator)>0&&mpz_cmp(cur.numerator,cur.denominator)<0);
        printf("depth=%d num_bits=%zu den_bits=%zu genealogy=%zu\n",depth,mpz_sizeinbase(cur.numerator,2),mpz_sizeinbase(cur.denominator,2),cur.genealogy.count);
        mpz_clears(pn,pd,NULL);tebdlc_poly_big_clear(&base);tebdlc_poly_big_clear(&cur);tebdlc_poly_big_clear(&next);
    }
}

static void test_native_to_big_resume_then_continue(void){
    const int target_depth=1000;
    tebdlc_poly_u64_gain base_u=ugain(3,10,"hybrid","root",5000);
    tebdlc_poly_u64_gain cur_u=base_u;
    tebdlc_poly_big_gain base_b,cur_b,next_b;
    tebdlc_poly_big_init(&base_b); tebdlc_poly_big_init(&cur_b); tebdlc_poly_big_init(&next_b);
    assert(tebdlc_poly_promote_u64(&base_u,&base_b)==TEBDLC_POLY_OK);
    int promoted=0;
    int transition_depth=0;
    for(int depth=2;depth<=target_depth;depth++){
        if(!promoted){
            tebdlc_poly_u64_result r=tebdlc_poly_u64_multiply(&cur_u,&base_u,(uint64_t)(5000+depth));
            if(r.status==TEBDLC_POLY_OK){ cur_u=r.value; }
            else {
                assert(r.status==TEBDLC_POLY_CAPACITY_EXPANSION_REQUIRED);
                transition_depth=depth;
                assert(tebdlc_poly_resume_multiply_exact(&r,(uint64_t)(5000+depth),&cur_b)==TEBDLC_POLY_OK);
                promoted=1;
            }
        } else {
            assert(tebdlc_poly_big_multiply(&cur_b,&base_b,(uint64_t)(5000+depth),&next_b)==TEBDLC_POLY_OK);
            mpz_set(cur_b.numerator,next_b.numerator); mpz_set(cur_b.denominator,next_b.denominator);
            cur_b.typing=next_b.typing; cur_b.genealogy=next_b.genealogy; cur_b.node_id=next_b.node_id;
        }
    }
    assert(promoted==1);
    assert(transition_depth==20);
    mpz_t pn,pd; mpz_inits(pn,pd,NULL); mpz_ui_pow_ui(pn,3U,1000U); mpz_ui_pow_ui(pd,10U,1000U);
    assert(mpz_cmp(cur_b.numerator,pn)==0 && mpz_cmp(cur_b.denominator,pd)==0);
    assert(cur_b.genealogy.count==1000U);
    printf("hybrid_transition_depth=%d final_num_bits=%zu final_den_bits=%zu genealogy=%zu\n",transition_depth,mpz_sizeinbase(cur_b.numerator,2),mpz_sizeinbase(cur_b.denominator,2),cur_b.genealogy.count);
    mpz_clears(pn,pd,NULL); tebdlc_poly_big_clear(&base_b); tebdlc_poly_big_clear(&cur_b); tebdlc_poly_big_clear(&next_b);
}

static void test_exhaustive_small_space_poly(void){
    unsigned long long count=0ULL;
    for(uint64_t da=2;da<=40;da++) for(uint64_t na=1;na<da;na++)
    for(uint64_t db=2;db<=40;db++) for(uint64_t nb=1;nb<db;nb++){
        tebdlc_poly_u64_gain a=ugain(na,da,"finite","A",7000),b=ugain(nb,db,"finite","B",7001);
        tebdlc_poly_u64_result r=tebdlc_poly_u64_multiply(&a,&b,7002);
        assert(r.status==TEBDLC_POLY_OK);
        assert(r.value.numerator>0U && r.value.numerator<r.value.denominator);
        assert(r.value.typing.provenance.count==2U);
        count++;
    }
    assert(count==608400ULL);
    printf("exhaustive_poly_pairs=%llu\n",count);
}

int main(void){
    test_r8_capacity_resume_exact();
    test_r9_same_value_distinct_genealogy();
    test_r9_context_boundary();
    test_fracto_recursive_3_10_depths();
    test_native_to_big_resume_then_continue();
    test_exhaustive_small_space_poly();
    puts("R8R9 poly-fractal/fracto-recursive tests: PASS");
    return 0;
}
