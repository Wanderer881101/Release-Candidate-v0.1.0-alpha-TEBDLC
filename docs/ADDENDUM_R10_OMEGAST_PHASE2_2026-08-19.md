# ADDENDUM R10 — ΩSt Phase 2 : stress structurel et historique

**Auteur et propriétaire intellectuel : Jonathan Therrien, Marieville, Québec.**

Date : 2026-08-19  
Statut : ADDENDUM EXPÉRIMENTAL À R10 — ΩSt demeure candidat, non canonique.  
Projet : TEBDLC — Tout est bon dans le cochon

## 1. Non-réécriture
Cet addendum ne remplace ni R10 ni le premier jalon `ΩSt_candidate`. Il ajoute une seconde batterie destinée à éprouver deux propriétés qui restaient insuffisamment séparées : diversité structurelle et coût historique reconstructible.

    ΩSt_phase2 = ΩSt_candidate + stress_structurel + stress_historique

avec :

    nouveau_test ≠ nouvelle_métrique
    davantage_de_bits ≠ davantage_de_valeur
    davantage_de_bits ≠ malveillance
    même_nombre_d_occurrences ≠ même_complexité_structurelle

## 2. Raccord réel au ledger de productivité
Contrairement au premier test qui pouvait construire directement certains facteurs, Phase 2 alimente le ledger via `tebdlc_px_record`. La factorisation de productivité devient donc l'entrée réelle de la mesure ΩSt candidate.

Le chemin testé est :

    observations comportementales
      → enregistrement productivité
      → factorisation sans perte
      → ledger reconstructible
      → ΩSt_candidate_bits

## 3. Stress à occurrence totale identique
Trois cas possèdent exactement 100 occurrences :

    100 occurrences / 1 facteur   = 992 bits
    100 occurrences / 10 facteurs = 2000 bits
    100 occurrences / 20 facteurs = 3440 bits

La quantité brute d'occurrences est identique, mais le nombre de structures distinctes augmente. Le codage candidat augmente en conséquence.

Ce résultat renforce expérimentalement la distinction :

    Volume(St) ≠ ΩSt_candidate

et soutient H33 dans le domaine testé.

## 4. Stress de répétition massive
Une même signature répétée 100 fois puis 400 fois donne :

    rep100 = 992 bits
    rep400 = 3400 bits

L'augmentation reste portée par l'information nécessaire à reconstruire les occurrences; la structure du facteur n'est pas dupliquée 400 fois.

## 5. Stress historique par espacement de séquences
Pour 100 occurrences de la même signature :

    deltas de séquence = 1    → 992 bits
    deltas de séquence = 128  → 1784 bits

Le nombre de facteurs et d'occurrences ne change pas. La différence provient uniquement du coût de reconstruction des séquences dans l'encodage ULEB128.

Ainsi, dans CET encodage candidat :

    même_structure + même_volume ≠ même_coût_historique

Ce résultat est important : ΩSt candidate conserve une trace du coût reconstructible de la généalogie temporelle, sans prétendre que ce coût est intrinsèquement optimal.

## 6. Borne actuelle
Le cas de 64 facteurs distincts — borne actuelle `TEBDLC_PX_MAX_FACTORS` — produit :

    distinct64 = 9488 bits

Ce résultat n'autorise aucune extrapolation au-delà de cette borne. Il documente au contraire la limite matérielle du ledger actuel.

## 7. Reproductibilité
Batterie exécutée dans le lab de session : GCC strict 3/3 PASS; Clang strict 3/3 PASS; oracle Python indépendant 3/3 PASS; Clang UBSan PASS; Clang ASan + leak detection PASS. Toutes les exécutions ont produit les mêmes valeurs.

## 8. Ce qui est soutenu
Sur les scénarios testés : diversité structurelle indépendante du nombre total d'occurrences; répétition reconstructible sans duplication de structure complète; coût historique des séquences; raccord `productivity → ΩSt`; déterminisme GCC/Clang/Python.

## 9. Ce qui ne doit pas être conclu
Phase 2 ne démontre pas l'optimalité ULEB128, une complexité universelle, une valeur comportementale positive/négative, une identité, une intention ou une malveillance, ni l'acceptabilité finale des bornes actuelles.

## 10. Suite logique conservée
Le prochain approfondissement doit porter sur `Relation`, `Preuve`, `Transformation` et généalogie structurée afin de vérifier si la mesure candidate reste reconstructible lorsque les signatures plates deviennent des structures reliées.

---
**Jonathan Therrien, Marieville, Québec.**  
**TEBDLC — Tout est bon dans le cochon. Tous droits réservés sauf autorisation explicite du propriétaire.**
