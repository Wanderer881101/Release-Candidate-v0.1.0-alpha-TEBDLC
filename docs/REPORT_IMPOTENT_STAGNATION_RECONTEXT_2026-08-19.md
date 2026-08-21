# Rapport expérimental — raccord gain impotent / stagnation / recontextualisation

**Jonathan Therrien, Marieville, Québec.**

## Objet
Tester concrètement le cas doctrinal suivant sans réécriture historique : un ensemble de gains est impotent relativement à `U1`, stagne, est compressé puis réactivé dans un nouveau contexte d'appel visant `U2`; une nouvelle preuve peut rendre `U2` intégrable sans rendre rétroactivement `U1` intégrable.

## Chaîne testée

`P(U1,C-origin) -> impotent -> stagnated/compressed -> decompression verified -> reactivated(C-call-new,U2) -> revalidation required -> proof rejected -> proof accepted for U2`

## Résultats observés
- masse d'origine exacte : `600/361 > 1`;
- `U1.unitary = false` avant stagnation;
- les deux constituants sont stagnés et compressés séparément, puis vérifiés à la décompression;
- la réactivation dans `C-call-new` exige explicitement une revalidation;
- une preuve où `compatible=false` est refusée et ne produit aucune unité;
- une preuve complète produit `U2.unitary=true`;
- après cette réussite, l'instantané historique conserve `U1.unitary=false` et `U1.integrability_proven=false`;
- 3/3 GCC et 3/3 Clang identiques;
- oracle Python 3/3 identique sur la sémantique de décision;
- Clang UBSan : aucun diagnostic;
- Clang ASan + leak detection : aucun diagnostic.

## Interprétation
Ce jalon démontre sur les scénarios construits que `impotent(P,U1)=vrai` et `integrable(P,U2)=vrai` peuvent coexister sans contradiction si les contextes, modèles d'intégration et preuves restent distincts. La masse `600/361` ne déclenche jamais l'unité par elle-même.

Il démontre également que la réactivation n'est pas une restauration de verdict : elle ouvre un nouvel espace de revalidation, tout en conservant le verdict historique du contexte d'origine.

## Limites
- la compression porte actuellement chaque membre fractionnaire séparément, pas encore une archive canonique unique de l'ensemble impotent complet;
- l'instantané de décision U1 dans le pont exo est séparé des archives compressées des membres;
- aucune politique autonome ne produit encore la preuve U2 : le banc injecte explicitement ses quatre composantes;
- aucune assimilation comportementale n'est encore exécutée;
- les tests ne constituent pas une preuve universelle sur tous les modèles d'intégration.
