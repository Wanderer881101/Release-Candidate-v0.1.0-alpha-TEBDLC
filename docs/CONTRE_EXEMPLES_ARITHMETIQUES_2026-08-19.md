# CORPUS DE CONTRE-EXEMPLES ARITHMÉTIQUES — TEBDLC

**Jonathan Therrien, Marieville, Québec.**

Date : 2026-08-19
Statut : CORPUS DE RÉFUTATION / VALIDATION

## Objet

Une règle arithmétique TEBDLC ne doit pas être acceptée seulement parce qu'elle fonctionne sur un exemple favorable. Elle doit survivre à des contre-exemples destinés à révéler fabrication d'unité, annulation, perte de provenance, confusion d'identité ou consolidation abusive.

## CE-01 — Division auto-unitaire

    f = 3/10
    f ÷ f = 1

Conclusion : la division entre gains permet de fabriquer l'unité à partir d'une fraction. Elle est interdite comme primitive.

## CE-02 — Division supra-unitaire

    3/10 ÷ 1/10 = 3

Conclusion : deux fractions peuvent fabriquer un entier supérieur à l'unité. Interdiction confirmée.

## CE-03 — Soustraction annulante

    G - G = 0

Si `G` représente un acquis historique réel, cette opération produit une nullité de calcul qui pourrait être confondue avec une inexistence. La soustraction entre gains est interdite comme primitive.

## CE-04 — Arrondi vers zéro

Une multiplication exacte répétée :

    (3/10)^n > 0

pour tout `n` fini. Une représentation flottante peut éventuellement sous-fluer vers zéro.

Conclusion : un `float` ne peut pas être l'autorité de conservation d'une fraction TEBDLC.

## CE-05 — Arrondi vers unité

    F = (10^40 - 1) / 10^40

alors :

    F < 1

même si un affichage à précision limitée montre `1.0`.

Conclusion : l'affichage ou l'arrondi ne constitue jamais une preuve de complétude.

## CE-06 — Même valeur, contextes incompatibles

    F1 = 3/10 [intégrité, session-A]
    F2 = 3/10 [intégrité, session-B]

La valeur numérique égale ne démontre pas leur composabilité.

Conclusion : toute quantité doit être typée par domaine, référentiel et contexte.

## CE-07 — Chimère d'identité

    G1 = observation valide de A
    G2 = observation valide de B
    H  = A = B

Si H est réfutée :

    CONSOLIDE(G1,G2|H)=0 [chimère]

mais `G1` et `G2` restent conservés.

Conclusion : zéro de consolidation n'est pas zéro des constituants.

## CE-08 — Chimère de continuité temporelle

Des événements partagent un profil/session apparent mais présentent une continuité physique ou contextuelle non démontrée. Une narration unifiée ne peut pas être assimilée à un gain consolidé sans preuve de relation.

Conclusion : association technique et identité réelle sont des couches distinctes.

## CE-09 — Gain impotent

    G = 45 + (10^30 - 1)/10^30

Alors :

    45 < G < 46

Le résidu fractionnaire est strictement positif mais n'achève pas l'unité suivante.

Conclusion : proximité d'un entier != entier démontré.

## CE-10 — Prolifération != partition

Un gain `G` produit deux descendants `D1`, `D2` qui possèdent de nouvelles propriétés. Imposer :

    G = D1 + D2

sans règle de mesure commune fabrique une conservation additive non prouvée.

Conclusion : prolifération et partition restent des relations différentes.

## CE-11 — Répétition != multiplicité de gain

La même preuve est observée deux fois :

    occurrence(P,t1)
    occurrence(P,t2)

Cela ne démontre pas `2 × G`.

Conclusion : occurrence, preuve et quantité de gain sont distinctes.

## CE-12 — UNKNOWN != ZERO

Une source ne répond pas ou une mesure est impossible. Affecter `0` à la valeur absente transforme ignorance en nullité.

Conclusion : `UNKNOWN` doit être conservé comme état non nul/non évalué distinct.

## CE-13 — Zéro d'activation != zéro d'existence

    activation(G)=0

avec un gain dormant conservé.

Conclusion : un zéro typé ne se propage jamais automatiquement vers un autre type de zéro.

## CE-14 — Dette soldée != histoire effacée

Un résultat de solde vaut zéro après remboursement. Réécrire l'historique comme si aucune dette ni remboursement n'avaient existé détruit deux gains/traces.

Conclusion : le résultat nul et les opérandes historiques coexistent.

## CE-15 — Fraction rationnelle != permission de diviser

`3/10` encode une quantité rationnelle exacte. Il ne s'agit pas d'une instruction `3 ÷ 10` applicable comme opération de gain générique.

Conclusion : représentation et opérateur sont séparés.

## Règle méthodologique

Toute nouvelle opération candidate doit recevoir au minimum :

1. exemple positif;
2. contre-exemple d'identité;
3. contre-exemple de contexte;
4. contre-exemple de zéro;
5. contre-exemple de fraction;
6. contre-exemple de provenance;
7. contre-exemple temporel;
8. preuve de non-perte ou statut `UNKNOWN`.

---

**Jonathan Therrien, Marieville, Québec.**
**TEBDLC — Tous droits réservés sauf autorisation explicite du propriétaire.**
