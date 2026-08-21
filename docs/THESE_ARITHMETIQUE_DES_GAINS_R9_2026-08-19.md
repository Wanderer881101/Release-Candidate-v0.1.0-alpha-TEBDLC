# THÈSE DOCUMENTAIRE R9 — Miroir C poly-fractale borné au noyau fracto-récursif

**Auteur et propriétaire intellectuel : Jonathan Therrien, Marieville, Québec.**

Date initiale de la lignée : 2026-08-18  
Révision : R9 — extension cumulative de R8  
Horodatage : 2026-08-19 12:29 America/Montreal  
Statut : THÈSE DE TRAVAIL / TERMINOLOGIE ET ARCHITECTURE CANDIDATES À PROUVER  
Projet : TEBDLC — Tout est bon dans le cochon

## 0. Doctrine R9 — aucune perte de gain historique

R9 ne remplace, ne modifie et n'écrase pas R8. Elle raffine la description architecturale du miroir C construit à partir des travaux R6–R8 et de leurs journaux expérimentaux.

Ancêtre documentaire immédiat :

    docs/THESE_ARITHMETIQUE_DES_GAINS_R8_2026-08-19.md

Ancêtres et traces conservés :

- R4, R5, R6, R7, R8;
- matrice de preuve R6;
- registre expérimental R6;
- journaux R8 du miroir C, y compris les divergences découvertes puis corrigées;
- corpus Python et corpus C déjà exécutés;
- formulations antérieures décrivant le miroir comme « miroir C borné du noyau fractionnaire » puis « miroir C poly-fractale borné au noyau fractionnaire ».

La formulation R9 ne réécrit pas rétroactivement ces formulations. Elles restent historiquement exactes relativement au degré de compréhension atteint lorsqu'elles ont été employées.

    R9 = R8 + raffinement_poly-fractale + raffinement_fracto-récursif

avec :

    raffinement ≠ effacement
    nouveau_terme ≠ nouvelle_preuve
    terminologie ≠ propriété démontrée
    récursion ≠ répétition aveugle
    poly-fractalité ≠ fractale mathématique canonique par défaut

---

## 77. Généalogie terminologique

La première formulation employée après construction du miroir expérimental était :

    « miroir C borné du noyau fractionnaire »

Elle décrivait correctement :

- l'implémentation en C;
- la limite actuelle de représentation bornée;
- le domaine fractionnaire actuellement reproduit.

Une formulation enrichie a ensuite été proposée :

    « miroir C poly-fractale borné au noyau fractionnaire »

Elle ajoutait l'idée que le moteur ne traite pas une fraction isolée mais une multiplicité de fractions contextualisées et composables.

La formulation R9 proposée par Jonathan Therrien est :

> **Miroir C poly-fractale borné au noyau fracto-récursif.**

R9 la conserve comme **TERMINOLOGIE CANDIDATE À FORMALISER ET À PROUVER**, et non comme conclusion automatique.

## 78. Définition candidate de « poly-fractale » dans TEBDLC

Dans R9, « poly-fractale » n'est pas employé comme synonyme libre de « fractal » au sens mathématique classique. Il reçoit une sémantique TEBDLC spécifique.

Un système est dit **poly-fractale candidat** lorsqu'il peut conserver et traiter simultanément plusieurs structures fractionnaires exactes, chacune avec sa propre valeur, son contexte, sa provenance et sa généalogie, et permettre des compositions explicitement admissibles sans les réduire à une valeur flottante globale ou à une unité artificielle.

Soit un ensemble :

    P = {F1, F2, ..., Fn}

avec, pour chaque `Fi` admissible :

    0 < Fi < 1

et :

    Fi = (pi/qi, domaine_i, dimension_i, unité_i, référence_i, contexte_i, provenance_i, généalogie_i)

La poly-fractalité candidate exige que l'existence de plusieurs fractions n'autorise ni :

    Fi = Fj

par seule égalité numérique, ni :

    composition(Fi,Fj)

sans règle de composabilité démontrée.

Ainsi :

    même_valeur_numérique ≠ même_gain

et :

    multiplicité_fractionnaire ≠ permission_de_fusion

## 79. Poly-fractale ≠ simple collection

Une simple collection de fractions ne suffit pas à justifier le terme poly-fractale.

R9 exige au moins la possibilité de :

