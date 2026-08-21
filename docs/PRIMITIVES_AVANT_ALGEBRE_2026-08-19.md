# PRIMITIVES AVANT ALGÈBRE — TEBDLC

**Jonathan Therrien, Marieville, Québec.**

Date : 2026-08-19
Statut : PREPARE / FORMALISATION CONCEPTUELLE À APPROFONDIR
Projet : TEBDLC — Tout est bon dans le cochon

## 1. But

Avant toute algèbre des gains, TEBDLC doit définir les objets qui pourront être opérés sans perte de sens. Les opérations primitives destructrices sont volontairement exclues à ce stade : aucune soustraction de gains, aucune division de gains, aucune compensation effaçant l'historique, aucune addition universelle non typée.

Le modèle de base sépare quatre couches :

    GAIN
    RELATION
    RÉSULTAT
    PREUVE

Un résultat nul n'annule jamais automatiquement ses gains constituants.

## 2. Zéro fermé

Le zéro n'est jamais une valeur par défaut. Il doit être démontré et typé.

    ZERO(type, domaine, référentiel, contexte, preuve)

Un `UNKNOWN`, un gain non quantifié, dormant, inactif, conflictuel, illégal, litigieux ou fractionnaire positif n'est jamais converti en zéro par commodité.

## 3. Gain chimère

Un gain chimère est le résultat nul d'une consolidation qui suppose à tort une unité de sujet, d'identité, de contexte ou de continuité.

Exemple :

    G1 = donnée valide de l'entité A
    G2 = donnée valide de l'entité B
    G3 = donnée valide de l'entité C

Une hypothèse H affirme à tort :

    A = B = C

La consolidation :

    C_H = CONSOLIDE(G1, G2, G3 | H)

peut alors produire :

    C_H = 0  [GAIN_CHIMÈRE]

sans impliquer :

    G1 = 0
    G2 = 0
    G3 = 0

Les constituants restent conservés. C'est la consolidation unifiée qui devient sans valeur lorsque son hypothèse identitaire est démontrée incohérente.

Le même principe s'applique lorsqu'une seule session, un seul profil ou un seul identifiant agrège des événements qui ne permettent pas de démontrer une continuité réelle unique.

## 4. Gain impotent

Un gain impotent est un gain strictement positif qui demeure insuffisant pour former l'unité entière suivante dans le référentiel considéré.

Exemple :

    G = 45 + Gi

avec :

    0 < Gi < 1

et :

    45 + Gi < 46

`Gi` n'est jamais nul. Son impotence est relationnelle au seuil `46`, pas à son existence.

Une suite décimale finie telle que :

    45.99999999999999999999999999

reste strictement inférieure à 46. Une écriture à répétition infinie `45.999...` doit rester soumise aux mathématiques standards, où elle vaut 46; elle ne peut donc pas servir à définir le gain impotent.

## 5. Identité

Deux observations égales numériquement ou textuellement ne sont pas automatiquement le même gain.

L'identité doit au minimum considérer :

    sujet / entité
    domaine
    référentiel
    contexte
    provenance
    temporalité
    nature de l'observation

Une erreur d'identité peut produire une chimère lors de la consolidation.

## 6. Occurrence et multiplicité

Une occurrence n'est pas automatiquement un nouveau gain.

    occurrence(G, t1)
    occurrence(G, t2)

peuvent représenter :

- répétition du même gain;
- nouvelle preuve du même gain;
- instance distincte d'un gain de même type;
- prolifération;
- événement indépendant.

La multiplicité doit être explicitement qualifiée avant toute opération quantitative.

## 7. Temporalité

TEBDLC doit distinguer au minimum :

    apparition
    observation
    activation
    persistance
    répétition
    expiration éventuelle
    simultanéité
    ordre

Deux gains identiques observés à des temps différents ne sont pas nécessairement interchangeables.

## 8. Contexte

Un gain est toujours situé dans un domaine et un contexte. La validité dans C1 n'autorise jamais automatiquement :

    G(C1) => G(C2)

Une extension de contexte exige une preuve distincte.

## 9. Relation

Une relation n'altère pas les gains qu'elle relie.

Exemples de relations candidates :

    SAME_ENTITY
    DISTINCT_ENTITY
    DEPENDS_ON
    DERIVED_FROM
    VARIANT_OF
    CONFLICTS_WITH
    COMPATIBLE_WITH
    OCCURS_BEFORE
    OCCURS_AFTER
    SAME_CONTEXT
    DISTINCT_CONTEXT
    PROLIFERATES_TO
    REFUNDS

