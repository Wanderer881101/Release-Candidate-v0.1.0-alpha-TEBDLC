# RAPPORT EXPÉRIMENTAL R8/R9 — Lab de session TEBDLC

**Jonathan Therrien, Marieville, Québec.**

Date : 2026-08-19
Environnement : Linux x86_64, Python 3.13.5, GCC 14.2.0, Clang 17.0.0, GMP 6.3.0

## 1. Objectif

Éprouver concrètement les hypothèses R8 et R9 suivantes sans dépendre des runners GitHub :

- détection préventive d'une limite `uint64_t`;
- promotion vers une représentation multi-précision;
- reprise exacte depuis les opérandes intacts;
- continuation fracto-récursive après promotion;
- conservation de provenance et de généalogie;
- distinction entre égalité numérique et identité généalogique;
- maintien des barrières de contexte;
- confinement fractionnaire sur un corpus exhaustif fini;
- répétabilité multi-compilateur;
- absence de diagnostics UBSan/ASan sur les chemins testés.

## 2. Architecture expérimentale

Le noyau expérimental distingue deux représentations :

1. `tebdlc_poly_u64_gain` — représentation native bornée;
2. `tebdlc_poly_big_gain` — représentation multi-précision GMP.

Le chemin R8 testé est :

    u64 exact
      -> détection préventive de capacité
      -> CAPACITY_EXPANSION_REQUIRED
      -> promotion des opérandes
      -> reprise exacte GMP
      -> continuation exacte

La logique ne reprend jamais depuis un produit tronqué ou partiellement corrompu.

## 3. Incident de compilation initial

Le premier build strict a échoué sous `-Werror` pour :

- trois avertissements `misleading-indentation`;
- une fonction de test inutilisée.

Aucun test numérique n'avait alors été exécuté. Les options strictes n'ont pas été relâchées; la forme C a été corrigée puis le build a réussi.

Statut : incident de construction conservé, non assimilé à un échec arithmétique.

## 4. Divergence de précision découverte par Python

Le premier diagnostic C de capacité retournait une borne supérieure de 66 bits pour le dénominateur du carré :

    (4294967295 / 4294967297)^2

L'oracle Python exact montre que le dénominateur réel requiert 65 bits. Le déclenchement de capacité reste correct (>64), mais le champ C était une borne conservative, non une mesure exacte.

Correction : les champs ont été renommés en `required_*_bits_upper_bound` afin de ne pas sur-déclarer leur précision.

Cette correction est documentaire et sémantique; aucune valeur de gain n'a été modifiée.

## 5. Résultat R8 — promotion et reprise exacte

Vecteur de seuil :

    n = 4294967295
    d = 4294967297
    (n/d)^2

La voie `uint64_t` retourne `CAPACITY_EXPANSION_REQUIRED` avant multiplication dangereuse.

Les deux opérandes sont ensuite promus vers GMP et l'opération est rejouée depuis ces opérandes exacts.

Résultat GMP observé : exactement le même rationnel que Python `Fraction(n,d) * Fraction(n,d)`.

Conclusion limitée au domaine testé : **reprise exacte démontrée expérimentalement pour ce vecteur de capacité**.

## 6. Résultat R9 — transition native vers fracto-récursion multi-précision

Base : `3/10`.

La branche native reste représentable jusqu'à profondeur 19. À profondeur 20, le dénominateur `10^20` dépasse `uint64_t`.

Observation :

    hybrid_transition_depth = 20

Après promotion/reprise, la branche continue jusqu'à profondeur 1000.

Sortie observée à profondeur 1000 :

    numerator_bits   = 1585
    denominator_bits = 3322
    genealogy        = 1000

Le résultat correspond exactement à :

    3^1000 / 10^1000

et reste strictement :

    > 0
    < 1

## 7. Profondeurs contrôlées

Résultats C et Python concordants :

| profondeur | bits numérateur | bits dénominateur |
|---:|---:|---:|
| 1 | 2 | 4 |
| 2 | 4 | 7 |
| 10 | 16 | 34 |
| 100 | 159 | 333 |
| 1000 | 1585 | 3322 |

La profondeur 1 porte son `node_id` courant mais n'a pas encore d'ancêtre enregistré dans `genealogy`; à partir de la première composition, la généalogie cumulée est enregistrée. Cela doit rester explicitement distingué de l'identité du nœud courant.

