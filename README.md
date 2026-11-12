# Philo 101

Mes cours de philosophie (*Philosophie et rationalité*) transformés en outils de révision : transcriptions intégrales, textes étudiés, synthèses, fiches et quiz.

**Site :** https://jeremy-pichette.github.io/philo-101/

Chaque module est une page HTML autonome : aucun serveur, aucune dépendance, fonctionne hors ligne. Sur iPhone : Safari → Partager → « Sur l’écran d’accueil ».

## Modules

| Module | Contenu | Lien |
| --- | --- | --- |
| **Socrate** | 2 séances · *Apologie de Socrate* et *Criton* (Platon) | [`socrate/`](socrate/) |

### Socrate

- **Cours** : transcription intégrale des deux séances, par chapitres, avec horodatages et recherche
- **Textes** : *Apologie* (§ 1-8) et *Criton* (§ 1-101) + corrigé des deux fiches d’activité
- **L’essentiel** : synthèse en 8 sections et lexique
- **Fiches** : 34 cartes (glisser → je savais / ← à revoir)
- **Quiz** : 20 questions avec explications

## Organisation

```
philo-101/
├── index.html                 # accueil du site (liste des modules)
├── socrate/
│   ├── index.html             # l’app de révision (fichier unique)
│   ├── transcription.md       # transcription intégrale en texte
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

La transcription est automatique : les noms propres ont été corrigés, mais certains passages peu audibles (échanges avec la classe) peuvent rester approximatifs. Les textes de Platon sont dans le domaine public (trad. Victor Cousin et Émile Chambry).
