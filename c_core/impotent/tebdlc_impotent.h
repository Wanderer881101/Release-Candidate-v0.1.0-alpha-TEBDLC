/* Jonathan Therrien, Marieville, Québec. */
#ifndef TEBDLC_IMPOTENT_H
#define TEBDLC_IMPOTENT_H
#include <stddef.h>
#include <stdint.h>
#include <gmp.h>
#include "../r8r9/tebdlc_poly_core.h"
#define TEBDLC_IMP_MAX_MEMBERS 128U
typedef enum { TEBDLC_IMP_OK=0, TEBDLC_IMP_INVALID=1, TEBDLC_IMP_INCOMPATIBLE_REFERENCE=2, TEBDLC_IMP_MEMBER_CAPACITY_REQUIRED=3, TEBDLC_IMP_PROOF_REQUIRED=4 } tebdlc_imp_status;
typedef enum { TEBDLC_IMP_MASS_LT_ONE=-1, TEBDLC_IMP_MASS_EQ_ONE=0, TEBDLC_IMP_MASS_GT_ONE=1 } tebdlc_imp_mass_relation;
typedef struct { tebdlc_poly_big_gain *members[TEBDLC_IMP_MAX_MEMBERS]; size_t count; const char *integration_model; const char *target_unit; } tebdlc_imp_set;
typedef struct { mpq_t mass; tebdlc_imp_mass_relation relation_to_one; int unitary_attained; int integrability_proven; size_t member_count; int initialized; } tebdlc_imp_assessment;
void tebdlc_imp_assessment_init(tebdlc_imp_assessment *a);
void tebdlc_imp_assessment_clear(tebdlc_imp_assessment *a);
tebdlc_imp_status tebdlc_imp_describe_mass(const tebdlc_imp_set *set, tebdlc_imp_assessment *out);
tebdlc_imp_status tebdlc_imp_apply_integrability_proof(tebdlc_imp_assessment *assessment, int coherent, int coverage_complete, int compatible, int completeness_proven);
#endif