## 8. Égalité numérique != identité généalogique

Deux branches :

    (1/2) * (1/3)
    (1/3) * (1/2)

produisent la même valeur `1/6`, mais avec provenances et identifiants de nœuds distincts.

Le test exige que les généalogies restent différentes malgré l'égalité numérique.

Statut : PASS sur les cas construits.

## 9. Barrière de contexte

Deux fractions numériquement identiques mais de contextes `A` et `B` sont refusées à la composition.

Statut : PASS.

## 10. Corpus exhaustif fini

Le noyau poly-fractal borné exécute tous les couples :

    1 <= n < d <= 40

pour les deux opérandes, soit :

    608400 compositions

par exécution.

Chaque résultat doit satisfaire :

    status == OK
    numerator > 0
    numerator < denominator

et conserver deux provenances distinctes dans ce corpus.

## 11. Répétabilité multi-compilateur

Builds ordinaires :

    -std=c11 -O2 -Wall -Wextra -Werror -pedantic

GCC : 3/3 PASS.
Clang : 3/3 PASS.

Les six sorties logiques sont octet-pour-octet identiques.

Temps observés :

- GCC : 7.18 s, 7.08 s, 7.30 s;
- Clang : 4.41 s, 4.58 s, 4.34 s.

Les temps sont contextuels et ne sont pas des invariants TEBDLC.

## 12. Sanitizers

Clang UBSan : PASS, stderr vide, ~5.27 s.
Clang ASan + leak detection : PASS, stderr vide, ~5.85 s.

Aucun diagnostic n'a été observé sur les chemins testés.

Cela ne prouve pas l'absence universelle de comportements indéfinis ou de défauts mémoire.

## 13. Timeout du runner agrégé

Une commande regroupant six runs + plusieurs builds sanitizers a dépassé la fenêtre d'exécution du runner de session.

Inspection après timeout : les trois runs GCC et deux runs Clang avaient déjà terminé avec PASS; le troisième run Clang était incomplet. Il a été relancé isolément et a produit la même sortie.

Les sanitizers ont ensuite été exécutés séparément et ont réussi.

Conclusion : timeout d'orchestration, pas échec du noyau.

## 14. État des invariants PFR

Ce jalon fournit des témoins exécutables compatibles avec :

- PFR-1 : reconstructibilité de valeur/métadonnées sur les nœuds testés;
- PFR-2 : la réinjection n'accorde aucun statut supplémentaire;
- PFR-3 : barrières de composabilité conservées;
- PFR-4 : aucun 0/1 artificiel observé;
- PFR-5 : interruption native avant corruption;
- PFR-6 : reprise depuis opérandes exacts;
- PFR-7 : égalité numérique avec généalogies distinctes;
- PFR-9 : aucune fusion automatique de branches;
- PFR-10 : profondeur 1000 strictement positive et <1;
- PFR-11 : transition de capacité traitée comme événement, non comme gain;
- PFR-12 : représentations Python/C différentes mais résultats canoniques concordants.

PFR-8 (définition générale d'une structure poly-fractale valide) reste principalement doctrinal et n'est pas prouvé universellement par ce corpus.

## 15. Ce qui reste non démontré

- généralité sur tous les rationnels;
- limites de provenance >32;
- limites de généalogie >4096;
- comportement multi-architecture / endianness;
- comportement sous d'autres versions de GMP;
- sécurité de concurrence/threading;
- persistance/sérialisation durable des objets GMP;
- stagnation/réactivation exo-sapienne;
- `ImpotentGainEnvelope` multi-précision dans ce nouveau noyau;
- preuve formelle des invariants PFR.

## 16. Conclusion

Le jalon démontre concrètement, dans cet environnement, qu'une branche fractionnaire bornée peut reconnaître sa limite native, préserver ses opérandes, être promue vers une représentation multi-précision, reprendre exactement l'opération et poursuivre une chaîne fracto-récursive jusqu'à profondeur 1000 sans perte numérique observée, tout en maintenant provenance, généalogie et barrières de contexte sur les cas testés.

Il s'agit d'une preuve expérimentale reproductible sur un domaine défini, pas d'une preuve universelle.

---

**Jonathan Therrien, Marieville, Québec.**
