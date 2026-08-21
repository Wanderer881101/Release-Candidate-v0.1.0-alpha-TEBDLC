/* Jonathan Therrien, Marieville, Québec. */
#ifndef TEBDLC_PRODUCTIVITY_H
#define TEBDLC_PRODUCTIVITY_H
#include <stddef.h>
#include <stdint.h>
#include "../behavior/tebdlc_behavior.h"
#define TEBDLC_PX_MAX_FACTORS 64U
#define TEBDLC_PX_MAX_OCCURRENCES 512U

typedef enum { TEBDLC_PX_OK=0, TEBDLC_PX_INVALID=1, TEBDLC_PX_CAPACITY=2 } tebdlc_px_status;
typedef struct {
    char *context;
    char *integration_model;
    char *target_unit;
    tebdlc_bh_outcome outcome;
    int coherent;
    int coverage_complete;
    int compatible;
    int completeness_proven;
    uint64_t sequences[TEBDLC_PX_MAX_OCCURRENCES];
    size_t occurrence_count;
} tebdlc_px_factor;
typedef struct {
    tebdlc_px_factor factors[TEBDLC_PX_MAX_FACTORS];
    size_t factor_count;
    size_t total_occurrences;
} tebdlc_px_ledger;

typedef struct {
    int productive;
    size_t factor_index;
    size_t occurrence_index;
} tebdlc_px_record_result;

void tebdlc_px_init(tebdlc_px_ledger *l);
void tebdlc_px_clear(tebdlc_px_ledger *l);
tebdlc_px_status tebdlc_px_record(tebdlc_px_ledger *l,const tebdlc_bh_observation *o,tebdlc_px_record_result *out);
const tebdlc_px_factor *tebdlc_px_find_by_sequence(const tebdlc_px_ledger *l,uint64_t sequence);
int tebdlc_px_reconstructs_all(const tebdlc_px_ledger *l,const tebdlc_bh_observation *events,size_t n);
#endif
