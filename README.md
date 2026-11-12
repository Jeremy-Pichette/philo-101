# Philo 101

Mes cours de philosophie (*Philosophie et rationalité*) transformés en outils de révision : transcriptions intégrales, textes étudiés, synthèses, fiches et quiz.

**Site :** https://jeremy-pichette.github.io/philo-101/

Le site est une **PWA** (Progressive Web App) : il s’installe sur l’écran d’accueil et fonctionne **hors ligne**.

- **iPhone / iPad** : ouvrir l’accueil du site dans Safari → Partager ⬆︎ → « Sur l’écran d’accueil ». Une seule app, **Philo 101**, donne accès à tous les modules (bouton « ‹ Philo 101 » pour revenir à l’accueil).
- **Android / ordinateur** : bouton « Installer » (page d’accueil ou Réglages de l’app).
- **Hors ligne** : les pages sont enregistrées automatiquement après la première visite. Pour écouter les cours sans réseau : Réglages → *Audios hors ligne* → Télécharger (31 Mo).

## Modules

| Module | Contenu | Lien |
| --- | --- | --- |
| **Socrate** | 2 séances · *Apologie de Socrate* et *Criton* (Platon) | [`socrate/`](socrate/) |

### Socrate

- **Cours** : transcription intégrale des deux séances, par chapitres, avec recherche
- **Écoute + paroles en direct** : lecteur audio intégré ; la phrase en cours s’illumine et le texte défile avec la voix (touchez une phrase ou un horodatage pour y sauter, vitesse 0,75× à 2×, contrôles sur l’écran verrouillé)
- **Textes** : *Apologie* (§ 1-8) et *Criton* (§ 1-101) + corrigé des deux fiches d’activité
- **L’essentiel** : synthèse en 8 sections et lexique
- **Fiches** : 34 cartes (glisser → je savais / ← à revoir)
- **Quiz** : 20 questions avec explications

## Organisation

```
philo-101/
├── index.html                 # accueil du site (liste des modules)
├── manifest.webmanifest       # manifeste PWA : l’app « Philo 101 »
├── sw.js                      # service worker (cache hors ligne, audios)
├── icons/                     # icônes de l’app Philo 101
├── socrate/
│   ├── index.html             # l’app de révision (fichier unique)
│   ├── icons/                 # icône du module (raccourci)
│   ├── transcription.md       # transcription intégrale en texte
│   ├── audio/                 # enregistrements des 2 séances (volume normalisé, AAC 48 kb/s)
│   └── sources/               # PowerPoint et fiches du cours (PDF)
└── outils/socrate/            # scripts qui ont servi à générer l’app
    ├── transcrire.py          # transcription audio (faster-whisper)
    ├── extraire_textes.py     # extraction des textes depuis les PDF
    ├── fixes.json             # corrections des noms propres mal reconnus
    ├── content.py             # synthèse, corrigés, fiches, quiz
    ├── template.html          # gabarit de l’app
    └── build.py               # assemble le tout dans socrate/index.html
```

## Notes

Après une modification du site, incrémenter `VERSION` dans `sw.js` pour forcer la mise à jour du cache chez les appareils déjà installés.

Les audios ont été normalisés (la voix de la prof était lointaine) et ré-encodés pour la lecture en streaming. Le lecteur ne fonctionne que si l’app est ouverte depuis le site (ou à côté du dossier `audio/`).

La transcription est automatique : les noms propres ont été corrigés, mais certains passages peu audibles (échanges avec la classe) peuvent rester approximatifs. Les textes de Platon sont dans le domaine public (trad. Victor Cousin et Émile Chambry).
