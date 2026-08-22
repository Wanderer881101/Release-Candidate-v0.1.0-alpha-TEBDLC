# TEBDLC v0.1.0-alpha — Release Candidate public

**Jonathan Therrien, Marieville, Québec.**

TEBDLC (« Tout est bon dans le cochon ») est un projet de R&D consacré à la conservation, la validation, la réconciliation et l’assimilation de gains démontrés.

## Rôle de ce dépôt

Ce dépôt public est la surface officielle de présentation et de vérification du Release Candidate `v0.1.0-alpha`.

Il **ne contient pas le package source TEBDLC complet contrôlé** et n’est pas l’endpoint de distribution du package privé. Il contient les éléments publics nécessaires pour identifier le produit figé, vérifier ses preuves publiables, comprendre les règles applicables et reproduire les validations de la couche de distribution de référence.

La disponibilité publique des métadonnées, politiques, schémas, tests de distribution et preuves non sensibles ne crée aucun droit implicite sur le package source contrôlé.

## Identité canonique du produit figé

- Release : `v0.1.0-alpha`
- Commit source privé canonique : `677a28d87164379cb2a268e55cfc30302ebc44ab`
- Arbre Git source privé : `63658d334ae8c3d280e9ef2c29845fffce2747e6`
- Fichiers suivis dans le package : `139`
- Package SHA-256 : `dd15a49e30a2419d504d315c29aa4f25d6c6590202bedbce8f78dc632f426ba3`
- Manifest SHA-256 : `ee8cff12529b190b7f9fcf7028a61a32af50f68dc3bfa6c39b24411f85521826`
- Licence SHA-256 : `86fddddedbd112c2c8b420d4b31802147a3bce702ff68db3683b816b39e69ac1`
- Politique territoriale SHA-256 : `1e0a639c10ae2d124f4d535536788b19912903f310c9e494d57e6fbcba9b6090`

Le tag privé canonique `v0.1.0-alpha` est vérifié identique au commit source ci-dessus (`ahead=0`, `behind=0`).

## Validation matérielle

Le candidat figé possède les preuves suivantes :

- Python 3.11 : `90/90 PASS`
- Python 3.12 : `90/90 PASS`
- Python 3.13 : `90/90 PASS`
- Concordance inter-runtime : PASS
- SHA-256 normalisé inter-runtime : `4dc648dfe39adfbd35b2d76783e9525ad52b82c9e82a1e0cad2cd1e141e90954`
- Clean-room package/arbre : PASS
- Stockage privé contrôlé et readback : PASS
- Livraison ALLOW avec identité exacte du package : PASS
- Chemins DENY / fail-closed : PASS
- Validation adversariale du package privé : PASS
- Provenance destinataire et cycle de credentials : PASS
- Monitoring et backup/recovery : PASS
- Provenance de falsification et isolation du registre : PASS
- Transport HTTPS / least privilege : PASS
- Final distribution proof : `SEALED_FREEZE_READY`
- Final audit checkpoint : `SEALED`
- Tag freeze : `FROZEN`

Les détails publics sont conservés dans `RELEASE_GATE_v0.1.0-alpha.md`, `validation/`, `distribution/` et les politiques versionnées.

## Distribution contrôlée

Les droits et conditions d’accès au package source contrôlé sont définis par :

- `LICENSE-SOURCE-AVAILABLE-DRAFT.md` — licence projet active v0.1 ;
- `TERRITORIAL_DISTRIBUTION_POLICY.md` — politique territoriale ;
- `FALSIFICATION_POLICY.md` — règles de provenance et de falsification ;
- `RELEASE_GATE_v0.1.0-alpha.md` — état de fermeture du Release.

Les classifications projet sont `PRIVILEGED`, `NEUTRAL` et `RESTRICTED`. Une distribution réelle reste également soumise aux règles impératives applicables au moment de la transaction.

## GitHub Release public

La **fiche GitHub Release publique** de `v0.1.0-alpha` doit être publiée dans **ce dépôt** :

`Wanderer881101/Release-Candidate-v0.1.0-alpha-TEBDLC`

Elle ne doit pas contenir le package source contrôlé en asset public. Elle sert à présenter l’identité figée, les hashes, les résultats de validation, les règles de distribution et la provenance publique.

Le package contrôlé reste lié cryptographiquement à l’identité canonique par les hashes ci-dessus et par les preuves privées scellées.

## Limites

TEBDLC est un produit de R&D. Les résultats publiés établissent les propriétés effectivement testées dans les environnements et domaines documentés ; ils ne constituent ni une preuve universelle, ni une certification gouvernementale, judiciaire ou juridique spécialisée.

Voir `RELEASE_NOTES_v0.1.0-alpha.md` et `PUBLICATION_RECORD_v0.1.0-alpha.md` pour le statut exact de publication.
