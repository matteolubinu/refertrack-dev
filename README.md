# Refertrack — sito ufficiale

Landing page di [Refertrack](https://apps.apple.com/it/app/refertrack-referti-ed-esami/id6792460771),
app iPhone che legge i referti del sangue con l'OCR sul dispositivo e mostra l'andamento di ogni
valore nel tempo.

Sito statico (HTML/CSS/JS, nessuna dipendenza) pubblicato con GitHub Pages su
<https://matteolubinu.github.io/refertrack/> — è anche il "Sito web dello sviluppatore" indicato
sulla scheda App Store.

## Struttura
- `index.html` — pagina unica
- `styles.css` — design system (token colori/tipografia dell'app)
- `script.js` — tema chiaro/scuro, reveal in scroll, menu mobile, accordion FAQ
- `assets/screens/` — screenshot dell'app in italiano, light mode, 900×1956 (dati demo, nessun dato reale)
- `assets/appstore-it.svg` — badge UFFICIALE Apple localizzato IT (da tools.applemediaservices.com), da non ricostruire a mano

## Se i prezzi cambiano
Le cifre compaiono in tre punti di `index.html`: la sezione `#prezzi`, la prima domanda della FAQ e
il `<meta name="description">`. Vanno tenute allineate a `Products.storekit` dell'app e alla scheda
App Store Connect.

## Sviluppo locale
```bash
python3 -m http.server 8000
# poi apri http://localhost:8000
```

## Pubblicazione
Questo repo (`refertrack-dev`) è la cronologia di sviluppo. Il deploy avviene dal repo
`refertrack` tramite `~/refertrack-public`, sincronizzato con un albero pulito.