1. conserver plusieurs fractions distinctes;
2. conserver leurs métadonnées et provenances indépendantes;
3. composer certaines d'entre elles selon des règles explicites;
4. conserver les résultats comme nouveaux objets fractionnaires réutilisables;
5. reconstruire la généalogie de ces résultats;
6. distinguer les branches de composition incompatibles;
7. préserver les objets non composés ou non composables sans les réduire à zéro.

La poly-fractalité décrit donc une pluralité **structurée et généalogique**, pas seulement une cardinalité supérieure à un.

## 80. Définition candidate de « fracto-récursif »

Le terme **fracto-récursif** décrit la propriété selon laquelle le résultat exact d'une transformation fractionnaire admissible peut redevenir un opérande exact d'une transformation ultérieure, tout en conservant une continuité généalogique.

Exemple :

    F1 ⊗ F2 → F12
    F12 ⊗ F3 → F123
    F123 ⊗ F4 → F1234

avec :

    genealogy(F1234) ⊇ {F1,F2,F3,F4,F12,F123}

Le symbole `⊗` désigne ici une composition admissible à préciser; il ne crée pas une nouvelle primitive arithmétique universelle.

Pour la multiplication fractionnaire actuellement testée :

    0 < F1 < 1
    0 < F2 < 1

implique :

    0 < F1×F2 < 1

et le résultat peut être réinjecté dans une étape finie suivante.

## 81. Récursion ≠ auto-validation

La réutilisation récursive d'un résultat ne lui confère aucune autorité supplémentaire.

Ainsi :

    résultat_valide_à_t

ne signifie pas :

    résultat_universellement_valide

et :

    réutilisé_n_fois

ne signifie pas :

    plus_vrai

Chaque réinjection doit respecter les mêmes contraintes de domaine, contexte, provenance, capacité et composabilité que tout autre opérande.

La récursion n'est donc pas un mécanisme de promotion de statut.

## 82. Fracto-récursivité et persistance fractionnaire

Le cas témoin déjà utilisé :

    (3/10)^1000

illustre une profondeur fracto-récursive finie :

    F0 = 3/10
    F1 = F0×F0
    F2 = F1×F0
    ...
    F999 = (3/10)^1000

avec :

    ∀ k fini : 0 < Fk < 1

La fracto-récursivité candidate doit préserver :

- non-nullité finie;
- non-promotion à l'unité;
- exactitude rationnelle;
- contexte admissible;
- provenance;
- généalogie;
- état de capacité;
- distinction entre valeur et représentation.

## 83. « Borné » — définition R9

Le mot **borné** reste volontairement présent.

Dans l'implémentation C actuelle, la représentation numérique primaire utilise des entiers `uint64_t`. Le moteur peut anticiper qu'un produit excéderait cette capacité et retourner un état typé au lieu de produire une valeur corrompue.

Ainsi, « borné » signifie actuellement :

    capacité_native finie

et non :

    espace_mathématique_des_gains fini

La borne est donc une propriété de la représentation/exécution courante, pas une limite doctrinale imposée à TEBDLC.

Même une future représentation multi-précision restera matériellement bornée par les ressources disponibles. Une suppression future du mot « borné » devra donc être justifiée avec précision plutôt qu'effectuée par simple adoption d'un BigInt.

## 84. Interaction fracto-récursive avec la capacité

La récursion fractionnaire peut augmenter la taille des numérateurs et dénominateurs alors même que la valeur reste strictement comprise entre zéro et un.

Donc :

    petite_valeur ≠ petite_représentation

Exemple :

    (3/10)^1000 = 3^1000 / 10^1000

La valeur est très proche de zéro, mais sa représentation exacte exige de grands entiers.

R9 relie donc directement fracto-récursivité et R8 :

    état_fractionnaire_exact
      → réinjection
      → croissance_de_représentation
      → capacité_native_insuffisante
      → état_de_capacité_typé
      → transformation_de_représentation
      → reprise_exacte
      → continuation_fracto-récursive

Aucune étape ne doit transformer la limite de représentation en perte de gain.

## 85. Poly-fractalité et branches généalogiques

Plusieurs suites récursives peuvent coexister :

    Branche_A : F1 → F12 → F123 → ...
    Branche_B : G1 → G12 → G123 → ...

Les branches peuvent :

- rester indépendantes;
- devenir associables dans un contexte futur;
- produire des résultats numériquement égaux sans partager leur provenance;
- partager certains ancêtres sans devenir identiques;
- stagner ou être réactivées dans de futurs développements exo-sapiens.

