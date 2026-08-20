# TEBDLC — Falsification Registry

**Projet d'origine : TEBDLC — Jonathan Therrien, Marieville, Québec, Canada.**

Cette branche est un registre isolé de falsifications, contre-exemples, reproductions adversariales et variantes expérimentales ciblant des versions précises de TEBDLC.

## Règle de séparation

- `main` = produit Release Candidate canonique ;
- `falsification-registry` = registre contradictoire/expérimental attribué et versionné.

Une entrée dans ce registre ne modifie pas automatiquement le produit et ne devient pas automatiquement une vérité canonique.

## Structure

Chaque entrée utilise un identifiant stable :

`FALS-000001`, `FALS-000002`, etc.

Structure recommandée :

```text
falsifications/
  FALS-000001/
    manifest.json
    README.md
    patch.diff
    tests/
    evidence/
    fingerprints/
    provenance/
```

## États autorisés

`SUBMITTED -> REPRODUCED -> ACCEPTED_AS_VALID_FALSIFICATION -> INCORPORATED`

États alternatifs conservant l'historique : `SUPERSEDED`, `REJECTED`.

## Attribution obligatoire

Chaque entrée doit distinguer :

- auteur/propriétaire déclaré du matériau TEBDLC ciblé ;
- falsificateur/contributeur ;
- version TEBDLC et commit SHA exacts ;
- version de la falsification ;
- provenance et filiation ;
- droits/licence déclarés par le falsificateur ;
- hashes et preuves disponibles.

Le registre conserve donc une chaîne de provenance et non une fusion d'auteurs.

## Principe de non-réécriture

Une falsification valide reste dans le registre même après correction du produit. La correction doit référencer la falsification sans supprimer son état historique.

Voir `FALSIFICATION_POLICY.md` pour les règles générales et `registry/manifest.schema.json` pour le format normatif du manifeste.
