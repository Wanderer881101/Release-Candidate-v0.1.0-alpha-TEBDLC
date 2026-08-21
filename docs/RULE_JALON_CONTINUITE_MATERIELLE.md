# RÈGLE TEBDLC — Continuité matérielle des jalons

**Jonathan Therrien, Marieville, Québec.**

Statut : règle opérationnelle de gouvernance et de preuve  
Date : 2026-08-19  
Projet : TEBDLC — Tout est bon dans le cochon

## 1. Principe

Après chaque **jalon solide**, TEBDLC doit persister un ensemble minimal de preuves permettant à une session, un agent, un développeur ou un auditeur ultérieur de reconstruire matériellement l'état atteint.

Un jalon n'est pas considéré comme matériellement continu par sa seule description narrative.

La règle est :

    jalon_solide
      → persistance(code_source,
                    tests,
                    vecteurs,
                    logs,
                    empreintes,
                    résultats,
                    documentation)
      → continuité_matérielle_candidate

et :

    absence_d_un_élément_obligatoire
      → continuité_matérielle_non_garantie

Cette règle applique le principe TEBDLC de non-perte :

    rien ne se perd, tout se transforme

à la continuité du développement lui-même.

## 2. Les sept familles obligatoires

Chaque jalon solide doit référencer ou contenir au minimum les sept familles suivantes.

### 2.1 Code source

Le code exact ayant produit les résultats documentés, ou une référence immuable et reconstructible vers ce code.

### 2.2 Tests

Les tests exécutés, avec leur version exacte. Une conclusion sans test reconstructible ne suffit pas lorsqu'elle dépend d'un comportement logiciel.

### 2.3 Vecteurs

Les entrées, cas de test, corpus, seeds ou règles déterministes permettant de reconstruire les entrées utilisées. Un vecteur peut être généré par un programme déterministe si le générateur, sa version et ses paramètres sont eux-mêmes persistés.

### 2.4 Logs

Les traces utiles de l'exécution : environnement, commandes, étapes, erreurs, divergences, corrections, diagnostics et événements pertinents.

### 2.5 Empreintes

Des empreintes permettant de relier les preuves aux objets réellement testés : SHA-256, identifiants de blobs/commits Git ou autre mécanisme explicitement qualifié. Les algorithmes et la portée de chaque empreinte doivent être indiqués.

### 2.6 Résultats

Les sorties observées, PASS/FAIL, divergences, métriques pertinentes, contre-exemples et limites de l'essai. Un résultat attendu ne doit jamais être substitué silencieusement à un résultat observé.

### 2.7 Documentation

Le pourquoi, le comment, l'interprétation, les limites, le statut de preuve et les questions ouvertes permettant à un professionnel de comprendre ce que le jalon démontre et ce qu'il ne démontre pas.

## 3. Continuité matérielle

Une session ultérieure ne doit pas être présentée comme continuation matérielle garantie d'un jalon si son bundle minimal n'est pas reconstructible.

On distingue :

    continuité_conceptuelle
    continuité_documentaire
    continuité_matérielle

La présence d'une discussion ou d'un résumé peut soutenir la continuité conceptuelle/documentaire, mais ne remplace pas les objets exécutables nécessaires à la continuité matérielle.

## 4. Références autorisées

La duplication intégrale de chaque artefact dans chaque dossier de jalon n'est pas obligatoire lorsque cela créerait un pléonasme matériel inutile.

Un manifeste peut référencer des objets déjà persistés ailleurs à condition que la référence soit :

- explicite;
- suffisamment stable pour reconstruction;
- accompagnée de son empreinte ou identifiant immuable lorsque nécessaire;
- non ambiguë quant à la version réellement utilisée.

Ainsi :

    référence_immuable ≠ perte

mais :

    référence_flottante_non_versionnée ≠ garantie_de_reconstruction

## 5. Corrections et divergences

Un jalon corrigé ne doit pas effacer le fait qu'une divergence a existé.

Le bundle doit permettre de reconstruire au minimum :

    état_avant
    → observation/divergence
    → correction
    → état_après

lorsque cette séquence est pertinente à la compréhension du résultat.

## 6. État d'un jalon

Un jalon peut porter notamment :

- `DRAFT` : préparation incomplète;
- `EXECUTED` : essais exécutés mais bundle non encore complet;
- `PERSISTED` : sept familles présentes ou référencées;
- `VERIFIED` : cohérence du bundle vérifiée;
- `SUPERSEDED` : transformé par un jalon ultérieur sans être effacé.

`PERSISTED` ou `VERIFIED` ne signifie pas que toutes les hypothèses contenues sont vraies. Cela signifie que l'état est reconstructible selon la portée déclarée.

## 7. Anti-pléonasme et non-perte

Cette règle ne doit pas produire sept copies artificielles du même fichier pour satisfaire sept catégories.

Un même artefact peut soutenir plusieurs catégories si ses rôles sont explicitement indiqués, mais le manifeste doit démontrer que chacune des sept exigences est réellement couverte.

    couverture_multiple_autorisée ≠ catégorie_absente

## 8. Discipline de fermeture d'un jalon

Avant de déclarer un jalon solide fermé :

1. identifier l'état exact du code;
2. persister les tests;
3. persister ou rendre reconstructibles les vecteurs;
4. persister les logs pertinents;
5. calculer/enregistrer les empreintes;
6. persister les résultats observés;
7. documenter interprétation et limites;
8. produire un manifeste de jalon;
9. valider le manifeste;
10. seulement ensuite qualifier la continuité matérielle du jalon.

## 9. Règle de prudence

Un bundle complet peut être faux, incomplet conceptuellement ou contenir un défaut non détecté. Il rend l'expérience reconstructible; il ne transforme pas automatiquement son contenu en vérité.

    reconstructibilité ≠ vérité
    persistance ≠ validation scientifique
    répétabilité ≠ universalité

## 10. Application immédiate

Cette règle s'applique à partir de son adoption et doit être utilisée pour les futurs jalons solides de TEBDLC. Les jalons historiques peuvent être rétro-documentés progressivement sans que leur absence initiale soit réécrite ou cachée.

---

**Jonathan Therrien, Marieville, Québec.**  
**TEBDLC — Tout est bon dans le cochon. Tous droits réservés sauf autorisation explicite du propriétaire.**