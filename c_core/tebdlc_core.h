/* Jonathan Therrien, Marieville, Québec. */
#ifndef TEBDLC_CORE_H
#define TEBDLC_CORE_H

#include <stdint.h>
#include <stddef.h>

#define TEBDLC_MAX_PROVENANCE 16U

typedef enum {
    TEBDLC_OK = 0,
    TEBDLC_CAPACITY_EXPANSION_REQUIRED = 1,
    TEBDLC_FORBIDDEN_OPERATION = 2,
    TEBDLC_INCOMPATIBLE_CONTEXT = 3,
    TEBDLC_INVALID_REPRESENTATION = 4,
    TEBDLC_PROVENANCE_CAPACITY_REQUIRED = 5
} tebdlc_status;

typedef struct {
    const char *items[TEBDLC_MAX_PROVENANCE];
    size_t count;
} tebdlc_provenance;

typedef struct {
    const char *domain;
    const char *dimension;
    const char *unit;
    const char *reference;
    const char *context;
    tebdlc_provenance provenance;
} tebdlc_context;

typedef struct {
    uint64_t numerator;
    uint64_t denominator;
    tebdlc_context typing;
} tebdlc_fractional_gain;

typedef struct {
    tebdlc_status status;
    tebdlc_fractional_gain value;
    tebdlc_fractional_gain left;
    tebdlc_fractional_gain right;
    uint64_t required_num_bits;
    uint64_t required_den_bits;
    size_t required_provenance_capacity;
} tebdlc_fractional_result;

tebdlc_status tebdlc_fractional_validate(const tebdlc_fractional_gain *gain);
int tebdlc_fractional_composable(const tebdlc_fractional_gain *a, const tebdlc_fractional_gain *b);
tebdlc_fractional_result tebdlc_fractional_multiply(const tebdlc_fractional_gain *a, const tebdlc_fractional_gain *b);
tebdlc_status tebdlc_fractional_add_forbidden(void);
tebdlc_status tebdlc_fractional_sub_forbidden(void);
tebdlc_status tebdlc_fractional_div_forbidden(void);

#endif