La liste reste ouverte et ne constitue pas encore une ontologie définitive.

## 10. Résultat

Un résultat est produit par une règle explicite appliquée à des gains et relations :

    R = Φ(G1, G2, ..., Gn | relations, contexte, règle)

Un résultat peut être zéro sans que les opérandes soient zéro.

Invariant candidat :

    R = 0  !=>  Gi = 0

pour chaque gain constituant `Gi`.

## 11. Preuve

Une preuve ne doit pas être confondue avec le gain ni avec le résultat. Elle soutient une affirmation portant sur eux.

Exemples :

    preuve d'identité
    preuve de distinction d'identités
    preuve de contexte
    preuve de fraction
    preuve de complétude
    preuve de nullité
    preuve de relation
    preuve de consolidation chimérique

L'absence de preuve n'est jamais une preuve de zéro.

## 12. Fractions exactes

Une fraction de gain normalisée reste :

    F = p/q

avec :

    0 < F < 1

pour le domaine fractionnaire strict.

La notation sémantique candidate reste :

    0⁺ ⟪ I_f ⟫ 1

avec conservation de la distinction entre zéro atteint, frontière vers zéro et unité démontrée.

## 13. Composition multiplicative

La multiplication reste la seule opération arithmétique candidate actuellement admise pour certains gains fractionnaires compatibles :

    F = F1 × F2 × ... × Fn

uniquement lorsque la composabilité est démontrée.

Elle ne constitue ni une soustraction, ni une division, ni une compensation.

Pour des fractions strictes compatibles :

    0 < Fi < 1

alors pour n fini :

    0 < ΠFi < 1

## 14. Partition sans division primitive

Une partition est une relation structurée entre un gain parent et des parties; elle n'implique pas que la division soit une opération primitive disponible à tous les gains.

Si une partition exhaustive et sans chevauchement est démontrée :

    PARTITION(G -> {G1, ..., Gn})

la conservation du parent doit pouvoir être vérifiée par une règle dédiée. Cette règle reste à formaliser et ne doit pas être confondue avec la prolifération.

## 15. Prolifération

La prolifération produit des descendants et n'est pas une simple découpe du parent.

    PROLIFERATION(G -> {D1, ..., Dn})

Les descendants peuvent posséder des propriétés nouvelles. Il est donc interdit d'imposer une conservation additive naïve comme si la prolifération était une partition.

## 16. Remboursement sans réduction historique

Un gain rembourseur peut produire un résultat de solde, mais il ne supprime jamais la dette historique ni le gain rembourseur.

    dette_historique = D
    gain_rembourseur = R
    résultat_solde = S

Même si :

    S = 0

TEBDLC conserve :

    D
    R
    S
    relation REFUNDS(R, D)

Le zéro du solde n'est pas le zéro des constituants.

## 17. Opérations interdites comme primitives à ce stade

Les opérations suivantes ne sont pas admises comme primitives générales :

    G1 - G2
    G1 / G2
    somme universelle de gains hétérogènes
    moyenne globale non typée
    arrondi vers 0
    arrondi vers 1
    compensation supprimant des termes historiques

Une mesure externe peut contenir une valeur négative ou être produite par une division dans son propre domaine; cela ne transforme pas la soustraction ou la division en opérateurs de gains TEBDLC.

## 18. Aspects restant à formaliser avant algèbre

Avant de construire une algèbre, il reste notamment à préciser :

- système de types pour les fractions et dimensions;
- règle de composabilité;
- support/chevauchement des gains de couverture;
- distinction dépendance/indépendance;
- sémantique exacte des relations;
- règles de consolidation;
- preuve de chimère;
- représentation canonique des gains impotents;
- temporalité et fenêtres événementielles;
- quantité vs existence vs occurrence;
- limites et suites infinies;
- représentation symbolique de fractions extrêmement petites;
- preuve de complétude unitaire;
- catalogue fermé des zéros admissibles;
- reconstruction sans modification des observations sources.

## 19. Principe directeur

TEBDLC doit préférer conserver un objet correctement typé comme `UNKNOWN` plutôt que lui attribuer une valeur ou une opération non démontrée.

Aucune conclusion ne doit modifier rétroactivement les gains qui l'ont produite.

    GAIN != RELATION != RÉSULTAT != PREUVE

et :

    RÉSULTAT = 0  n'implique pas  GAIN = 0

---

**Jonathan Therrien, Marieville, Québec.**
**TEBDLC — Tout est bon dans le cochon. Tous droits réservés sauf autorisation explicite du propriétaire.**
