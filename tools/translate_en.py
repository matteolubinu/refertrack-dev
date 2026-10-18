#!/usr/bin/env python3
"""Genera en/index.html da index.html (italiano) con le traduzioni qui sotto.
Uso: python3 tools/translate_en.py   (dalla cartella del sito). Se cambi un testo italiano, aggiorna la riga qui
e rilancia: lo script si ferma se un testo italiano non è più presente, così le due lingue non si disallineano."""
import re, json, html, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
src = (ROOT / 'index.html').read_text()
# via dall'italiano i pezzi che riguardano il cambio lingua: nell'inglese si rifanno al contrario
src = re.sub(r'<link rel="alternate" hreflang[^>]*/>\n', '', src)
src = re.sub(r'<a class="lang-switch"[^>]*>.*?</a>\n\s*', '', src)
src = re.sub(r'<!-- lang-footer -->.*?<!-- /lang-footer -->', '', src, flags=re.S)

T = [
("Vai ai contenuti", "Skip to content"),
("Come funziona", "How it works"),
("Funzioni", "Features"),
("Prezzi", "Pricing"),
("Disponibile su App Store", "Available on the App Store"),
("I tuoi referti e i vaccini, finalmente", "Your lab results and vaccines, finally"),
("sotto controllo.", "under control."),
("Refertrack legge da solo i valori dai tuoi referti (foto o PDF) e ti mostra l'andamento di ogni parametro nel tempo. E tiene il conto dei vaccini, con le scadenze dei richiami — niente più fogli sparsi o Excel improvvisati.",
 "Refertrack reads the values from your lab reports (photo or PDF) by itself and shows how each one changes over time. It also keeps track of your vaccines and when boosters are due, so there are no more loose papers or makeshift spreadsheets."),
("Lettura dei referti gratis, per sempre · tutto resta sul tuo iPhone", "Reading your reports is free, forever · everything stays on your iPhone"),
("Tutto resta sul telefono", "Everything stays on your phone"),
("Nessun tracciamento", "No tracking"),
("Lettura referti gratis per sempre", "Free report reading, forever"),
("Pensata in Italia", "Designed in Italy"),
("In tre passaggi", "In three steps"),
("Dal foglio del laboratorio al grafico, in un minuto", "From the lab sheet to a chart, in a minute"),
("Non devi ricopiare niente a mano: tu fotografi, l'app legge, e da lì in poi ogni controllo si aggiunge da solo alla storia dei tuoi valori.",
 "You never retype anything: you take a photo, the app reads it, and from then on every check-up is added to the history of your values."),
("Fotografa o importa", "Photograph or import"),
("Scatta una foto del referto, importa il PDF del laboratorio o scegli un'immagine che hai già nella galleria.",
 "Take a photo of the report, import the lab's PDF, or pick an image you already have in your photo library."),
("Conferma i valori", "Confirm the values"),
("L'OCR sul dispositivo legge ogni valore e te lo mostra accanto al pezzo di referto da cui l'ha preso: confermi tu, prima che venga salvato.",
 "On-device OCR reads each value and shows it next to the part of the report it came from. You confirm it before it is saved."),
("Guarda l'andamento", "Watch the trend"),
("Ogni parametro entra nel suo grafico e si unisce ai controlli precedenti, con la zona di riferimento sempre in vista.",
 "Each parameter goes into its own chart and joins your earlier check-ups, with the reference range always in view."),
("Gratis su App Store · richiede iPhone con iOS 26 o successivo.", "Free on the App Store · requires an iPhone with iOS 26 or later. The app speaks Italian, English, French, German and Spanish; the screenshots on this page show the Italian version."),
("Zero digitazione", "Zero typing"),
("Fotografa il referto, i valori arrivano da soli", "Photograph the report, the values arrive on their own"),
("Fotocamera, un PDF del laboratorio o una foto già nella galleria: l'OCR sul dispositivo legge ogni valore e te lo mostra da confermare prima di salvare — mai un dato inventato.",
 "Camera, a lab PDF or a photo already in your library: on-device OCR reads each value and shows it for you to confirm before saving. Never an invented number."),
("Scansione, PDF o foto dalla galleria", "Scan, PDF or photo from your library"),
("Ogni valore da confermare o correggere", "Every value to confirm or correct"),
("Riconoscimento gratuito e senza limiti", "Free, unlimited recognition"),
("Il tempo, non il singolo numero", "Time, not a single number"),
("Ogni valore diventa un andamento", "Every value becomes a trend"),
("Un numero da solo dice poco. Refertrack unisce lo stesso parametro tra un referto e l'altro e ti mostra da dove arriva e dove sta andando, con la zona di riferimento in evidenza.",
 "A single number says little. Refertrack joins the same parameter across reports and shows where it comes from and where it is heading, with the reference range highlighted."),
("Grafico continuo tra tutti i controlli", "One continuous chart across all check-ups"),
("Zona normale sempre visibile", "Normal range always visible"),
("Storico completo, tutti gli anni, anche gratis", "Full history, every year, even on the free plan"),
("Un colpo d'occhio", "At a glance"),
("Un referto intero, riassunto in una riga", "A whole report, summarised in one line"),
("Appena salvato, ogni controllo ti dice quanti valori sono fuori range e cosa è cambiato dalla volta prima, con i parametri già raggruppati per categoria.",
 "As soon as it is saved, each check-up tells you how many values are out of range and what changed since last time, with parameters already grouped by category."),
("Quanti valori sono fuori range", "How many values are out of range"),
("In aumento o in calo rispetto al controllo precedente", "Up or down compared with the previous check-up"),
("Emocromo, lipidi, tiroide e le altre categorie, separate", "Blood count, lipids, thyroid and the other categories, kept apart"),
("Archivio", "Archive"),
("Referti e documenti, in un posto solo", "Reports and documents, in one place"),
("Gli esami con i valori da una parte, i documenti dall'altra: ricette, ecografie, lettere di dimissione. Il file originale resta sempre lì, pronto da riaprire o condividere.",
 "Tests with their values on one side, documents on the other: prescriptions, ultrasounds, discharge letters. The original file is always there, ready to reopen or share."),
("Esami e documenti, separati ma insieme", "Tests and documents, separate but together"),
("Il documento originale sempre condivisibile", "The original document is always shareable"),
("Nessun referto viene mai eliminato dall'app", "The app never deletes a report"),
("Non solo il sangue", "Not just blood tests"),
("Anche i vaccini, e quando rifarli", "Vaccines too, and when to repeat them"),
("Fotografa il certificato vaccinale o inserisci le date a mano: Refertrack riconosce le somministrazioni e calcola quando scade ogni richiamo, sul calendario del tuo Paese. A colpo d'occhio vedi cosa è scaduto, cosa scade presto e cosa è a posto.",
 "Photograph your vaccination certificate or enter the dates by hand: Refertrack recognises the doses and works out when each booster is due, using your country's schedule. At a glance you see what is overdue, what is due soon and what is up to date."),
("Foto del libretto o inserimento manuale", "Photo of the record or manual entry"),
("Scadenze sul calendario di Italia, Germania, Francia e Spagna", "Schedules for Italy, Germany, France and Spain"),
("Un promemoria quando un richiamo si avvicina", "A reminder when a booster is getting close"),
("E quando ti serve qualcosa in più", "And when you need a little more"),
("Le funzioni che entrano in gioco dopo qualche controllo, quando l'archivio inizia a diventare una storia.",
 "The features that matter after a few check-ups, when the archive starts to become a story."),
("Confronto tra due referti", "Compare two reports"),
("Metti a confronto due controlli, parametro per parametro, e vedi subito cosa è cambiato tra l'uno e l'altro.",
 "Compare two check-ups, parameter by parameter, and see right away what changed between them."),
("Un profilo in più", "An extra profile"),
("Tieni anche i referti e i vaccini di un figlio o di un familiare, separati dai tuoi, sullo stesso telefono.",
 "Keep a child's or a relative's reports and vaccines too, separate from yours, on the same phone."),
("Promemoria per i controlli", "Check-up reminders"),
("Ricordati di rifare un esame quando serve. Uno è sempre incluso; con Refertrack+ ne imposti quanti vuoi e ricevi un avviso quando un valore va nella stessa direzione da tre controlli di fila.",
 "Remember to repeat a test when it is due. One is always included; with Refertrack+ you can set as many as you like and get an alert when a value moves in the same direction for three check-ups in a row."),
("Il grafico da mostrare al medico", "The chart to show your doctor"),
("Esporta l'andamento di un parametro come immagine e mandalo al tuo medico, senza fargli sfogliare dieci referti.",
 "Export a parameter's trend as an image and send it to your doctor, without making them leaf through ten reports."),
("Privacy, per davvero", "Privacy, for real"),
("I tuoi dati sanitari non escono dal telefono.", "Your health data never leaves your phone."),
("Refertrack non ha un server. La lettura del referto, i valori e i grafici vivono sul tuo iPhone: non c'è nessun account da creare e nessuno, nemmeno io, può vedere i tuoi esami.",
 "Refertrack has no server. Report reading, values and charts live on your iPhone: there is no account to create and nobody, not even me, can see your tests."),
("Elaborazione sul dispositivo", "Processing on the device"),
("Foto, PDF e riconoscimento dei valori restano dentro l'iPhone: niente viene caricato per essere analizzato altrove.",
 "Photos, PDFs and value recognition stay inside the iPhone: nothing is uploaded to be analysed elsewhere."),
("Nessun account, nessun tracciamento", "No account, no tracking"),
("Non serve registrarsi, non ci sono analytics di terze parti e non c'è pubblicità. Puoi anche proteggere l'app con Face ID.",
 "No sign-up, no third-party analytics and no ads. You can also protect the app with Face ID."),
("Il backup è solo il tuo", "The backup is only yours"),
("Se attivi la sincronizzazione, i dati viaggiano cifrati nel tuo iCloud personale — lo stesso di foto e messaggi, non un cloud di Refertrack.",
 "If you turn on sync, your data travels encrypted to your personal iCloud, the same one as your photos and messages, not a Refertrack cloud."),
("Leggi la Privacy Policy", "Read the Privacy Policy (in Italian)"),
("Prezzi onesti", "Honest pricing"),
("La lettura dei referti è gratis. Per sempre.", "Reading your reports is free. Forever."),
("Nessuna prova a tempo e nessuna carta richiesta per iniziare. Refertrack+ aggiunge le funzioni in più, con un abbonamento annuale oppure un acquisto unico.",
 "No trial clock and no card needed to start. Refertrack+ adds the extra features, as a yearly subscription or a one-time purchase."),
("Gratis", "Free"),
("€0", "€0"),
("/ per sempre", "/ forever"),
("Tutto quello che serve per iniziare a tenere in ordine gli esami.", "Everything you need to start keeping your tests in order."),
("Scansione e riconoscimento illimitati", "Unlimited scanning and recognition"),
("Andamento e storico completo", "Trends and full history"),
("Archivio referti e documenti", "Archive of reports and documents"),
("Vaccini: scaduto, in scadenza o in regola", "Vaccines: overdue, due soon or up to date"),
("Un profilo e un promemoria attivo", "One profile and one active reminder"),
("Scarica gratis", "Download for free"),
("Consigliato", "Recommended"),
("€14,99", "€14.99"),
("/ anno", "/ year"),
("oppure €44,99 una tantum — a vita, nessun rinnovo.", "or €44.99 one time: for life, no renewal."),
("Confronto diretto tra due referti", "Side-by-side comparison of two reports"),
("Un profilo in più per un familiare", "An extra profile for a family member"),
("Avviso sui valori in movimento da 3 controlli", "Alert on values moving for 3 check-ups"),
("Grafico da condividere col medico", "Chart to share with your doctor"),
("Vaccini: date esatte dei richiami e libretto di famiglia", "Vaccines: exact booster dates and a family record"),
("Ricerca nell'archivio e promemoria illimitati", "Archive search and unlimited reminders"),
("Scopri Refertrack+", "Discover Refertrack+"),
("Il riconoscimento dei referti resta gratuito in ogni caso e nessun dato viene mai eliminato: se non rinnovi, l'archivio e i grafici restano tuoi.",
 "Report recognition stays free in any case and no data is ever deleted: if you don't renew, your archive and charts remain yours."),
("Domande frequenti", "Frequently asked questions"),
("Quanto costa?", "How much does it cost?"),
("L'app è gratuita e la lettura dei referti lo resta per sempre, senza limiti di scansioni. Refertrack+ costa €14,99 all'anno oppure €44,99 una tantum (a vita, senza rinnovo) e aggiunge confronto tra referti, un profilo in più, avvisi sui valori in movimento, condivisione del grafico, le date esatte dei richiami dei vaccini col libretto di famiglia e promemoria illimitati.",
 "The app is free and report reading stays free forever, with no scan limits. Refertrack+ costs €14.99 a year or €44.99 one time (for life, no renewal) and adds comparison between reports, an extra profile, alerts on moving values, chart sharing, exact vaccine booster dates with a family record, and unlimited reminders."),
("I miei dati sanitari sono al sicuro?", "Is my health data safe?"),
("Sì: foto e valori vengono elaborati sul tuo iPhone, mai su un server di Refertrack. Non c'è un account da creare, non c'è tracciamento e l'unico backup è quello del tuo iCloud personale, se lo attivi.",
 "Yes: photos and values are processed on your iPhone, never on a Refertrack server. There is no account to create, no tracking, and the only backup is your personal iCloud, if you turn it on."),
("Legge anche i referti in altre lingue?", "Does it read reports in other languages?"),
("Sì. Refertrack parla italiano, inglese, francese, tedesco e spagnolo, e riconosce i nomi dei parametri anche sui referti stranieri in quelle lingue — utile se ti capita di fare esami all'estero.",
 "Yes. Refertrack speaks Italian, English, French, German and Spanish, and recognises parameter names on foreign reports in those languages, which is handy if you have tests done abroad."),
("Tiene anche i vaccini?", "Does it track vaccines too?"),
("Sì. Fotografi il certificato vaccinale o inserisci le date a mano, e Refertrack calcola quando scade ogni richiamo sul calendario del tuo Paese (Italia, Germania, Francia, Spagna) e te lo ricorda. Sapere se un vaccino è scaduto o in regola è gratis; con Refertrack+ vedi le date esatte e gestisci il libretto di tutta la famiglia. Le scadenze sono indicative e non sostituiscono il parere del medico.",
 "Yes. You photograph the vaccination certificate or enter the dates by hand, and Refertrack works out when each booster is due using your country's schedule (Italy, Germany, France, Spain) and reminds you. Knowing whether a vaccine is overdue or up to date is free; with Refertrack+ you see the exact dates and manage the whole family's record. Due dates are indicative and do not replace your doctor's advice."),
("Refertrack mi dice se un valore è preoccupante?", "Does Refertrack tell me if a value is worrying?"),
("No, e non è quello che vuole fare. Refertrack organizza i tuoi valori e ti mostra come si muovono rispetto agli intervalli di riferimento del laboratorio: non fa diagnosi e non sostituisce il parere del tuo medico.",
 "No, and that is not what it sets out to do. Refertrack organises your values and shows how they move against the lab's reference ranges: it does not diagnose and does not replace your doctor's advice."),
("Su quali dispositivi funziona?", "Which devices does it work on?"),
("Su iPhone con iOS 26 o successivo. I dati si sincronizzano tra i tuoi dispositivi tramite il tuo iCloud personale, se attivi la sincronizzazione.",
 "On iPhone with iOS 26 or later. Data syncs between your devices through your personal iCloud, if you turn sync on."),
("I tuoi esami, in ordine da oggi.", "Your tests, in order from today."),
("Scaricala gratis, fotografa il primo referto e guarda cosa succede al prossimo controllo.", "Download it for free, photograph your first report and see what happens at your next check-up."),
("I tuoi referti e i tuoi vaccini, letti dal telefono e tenuti in ordine.", "Your lab reports and vaccines, read by your phone and kept in order."),
("Prodotto", "Product"),
("Scarica", "Download"),
("Supporto", "Support"),
("Legale", "Legal"),
("Privacy Policy", "Privacy Policy (Italian)"),
("Termini di Utilizzo (EULA)", "Terms of Use (EULA, Italian)"),
("Refertrack. Tutti i diritti riservati.", "Refertrack. All rights reserved."),
("Refertrack non è un dispositivo medico e non sostituisce il parere del medico.", "Refertrack is not a medical device and does not replace your doctor's advice."),
]
ATTR = [
("Alterna anteprima chiara/scura", "Switch between light and dark preview"),
("Apri menu", "Open menu"),
("Navigazione principale", "Main navigation"),
("Scaricalo su App Store", "Download on the App Store"),
("La schermata iniziale di Refertrack, con il valore fuori range e gli ultimi referti", "Refertrack's home screen, with the out-of-range value and the latest reports"),
("La revisione di un referto in Refertrack: il valore letto dall'OCR accanto al ritaglio della foto", "Reviewing a report in Refertrack: the value read by OCR next to the crop of the photo"),
("Il dettaglio della Vitamina D in Refertrack, con il grafico dell'andamento e la zona normale", "The Vitamin D detail in Refertrack, with the trend chart and the normal range"),
("Il dettaglio di un check-up in Refertrack, con i valori raggruppati per categoria", "A check-up detail in Refertrack, with values grouped by category"),
("L'elenco dei referti in Refertrack, con lo stato di ogni controllo", "The list of reports in Refertrack, with the status of each check-up"),
("La panoramica dei vaccini in Refertrack: i contatori scaduto, in scadenza e a posto, con la card dell'antitetanica scaduta da 7 anni", "The vaccines overview in Refertrack: overdue, due soon and up-to-date counters, with the tetanus card overdue by 7 years"),
]

