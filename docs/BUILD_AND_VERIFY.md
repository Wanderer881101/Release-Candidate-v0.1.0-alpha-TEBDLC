# TEBDLC — Build, test et vérification produit

**Jonathan Therrien, Marieville, Québec.**

Ce document décrit le contrat de build public préparatoire à la version produit `0.1.0`. Il ne remplace pas les journaux expérimentaux : il fournit un chemin reproductible pour reconstruire et vérifier l'état courant depuis un checkout.

## 1. Philosophie

Le build local est la validation primaire reproductible. GitHub Actions est une contre-validation externe lorsqu'un runner est disponible.

`runner indisponible ≠ test TEBDLC échoué`

`test exécuté avec résultat FAIL = échec fonctionnel dans le domaine du test`

## 2. Prérequis

Python : Python >= 3.11, pip, pytest.

C : compilateur C11, GMP, OpenSSL/libcrypto et zlib. Clang est requis pour `make sanitize`.

Debian/Ubuntu :

```bash
sudo apt-get update
sudo apt-get install build-essential clang libgmp-dev libssl-dev zlib1g-dev python3 python3-pip
```

## 3. Commandes officielles

```bash
make help
make setup
make build
make test
make verify
make sanitize
make clean
```

### `make setup`

Installe `pytest`, puis TEBDLC en mode éditable avec `pip install -e .`.

### `make build`

Vérifie la disponibilité des dépendances natives, compile les modules/tests C et compile le bytecode Python.

### `make test`

Exécute :

1. la suite `pytest` sous `tests/`;
2. core C borné;
3. miroir R8/R9 multi-précision;
4. gain impotent;
5. stagnation/compression/réactivation;
6. pont exo/recontextualisation;
7. assimilation comportementale;
8. factorisation/productivité;
9. `ΩSt` Phase 2.

### `make verify`

Exécute `make test`, puis les oracles Python indépendants associés aux familles C pour lesquelles un oracle est persisté.

### `make sanitize`

Compile et exécute le chemin `behavior -> productivity -> ΩSt Phase 2` sous :

- UBSan avec arrêt sur comportement indéfini;
- ASan avec détection de fuites activée.

Cette cible n'affirme pas que chaque ligne de chaque module a été couverte par sanitizer. Elle formalise le chemin actuellement branché et doit être étendue lorsque la couverture produit s'élargit.

### `make clean`

Supprime seulement les sorties régénérables : dossier `build/`, caches de test usuels, `__pycache__` et bytecode Python. Les sources, preuves, vecteurs, journaux et manifestes restent intacts.

## 4. Interface Python / CLI

Après installation :

```bash
tebdlc --version
tebdlc info
tebdlc self-check
tebdlc self-check --json
```

Le `self-check` ne dépend d'aucun service externe : il construit un gain déterministe, l'ajoute à un ledger local et vérifie sa récupération canonique.

## 5. Sorties de build

Les exécutables locaux sont placés sous :

```text
build/c/
build/sanitize/
```

Ils sont dérivés des sources du dépôt. Les preuves persistées sous `evidence/` ne doivent pas être remplacées par ces binaires locaux.

## 6. Validation du Makefile avant intégration

Le contrat C du Makefile a été reproduit dans le laboratoire de session avant son ajout au dépôt avec les dépendances :

- GCC/compilateur C11;
- GMP;
- OpenSSL/libcrypto;
- zlib;
- Clang pour UBSan/ASan.

Les huit exécutables/tests C câblés dans `make test-c` ont passé dans ce lab. `make sanitize` a également passé sur `ΩSt` Phase 2. Ce résultat est une validation de ce parcours et de cet environnement, pas une preuve universelle de portabilité.

## 7. GitHub Actions

La CI doit reproduire le contrat local au lieu d'introduire une seconde logique de build. Le workflow utilise donc `make test-python`, `make test-c` et `make sanitize`.

Sur un dépôt privé, une indisponibilité de minutes GitHub Actions ou une contrainte de facturation peut empêcher les jobs de réellement exécuter les tests. Un tel état doit être classé comme indisponibilité de runner/plateforme tant que les logs ne démontrent pas un échec fonctionnel.

## 8. Limites avant release

Avant la publication d'un premier release public, restent notamment à décider :

- la licence ou les permissions d'utilisation externes;
- le contenu final du `.gitignore`;
- les plateformes officiellement supportées;
- le niveau exact de support des binaires précompilés, le cas échéant;
- la politique de signature des tags/releases et des sommes SHA-256.

Aucune de ces décisions ne doit supprimer les artefacts nécessaires à la reproductibilité scientifique ou à la continuité matérielle.
