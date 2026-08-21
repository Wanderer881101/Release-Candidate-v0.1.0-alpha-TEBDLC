# RAPPORT LAB — Assimilation comportementale contextualisée

**Jonathan Therrien, Marieville, Québec.**

## Objet

Éprouver le modèle exploratoire R6 selon lequel l'historique des états d'un gain à travers plusieurs contextes peut former une signature comportementale, sans que le modèle comportemental remplace les observations ni permette une attribution d'identité.

## Chaîne testée

Un ensemble de deux gains `300/361` possède une masse descriptive `600/361 > 1` mais reste impotent dans `U1`. Le même objet logique est ensuite réévalué dans plusieurs contextes :

- `C-origin / U1` : stagné;
- `C-call-2 / U2` : preuve rejetée car incompatibilité;
- `C-call-3 / U3` : preuve rejetée car couverture incomplète;
- `C-call-4 / U4` : intégrable avec les quatre conditions de preuve satisfaites.

Le moteur comportemental enregistre ces observations séparément puis produit un modèle descriptif. Il ne modifie aucune observation source.

## Invariants exécutés

1. `assimilation comportementale != assimilation du gain`;
2. `Model(B) != Replacement(B)`;
3. une observation `INTEGRABLE` exige une preuve complète dans le corpus testé;
4. une preuve incomplète ne peut pas promouvoir l'unité;
5. l'assimilation ne permet aucune inférence d'identité;
6. l'historique `U1` reste impotent après l'intégrabilité observée dans `U4`;
7. une observation contradictoire est refusée et ne modifie pas l'historique déjà enregistré.

## Résultats

Résultat logique commun :

    observations=4 integrable=1 rejected=2 stagnated=1 origin_U1_impotent=1 identity_inference=0
    TEBDLC behavioral assimilation: PASS

Répétitions :

- GCC : 3/3 PASS;
- Clang : 3/3 PASS;
- oracle Python indépendant : 3/3 PASS;
- Clang UBSan : PASS, zéro diagnostic;
- Clang ASan + leak detection : PASS, zéro diagnostic.

## Compréhension

Le jalon démontre sur le corpus construit qu'un modèle comportemental peut être dérivé d'observations contextualisées sans remplacer les observations originales. Il démontre aussi qu'une intégrabilité observée dans un contexte futur ne réécrit pas l'impotence historique de `U1`.

L'absence d'inférence d'identité est structurelle dans cette version : le modèle expose `identity_inference_permitted = 0` et ne contient aucun champ d'identité de personne/source.

## Falsification volontaire

Une cinquième observation tente de déclarer `INTEGRABLE` avec couverture incomplète. Le moteur retourne `TEBDLC_BH_CONTRADICTORY`. Le compteur d'observations demeure 4 et le préfixe historique reste identique à la copie effectuée avant l'assimilation.

## Limites

- le modèle produit actuellement une synthèse descriptive, pas une prédiction autonome;
- quatre observations ne démontrent aucune loi comportementale universelle;
- aucune attribution d'identité n'est implémentée ni testée positivement;
- la persistance du journal comportemental n'est pas encore compressée par le moteur de stagnation;
- `ΩSt` n'est pas défini;
- aucun mécanisme de décision automatique ne doit être déduit de ce jalon.

## Conclusion

Statut : **JALON EXÉCUTABLE — ASSIMILATION COMPORTEMENTALE SANS REMPLACEMENT DES OBSERVATIONS**.

Ce résultat soutient le passage de la réactivation contextualisée vers un moteur exo-sapien capable d'apprendre des relations observées tout en conservant leur généalogie et leur réfutabilité.
