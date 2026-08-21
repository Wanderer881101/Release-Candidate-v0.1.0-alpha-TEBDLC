# JOURNAL EXPÉRIMENTAL R8 — Miroir C — PHASE 2

**Jonathan Therrien, Marieville, Québec.**

Horodatage : 2026-08-19 12:10+ America/Montreal
Branche : `proof/r6-executable-invariants`
Document parent : `docs/LOG_R8_MIROIR_C_2026-08-19.md`

## 0. Règle de continuité

Le journal Phase 1 reste intact. Les limites qui y sont inscrites étaient réelles au moment de l'observation. Phase 2 documente leur transformation :

    divergence observée → correction → nouveau test → nouveau résultat

Aucune correction ne réécrit rétroactivement le fait que la divergence a existé.

## 1. Divergence ciblée

Phase 1 avait identifié :

    provenance_C_simple ≠ provenance_Python_multi-valeurs

Le modèle Python fusionne les provenances des deux opérandes, élimine les doublons et produit un ordre canonique.

## 2. Transformation implémentée

Le Core C contient désormais :

- `tebdlc_provenance` multi-valeurs;
- une capacité bornée expérimentale `TEBDLC_MAX_PROVENANCE = 16`;
- fusion des provenances des deux opérandes;
- élimination des doublons;
- tri lexical canonique;
- statut `TEBDLC_PROVENANCE_CAPACITY_REQUIRED` si la capacité de provenance est insuffisante;
- conservation du besoin de capacité au lieu d'une troncature silencieuse.

Cette capacité bornée n'est pas canonique. Elle sert à rendre un futur dépassement explicite et traitable selon R8.

## 3. Test de provenance

Entrée :

    A.provenance = ["A", "shared"]
    B.provenance = ["B", "shared"]

Opération :

    3/10 × 2/5

Résultat attendu et observé :

    value = 3/25
    provenance = ["A", "B", "shared"]
    provenance_count = 3

Le doublon `shared` n'est pas répété.

Statut : **PASS sur le cas testé**.

## 4. Corpus exhaustif C

Le harnais C exécute maintenant le même domaine fini de petites fractions que le corpus Python R6 :

- dénominateurs 2..40;
- numérateurs 1..d-1;
- 780 fractions candidates avant répétitions de valeurs réduites;
- 608400 paires ordonnées;
- chaque résultat doit retourner `TEBDLC_OK`;
- chaque résultat doit satisfaire `0 < numerator < denominator`.

## 5. Répétitions GCC — Phase 2

Compilateur observé : GCC 14.2.0.

Options :

    -std=c11 -Wall -Wextra -Werror -pedantic

Trois exécutions successives :

    RUN-C2-GCC-01 : PASS pairs=608400 status=1 numbits=64 denbits=66 prov=3
    RUN-C2-GCC-02 : PASS pairs=608400 status=1 numbits=64 denbits=66 prov=3
    RUN-C2-GCC-03 : PASS pairs=608400 status=1 numbits=64 denbits=66 prov=3

Aucune divergence logique observée entre les trois exécutions.

Total des compositions fractionnaires de Phase 2 exécutées sous GCC :

    3 × 608400 = 1 825 200

sans violation observée du confinement fractionnaire sur ce domaine fini.

## 6. Clang — précision méthodologique

Une première tentative Clang de Phase 2 sur une **transcription locale compacte** a échoué avant exécution parce que cette transcription contenait `int main()` au lieu de `int main(void)`, et `-Werror -Wstrict-prototypes` a correctement refusé le programme.

Cette erreur appartenait au harnais local de reproduction, pas au fichier GitHub, dont `main(void)` est explicite. Elle est conservée ici afin de ne pas transformer une erreur opératoire en non-événement.

Après correction de cette transcription locale :

    RUN-C2-CLANG-01 : PASS pairs=608400 status=1 numbits=64 denbits=66 prov=3

Compilateur : Clang 17.0.0.

Une tentative supplémentaire de cloner directement la branche GitHub dans le conteneur a été bloquée par l'absence de résolution réseau (`Could not resolve host: github.com`). Elle n'est donc pas comptée comme test de code.

## 7. Événement de capacité confirmé

Cas :

    n = 4294967295
    d = 4294967297
    (n/d) × (n/d)

Résultat répété :

    status = TEBDLC_CAPACITY_EXPANSION_REQUIRED
    required_num_bits = 64
    required_den_bits = 66

Les opérandes restent présents dans `tebdlc_fractional_result`.

Interprétation : la représentation `uint64_t` reconnaît que le dénominateur final dépasse sa capacité avant de produire une valeur corrompue.

## 8. État de conformité après Phase 2

Acquis expérimentaux sur le sous-ensemble testé :

- multiplication rationnelle exacte tant que la représentation bornée suffit;
- réduction croisée exacte;
- refus de zéro et de l'unité comme gain fractionnaire;
- refus de `+`, `-`, `/` comme primitives de gain;
- frontière de contexte;
- provenance multi-valeurs fusionnée, dédupliquée et triée sur le cas testé;
- détection explicite de capacité avant overflow du produit;
- 608400 paires exécutées par run C;
- répétabilité GCC ×3;
- reproduction Clang ×1 sur la transcription corrigée.

## 9. Ce qui reste non prouvé / non construit

Le terme **miroir C complet** reste interdit à ce stade, car manquent encore :

1. multi-précision réelle;
2. reprise exacte après `TEBDLC_CAPACITY_EXPANSION_REQUIRED`;
3. test de capacité de provenance >16 avec transformation de représentation;
4. reproduction C de `ImpotentGainEnvelope`;
5. comparaison automatisée sortie-par-sortie Python/C à partir d'un corpus canonique partagé;
6. sanitizers et analyse statique consignés;
7. multi-architecture;
8. sérialisation canonique inter-langages;
9. gestion mémoire et ownership définitifs des chaînes/provenances;
10. tests de fuzzing/property-based côté C.

## 10. Conclusion Phase 2

Le résultat peut désormais être qualifié de :

> **miroir C borné du noyau fractionnaire, avec provenance canonique expérimentale, détection non silencieuse des limites de capacité et reproduction du corpus fini R6.**

Il ne peut pas encore être qualifié de miroir intégral TEBDLC ni de miroir exact pour les valeurs nécessitant multi-précision.

---

**Jonathan Therrien, Marieville, Québec.**
**TEBDLC — Tout est bon dans le cochon. Tous droits réservés sauf autorisation explicite du propriétaire.**
