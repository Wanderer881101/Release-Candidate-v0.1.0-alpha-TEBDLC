# RAPPORT LAB — Productivité de réactivation et factorisation sans perte

**Jonathan Therrien, Marieville, Québec.**

## Objet
Éprouver la distinction entre une réactivation qui introduit une information contextuelle nouvelle et une répétition exacte qui ne doit ni être assimilée à un gain, ni être supprimée, ni forcer une boucle active coûteuse.

## Scénario
102 événements sont injectés. Les 100 premiers portent exactement la même signature `C-loop/U2/PROOF_REJECTED`; les événements 101 et 102 portent une seconde signature `C-new/U4/INTEGRABLE`.

Le ledger factorisé conserve une signature une seule fois et garde explicitement chaque numéro de séquence qui l'a produite. Il peut donc reconstruire la signature associée à chacune des 102 occurrences.

## Résultat
`events=102 factors=2 productive=2 repeated_nonproductive=100 reconstructible=1`.

- GCC 3/3 PASS;
- Clang 3/3 PASS;
- oracle Python 3/3 PASS;
- UBSan : aucun diagnostic;
- ASan/leak detection : aucun diagnostic.

## Compréhension
La première occurrence d'une signature est productive relativement à l'état connu; sa répétition exacte est non productive mais demeure une occurrence historique. Une signature différente redevient productive. La factorisation réduit la répétition structurelle sans perdre les occurrences.

Cette définition ne prétend pas mesurer `ΩSt`. Elle fournit seulement un premier mécanisme falsifiable permettant de distinguer répétition exacte et nouveauté structurelle.

## Limites
- capacités fixes : 64 facteurs, 512 occurrences par facteur;
- aucune métrique de coût irréductible n'est encore définie;
- une nouveauté de signature n'est pas automatiquement un gain;
- la factorisation ne décide aucune action et n'infère aucune identité;
- les séquences sont supposées explicitement identifiées.
