# RAPPORT LAB — Gain impotent sur noyau R8/R9

**Jonathan Therrien, Marieville, Québec.**

## Objet
Éprouver IMP-1 à IMP-12 sur le noyau multi-précision R8/R9 sans assimiler la masse descriptive à une addition primitive de gains.

## Construction
Une couche séparée `tebdlc_impotent` agrège uniquement une masse descriptive rationnelle exacte (`mpq_t`) sur des gains partageant domaine, dimension, unité, référence et contexte. La masse ne modifie jamais `unitary_attained`.

L'unité exige un appel séparé de preuve d'intégrabilité comportant quatre conditions explicites : cohérence, couverture complète, compatibilité et complétude démontrée.

## Résultats observés
- `100/361 + 100/361 = 200/361 < 1`, unité = faux.
- `180/361 + 181/361 = 1`, unité = faux.
- `300/361 + 300/361 = 600/361 > 1`, unité = faux.
- `999999/1000003 + 999999/1000003 = 1999998/1000003 > 1`, unité = faux.
- une preuve incomplète est refusée et ne change pas l'unité;
- une preuve complète explicitement fournie peut changer le statut d'intégrabilité sans réécrire la masse;
- deux contextes incompatibles sont refusés avant consolidation descriptive.

## Répétabilité
- GCC : 3/3 PASS, sorties identiques.
- Clang : 3/3 PASS, sorties identiques à GCC.
- Python `fractions.Fraction` : concordance exacte des masses.
- Clang UBSan : PASS, aucun diagnostic.
- Clang ASan + leak detection : PASS, aucun diagnostic.

## Interprétation
Le jalon fournit un témoin exécutable de `quantité suffisante ⇏ intégrabilité suffisante` sur les cas testés. Les trois régimes de masse `<1`, `=1`, `>1` restent orthogonaux au statut d'unité.

## Limites
- corpus construit et fini;
- la preuve d'intégrabilité est actuellement une interface explicite, pas encore un moteur de preuve autonome;
- l'unité alternative cohérente n'est pas encore construite automatiquement;
- la relation `>TEBDLC` n'est pas canonisée comme opérateur;
- capacité de 128 membres dans cette expérience.
