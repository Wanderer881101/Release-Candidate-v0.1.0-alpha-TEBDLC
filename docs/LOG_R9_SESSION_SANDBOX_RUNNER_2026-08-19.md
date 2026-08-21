# JOURNAL R9 — Runner sandbox indépendant de GitHub

**Jonathan Therrien, Marieville, Québec.**

Horodatage : 2026-08-19 15:35 America/Montreal
Branche source : `proof/r6-executable-invariants`
Statut : EXPÉRIENCE REPRODUCTIBLE DANS LE SANDBOX DE SESSION / NON ASSIMILÉE À UNE PREUVE UNIVERSELLE

## 1. Objet

Vérifier qu'une session ChatGPT disposant d'un environnement d'exécution isolé peut servir de runner expérimental TEBDLC sans dépendre de GitHub Actions pour l'exécution elle-même.

Le code a été lu depuis GitHub par le connecteur autorisé, puis injecté dans le système de fichiers local du sandbox de session. Le sandbox n'avait pas de résolution réseau directe vers `github.com`; l'échec de `git clone` a donc été conservé comme limite d'environnement, puis contourné par alimentation explicite via le connecteur GitHub.

Cette architecture expérimentale est donc :

    GitHub/Projet comme source versionnée
      → connecteur autorisé
      → sandbox de session isolé
      → compilation / exécution / logs
      → rapport + empreintes

L'exécution des tests ne dépend pas du runner GitHub Actions.

## 2. Environnement observé

- Linux x86_64;
- Python 3.13.5;
- GCC 14.2.0;
- Clang 17.0.0;
- 5 CPU logiques observés;
- environ 5.9 GiB de RAM disponible au niveau du conteneur;
- réseau direct vers GitHub non disponible dans ce sandbox.

## 3. Sources testées

Sous-ensemble C :

- `c_core/tebdlc_core.h`;
- `c_core/tebdlc_core.c`;
- `c_core/test_tebdlc_core.c`.

Empreintes SHA-256 calculées dans le sandbox :

- `tebdlc_core.h` : `43325cd594c4d5058c01aa29f51e97a6d465af3d9191fee4461e5acfdb183729`;
- `tebdlc_core.c` : `976110c30be3879e9a2cb4068277f2b832ab2f4bd9480499a5efff4e0a6a4206`;
- `test_tebdlc_core.c` : `1716155d2ab82f0f5f1254507dfa28c871cc1001cbacd59b04f0c07b7e0bff9b`.

Ces empreintes servent à relier le résultat aux octets effectivement exécutés dans cette expérience.

## 4. Protocole

Compilation stricte C11 :

    -std=c11 -Wall -Wextra -Werror -pedantic

Deux compilateurs : GCC et Clang.

Chaque binaire a été exécuté trois fois indépendamment dans la même session.

Le corpus inclut :

- provenance canonique;
- opérateurs interdits;
- frontière contextuelle;
- zéro/unité invalides comme gain fractionnaire;
- réduction croisée;
- événement volontaire de capacité;
- 608 400 compositions binaires du domaine fini `1 <= n < d <= 40`.

## 5. Résultats des six runs

GCC RUN-1 : PASS
GCC RUN-2 : PASS
GCC RUN-3 : PASS
Clang RUN-1 : PASS
Clang RUN-2 : PASS
Clang RUN-3 : PASS

Résultat logique commun :

    capacity status=1
    required_num_bits=64
    required_den_bits=66
    exhaustive_pairs=608400
    TEBDLC C mirror tests: PASS

Temps observés du premier run : environ 0.24 s avec GCC et 0.23 s avec Clang. Les temps ne sont pas traités comme invariants.

## 6. Sanitizers

Exécutions supplémentaires :

- GCC + UndefinedBehaviorSanitizer : PASS, aucun diagnostic;
- Clang + UndefinedBehaviorSanitizer : PASS, aucun diagnostic;
- Clang + AddressSanitizer avec détection de fuite : PASS, aucun diagnostic.

Ces résultats concernent uniquement les chemins exécutés par le corpus courant.

## 7. Interprétation

L'expérience démontre concrètement qu'un sandbox d'exécution attaché à une session peut servir de runner TEBDLC indépendant du mécanisme GitHub Actions pour :

- compiler;
- exécuter;
- répéter;
- confronter plusieurs compilateurs;
- activer des sanitizers;
- produire des logs;
- calculer des empreintes des sources;
- générer un artefact exportable.

Cela permet notamment de distinguer :

    panne GitHub Actions != échec logique TEBDLC

à condition que les sources injectées et l'environnement soient eux-mêmes journalisés.

## 8. Limites importantes

Ce sandbox de session n'est pas considéré comme stockage permanent ni comme service de fond. Sa durée de vie et sa reproductibilité infrastructurelle ne doivent pas être présumées au-delà de la session disponible.

La session n'est donc pas assimilée à un conteneur souverain persistant au sens infrastructurel. Elle est traitée comme une **instance expérimentale éphémère et instrumentée**.

La fonction Projet pourrait conceptuellement servir de couche d'organisation/provenance autour d'un tel runner, mais cette expérience ne démontre pas qu'un Projet ChatGPT fournisse aujourd'hui un conteneur persistant ou une CI autonome.

## 9. Gain expérimental

Le gain démontré ici est l'existence d'une voie d'exécution supplémentaire :

    GitHub Actions
    ≠ sandbox de session

Les deux peuvent confronter les mêmes sources sans partager le même orchestrateur d'exécution.

Cette indépendance partielle augmente la capacité de falsification, mais ne constitue pas à elle seule une preuve universelle.

---

**Jonathan Therrien, Marieville, Québec.**
**TEBDLC — Tout est bon dans le cochon. Tous droits réservés sauf autorisation explicite du propriétaire.**