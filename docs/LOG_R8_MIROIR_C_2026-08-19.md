# JOURNAL EXPÉRIMENTAL R8 — Construction du miroir C

**Jonathan Therrien, Marieville, Québec.**

Horodatage initial : 2026-08-19 12:10 America/Montreal
Branche : `proof/r6-executable-invariants`
Révision doctrinale de référence : R8

## 0. Objet

Ce journal trace avant, pendant et après la construction du premier miroir sémantique C de TEBDLC. Il ne remplace ni la thèse ni la matrice de preuve. Il documente l'exécution réelle, les décisions, les limites, les divergences et les résultats observés.

## 1. État avant construction

Le modèle Python actuel expose notamment :

- `ExactFractionalGain` avec rationnels exacts;
- multiplication uniquement entre contextes compatibles;
- refus explicite de `+`, `-`, `/` comme primitives de gain;
- conservation/déduplication de provenance;
- `ImpotentGainEnvelope` séparant masse arithmétique et intégrabilité;
- corpus R6 de 780 fractions et 608400 paires;
- cas profond `(3/10)^1000`;
- cas impotent `600/361 > 1` sans unité.

R8 ajoute la contrainte suivante pour le miroir C :

    valeur ≠ représentation ≠ capacité

et exige :

    capacité insuffisante
      → état typé
      → aucune valeur corrompue
      → promotion/reprise exacte lorsque disponible

## 2. Choix de cette première itération

Cette première version C est volontairement bornée à `uint64_t` afin de rendre les seuils de capacité observables. Elle ne prétend pas encore fournir la multi-précision finale.

Cette limitation est intentionnelle : le but est de prouver que le Core C sait refuser une opération avant overflow silencieux et produire un état `TEBDLC_CAPACITY_EXPANSION_REQUIRED` reconstructible.

La version initiale doit donc :

1. normaliser des rationnels strictement compris entre 0 et 1;
2. conserver les métadonnées sémantiques essentielles par références immuables;
3. vérifier la composabilité;
4. multiplier avec anticipation d'overflow;
5. refuser addition/soustraction/division comme opérations de gain;
6. exposer un résultat typé;
7. ne jamais convertir vers `double` pour poursuivre un calcul exact;
8. conserver les opérandes lorsqu'une expansion est requise.

## 3. Risques connus avant implémentation

- overflow de `uint64_t` lors du produit numérateur/dénominateur;
- overflow dans les contrôles eux-mêmes si mal écrits;
- normalisation pouvant masquer un besoin de capacité si appliquée trop tard;
- perte de provenance si les structures utilisent des buffers non possédés correctement;
- confusion entre erreur de capacité et valeur zéro;
- divergence sémantique avec Python sur la réduction des fractions;
- erreur de comparaison par produit croisé pouvant elle-même overflow.

## 4. Stratégies retenues

- `a > UINT64_MAX / b` pour anticiper le dépassement avant multiplication;
- réduction croisée par `gcd` avant multiplication afin de limiter la taille sans changer la valeur;
- aucun produit croisé potentiellement dangereux pour vérifier `value < 1`; utiliser `numerator < denominator` sur une fraction normalisée positive;
- métadonnées textuelles référencées, sans mutation pendant l'opération;
- statut séparé de la valeur;
- résultat non initialisé comme valeur valide lorsqu'un statut n'est pas `TEBDLC_OK`.

## 5. Statuts expérimentaux

- `TEBDLC_OK`
- `TEBDLC_CAPACITY_EXPANSION_REQUIRED`
- `TEBDLC_FORBIDDEN_OPERATION`
- `TEBDLC_INCOMPATIBLE_CONTEXT`
- `TEBDLC_INVALID_REPRESENTATION`

Ces statuts restent expérimentaux et ne constituent pas encore une ABI canonique.

## 6. Pendant la construction

### 6.1. Fichiers créés

- `c_core/tebdlc_core.h`
- `c_core/tebdlc_core.c`
- `c_core/test_tebdlc_core.c`

### 6.2. Implémentation

Le miroir borné utilise :

- validation `0 < numerator < denominator`;
- comparaison stricte des champs `domain`, `dimension`, `unit`, `reference`, `context`;
- réduction croisée par `gcd` avant multiplication;
- détection préventive de dépassement avec division de borne `UINT64_MAX / operand`;
- résultat typé contenant une copie des opérandes lors d'un événement de capacité;
- aucun fallback flottant;
- fonctions explicites retournant `TEBDLC_FORBIDDEN_OPERATION` pour addition, soustraction et division.

### 6.3. Cas de test construits

