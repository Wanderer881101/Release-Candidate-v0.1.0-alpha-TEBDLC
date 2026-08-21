# THÈSE DOCUMENTAIRE R7 — Architecture canonique C, IR TEBDLC et validation inter-langages

**Auteur et propriétaire intellectuel : Jonathan Therrien, Marieville, Québec.**

Date initiale de la lignée : 2026-08-18  
Révision : R7 — extension cumulative de R6  
Horodatage : 2026-08-19 11:45 America/Montreal  
Statut : THÈSE DE TRAVAIL / ARCHITECTURE CANDIDATE À PROUVER  
Projet : TEBDLC — Tout est bon dans le cochon

## 0. Doctrine R7 — aucune perte de gain historique

R7 n'écrase, ne remplace et ne réécrit pas R6. Elle constitue une extension architecturale cumulative de la lignée documentaire.

Ancêtre documentaire immédiat :

    docs/THESE_ARITHMETIQUE_DES_GAINS_R6_2026-08-19.md
    blob R6 observé sur la branche : 2ea69c20d5e4e26dd05ba8abf0a6de7dccd22caa

R7 doit être lue avec R6. Toutes les doctrines, hypothèses, erreurs historiques, invariants, contre-exemples et questions ouvertes de R6 conservent leur statut antérieur. Leur absence de duplication textuelle dans ce fichier ne constitue ni suppression ni invalidation : R6 demeure matériellement présente comme document autonome et ancêtre reconstructible.

    R7 = R6 + delta architectural R7
    extension ≠ remplacement
    héritage ≠ promotion de statut
    portage ≠ preuve
    conformité inter-langages ≠ vérité automatique

La présente révision formalise l'hypothèse selon laquelle TEBDLC peut être défini indépendamment d'un langage de programmation, disposer d'un noyau canonique principal en C et conserver des implémentations indépendantes destinées à tenter de falsifier ce noyau.

## 36. Problème à résoudre

Les premiers essais exécutables R6 sont actuellement exprimés dans l'écosystème Python. Des répétitions sur Python peuvent démontrer de la reproductibilité dans cet environnement, mais plusieurs versions d'un même langage peuvent partager une même erreur de conception, une même interprétation de la spécification ou un même défaut d'implémentation.

Ainsi :

    Python 3.11 = Python 3.12 = Python 3.13

ne suffit pas à démontrer :

    spécification TEBDLC = vérité de l'implémentation

R7 cherche donc une architecture permettant simultanément :

1. une implémentation canonique portable;
2. des interfaces vers les langages contemporains;
3. des implémentations indépendantes de vérification;
4. des vecteurs de test communs;
5. une représentation sémantique qui ne dépende pas du langage hôte;
6. une traçabilité des divergences entre implémentations.

## 37. Principe : la sémantique TEBDLC précède le langage

Le langage C n'est pas déclaré source ultime de vérité. La hiérarchie candidate est :

    Thèse / spécification TEBDLC
        ↓
    TEBDLC IR + invariants
        ↓
    implémentations

Le C reçoit le rôle candidat de **noyau canonique principal**, mais une divergence entre le C et une autre implémentation ne doit jamais être tranchée par la seule autorité du C.

    vérité TEBDLC ≠ comportement du compilateur C
    vérité TEBDLC ≠ comportement Python
    vérité TEBDLC ≠ majorité des implémentations

La spécification, les invariants, les preuves et les résultats reproductibles restent nécessaires pour arbitrer.

## 38. Core C canonique candidat

Architecture candidate :

    Spécification R7
          ↓
      TEBDLC IR
          ↓
      Core C
          ↓
    ABI C stable
      ↙  ↓  ↘
 Python Rust Go ...

Le Core C devrait porter uniquement les éléments dont la sémantique est suffisamment définie et testable. Au stade actuel, les candidats naturels sont :

- représentation rationnelle exacte;
- multiplication fractionnaire admissible;
- refus des opérations de gain interdites;
- règles de composabilité;
- domaine, dimension, unité, référence et contexte;
- provenance et généalogie;
- état d'intégrabilité;
- enveloppe du gain impotent;
- sérialisation canonique;
- erreurs typées et explicites.