TD = dict(T)
AD = dict(ATTR)
used = set()

def node(m):
    raw = m.group(1)
    t = raw.strip()
    if t in TD:
        used.add(t)
        return '>' + raw.replace(t, TD[t]) + '<'
    return m.group(0)

body_start = src.index('<body>')
head, body = src[:body_start], src[body_start:]
# lascia intatti script e svg
parts = re.split(r'(<script.*?</script>|<svg.*?</svg>)', body, flags=re.S)
# il testo attaccato a un <svg> non ha '>' o '<' dal lato dello svg: li aggiungo e li tolgo dopo
parts = [p if p.startswith(('<script', '<svg')) else re.sub(r'>([^<]+)<', node, '>' + p + '<')[1:-1] for p in parts]
body = ''.join(parts)

def attr(m):
    v = html.unescape(m.group(2))
    if v in AD:
        used.add(v)
        return f'{m.group(1)}="{html.escape(AD[v], quote=True).replace("&#x27;", chr(39))}"'
    return m.group(0)
body = re.sub(r'\b(alt|aria-label|title)="([^"]*)"', attr, body)

# percorsi: la pagina sta in en/
def up(m):
    return f'{m.group(1)}="../{m.group(2)}'
body = re.sub(r'\b(href|src)="((?:assets|fonts|styles\.css|script\.js)[^"]*)', up, body)
head = re.sub(r'\b(href|src)="((?:assets|fonts|styles\.css|script\.js)[^"]*)', up, head)
body = body.replace('../assets/appstore-it.svg', '../assets/appstore-en.svg')
body = body.replace('https://apps.apple.com/it/app/refertrack-referti-ed-esami/id6792460771', 'https://apps.apple.com/app/id6792460771')