1. `3/10 × 3/10 → 9/100`;
2. addition/soustraction/division refusées;
3. contextes différents refusés;
4. zéro et unité refusés comme `ExactFractionalGain` borné;
5. réduction croisée évitant un faux événement de capacité;
6. multiplication volontairement au-delà de la capacité du dénominateur `uint64_t`, avec conservation des deux opérandes dans le résultat typé.

## 7. Résultats observés

### 7.1. Environnement local

Compilateurs observés :

- GCC 14.2.0;
- Clang 17.0.0.

Options :

    -std=c11 -Wall -Wextra -Werror -pedantic

### 7.2. Répétitions GCC

Trois compilations/exécutions successives ont donné le même résultat :

    PASS status=1 required_num_bits=64 required_den_bits=66

RUN-C-GCC-01 : PASS
RUN-C-GCC-02 : PASS
RUN-C-GCC-03 : PASS

Aucune différence logique observée entre les trois exécutions.

### 7.3. Exécution Clang

Une compilation/exécution Clang a donné :

    PASS status=1 required_num_bits=64 required_den_bits=66

RUN-C-CLANG-01 : PASS

Résultat logique identique aux trois runs GCC sur le corpus courant.

### 7.4. Compréhension du seuil

Le cas volontaire :

    n = 4294967295
    d = 4294967297
    (n/d) × (n/d)

produit un numérateur encore représentable dans 64 bits, mais un dénominateur nécessitant plus de 64 bits. Le Core C retourne donc `TEBDLC_CAPACITY_EXPANSION_REQUIRED` avant de calculer un dénominateur corrompu.

Le diagnostic retourné est :

    required_num_bits = 64
    required_den_bits = 66

Le statut `1` correspond à `TEBDLC_CAPACITY_EXPANSION_REQUIRED` dans cette ABI expérimentale.

### 7.5. Résultat important

Le test ne prouve pas encore la reprise multi-précision. Il démontre actuellement que la représentation bornée peut :

- reconnaître sa propre insuffisance;
- refuser de fabriquer une valeur;
- préserver les opérandes nécessaires à une reprise future;
- distinguer cet état de zéro, de l'unité et d'une valeur valide.

## 8. Interprétation

Le premier miroir C valide donc un sous-ensemble de R8 :

    capacité insuffisante ≠ valeur corrompue

et fournit un témoin exécutable de :

    opération exacte
      → détection préventive
      → état typé reconstructible

La répétition sous GCC et la reproduction sous Clang augmentent la confiance dans le comportement observé sur cet environnement. Elles ne constituent pas une preuve universelle multi-architecture.

La réduction croisée est particulièrement importante : elle évite de signaler artificiellement un besoin de capacité lorsqu'une simplification exacte rend le produit représentable. Cela distingue un vrai manque de capacité d'un mauvais ordre d'opérations.

## 9. Divergence/limite découverte pendant la construction

La provenance n'est **pas encore un miroir exact** du modèle Python.

Python conserve un tuple de chaînes, fusionne les provenances des opérandes, élimine les doublons et les trie. La première structure C ne contient encore qu'une référence textuelle `provenance` et le résultat valide reprend actuellement les métadonnées du premier opérande.

Statut : **DIVERGENCE SÉMANTIQUE CONNUE — À CORRIGER AVANT CONFORMITÉ DU MIROIR**.

Cette divergence n'est pas masquée par les tests de capacité et interdit de déclarer la première itération comme miroir C complet de `ExactFractionalGain`.

Autres limites :

- multi-précision non encore implémentée;
- reprise exacte après promotion non encore exécutée;
- `ImpotentGainEnvelope` non encore reproduit en C;
- corpus exhaustif des 608400 paires non encore exécuté dans le binaire C;
- sanitizers non encore consignés dans ce journal;
- aucune validation multi-architecture;
- durées d'exécution non mesurées dans cette première série C.

## 10. Prochaine correction obligatoire

Avant de qualifier le miroir de sémantiquement conforme au sous-ensemble Python, il faut au minimum :

1. représenter une provenance multi-valeurs en C;
2. fusionner/dédupliquer de manière canonique les provenances comme Python;
3. tester la conservation de provenance sur multiplication;
4. exécuter le corpus des 608400 paires en C;
5. ajouter une voie multi-précision et démontrer la reprise exacte après `CAPACITY_EXPANSION_REQUIRED`;
6. reproduire ensuite l'enveloppe impotente et ses trois régimes de masse.

## 11. Conclusion provisoire

Résultat actuel : **MIROIR C BORNÉ PARTIEL, TESTABLE ET NON SILENCIEUX EN CAS DE CAPACITÉ INSUFFISANTE**.

Il ne doit pas encore être décrit comme miroir exact complet.

---

**Jonathan Therrien, Marieville, Québec.**
**TEBDLC — Tout est bon dans le cochon. Tous droits réservés sauf autorisation explicite du propriétaire.**