La stagnation, la compression/décompression, la réactivation, la revalidation et l'assimilation comportementale ne doivent entrer dans le Core C qu'après formalisation et essais suffisants. R7 ne les promeut pas par anticipation.

## 39. Pourquoi C

Le C est retenu comme candidat pour plusieurs propriétés architecturales :

- ABI largement interopérable;
- capacité d'être appelé depuis Rust, Go, Python, C++, Java/.NET par couches appropriées et de nombreux autres environnements;
- contrôle explicite de la mémoire et des représentations;
- portabilité historique importante;
- faible dépendance à un runtime unique;
- aptitude à servir de frontière commune entre langages.

Ces avantages ne constituent pas une preuve que C est intrinsèquement plus sûr ou plus exact.

Le C introduit aussi des risques propres :

- débordements numériques;
- erreurs de mémoire;
- comportements indéfinis;
- conversions implicites;
- différences d'ABI et de plateforme;
- dépendance possible au compilateur et aux options de compilation.

R7 exige donc que le choix du C soit lui-même soumis à preuve et à contre-tests.

## 40. Fractions exactes et interdiction de perte numérique

Les invariants fractionnaires R6 exigent une représentation exacte. Une représentation bornée naïve telle que :

    uint64_t numerator;
    uint64_t denominator;

ne suffit pas pour des chaînes profondes comme :

    (3/10)^1000 = 3^1000 / 10^1000

Le Core C doit donc utiliser soit une représentation multi-précision vérifiée, soit une bibliothèque d'entiers arbitraires explicitement qualifiée et testée.

Invariant candidat R7 :

    overflow silencieux ⇒ violation TEBDLC

Le comportement admissible en présence d'une capacité numérique insuffisante est une erreur explicite et traçable, jamais une valeur tronquée présentée comme exacte.

    overflow ⇒ ERROR typée
    overflow ⇏ valeur approximée silencieuse
    approximation ⇏ intégrité unitaire

Le choix concret de la bibliothèque ou de la représentation multi-précision reste ouvert et doit faire l'objet de benchmarks, tests différentiels, audits de dépendance et essais multi-plateformes.

## 41. TEBDLC IR — représentation intermédiaire indépendante du langage

R7 introduit **TEBDLC IR (Intermediate Representation)** comme candidat architectural.

Objectif : représenter la sémantique TEBDLC sous une forme canonique indépendante de Python, C, Rust ou Go.

Exemple conceptuel non définitif :

    GAIN {
        value: 300/361
        domain: integrity
        dimension: coverage
        unit: ratio
        reference: R
        context: C17
        provenance: [...]
        genealogy: [...]
        integrability: ...
    }

L'IR ne doit pas devenir un simple format de transport. Il doit préserver les distinctions doctrinales pertinentes :

    Gain ≠ Relation ≠ Résultat ≠ Preuve
    représentation rationnelle ≠ division de gains
    masse ≠ intégrabilité
    valeur ≠ provenance
    contexte d'origine ≠ contexte d'appel

Une future spécification de l'IR devra définir :

- types;
- cardinalités;
- ordre canonique;
- normalisation des rationnels;
- représentation des erreurs;
- provenance;
- généalogie;
- versionnage;
- compatibilité ascendante/descendante;
- règles de sérialisation;
- empreinte canonique;
- comportement devant les champs inconnus;
- politique de non-perte lors d'une migration de version.

## 42. Bindings ≠ implémentations indépendantes

Une distinction essentielle est introduite.

### 42.1 Bindings

Si Python, Rust et Go appellent tous le même Core C :

    Python(C) = PASS
    Rust(C) = PASS
    Go(C) = PASS

cela démontre principalement que plusieurs interfaces peuvent utiliser le même noyau et obtenir les mêmes sorties.

Cela ne constitue pas trois preuves indépendantes de la logique interne du Core C. Une erreur du Core C peut être reproduite identiquement par tous ses bindings.

### 42.2 Implémentations indépendantes

