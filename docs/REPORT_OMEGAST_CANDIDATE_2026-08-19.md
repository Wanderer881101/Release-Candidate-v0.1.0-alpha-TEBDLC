# RAPPORT EXPÉRIMENTAL — ΩSt candidat

**Auteur : Jonathan Therrien, Marieville, Québec.**  
Date : 2026-08-19  
Statut : CANDIDAT EXPÉRIMENTAL — aucune canonisation universelle.

## Objet
Transformer l'hypothèse exploratoire `ΩSt = complexité stagnante irréductible` en première mesure falsifiable sans prétendre mesurer une complexité algorithmique absolue.

## Définition expérimentale
Pour un ledger déjà factorisé sans perte, on encode canoniquement :
1. chaque signature de facteur (contexte, modèle d'intégration, unité cible, outcome et quatre drapeaux de preuve);
2. chaque multiplicité et les séquences exactes par deltas ULEB128.

`ΩSt_candidate_bits = structural_bits + occurrence_bits`.

Cette quantité est la longueur exacte de CET encodage canonique candidat. Elle n'est ni une preuve de minimalité globale, ni la complexité de Kolmogorov, ni une mesure de malveillance.

## Résultats
- 1 répétition d'une signature : 184 bits.
- 100 répétitions de la même signature : 976 bits.
- 10 signatures distinctes : 1280 bits.
- 20 signatures distinctes : 2800 bits.
- Les 99 répétitions supplémentaires ajoutent 792 bits dans cet encodage, bien moins qu'un stockage naïf de 99 identifiants 64-bit (6336 bits).
- Doubles/non-croissances de séquence sont refusés : la reconstruction exacte prime sur une mesure artificiellement plus petite.

## Batteries
- GCC strict : 3/3 PASS.
- Clang strict : 3/3 PASS.
- Oracle Python indépendant : 3/3 PASS.
- Clang UBSan : PASS.
- Clang ASan + leak detection : PASS.
- Premier build : REFUSÉ par `-Werror=misleading-indentation` avant test fonctionnel; correction de forme puis même sévérité conservée.

## Interprétation
Le résultat soutient H33 sous une forme opérationnelle limitée : le coût représentatif dépend de la structure non factorisée et non du seul nombre brut. Cent répétitions identiques coûtent moins dans ce codage que dix/vingt signatures indépendantes malgré un nombre d'événements supérieur.

## Limites
- La mesure dépend du code canonique choisi; aucune optimalité universelle n'est prouvée.
- Les chaînes sont actuellement comptées octet par octet; dictionnaires, DAG généalogiques et compression entropique ne sont pas encore intégrés.
- Le ledger amont est borné (64 facteurs, 512 occurrences/facteur).
- `ΩSt` reste candidat : ce jalon prouve une mesure reconstructible et falsifiable, pas la notion finale d'irréductibilité.
