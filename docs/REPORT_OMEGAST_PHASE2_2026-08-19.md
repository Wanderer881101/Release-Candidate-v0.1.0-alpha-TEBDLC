# RAPPORT EXPÉRIMENTAL — ΩSt Phase 2

**Jonathan Therrien, Marieville, Québec.**

Objet : stress structurel/historique de `ΩSt_candidate_bits` via le ledger de productivité réel.

Résultats canoniques observés : `rep100=992`, `rep400=3400`, `gap100(step=128)=1784`, `mix10x10=2000`, `mix20x5=3440`, `distinct64=9488` bits.

À 100 occurrences constantes : `1 facteur < 10 facteurs < 20 facteurs` en coût d'encodage candidat. À 100 occurrences et une signature constante, des deltas de séquence 128 coûtent plus que des deltas 1 parce que l'histoire exacte reste reconstructible.

Validation : GCC 3/3, Clang 3/3, Python 3/3, UBSan PASS, ASan/leak PASS.

Statut : résultat reproductible dans le domaine testé; ΩSt reste métrique candidate relative à son encodage, non preuve universelle.
