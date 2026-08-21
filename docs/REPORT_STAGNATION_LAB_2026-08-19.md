# RAPPORT LAB — Stagnation, compression, réactivation et revalidation

**Jonathan Therrien, Marieville, Québec.**

## Objet
Éprouver le cycle exploratoire R6 : `ACTIVE → STAGNATED → COMPRESSED → REACTIVATED → REVALIDATED`, sans écraser le contexte d'origine et sans réutiliser automatiquement un ancien résultat.

## Construction
- sérialisation canonique binaire longueur-préfixée du gain exact, métadonnées, provenance, généalogie et node id;
- SHA-256 du contenu canonique;
- compression zlib sans perte;
- décompression avec vérification de longueur, SHA-256 et égalité octet-à-octet avec le canon original;
- contexte d'origine conservé séparément du contexte d'appel;
- réactivation retourne explicitement `REVALIDATION_REQUIRED`;
- revalidation négative restagne; revalidation positive produit `REVALIDATED`;
- corruption volontaire du flux compressé refusée.

## Résultats
- canon test : 325 octets;
- représentation compressée : 137 octets;
- GCC : 3/3 PASS identiques;
- Clang : 3/3 PASS identiques à GCC;
- UBSan : aucun diagnostic;
- ASan + leak detection : aucun diagnostic;
- contexte d'origine `C-origin` préservé pendant un appel `C-call-new`;
- aucune activation automatique après réactivation;
- corruption compressée détectée.

## Interprétation
Le jalon fournit un témoin exécutable de `compression ≠ perte nécessaire`, `réactivation ≠ réutilisation aveugle` et `contexte d'appel ≠ remplacement du contexte d'origine` sur le domaine testé.

## Limites
- format canonique `TST1` expérimental;
- le canon non compressé reste encore en mémoire pour la vérification stricte;
- la revalidation est une preuve externe, pas encore un moteur autonome;
- Relation/Preuve/Transformation ne sont pas encore sérialisés comme objets indépendants;
- `ΩSt` et l'assimilation comportementale ne sont pas encore implémentés.
