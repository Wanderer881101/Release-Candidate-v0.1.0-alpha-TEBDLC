# CATALOGUE FERMÉ DES ZÉROS — TEBDLC

**Jonathan Therrien, Marieville, Québec.**

Date : 2026-08-19
Statut : FORMALISATION CANDIDATE À TESTER

## Principe

Dans TEBDLC, `0` n'est jamais une valeur par défaut. Tout zéro doit répondre à : zéro de quoi, dans quel domaine, selon quel référentiel, dans quel contexte, et avec quelle preuve.

Forme conceptuelle :

    ZERO(kind, domain, reference, context, evidence)

Tout ce qui ne satisfait pas cette exigence reste non nul, inconnu, non quantifié ou non applicable selon le cas; il n'est jamais converti silencieusement à zéro.

## Z0 — ZERO_EXISTENCE

Nullité d'existence démontrée pour l'objet exact et dans le référentiel exact considéré.

    ZERO_EXISTENCE(G | D,R,C,P)

Ce zéro n'est jamais universalisé hors du domaine `D`, du référentiel `R`, du contexte `C` et de la preuve `P`.

## Z1 — ZERO_QUANTITY

La quantité mesurée sur une dimension définie vaut exactement zéro.

    quantity(G,dimension)=0

Cela n'implique pas que le gain ou les autres dimensions sont nuls.

## Z2 — ZERO_VARIATION

Aucune variation n'est observée sur une dimension entre deux états explicitement comparables.

    delta(dimension)=0

La valeur sous-jacente peut être non nulle avant et après.

## Z3 — ZERO_COVERAGE

Aucun élément d'un ensemble de référence explicitement fermé n'est couvert.

    coverage(G,D)=0/|D|

Ce zéro est un zéro de couverture, pas un zéro d'existence générale.

## Z4 — ZERO_EXPRESSION

Un gain existant n'est pas exprimé dans l'état courant.

    expression(G,t)=0

Il ne doit jamais être converti en `ZERO_EXISTENCE`.

## Z5 — ZERO_ACTIVATION

Un gain existe mais son mécanisme d'activation est inactif.

    activation(G,t)=0

`activation=0` n'annule ni l'identité, ni la provenance, ni la capacité potentielle.

## Z6 — ZERO_ADMISSIBILITY

Une politique ou contrainte applicable interdit l'assimilation, l'activation ou l'export du gain.

    admissibility(G)=0

Il s'agit d'un zéro d'autorisation, jamais d'un zéro de réalité fonctionnelle.

## Z7 — ZERO_DEBT

Le solde courant d'une dette est nul après traitement, alors que la dette historique et les gains rembourseurs restent conservés.

    debt_balance=0

L'historique n'est jamais réécrit en « aucune dette n'a existé ».

## Z8 — ZERO_CONFLICT

Aucun conflit n'est démontré dans un périmètre fermé et une procédure de vérification définie.

    conflict_count=0

Une absence de conflit observé sans procédure suffisante doit rester `UNKNOWN`, et non `ZERO_CONFLICT`.

## Z9 — ZERO_CHIMERA_CONSOLIDATION

La valeur d'une consolidation est nulle lorsque l'unité supposée entre ses constituants est démontrée incohérente.

    C_H = CONSOLIDE(G1,...,Gn | H)
    invalid(H) => value(C_H)=0

mais :

    value(Gi) != 0

reste possible et doit être préservé pour chaque constituant.

## Z10 — ZERO_RESULT

Une règle valide peut produire un résultat nul sans annuler ses opérandes.

    R = Phi(G1,...,Gn)=0

n'implique jamais :

    Gi=0

## Z11 — ZERO_RESIDUAL

Un résidu ou solde calculé peut être exactement nul à l'issue d'une procédure, tout en conservant tous les termes qui ont conduit à ce résultat.

Ce zéro est distinct de `ZERO_DEBT` car le résidu peut concerner d'autres mécanismes futurs.

## Z12 — ZERO_PROLIFERATION_OBSERVED

Aucun descendant n'a été observé pendant une fenêtre de prolifération explicitement définie :

    observed_descendants(G,window)=0

Cela n'implique pas que le gain est non proliférable. `proliférable` décrit une capacité; ce zéro décrit un résultat observé.

## Z13 — ZERO_OCCURRENCE

Aucune occurrence n'est observée dans une fenêtre et un canal définis :

    occurrences(G,window,channel)=0

Ce zéro ne prouve pas l'inexistence du gain hors de cette fenêtre ou de ce canal.

## Frontières exclues du zéro

Ne sont jamais des zéros par défaut :

    UNKNOWN
    NON_QUANTIFIED
    DORMANT
    INACTIVE_CAPABILITY
    CONFLICTUAL
    ILLEGAL
    STOLEN
    LITIGIOUS
    CONTAMINATED
    FRACTION_POSITIVE
    IMPOTENT_GAIN
    0⁺

## Invariants candidats

    Z-1  ZERO doit toujours être typé.
    Z-2  ZERO doit toujours être borné par domaine/référentiel/contexte.
    Z-3  ZERO exige une preuve ou une règle déterministe vérifiée.
    Z-4  un ZERO de propriété n'implique jamais ZERO_EXISTENCE sans preuve distincte.
    Z-5  UNKNOWN ne peut jamais être converti en ZERO.
    Z-6  0⁺ ne peut jamais être sérialisé comme 0.
    Z-7  ZERO_RESULT n'annule jamais les opérandes historiques.
    Z-8  ZERO_CHIMERA_CONSOLIDATION n'annule jamais automatiquement ses constituants.
    Z-9  ZERO_PROLIFERATION_OBSERVED n'annule jamais la propriété proliférable.
    Z-10 un zéro non typé est invalide dans le noyau futur.

## Fermeture du catalogue

Le catalogue est « fermé » au sens suivant : un nouveau type de zéro ne peut pas apparaître implicitement. Il doit être ajouté par révision documentaire avec définition, domaine, contre-exemples, règle de preuve et tests dédiés.

---

**Jonathan Therrien, Marieville, Québec.**
**TEBDLC — Tous droits réservés sauf autorisation explicite du propriétaire.**