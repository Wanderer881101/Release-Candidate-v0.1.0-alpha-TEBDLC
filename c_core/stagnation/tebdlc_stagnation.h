/* Jonathan Therrien, Marieville, Québec. */
#ifndef TEBDLC_STAGNATION_H
#define TEBDLC_STAGNATION_H
#include <stddef.h>
#include <stdint.h>
#include "../r8r9/tebdlc_poly_core.h"
typedef enum { TEBDLC_ST_ACTIVE=0, TEBDLC_ST_STAGNATED=1, TEBDLC_ST_COMPRESSED=2, TEBDLC_ST_REACTIVATED=3, TEBDLC_ST_REVALIDATED=4 } tebdlc_st_state;
typedef enum { TEBDLC_ST_OK=0, TEBDLC_ST_INVALID=1, TEBDLC_ST_ALLOC=2, TEBDLC_ST_COMPRESS_FAIL=3, TEBDLC_ST_DECOMPRESS_FAIL=4, TEBDLC_ST_INTEGRITY_FAIL=5, TEBDLC_ST_REVALIDATION_REQUIRED=6 } tebdlc_st_status;
typedef struct { unsigned char *canonical; size_t canonical_len; unsigned char *compressed; size_t compressed_len; unsigned char sha256[32]; tebdlc_st_state state; char *origin_context; char *call_context; } tebdlc_st_archive;
void tebdlc_st_archive_init(tebdlc_st_archive *a);
void tebdlc_st_archive_clear(tebdlc_st_archive *a);
tebdlc_st_status tebdlc_st_stagnate_gain(const tebdlc_poly_big_gain *gain, tebdlc_st_archive *out);
tebdlc_st_status tebdlc_st_compress(tebdlc_st_archive *a);
tebdlc_st_status tebdlc_st_decompress_verify(tebdlc_st_archive *a);
tebdlc_st_status tebdlc_st_reactivate(tebdlc_st_archive *a,const char *call_context);
tebdlc_st_status tebdlc_st_revalidate(tebdlc_st_archive *a,int proof_valid,int *became_active);
#endif