La voie de preuve doit donc conserver au moins une implémentation indépendante du Core C :

    Spécification / IR
       ↙     ↓      ↘
    Core C  Python  Rust

avec, lorsque les domaines sont équivalents :

    Output_C(X) ?= Output_Python(X) ?= Output_Rust(X)

Une divergence devient un objet d'investigation; elle n'établit pas automatiquement quel participant est correct.

## 43. Double voie : production et preuve

R7 propose deux voies qui ne doivent pas être confondues.

### Voie de production

    TEBDLC IR → Core C → ABI C → bindings

Objectif : portabilité, stabilité, performance, intégration.

### Voie de preuve

    TEBDLC IR → implémentations indépendantes → confrontation des sorties

Objectif : falsification, détection de divergences, vérification de la spécification.

Le même langage peut participer aux deux voies, mais une couche qui appelle directement le Core C ne doit pas être comptée comme implémentation indépendante de ce Core.

## 44. Le Python existant n'est pas perdu

Le travail Python construit jusqu'à R6 ne doit pas être jeté ni rétrogradé arbitrairement.

Il peut se transformer en plusieurs rôles :

- modèle de référence expérimental;
- oracle candidat, tant que son autorité reste testée;
- générateur de vecteurs;
- moteur de property-based testing;
- laboratoire d'hypothèses;
- implémentation indépendante de vérification lorsque son code ne délègue pas au Core C;
- binding de production distinct lorsqu'il délègue au Core C.

Il faut distinguer explicitement ces deux derniers rôles afin d'éviter une fausse indépendance.

    Python-reference ≠ Python-binding-C

Le premier peut contester le Core C. Le second vérifie surtout son intégration.

## 45. Corpus canonique inter-langages

Les implémentations doivent pouvoir consommer les mêmes vecteurs sémantiques.

Exemple conceptuel :

    INPUT
      operation = multiply
      left = 3/10
      right = 3/10

    EXPECTED
      numerator = 9
      denominator = 100
      unitary = false

Autre cas :

    INPUT
      acquired_integer = 45
      candidate_integer = 46
      impotent = [300/361, 300/361]

    EXPECTED
      mass = 600/361
      unitary_attained = false

Le format concret du corpus reste à définir. JSON peut servir au prototypage, mais R7 ne le canonise pas encore. Une sérialisation canonique devra éviter les ambiguïtés de nombres flottants, d'ordre de champs et de normalisation.

Les résultats comparés doivent être sémantiques et canoniques, pas dépendre de l'adresse mémoire, de la disposition interne d'un objet ou d'une représentation propre au langage.

## 46. Test différentiel inter-langages

Pour une entrée canonique X :

    R_C = CoreC(X)
    R_P = ReferencePython(X)
    R_R = ReferenceRust(X)

La condition de conformité candidate est :

    Canon(R_C) = Canon(R_P) = Canon(R_R)

Si :

    Canon(R_A) ≠ Canon(R_B)

alors :

    Δ(A,B,X)

est enregistré comme divergence reproductible à investiguer.

Une majorité 2 contre 1 n'est pas automatiquement une preuve. La résolution doit revenir aux invariants, à la spécification, aux preuves mathématiques disponibles et à la reconstruction de l'exécution.

## 47. Génération croisée et falsification

R7 autorise une étape plus exigeante que la consommation d'un corpus statique : plusieurs implémentations peuvent générer indépendamment des cas de test.

Exemple :

    Generator_Python → cas Xp
    Generator_Rust   → cas Xr
    Generator_C      → cas Xc

puis chaque moteur tente de résoudre les cas produits par les autres.

Cette méthode vise à réduire le risque qu'un corpus généré par une seule implémentation encode silencieusement les mêmes hypothèses ou erreurs que cette implémentation.

Le générateur n'est jamais assimilé à un oracle du seul fait qu'il a produit l'entrée.

## 48. Matrice de validation candidate

La future validation R7 devrait distinguer au minimum :