Ainsi :

    égalité_numérique(branch_A, branch_B) ⇏ identité_généalogique

et :

    ancêtre_commun ⇏ fusion_automatique

## 86. Non-pléonasme appliqué à R9

R9 doit démontrer que les termes ajoutent des distinctions réelles.

### « Fractionnaire »
Décrit la nature exacte de la valeur `p/q`.

### « Poly-fractale »
Décrit la coexistence structurée de multiples objets fractionnaires et branches généalogiques.

### « Fracto-récursif »
Décrit la réinjection admissible de résultats fractionnaires dans des transformations ultérieures avec conservation de continuité.

### « Borné »
Décrit la capacité finie de la représentation/exécution courante et non la valeur mathématique.

### « Miroir C »
Décrit l'objectif d'équivalence sémantique avec le sous-ensemble de référence indépendamment de la représentation mémoire.

Si des tests futurs démontrent que deux de ces termes décrivent toujours exactement la même propriété, la règle anti-pléonasme exigera une révision.

## 87. Forme architecturale candidate R9

La structure candidate devient :

    Spécification TEBDLC
            ↓
        TEBDLC IR
            ↓
    Miroir C poly-fractale
      borné au noyau
       fracto-récursif
            ↓
      états de capacité
            ↓
    promotion / reprise exacte
            ↓
      continuation

En parallèle :

    Python-reference
          ↕ comparaison canonique
    Miroir C

et ultérieurement :

    Rust-reference / autres implémentations indépendantes

## 88. Invariants candidats PFR-1 à PFR-12

Les invariants suivants sont introduits comme candidats à falsifier :

    PFR-1   chaque nœud fractionnaire exact reste reconstructible depuis sa valeur canonique et ses métadonnées requises
    PFR-2   une réinjection récursive ne change pas automatiquement le statut de validation du gain
    PFR-3   une composition récursive admissible ne peut contourner les règles de composabilité
    PFR-4   une branche récursive ne peut fabriquer 0 ou 1 par overflow, arrondi ou troncature silencieuse
    PFR-5   une limite de capacité doit interrompre la représentation bornée avant corruption
    PFR-6   une reprise après promotion doit utiliser des opérandes exacts/reconstructibles
    PFR-7   deux branches numériquement égales restent distinctes si leurs provenances/généalogies diffèrent
    PFR-8   une multiplicité de fractions ne constitue pas automatiquement une structure poly-fractale valide
    PFR-9   la poly-fractalité ne permet aucune fusion sans règle d'association/composition démontrée
    PFR-10  la profondeur récursive finie ne transforme pas une limite vers zéro en zéro atteint
    PFR-11  les transitions de capacité appartiennent à la généalogie de la branche sans devenir automatiquement des gains
    PFR-12  une divergence de représentation Python/C est admissible seulement si la sémantique canonique et les invariants restent équivalents

Aucun invariant PFR n'est déclaré prouvé universellement par sa seule définition.

## 89. Hypothèses R9 — H65 à H76

H65. La notion de poly-fractale permet de distinguer une pluralité structurée de gains fractionnaires d'une simple collection non relationnelle.

H66. La notion de fracto-récursivité décrit une propriété supplémentaire par rapport au caractère fractionnaire seul.

H67. Une profondeur fracto-récursive finie peut être conservée exactement tant que la représentation s'étend sans approximation.

H68. La généalogie d'une branche fracto-récursive peut être reconstruite sans exiger de conserver chaque représentation intermédiaire sous forme active non compressée.

H69. Une représentation multi-précision permettra de continuer certaines branches actuellement interrompues par la borne `uint64_t` sans changer leur valeur sémantique.

H70. Le mot « borné » reste applicable même avec multi-précision lorsque des limites matérielles ou politiques existent.

H71. Deux branches fracto-récursives peuvent converger numériquement sans devenir généalogiquement équivalentes.

H72. Un événement de capacité au sein d'une branche peut être traité comme transformation généalogique sans être assimilé à un gain.

H73. Le corpus exhaustif fini déjà utilisé peut être étendu pour comparer les branches Python/C au-delà d'une seule multiplication.

H74. Des tests de profondeurs récursives variables révéleront des divergences qui ne sont pas visibles dans des compositions binaires isolées.

H75. La combinaison poly-fractale + fracto-récursive peut servir ultérieurement de support aux mécanismes de stagnation/réactivation sans les assimiler prématurément.

