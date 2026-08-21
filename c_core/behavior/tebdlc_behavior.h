/* Jonathan Therrien, Marieville, Québec. */
#ifndef TEBDLC_BEHAVIOR_H
#define TEBDLC_BEHAVIOR_H
#include <stddef.h>
#include <stdint.h>

#define TEBDLC_BH_MAX_OBSERVATIONS 64U

typedef enum {
    TEBDLC_BH_STAGNATED=0,
    TEBDLC_BH_REVALIDATION_REQUIRED=1,
    TEBDLC_BH_PROOF_REJECTED=2,
    TEBDLC_BH_INTEGRABLE=3
} tebdlc_bh_outcome;

typedef enum {
    TEBDLC_BH_OK=0,
    TEBDLC_BH_INVALID=1,
    TEBDLC_BH_CAPACITY=2,
    TEBDLC_BH_CONTRADICTORY=3
} tebdlc_bh_status;

typedef struct {
    uint64_t sequence;
    char *context;
    char *integration_model;
    char *target_unit;
    tebdlc_bh_outcome outcome;
    int coherent;
    int coverage_complete;
    int compatible;
    int completeness_proven;
} tebdlc_bh_observation;

typedef struct {
    tebdlc_bh_observation observations[TEBDLC_BH_MAX_OBSERVATIONS];
    size_t count;
} tebdlc_bh_history;

typedef struct {
    size_t source_observation_count;
    size_t integrable_count;
    size_t rejected_count;
    size_t stagnated_count;
    int all_integrable_observations_had_complete_proof;
    int incomplete_proof_never_promoted_unit;
    int observations_preserved;
    int identity_inference_permitted;
} tebdlc_bh_model;

void tebdlc_bh_history_init(tebdlc_bh_history *h);
void tebdlc_bh_history_clear(tebdlc_bh_history *h);
tebdlc_bh_status tebdlc_bh_record(
    tebdlc_bh_history *h,
    uint64_t sequence,
    const char *context,
    const char *integration_model,
    const char *target_unit,
    tebdlc_bh_outcome outcome,
    int coherent,
    int coverage_complete,
    int compatible,
    int completeness_proven);
tebdlc_bh_status tebdlc_bh_assimilate(const tebdlc_bh_history *h, tebdlc_bh_model *out);
int tebdlc_bh_history_equal_prefix(const tebdlc_bh_history *h, const tebdlc_bh_observation *snapshot, size_t n);
#endif