1. **multi-version** : Python 3.11 / 3.12 / 3.13;
2. **multi-langage** : C / Python / Rust / Go selon disponibilité;
3. **multi-compilateur C** : au minimum plusieurs compilateurs lorsque l'environnement le permet;
4. **multi-architecture** : tailles de mots, endianness et architectures disponibles;
5. **multi-optimisation** : builds debug/release et niveaux d'optimisation pertinents;
6. **sanitizers et analyse statique** pour le C;
7. **property-based testing**;
8. **fuzzing** des parseurs, sérialisations et frontières ABI;
9. **vecteurs canoniques reproductibles**;
10. **contre-exemples minimisés et conservés**.

Un résultat ne doit jamais être présenté comme universel lorsque son domaine expérimental est fini ou dépend d'un environnement particulier.

## 49. Compatibilité avec la non-perte de gain

Le passage à C ne signifie pas :

    Python → suppression

mais :

    Python_existant → référence / test / génération / binding selon rôle

De même :

    R6 → R7

ne signifie pas :

    R6 → 0

La transformation architecturale doit conserver :

- les vecteurs déjà testés;
- les résultats historiques;
- les divergences;
- les hypothèses non prouvées;
- les erreurs découvertes;
- les environnements d'essai;
- les raisons d'une décision;
- les anciennes représentations nécessaires à la reconstruction.

## 50. Risque de traducteur infidèle

Si TEBDLC IR sert à produire du C, Rust, Go ou Python, le traducteur lui-même devient un composant à tester.

Il ne suffit pas que :

    IR → C compile

Il faut vérifier :

    Sem(IR) ≡ Sem(C_généré)

et de même pour chaque cible.

Une traduction syntaxiquement valide mais sémantiquement infidèle constitue une perte ou une transformation non autorisée.

Le traducteur doit donc posséder :

- tests de round-trip lorsque possible;
- vecteurs de conformité;
- provenance de génération;
- version du générateur;
- version de l'IR;
- empreinte des entrées/sorties;
- diagnostics explicites des constructions non représentables.

Une construction IR non représentable dans une cible ne doit jamais être approximée silencieusement.

## 51. Versionnage et rétrocompatibilité

L'IR et l'ABI devront être versionnés indépendamment du numéro de révision documentaire.

    R7_document ≠ IR_v1 ≠ ABI_v1

Une future R8 pourrait conserver IR_v1 ou introduire IR_v2. Le numéro de thèse décrit la généalogie conceptuelle; il ne doit pas être confondu avec une version de protocole ou de bibliothèque.

Une migration :

    IR_v1 → IR_v2

doit être considérée comme transformation TEBDLC et soumise aux principes de provenance, reconstruction et non-perte.

## 52. Hypothèses R7 — H41 à H52

H41. La sémantique TEBDLC peut être spécifiée indépendamment du langage qui l'implémente.

H42. Un Core C peut servir de noyau canonique principal sans devenir l'autorité sémantique ultime.

H43. Une ABI C stable peut fournir une frontière d'interopérabilité utile vers plusieurs langages sans exiger une réécriture complète du noyau.

H44. Des bindings vers un même Core C ne constituent pas des implémentations indépendantes de preuve du Core.

H45. Au moins une implémentation indépendante du Core C améliore la capacité de détecter des erreurs communes à une seule implémentation.

H46. TEBDLC IR peut préserver la sémantique nécessaire à la traduction et à la confrontation inter-langages sans dépendre de la représentation interne d'un langage.

H47. Le Python existant peut être transformé en modèle de référence, générateur et/ou oracle candidat sans perte de ses gains historiques.

H48. Un overflow silencieux dans une primitive exacte constitue une violation de la sémantique TEBDLC.

H49. Une divergence inter-langages doit être conservée comme objet d'investigation plutôt que résolue automatiquement par vote majoritaire.

H50. La génération croisée de cas de test peut révéler des hypothèses communes qu'un corpus provenant d'un seul générateur ne révèle pas.

H51. Un traducteur IR→langage doit démontrer sa fidélité sémantique et ne peut être considéré correct du seul fait que le code produit compile.

H52. Le versionnage documentaire, le versionnage IR et le versionnage ABI doivent rester distincts afin de préserver la généalogie et d'éviter les équivalences artificielles.

