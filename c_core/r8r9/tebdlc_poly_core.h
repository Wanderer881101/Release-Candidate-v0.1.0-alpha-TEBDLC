/* Jonathan Therrien, Marieville, Québec. */
#ifndef TEBDLC_POLY_CORE_H
#define TEBDLC_POLY_CORE_H

#include <stddef.h>
#include <stdint.h>
#include <gmp.h>

#define TEBDLC_POLY_MAX_PROVENANCE 32U
#define TEBDLC_POLY_MAX_GENEALOGY 4096U

typedef enum {
    TEBDLC_POLY_OK = 0,
    TEBDLC_POLY_CAPACITY_EXPANSION_REQUIRED = 1,
    TEBDLC_POLY_FORBIDDEN_OPERATION = 2,
    TEBDLC_POLY_INCOMPATIBLE_CONTEXT = 3,
    TEBDLC_POLY_INVALID_REPRESENTATION = 4,
    TEBDLC_POLY_PROVENANCE_CAPACITY_REQUIRED = 5,
    TEBDLC_POLY_GENEALOGY_CAPACITY_REQUIRED = 6,
    TEBDLC_POLY_ALLOCATION_FAILURE = 7
} tebdlc_poly_status;

typedef struct {
    const char *items[TEBDLC_POLY_MAX_PROVENANCE];
    size_t count;
} tebdlc_poly_provenance;

typedef struct {
    uint64_t node_ids[TEBDLC_POLY_MAX_GENEALOGY];
    size_t count;
} tebdlc_poly_genealogy;

typedef struct {
    const char *domain;
    const char *dimension;
    const char *unit;
    const char *reference;
    const char *context;
    tebdlc_poly_provenance provenance;
} tebdlc_poly_context;

typedef struct {
    uint64_t numerator;
    uint64_t denominator;
    tebdlc_poly_context typing;
    tebdlc_poly_genealogy genealogy;
    uint64_t node_id;
} tebdlc_poly_u64_gain;

typedef struct {
    mpz_t numerator;
    mpz_t denominator;
    tebdlc_poly_context typing;
    tebdlc_poly_genealogy genealogy;
    uint64_t node_id;
    int initialized;
} tebdlc_poly_big_gain;

typedef struct {
    tebdlc_poly_status status;
    tebdlc_poly_u64_gain value;
    tebdlc_poly_u64_gain left;
    tebdlc_poly_u64_gain right;
    uint64_t required_num_bits_upper_bound;
    uint64_t required_den_bits_upper_bound;
} tebdlc_poly_u64_result;

void tebdlc_poly_big_init(tebdlc_poly_big_gain *g);
void tebdlc_poly_big_clear(tebdlc_poly_big_gain *g);
tebdlc_poly_status tebdlc_poly_promote_u64(const tebdlc_poly_u64_gain *src, tebdlc_poly_big_gain *dst);
tebdlc_poly_u64_result tebdlc_poly_u64_multiply(const tebdlc_poly_u64_gain *a, const tebdlc_poly_u64_gain *b, uint64_t result_node_id);
tebdlc_poly_status tebdlc_poly_big_multiply(const tebdlc_poly_big_gain *a, const tebdlc_poly_big_gain *b, uint64_t result_node_id, tebdlc_poly_big_gain *out);
tebdlc_poly_status tebdlc_poly_resume_multiply_exact(const tebdlc_poly_u64_result *event, uint64_t result_node_id, tebdlc_poly_big_gain *out);
tebdlc_poly_status tebdlc_poly_big_validate(const tebdlc_poly_big_gain *g);
int tebdlc_poly_big_equal_value(const tebdlc_poly_big_gain *a, const tebdlc_poly_big_gain *b);
char *tebdlc_poly_big_canonical(const tebdlc_poly_big_gain *g);

#endif
