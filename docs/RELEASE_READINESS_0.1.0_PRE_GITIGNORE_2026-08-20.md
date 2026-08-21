# TEBDLC 0.1.0 — Release readiness avant `.gitignore`

**Jonathan Therrien, Marieville, Québec.**

Date : 2026-08-20  
Statut : PRÉ-RELEASE TECHNIQUE / ARRÊT VOLONTAIRE AVANT CRÉATION DU `.gitignore`

## 1. Objet

Ce document fixe l'état produit atteint avant la décision explicite sur le `.gitignore`. Il ne publie pas de release et ne modifie pas les droits d'utilisation définis dans `NOTICE.md`.

## 2. Contrat utilisateur désormais disponible

Depuis un checkout disposant des dépendances système :

```bash
make setup
make build
make test
make verify
make sanitize
make release-check
```

L'interface Python fournit également :

```bash
tebdlc info
tebdlc self-check
python3 -m tebdlc self-check
```

## 3. Build C unifié

Le `Makefile` construit et exécute huit familles C :

1. core fractionnaire borné;
2. R8/R9 multi-précision/fracto-récursif;
3. gain impotent;
4. stagnation/compression/réactivation;
5. pont exo/recontextualisation;
6. assimilation comportementale;
7. productivité/factorisation;
8. `ΩSt` Phase 2.

Dépendances déclarées : C11, GMP, OpenSSL/libcrypto et zlib; Clang est utilisé pour les sanitizers.

Le chemin C du Makefile a été reconstruit dans le laboratoire de session à partir des bundles matériels précédemment persistés. Les huit familles ont passé. `make sanitize` a également passé sur le chemin `behavior -> productivity -> ΩSt Phase 2` sous UBSan et ASan.

## 4. Packaging Python

`pyproject.toml` conserve la version `0.1.0` et expose maintenant :

```text
tebdlc = tebdlc.cli:main
```

La CLI possède un `self-check` local déterministe ne nécessitant aucun réseau.

## 5. CI GitHub corrigée en tenant compte d'un dépôt privé

Le workflow CI reproduit maintenant le contrat local :

- matrice Python 3.11 / 3.12 / 3.13;
- tests CLI;
- tests C;
- oracles indépendants;
- sanitizers.

Pour éviter qu'un dépôt privé consomme automatiquement des minutes de runner, les jobs automatiques ne s'exécutent que lorsque le dépôt est public; un `workflow_dispatch` permet une exécution manuelle privée.

Après cette modification, le run associé au commit `620123469c5e329b29c9b5b85c3e055b2fad4b25` est correctement classé `skipped`, et non `failure`. Ce résultat confirme la distinction :

`runner volontairement non exécuté ≠ échec TEBDLC`.

## 6. Audit structurel hors réseau

`tools/release_readiness.py` contrôle :

- présence des composants requis;
- fichiers suivis présentant des signatures usuelles d'artefacts générés;
- fichiers suivis ressemblant à des secrets/configurations privées courants;
- présence ou absence du `.gitignore`.

Ce contrôle est volontairement décrit comme un audit de motifs et ne prétend pas remplacer un scanner de secrets complet de l'historique Git.

## 7. Documentation produit

Le `README.md` documente maintenant :

- statut produit;
- composants;
- prérequis Python/C;
- installation;
- CLI;
- build/test/verify/sanitize;
- propriété intellectuelle;
- distinction validation locale / GitHub Actions;
- liens de traçabilité documentaire.

`docs/BUILD_AND_VERIFY.md` constitue le contrat détaillé de reconstruction et vérification.

## 8. Points volontairement non décidés ici

### 8.1 `.gitignore`

Il n'est pas créé dans ce jalon. Son contenu doit être approuvé explicitement afin de ne pas transformer un filtre de dérivés en perte de preuves ou de composants nécessaires.

### 8.2 Licence / permissions publiques

`NOTICE.md` reste la règle en vigueur : droits réservés, aucune licence open source implicite. Une publication destinée à permettre des usages externes devra préciser les permissions choisies par le propriétaire.

### 8.3 Plateformes officiellement supportées

Le laboratoire courant soutient principalement Linux x86_64. Le dépôt ne doit pas annoncer Windows/macOS/ARM comme officiellement validés tant que leur parcours complet n'a pas été exécuté.

### 8.4 Release GitHub finale

Aucun tag ni release public n'est créé par ce jalon. La publication devra intervenir après :

1. décision `.gitignore`;
2. audit de secrets historique dédié;
3. décision de licence/permissions;
4. dernier parcours de vérification depuis un checkout propre;
5. choix de signature/tag/archives et sommes SHA-256.

## 9. Principe de non-perte appliqué

La préparation produit ajoute une couche d'utilisation au-dessus de la lignée expérimentale; elle ne remplace ni la thèse, ni les preuves, ni les journaux.

`produit utilisable + preuves reconstructibles > produit simplifié par suppression de preuves`.

---

**Jonathan Therrien, Marieville, Québec.**
