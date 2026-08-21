/* Jonathan Therrien, Marieville, Québec. */
#ifndef TEBDLC_EXO_BRIDGE_H
#define TEBDLC_EXO_BRIDGE_H
#include <gmp.h>
#include "../impotent/tebdlc_impotent.h"
#include "../stagnation/tebdlc_stagnation.h"

typedef enum {
    TEBDLC_EXO_OK=0,
    TEBDLC_EXO_INVALID=1,
    TEBDLC_EXO_REVALIDATION_REQUIRED=2,
    TEBDLC_EXO_PROOF_REJECTED=3
} tebdlc_exo_status;

typedef struct {
    mpq_t mass;
    tebdlc_imp_mass_relation relation_to_one;
    int original_unitary_attained;
    int original_integrability_proven;
    char *origin_integration_model;
    char *origin_target_unit;
    char *origin_context;
    int initialized;
} tebdlc_exo_origin_snapshot;

typedef struct {
    tebdlc_exo_origin_snapshot origin;
    char *call_integration_model;
    char *call_target_unit;
    char *call_context;
    int call_integrability_proven;
    int call_unitary_attained;
    int historical_origin_preserved;
} tebdlc_exo_reactivation;

void tebdlc_exo_reactivation_init(tebdlc_exo_reactivation *r);
void tebdlc_exo_reactivation_clear(tebdlc_exo_reactivation *r);
tebdlc_exo_status tebdlc_exo_capture_impotent_origin(const tebdlc_imp_set *set,const tebdlc_imp_assessment *assessment,tebdlc_exo_reactivation *out);
tebdlc_exo_status tebdlc_exo_reactivate_for_unit(tebdlc_exo_reactivation *r,const char *call_integration_model,const char *call_target_unit,const char *call_context);
tebdlc_exo_status tebdlc_exo_revalidate_new_unit(tebdlc_exo_reactivation *r,int coherent,int coverage_complete,int compatible,int completeness_proven);
int tebdlc_exo_origin_still_impotent(const tebdlc_exo_reactivation *r);
#endif
