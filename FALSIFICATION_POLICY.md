# TEBDLC — Politique de falsification et registre de provenance

**Jonathan Therrien, Marieville, Québec.**
**Auteur du projet TEBDLC : Jonathan Therrien, Marieville, Québec, Canada.**

Cette politique définit comment les tentatives de falsification, contre-exemples, variantes expérimentales et reproductions adversariales peuvent être conservées sans effacer ni mélanger la propriété intellectuelle, la provenance ou l'historique des contributions.

## Principe fondamental

Une falsification n'efface jamais la provenance du matériau TEBDLC utilisé et ne transfère pas automatiquement la propriété intellectuelle d'une contribution tierce au projet TEBDLC.

Chaque contribution doit préserver au minimum :

- la version TEBDLC ciblée ;
- le commit SHA TEBDLC exact ;
- l'auteur/propriétaire déclaré du matériau TEBDLC ;
- l'identité ou pseudonyme déclaré du falsificateur ;
- la version propre de la falsification ;
- la provenance des fichiers et transformations ;
- les hashes des sources et preuves ;
- le statut expérimental ;
- les droits/licences déclarés par le contributeur.

## Registre isolé

Le registre canonique des falsifications vit dans la branche isolée `falsification-registry`.

La branche `main` représente le produit Release Candidate. Une falsification enregistrée ne modifie donc jamais directement le produit canonique. Une correction issue d'une falsification validée doit suivre un processus séparé de revue/PR vers la branche produit.

## États

- `SUBMITTED` — soumise, non reproduite ;
- `REPRODUCED` — reproduite indépendamment ;
- `ACCEPTED_AS_VALID_FALSIFICATION` — contre-exemple accepté pour le périmètre déclaré ;
- `INCORPORATED` — une correction ou évolution issue de la falsification a été intégrée au produit ;
- `SUPERSEDED` — remplacée par une version/généalogie ultérieure sans disparition historique ;
- `REJECTED` — rejetée avec justification et preuves conservées.

## Propriété intellectuelle et attribution

Le registre distingue explicitement :

`IP_TEBDLC + IP_contributeur + version + provenance + preuves`

et ne doit jamais réduire cette chaîne à un auteur unique lorsqu'elle ne l'est pas.

Les déclarations contenues dans les manifestes documentent l'attribution et les intentions déclarées ; elles ne remplacent pas, à elles seules, les règles juridiques applicables ni un contrat formel lorsque celui-ci est nécessaire.

## Exigences minimales d'une falsification

Une entrée doit contenir :

1. `manifest.json` ;
2. une description reproductible ;
3. la cible exacte (`version`, `commit SHA`, claim/invariant ciblé) ;
4. les fichiers modifiés ou patchs ;
5. les tests et commandes d'exécution ;
6. les preuves/résultats ;
7. les empreintes cryptographiques disponibles ;
8. la déclaration d'auteur/provenance/licence du contributeur ;
9. l'historique des versions de la falsification ;
10. les relations parent/enfant avec d'autres falsifications, s'il y a lieu.

## Non-réécriture

Une falsification validée puis corrigée dans TEBDLC reste enregistrée. La correction ne réécrit pas rétroactivement le fait que le contre-exemple existait pour une version donnée.

Exemple :

`TEBDLC v0.1.0-alpha@SHA_A -> FALS-000042 -> correction -> TEBDLC v0.1.1@SHA_B`

`FALS-000042` reste alors une preuve historique rattachée à `SHA_A`.