H76. La terminologie « miroir C poly-fractale borné au noyau fracto-récursif » ne doit être canonisée définitivement que si les termes restent non pléonastiques et correspondent à des propriétés observables distinctes.

Aucune hypothèse H65–H76 n'est assimilée automatiquement.

## 90. Protocole expérimental R9

Pour éprouver R9, le prochain banc de preuve devra au minimum :

1. générer plusieurs branches fractionnaires indépendantes;
2. conserver une identité généalogique distincte pour chaque branche;
3. exécuter des profondeurs récursives `1, 2, 10, 100, 1000` lorsque la capacité le permet;
4. comparer Python et C à chaque profondeur atteignable;
5. provoquer le seuil de capacité à différentes profondeurs;
6. vérifier que la branche reste reconstructible au seuil;
7. reprendre la branche avec une représentation élargie lorsque celle-ci sera disponible;
8. vérifier que le résultat après reprise correspond exactement au Python-reference;
9. tester deux branches de même valeur mais de provenance distincte;
10. tester des branches incompatibles de domaine/contexte;
11. vérifier qu'aucune fusion automatique ne survient;
12. répéter chaque série au moins trois fois;
13. conserver les temps comme mesures contextuelles et non comme invariants;
14. consigner toute divergence dans le journal avant correction;
15. tenter explicitement de falsifier PFR-1 à PFR-12.

## 91. Critères de refus de la qualification R9

La qualification « poly-fractale borné au noyau fracto-récursif » doit être refusée ou révisée si l'un des points suivants est démontré :

- les branches ne possèdent aucune distinction structurelle au-delà d'une simple liste;
- la réinjection n'est pas réellement supportée ou ne conserve pas la généalogie;
- les termes poly-fractale et fracto-récursif se révèlent pléonastiques dans l'implémentation réelle;
- une branche peut perdre valeur, contexte ou provenance silencieusement;
- une limite de capacité produit une valeur corrompue;
- une reprise modifie la valeur exacte;
- des branches de provenance distincte sont fusionnées par simple égalité numérique;
- la récursion permet de contourner une opération interdite;
- une profondeur accrue est interprétée comme preuve accrue;
- la terminologie empêche plutôt qu'elle n'améliore la falsifiabilité du modèle.

## 92. Ce que R9 ne prétend pas encore démontrer

R9 ne démontre pas encore :

- que « poly-fractale » possède une définition mathématique externe reconnue correspondant exactement à TEBDLC;
- que « fracto-récursif » constitue une nouvelle classe mathématique générale;
- que le miroir C actuel supporte une profondeur récursive arbitraire;
- que la multi-précision et la reprise exacte sont déjà implémentées;
- que toute généalogie peut être compressée sans perte;
- que les mécanismes exo-sapiens de stagnation/réactivation sont déjà intégrés au noyau;
- que PFR-1 à PFR-12 résistent à tous les contre-exemples;
- que H65 à H76 doivent être assimilées.

Les termes R9 sont donc des instruments de précision architecturale et de recherche, pas des labels destinés à masquer les limites actuelles.

## 93. Principe directeur R9

R9 ajoute les distinctions suivantes :

    fractionnaire ≠ poly-fractale
    poly-fractale ≠ simple collection
    récursif ≠ répété
    fracto-récursif ≠ validation récursive
    égalité numérique ≠ identité généalogique
    profondeur ≠ autorité
    petite valeur ≠ petite représentation
    borne de représentation ≠ borne mathématique du gain
    événement de capacité ≠ rupture de branche
    reprise exacte ≠ nouvelle branche sans ascendance

La formulation candidate complète devient :

> **Miroir C poly-fractale borné au noyau fracto-récursif**

c'est-à-dire, dans l'état actuel de recherche :

> une implémentation C expérimentale visant l'équivalence sémantique du sous-ensemble TEBDLC testé, capable de conserver plusieurs branches de gains fractionnaires exacts, d'autoriser la réinjection de résultats selon des règles de composabilité explicites, de préserver leur provenance et leur généalogie, et de reconnaître ses limites de représentation sans transformer ces limites en pertes silencieuses ou en résultats artificiels.

Cette définition reste candidate jusqu'à falsification suffisante et validation expérimentale des propriétés qu'elle prétend distinguer.

---

**Jonathan Therrien, Marieville, Québec.**  
**TEBDLC — Tout est bon dans le cochon. Tous droits réservés sauf autorisation explicite du propriétaire.**