# testa
head = head.replace('<html lang="it">', '<html lang="en">')
HEAD = {
 '<title>Refertrack — I tuoi referti e i vaccini, sotto controllo</title>': '<title>Refertrack — Your lab results and vaccines, under control</title>',
 re.search(r'<meta name="description" content="[^"]*" />', head).group(0):
   '<meta name="description" content="Refertrack reads your lab reports with on-device OCR and shows how each value changes over time. It also tracks your vaccines and when boosters are due. On the App Store for iPhone: reading reports is free, forever." />',
 'og:title" content="Refertrack — I tuoi referti e i vaccini, sotto controllo"': 'og:title" content="Refertrack — Your lab results and vaccines, under control"',
 re.search(r'<meta property="og:description" content="[^"]*" />', head).group(0):
   '<meta property="og:description" content="Photograph the report: the values arrive on their own and become a trend over time. And your vaccines, with booster due dates. Everything stays on your iPhone. Download it free on the App Store." />',
 'content="https://matteolubinu.github.io/refertrack/" />\n<meta property="og:site_name"': 'content="https://matteolubinu.github.io/refertrack/en/" />\n<meta property="og:site_name"',
 '<link rel="canonical" href="https://matteolubinu.github.io/refertrack/" />': '<link rel="canonical" href="https://matteolubinu.github.io/refertrack/en/" />\n<link rel="alternate" hreflang="it" href="https://matteolubinu.github.io/refertrack/" />\n<link rel="alternate" hreflang="en" href="https://matteolubinu.github.io/refertrack/en/" />\n<link rel="alternate" hreflang="x-default" href="https://matteolubinu.github.io/refertrack/" />',
}
for a, b in HEAD.items():
    assert a in head, a[:70]
    head = head.replace(a, b, 1)
