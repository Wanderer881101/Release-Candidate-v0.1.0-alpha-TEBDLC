# Jonathan Therrien, Marieville, Québec.
PYTHON ?= python3
CC ?= cc
CLANG ?= clang
BUILD_DIR ?= build
CFLAGS ?= -std=c11 -Wall -Wextra -Wpedantic -Werror -O2
SAN_CFLAGS ?= -std=c11 -Wall -Wextra -Wpedantic -Werror -O1 -fno-omit-frame-pointer

.PHONY: help setup build build-c test test-python test-c verify verify-oracles sanitize release-check clean check-deps dirs

help:
	@printf '%s\n' \
	  'TEBDLC product build targets:' \
	  '  make setup          Install Python package + pytest in current environment' \
	  '  make build          Compile Python bytecode and all C test executables' \
	  '  make test           Run Python and C tests' \
	  '  make verify         Run tests plus independent Python C-oracles' \
	  '  make sanitize       Run C verification under UBSan and ASan (Clang)' \
	  '  make release-check  Audit tracked product structure before release' \
	  '  make clean          Remove only locally generated build/cache artifacts'

setup:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install pytest
	$(PYTHON) -m pip install -e .

check-deps:
	@command -v $(PYTHON) >/dev/null || { echo 'missing Python'; exit 1; }
	@command -v $(CC) >/dev/null || { echo 'missing C compiler'; exit 1; }
	@printf '#include <gmp.h>\nint main(void){mpz_t x;mpz_init(x);mpz_clear(x);return 0;}\n' | $(CC) -x c - -lgmp -o $(BUILD_DIR).dep-gmp
	@printf '#include <openssl/evp.h>\nint main(void){return EVP_sha256()==0;}\n' | $(CC) -x c - -lcrypto -o $(BUILD_DIR).dep-crypto
	@printf '#include <zlib.h>\nint main(void){return zlibVersion()==0;}\n' | $(CC) -x c - -lz -o $(BUILD_DIR).dep-zlib
	@rm -f $(BUILD_DIR).dep-gmp $(BUILD_DIR).dep-crypto $(BUILD_DIR).dep-zlib

dirs:
	mkdir -p $(BUILD_DIR)/c

build: check-deps build-c
	$(PYTHON) -m compileall -q src tests

build-c: dirs
	$(CC) $(CFLAGS) c_core/tebdlc_core.c c_core/test_tebdlc_core.c -o $(BUILD_DIR)/c/test_core
	$(CC) $(CFLAGS) c_core/r8r9/tebdlc_poly_core.c c_core/r8r9/test_r8r9_poly.c -lgmp -o $(BUILD_DIR)/c/test_r8r9
	$(CC) $(CFLAGS) c_core/r8r9/tebdlc_poly_core.c c_core/impotent/tebdlc_impotent.c c_core/impotent/test_impotent.c -lgmp -o $(BUILD_DIR)/c/test_impotent
	$(CC) $(CFLAGS) c_core/r8r9/tebdlc_poly_core.c c_core/stagnation/tebdlc_stagnation.c c_core/stagnation/test_stagnation.c -lgmp -lcrypto -lz -o $(BUILD_DIR)/c/test_stagnation
	$(CC) $(CFLAGS) c_core/r8r9/tebdlc_poly_core.c c_core/impotent/tebdlc_impotent.c c_core/stagnation/tebdlc_stagnation.c c_core/exo/tebdlc_exo_bridge.c c_core/exo/test_exo_bridge.c -lgmp -lcrypto -lz -o $(BUILD_DIR)/c/test_exo
	$(CC) $(CFLAGS) c_core/r8r9/tebdlc_poly_core.c c_core/impotent/tebdlc_impotent.c c_core/exo/tebdlc_exo_bridge.c c_core/behavior/tebdlc_behavior.c c_core/behavior/test_behavior.c -lgmp -o $(BUILD_DIR)/c/test_behavior
	$(CC) $(CFLAGS) c_core/behavior/tebdlc_behavior.c c_core/productivity/tebdlc_productivity.c c_core/productivity/test_productivity.c -o $(BUILD_DIR)/c/test_productivity
	$(CC) $(CFLAGS) c_core/behavior/tebdlc_behavior.c c_core/productivity/tebdlc_productivity.c c_core/omega/tebdlc_omega_st.c c_core/omega/test_omega_st_phase2.c -o $(BUILD_DIR)/c/test_omega_phase2

test-python:
	$(PYTHON) -m pytest

test-c: build-c
	@set -e; for t in $(BUILD_DIR)/c/test_core $(BUILD_DIR)/c/test_r8r9 $(BUILD_DIR)/c/test_impotent $(BUILD_DIR)/c/test_stagnation $(BUILD_DIR)/c/test_exo $(BUILD_DIR)/c/test_behavior $(BUILD_DIR)/c/test_productivity $(BUILD_DIR)/c/test_omega_phase2; do echo "==> $$t"; "$$t"; done

test: test-python test-c

verify-oracles:
	$(PYTHON) c_core/r8r9/python_oracle_r8r9.py
	$(PYTHON) c_core/impotent/python_oracle_impotent.py
	$(PYTHON) c_core/exo/python_oracle_bridge.py
	$(PYTHON) c_core/behavior/python_oracle_behavior.py
	$(PYTHON) c_core/productivity/python_oracle_productivity.py
	$(PYTHON) c_core/omega/python_oracle_omega_st.py
	$(PYTHON) c_core/omega/python_oracle_omega_st_phase2.py

verify: test verify-oracles

sanitize:
	@command -v $(CLANG) >/dev/null || { echo 'clang is required for sanitize'; exit 1; }
	mkdir -p $(BUILD_DIR)/sanitize
	$(CLANG) $(SAN_CFLAGS) -fsanitize=undefined -fno-sanitize-recover=all c_core/behavior/tebdlc_behavior.c c_core/productivity/tebdlc_productivity.c c_core/omega/tebdlc_omega_st.c c_core/omega/test_omega_st_phase2.c -o $(BUILD_DIR)/sanitize/omega_ubsan
	$(BUILD_DIR)/sanitize/omega_ubsan
	$(CLANG) $(SAN_CFLAGS) -fsanitize=address c_core/behavior/tebdlc_behavior.c c_core/productivity/tebdlc_productivity.c c_core/omega/tebdlc_omega_st.c c_core/omega/test_omega_st_phase2.c -o $(BUILD_DIR)/sanitize/omega_asan
	ASAN_OPTIONS=detect_leaks=1 $(BUILD_DIR)/sanitize/omega_asan

release-check:
	$(PYTHON) tools/release_readiness.py

clean:
	rm -rf $(BUILD_DIR) .pytest_cache .mypy_cache .ruff_cache htmlcov
	find src tests c_core -type d -name __pycache__ -prune -exec rm -rf {} + 2>/dev/null || true
	find src tests c_core -type f \( -name '*.pyc' -o -name '*.pyo' \) -delete 2>/dev/null || true