Aucune hypothèse H41–H52 n'est promue à vérité canonique par sa seule inscription en R7.

## 53. Protocole expérimental R7 à construire

Avant de déclarer le Core C conforme, il faudra au minimum :

1. figer un sous-ensemble explicitement testable de la spécification;
2. définir une représentation canonique des entrées/sorties;
3. porter le corpus R6 sans changer ses attentes;
4. exécuter le corpus sur le modèle Python indépendant;
5. exécuter le même corpus sur le Core C;
6. comparer bit-à-bit les sérialisations canoniques lorsque cette comparaison est pertinente;
7. comparer sémantiquement les champs lorsque la représentation binaire n'est pas censée être identique;
8. répéter les essais;
9. conserver chaque divergence et sa réduction minimale;
10. introduire ensuite Rust/Go comme bindings et/ou implémentations indépendantes en indiquant clairement leur rôle;
11. tester plusieurs compilateurs/architectures lorsque disponibles;
12. documenter le pourquoi, le comment, les résultats, l'interprétation et les limites de chaque essai dans le registre expérimental.

## 54. Critères de refus

Le Core C ou un traducteur doit être refusé comme conforme au sous-ensemble testé si l'un des événements suivants est observé sans explication conforme à la spécification :

- fraction positive transformée en zéro par overflow ou sous-flux;
- fraction non unitaire transformée en unité par approximation;
- perte de provenance;
- perte de contexte nécessaire;
- fusion de domaines incompatibles;
- réintroduction silencieuse de division de gains;
- exposant zéro utilisé comme promotion d'un gain fractionnaire;
- sérialisation ambiguë produisant deux sens pour une même forme;
- traduction qui omet un champ sémantiquement requis;
- divergence non enregistrée;
- erreur convertie silencieusement en résultat valide.

## 55. Ce que R7 ne prétend pas encore démontrer

R7 ne démontre pas encore :

- que C est définitivement le meilleur langage pour TEBDLC;
- qu'un Core C complet existe;
- que l'IR proposée est complète;
- que Rust ou Go reproduiront exactement le comportement attendu;
- que les bindings seront sûrs;
- que l'ABI sera stable sur toutes les plateformes;
- que les bibliothèques multi-précision candidates satisfont les exigences;
- que le traducteur peut être généralisé à toutes les constructions futures;
- que les hypothèses exo-sapiennes non encore exécutables sont résolues par cette architecture.

Ces points restent des objets de recherche et de preuve.

## 56. Principe directeur R7

R7 retient provisoirement la structure suivante :

    THÈSE / SPÉCIFICATION
            ↓
        TEBDLC IR
       ↙    ↓     ↘
    Core C  Python-ref  Rust-ref ...
       ↓
     ABI C
    ↙  ↓  ↘
 Python Rust Go ...
 bindings de production

avec :

    spécification ≠ implémentation
    Core C ≠ vérité automatique
    binding ≠ implémentation indépendante
    compilation ≠ conformité
    répétabilité ≠ universalité
    majorité ≠ preuve
    traduction ≠ fidélité démontrée
    portabilité ≠ sécurité démontrée
    optimisation ≠ permission de perte

La finalité est de rendre TEBDLC **portable sans rendre sa sémantique dépendante d'un langage**, et **testable par plusieurs implémentations sans confondre accord des implémentations et preuve absolue**.

## 57. Continuité documentaire

R7 conserve explicitement la R6 comme ancêtre autonome. Les futurs tests R7 doivent être ajoutés au registre expérimental avec leur environnement, protocole, résultats bruts, répétitions, interprétation, limites et contre-exemples.

Toute future R8 devra pouvoir expliquer :

- ce qu'elle hérite de R7;
- ce qu'elle transforme;
- ce qu'elle réfute;
- ce qu'elle ajoute;
- pourquoi;
- avec quelles preuves;
- et comment reconstruire les états précédents.

---

**Jonathan Therrien, Marieville, Québec.**  
**TEBDLC — Tout est bon dans le cochon. Tous droits réservés sauf autorisation explicite du propriétaire.**