head = head.replace('og:image" content="https://matteolubinu.github.io/refertrack/assets', 'og:image" content="https://matteolubinu.github.io/refertrack/assets')
if 'og:locale' not in head:
    head = head.replace('<meta property="og:site_name"', '<meta property="og:locale" content="en_US" />\n<meta property="og:site_name"', 1)

# JSON-LD in inglese, dalle domande tradotte
faq = []
for m in re.finditer(r'<button class="faq-q"[^>]*>(.*?)<svg.*?</button>\s*<div class="faq-a"><p>(.*?)</p></div>', body, flags=re.S):
    faq.append((html.unescape(re.sub(r'<[^>]+>', '', m.group(1))).strip(), html.unescape(re.sub(r'<[^>]+>', '', m.group(2))).strip()))
ld = {"@context": "https://schema.org", "@graph": [
 {"@type": "SoftwareApplication", "name": "Refertrack", "operatingSystem": "iOS", "applicationCategory": "HealthApplication",
  "url": "https://matteolubinu.github.io/refertrack/en/", "downloadUrl": "https://apps.apple.com/app/id6792460771",
  "inLanguage": ["en", "it", "de", "fr", "es"],
  "description": "Refertrack reads the values of lab reports with on-device OCR and shows how each parameter changes over time. It also tracks vaccines and booster due dates. Your data stays on the iPhone.",
  "screenshot": "https://matteolubinu.github.io/refertrack/assets/screens/01-dashboard.webp",
  "offers": [{"@type": "Offer", "name": "Free", "price": "0", "priceCurrency": "EUR"},
             {"@type": "Offer", "name": "Refertrack+ yearly", "price": "14.99", "priceCurrency": "EUR"},
             {"@type": "Offer", "name": "Refertrack+ lifetime", "price": "44.99", "priceCurrency": "EUR"}]},
 {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]}
head = re.sub(r'<script type="application/ld\+json">.*?</script>\n', '<script type="application/ld+json">\n' + json.dumps(ld, ensure_ascii=False, indent=2) + '\n</script>\n', head, flags=re.S)

# selettore di lingua
sw = '<a class="lang-switch" href="../" hreflang="it" lang="it">Italiano</a>\n      '
body = body.replace('<div class="nav-cta">\n      ', '<div class="nav-cta">\n      ' + sw, 1)
body = body.replace('<h5 class="footer-gap">Download</h5>', '<h5>Language</h5>\n        <ul>\n          <li><a href="../" hreflang="it" lang="it">Italiano</a></li>\n        </ul>\n        <h5 class="footer-gap">Download</h5>', 1)

out = head + body
(ROOT / 'en').mkdir(exist_ok=True)
(ROOT / 'en' / 'index.html').write_text(out)

missing = [k for k in list(TD) + list(AD) if k not in used]
print('traduzioni non usate (testo italiano cambiato?):', missing)
left = sorted({t.strip() for t in re.findall(r'>([^<]+)<', re.sub(r'<script.*?</script>', '', out[out.index('<body>'):], flags=re.S)) if re.search(r"\b(il|la|che|per|di|del|con|non|sono|una|un)\b", t.strip()) })
print('testi ancora in italiano:', left)
