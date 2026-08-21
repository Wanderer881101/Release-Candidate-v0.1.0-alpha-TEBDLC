# CONSOLIDATION R10 — ΩSt Phase 2 : structure, histoire reconstructible et continuité matérielle

**Auteur et propriétaire intellectuel : Jonathan Therrien, Marieville, Québec.**

Date : 2026-08-20  
Projet : TEBDLC — Tout est bon dans le cochon  
Statut : CONSOLIDATION ADDITIVE — NE REMPLACE PAS R10 NI L'ADDENDUM PHASE 2

## 1. Objet

Ce document consolide les éléments produits après la R10 et son premier jalon `ΩSt_candidate`, sans modifier rétroactivement les documents antérieurs.

La lignée matérielle est :

    R10
      → ΩSt candidat Phase 1
      → ADDENDUM_R10_OMEGAST_PHASE2
      → corpus structurel/historique Phase 2
      → bundle et preuves Phase 2

Aucun document antérieur n'est supprimé ni déclaré faux du seul fait de cette extension.

## 2. Question expérimentale Phase 2

La Phase 2 demande si `ΩSt_candidate_bits` réagit principalement au volume brut ou si elle distingue aussi :

- la diversité structurelle des facteurs;
- la multiplicité factorisable;
- le coût reconstructible de l'histoire des occurrences;
- les limites du ledger actuel.

La mesure reste :

    ΩSt_candidate_bits = structural_bits + occurrence_bits

et demeure relative à l'encodage candidat défini antérieurement.

## 3. Résultats consolidés

Les cas exécutés donnent :

    100 occurrences / 1 facteur / pas 1   = 992 bits
    400 occurrences / 1 facteur / pas 1   = 3400 bits
    100 occurrences / 1 facteur / pas 128 = 1784 bits
    100 occurrences / 10 facteurs         = 2000 bits
    100 occurrences / 20 facteurs         = 3440 bits
    64 occurrences / 64 facteurs          = 9488 bits

À volume identique de 100 occurrences :

    1 facteur  = 992 bits
    10 facteurs = 2000 bits
    20 facteurs = 3440 bits

Donc, dans ce modèle et sur ce corpus :

    volume brut identique ≠ complexité représentative identique

et :

    diversité structurelle ↑ ⇒ ΩSt_candidate_bits ↑

sur les cas testés.

## 4. Histoire reconstructible

Deux ensembles peuvent posséder la même signature et le même nombre d'occurrences tout en exigeant un coût différent pour reconstruire leurs positions historiques.

Le cas témoin compare :

    100 occurrences, deltas = 1   → 992 bits
    100 occurrences, deltas = 128 → 1784 bits

Ainsi, dans l'encodage candidat :

    même structure + même volume ≠ même coût historique reconstructible

Cette propriété est importante parce que la non-perte de gain interdit de compacter une chronologie au point de perdre la capacité de la reconstruire lorsque cette chronologie fait partie de la preuve.

## 5. Raccord aux couches comportementales existantes

Le test Phase 2 utilise les structures `tebdlc_bh_observation` et `tebdlc_px_ledger` déjà développées. La chaîne effective devient donc :

    observation comportementale
      → signature factorisable
      → ledger de productivité
      → occurrences reconstructibles
      → ΩSt_candidate

Cela ne signifie pas que `ΩSt_candidate` mesure une personne, une identité, une intention ou une malveillance. Elle mesure uniquement le coût de l'encodage déclaré des structures fournies au moteur.

## 6. Batterie de validation

Le jalon Phase 2 est accompagné de :

- test C strict;
- oracle Python indépendant;
- 3 exécutions GCC;
- 3 exécutions Clang;
- 3 exécutions de l'oracle Python;
- UBSan;
- ASan avec détection de fuites;
- vecteurs de référence;
- logs bruts;
- empreintes;
- manifeste de continuité;
- rapport expérimental;
- bundle de laboratoire complet.

Les résultats observés sont stables dans l'environnement testé. Cette stabilité ne constitue pas une preuve universelle.

## 7. Bundle matériel

Le bundle complet du laboratoire est identifié comme :

    TEBDLC_omegast_phase2_2026-08-19.tar.gz

avec SHA-256 :

    41a4d2fb62a22417096f45d1dc0182947b5f49b95422ff4422c7bcc3171080d1

Les exécutables GCC, Clang, UBSan et ASan présents dans le bundle sont des artefacts dérivés. Leurs empreintes exactes sont conservées dans :

    evidence/milestones/omegast-phase2-structural-history-2026-08-19/BUNDLE_PROVENANCE.txt

Ils ne deviennent pas la source canonique : le code, les tests et la procédure reproductible restent l'autorité matérielle.

## 8. Limites conservées

La Phase 2 ne démontre pas :

1. une métrique universellement minimale;
2. une équivalence à une complexité de Kolmogorov;
3. une indépendance par rapport au choix d'encodage;
4. un comportement au-delà des bornes actuelles du ledger;
5. une représentation complète de `Gain / Relation / Preuve / Transformation / Contexte / Généalogie`;
6. une capacité d'attribution identitaire;
7. une propriété générale sur toutes architectures matérielles ou tous compilateurs.

La borne de 64 facteurs distincts est testée comme limite actuelle, pas comme cible définitive.

## 9. Conséquence pour la suite

Le prochain test légitime ne consiste pas simplement à augmenter les nombres. Il consiste à enrichir la structure encodée en séparant explicitement :

    Gain
    Relation
    Preuve
    Transformation
    Contexte
    Généalogie

puis à vérifier si l'encodage candidat reste reconstructible, falsifiable et cohérent lorsqu'une stagnation devient relationnelle plutôt que seulement une signature plate.

Cette direction prolonge R10; elle ne justifie pas à elle seule une nouvelle révision doctrinale.

## 10. Règle de non-perte appliquée

Pour ce jalon :

    source + tests + vecteurs + logs + empreintes + résultats + documentation + provenance du bundle

sont persistés ou référencés matériellement.

Un futur changement d'encodage devra créer une nouvelle preuve comparative. Il ne devra pas réécrire silencieusement les valeurs Phase 1 ou Phase 2.

---

**Jonathan Therrien, Marieville, Québec.**  
**TEBDLC — Tout est bon dans le cochon. Tous droits réservés sauf autorisation explicite du propriétaire.**
