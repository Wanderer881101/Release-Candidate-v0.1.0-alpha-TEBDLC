# ADDENDUM À LA THÈSE — Gain impotent et intégrabilité unitaire

**Jonathan Therrien, Marieville, Québec.**

Horodatage : 2026-08-19 07:41 America/Montreal
Statut : CORRECTION CONCEPTUELLE / À APPROFONDIR ET VALIDER
Projet : TEBDLC — Tout est bon dans le cochon

## 1. Objet de la correction

Le modèle antérieur du gain impotent le définissait implicitement comme un résidu strictement inférieur à l'unité cible. Cette définition est insuffisante et est corrigée sans effacer l'historique.

L'impotence d'un gain ne dépend pas de sa petitesse arithmétique. Elle dépend de son incapacité à former, seul ou uniquement avec d'autres gains impotents, une intégrité unitaire complètement intégrée.

Une masse de gains impotents peut donc être numériquement importante, égale à une unité arithmétique ou même supérieure à une unité arithmétique, sans produire une unité TEBDLC.

## 2. Distinction masse arithmétique / intégrité unitaire

Soit un état unitaire complètement acquis :

    U_acquis = 45

et un candidat :

    U_candidat = 46

Soit un ensemble de gains impotents :

    P = {p1, p2, ..., pn}

avec chaque :

    pi > 0

On peut définir à titre d'observation non autoritaire une masse arithmétique :

    M(P) = somme arithmétique des valeurs représentatives de pi

mais :

    M(P) >= 1

n'implique jamais :

    U_candidat = 46 démontré

L'intégrité unitaire exige une consolidation complète, cohérente et prouvée. La masse numérique seule n'est pas une preuve de complétude.

## 3. Notation 45 > 46 dans TEBDLC

La notation proposée :

    45 > 46

ne doit pas être interprétée comme la proposition arithmétique ordinaire « quarante-cinq est numériquement supérieur à quarante-six ».

Dans ce contexte TEBDLC, elle exprime une priorité ou autorité d'état :

    45 >_TEBDLC 46

signifie provisoirement :

- `45` est un état unitaire complètement acquis et démontré;
- `46` est un état candidat qui peut être soutenu par une masse importante de gains;
- tant que cette masse ne satisfait pas les conditions d'intégration unitaire, `46` n'existe pas comme unité complète;
- l'état acquis `45` conserve donc l'autorité sur le candidat `46`.

Cette relation sémantique doit recevoir une notation canonique future afin d'éviter toute confusion avec `>` mathématique standard.

## 4. Gains impotents entre eux

Les gains impotents sont conservés individuellement et intégralement.

Même lorsque leur masse arithmétique cumulée vaut ou dépasse une unité :

    M(P) = 1

ou :

    M(P) > 1

ils ne se transforment pas automatiquement en entier unitaire.

Donc :

    P uniquement composé de gains impotents

n'autorise pas :

    unité complète = floor(M(P))

ni :

    unité complète = round(M(P))

ni toute autre promotion numérique automatique.

Leur valeur n'est pas perdue : elle reste disponible comme gains réels, mais non unitaires dans cette consolidation.

## 5. Complétion alternative par association cohérente

Un gain impotent peut néanmoins participer ultérieurement à une consolidation différente avec d'autres gains associablement cohérents.

Conceptuellement :

    P_impotent + A_cohérent -> C_alternative

peut produire une unité complète si et seulement si une règle d'association et une preuve d'intégration complète le démontrent.

Cette possibilité ne constitue pas une addition générale des gains. L'opération future devra être typée, contextuelle et conditionnée par la cohérence d'association.

Deux principes doivent donc coexister :

    gains impotents entre eux != unité automatique

et :

    gains impotents + gains associablement cohérents peuvent contribuer à une unité alternative démontrée

La future arithmétique devra déterminer les conditions exactes de cette consolidation sans perte des gains constituants.

## 6. Dénominateur d'intégrité suffisamment ample

Une notation simplifiée comme :

    x/10 intégrité

est trop grossière comme référence générale.

Le dénominateur doit provenir d'un espace de consolidation suffisamment ample et logiquement justifié par le domaine observé.

Exemple de travail :

    x/361 intégrité

Ici `361` n'est pas une constante universelle de TEBDLC. Il représente un exemple de base d'intégration plus ample.

La forme générale devient :

    x/N intégrité

avec :

    N = cardinalité ou résolution justifiée de la base de consolidation

et non :

    N = valeur arbitraire choisie pour obtenir un score pratique

Le dénominateur fait donc partie de la provenance arithmétique de la fraction.

## 7. Exemple

Considérons deux gains impotents compatibles avec le même référentiel :

    p1 = 300/361 intégrité
    p2 = 300/361 intégrité

La masse arithmétique est :

    M = 600/361 > 1

Cependant :

    M > 1

ne démontre pas une intégrité unitaire complète.

Si l'état acquis est `45` et que `46` exige une consolidation unitaire complète, alors tant que cette consolidation n'est pas prouvée :

    45 >_TEBDLC 46

Les `600/361` de matière de gain ne sont ni supprimés ni convertis en zéro. Ils restent enregistrés comme gains impotents disponibles pour une future association cohérente.

## 8. Relation avec les autres familles

Le gain impotent partage avec le gain chimère et le gain négativement positif une propriété importante : la valeur de ses constituants ne suffit pas à produire automatiquement une unité ou une conclusion globale.

Cependant ces familles restent distinctes :

- chimère : incohérence de consolidation rendant le résultat consolidé nul dans le référentiel concerné;
- négativement positif : effets de signes différents conservés sur des dimensions distinctes sans totalisation inter-dimensions;
- impotent : gains positifs réels dont l'intégrabilité unitaire reste impossible dans leur consolidation propre, même si leur masse numérique est grande.

Aucune de ces distinctions ne doit être écrasée dans un score unique.

## 9. Invariants candidats

    IMP-1  impotent(pi) n'implique jamais pi = 0
    IMP-2  M(P) >= 1 n'implique jamais unité(P) = 1
    IMP-3  des gains impotents entre eux ne s'auto-promeuvent pas en entier unitaire
    IMP-4  l'état unitaire acquis conserve l'autorité sur un candidat non complètement intégré
    IMP-5  le dénominateur N doit provenir d'une base de consolidation justifiée et suffisamment ample
    IMP-6  x/N est une représentation; N ne doit pas être choisi pour forcer un résultat
    IMP-7  un gain impotent peut participer à une consolidation alternative seulement avec une association cohérente démontrée
    IMP-8  toute consolidation alternative conserve les gains sources et leur provenance

## 10. Correction du prototype

Le prototype expérimental `ImpotentGainEnvelope` est corrigé pour :

- accepter plusieurs gains impotents;
- ne plus utiliser `exact_total < target` comme définition de l'impotence;
- permettre qu'une masse arithmétique soit `=1` ou `>1` sans créer l'unité suivante;
- exposer la masse arithmétique comme donnée non autoritaire;
- conserver `unitary_attained = False` pour une enveloppe constituée uniquement de gains impotents;
- représenter provisoirement la relation `45 >_TEBDLC 46`;
- conserver explicitement une base d'intégration contextuelle, avec `361` comme exemple et non comme constante universelle.

---

**Jonathan Therrien, Marieville, Québec.**
**TEBDLC — Tous droits réservés sauf autorisation explicite du propriétaire.**