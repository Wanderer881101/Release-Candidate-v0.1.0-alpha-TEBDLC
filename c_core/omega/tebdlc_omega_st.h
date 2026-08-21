/* Jonathan Therrien, Marieville, Québec. */
#ifndef TEBDLC_OMEGA_ST_H
#define TEBDLC_OMEGA_ST_H
#include <stddef.h>
#include <stdint.h>
#include "../productivity/tebdlc_productivity.h"
#define TEBDLC_OMEGA_MAX_FACTORS TEBDLC_PX_MAX_FACTORS
typedef struct {
    size_t factor_count;
    size_t total_occurrences;
    size_t factorized_repetition_count;
    uint64_t structural_bits;
    uint64_t occurrence_bits;
    uint64_t omega_st_bits;
    int exact_reconstructibility_required;
} tebdlc_omega_st_measure;
uint64_t tebdlc_omega_uleb128_bits(uint64_t value);
uint64_t tebdlc_omega_string_bits(const char *s);
uint64_t tebdlc_omega_factor_structural_bits(const tebdlc_px_factor *f);
uint64_t tebdlc_omega_factor_occurrence_bits(const tebdlc_px_factor *f);
int tebdlc_omega_measure(const tebdlc_px_ledger *ledger, tebdlc_omega_st_measure *out);
#endif
