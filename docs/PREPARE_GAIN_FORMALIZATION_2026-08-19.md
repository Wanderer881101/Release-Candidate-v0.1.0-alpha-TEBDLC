# PREPARE — Formalisation approfondie des gains TEBDLC

**Jonathan Therrien, Marieville, Québec.**

Date : 2026-08-19
Statut : PREPARE
Projet : TEBDLC — Tout est bon dans le cochon

## Mission

Approfondir l'arithmétique des gains sans perte des acquis conceptuels déjà documentés. La tranche doit utiliser le chemin le plus raffiné, prouvable et applicable possible, mais refuser toute promotion prématurée d'une hypothèse en invariant assimilé.

## Contraintes déjà acquises à préserver

- `GAIN != RELATION != RÉSULTAT != PREUVE`;
- zéro fermé, typé et démontré;
- `UNKNOWN != 0`;
- `0⁺` distinct de `0`;
- `I=1` exige une preuve de complétude;
- une fraction strictement positive ne peut être arrondie à zéro;
- une fraction strictement inférieure à un ne peut être arrondie à un;
- multiplication fractionnaire seulement lorsque la composabilité est démontrée;
- aucune soustraction primitive de gains;
- aucune division primitive de gains;
- la division est particulièrement interdite parce que `f ÷ f = 1` pour tout `f != 0`, ce qui permettrait de fabriquer une unité à partir d'un gain fractionnaire;
- `p/q` comme représentation rationnelle exacte n'autorise pas `G1 ÷ G2`;
- gain chimère : nullité de la consolidation incohérente, sans nullité automatique des constituants;
- gain impotent : gain strictement positif restant sous le seuil d'unité suivant;
- remboursement : résultat de solde sans destruction des termes historiques;
- partition et prolifération sont distinctes;
- aucune addition universelle de gains hétérogènes.

## Objectifs de cette tranche

1. définir un catalogue fermé initial des zéros admissibles;
2. définir un système minimal de types pour les quantités fractionnaires;
3. formaliser les critères de composabilité;
4. construire des contre-exemples empêchant division, soustraction, arrondi et consolidation non prouvée;
5. prototyper une représentation rationnelle exacte qui ne sous-flue jamais vers zéro;
6. vérifier qu'aucun opérateur Python de division ou soustraction n'est exposé par ce prototype;
7. préserver provenance, domaine, référentiel et contexte dans chaque quantité;
8. documenter les limites et les nouveaux gains émergents sans les assimiler automatiquement.

## Non-objectifs

- ne pas créer encore une algèbre complète;
- ne pas définir une fonction universelle de valeur globale;
- ne pas résoudre automatiquement les conflits;
- ne pas convertir des mesures négatives externes en opérateurs de soustraction de gains;
- ne pas prétendre que toute fraction est composable avec toute autre;
- ne pas modifier la sémantique historique du moteur `TEBDLC` existant sans cycle dédié.

## Critères de réussite

- documentation cohérente avec la thèse R2;
- code expérimental isolé et importable;
- tests exacts utilisant des rationnels;
- tests démontrant l'impossibilité opératoire de `-` et `/` sur les nouvelles quantités;
- tests de multiplication préservant `0 < F < 1`;
- tests montrant qu'une valeur proche de 1 reste distincte de 1;
- tests montrant qu'une consolidation chimérique n'annule pas ses constituants;
- attribution obligatoire conservée dans tous les nouveaux fichiers.

## Rollback

Toute erreur sera corrigée par nouvelle révision/commit. Aucun fichier historique ne sera supprimé pour masquer une hypothèse abandonnée.
