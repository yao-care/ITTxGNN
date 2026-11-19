---
layout: default
title: Informativa sulla privacy
nav_order: 95
permalink: /privacy-policy/
description: "Informativa sulla privacy di ITTxGNN: sito statico senza account né moduli; utilizza i cookie analitici di Google Analytics 4 per le statistiche di utilizzo."
---

# Informativa sulla privacy

<div class="key-takeaway">
Questo è un sito statico — nessuna registrazione, nessun modulo. Utilizza i cookie analitici di Google Analytics 4 per elaborare statistiche di utilizzo.
</div>

---

## Che cosa raccogliamo

<p class="key-answer" data-question="ITTxGNN raccoglie dati personali?">
<strong>Solo statistiche di utilizzo, tramite Google Analytics 4.</strong> Questo sito è ospitato su GitHub Pages come sito
puramente statico. Non esiste alcun sistema di account e non ci sono moduli, e non raccogliamo nomi, indirizzi e-mail né
cartelle cliniche. Il sito utilizza i cookie analitici di Google Analytics 4 per elaborare statistiche di utilizzo (pagine
visualizzate, sito di provenienza, profondità di scorrimento e tempo sulla pagina). I cookie vengono impostati al
caricamento della pagina; termini di ricerca, contenuti dei moduli e parametri di query dell'URL non vengono inviati.
</p>

---

## Servizi di terze parti

Il sito utilizza le seguenti risorse di terze parti, che possono registrare gli accessi secondo le rispettive
politiche:

| Servizio | Finalità | Informativa sulla privacy |
|---------|---------|----------------|
| GitHub Pages | Hosting del sito | [GitHub Privacy Statement](https://docs.github.com/site-policy/privacy-policies/github-privacy-statement) |
| Google Analytics 4 (www.googletagmanager.com, google-analytics.com) | Statistiche di visita (pagine viste, provenienza); usa cookie di analisi. Non vengono inviati termini di ricerca, contenuti dei moduli né parametri dell’URL. | [Norme sulla privacy di Google](https://policies.google.com/privacy) |
| cdn.jsdelivr.net | Librerie di script: grafici d3 in tutte le pagine; Fuse.js per il confronto dei nomi e il client SMART on FHIR nelle pagine SMART | [Informativa sulla privacy di jsDelivr](https://www.jsdelivr.com/terms/privacy-policy-jsdelivr-net) |
| clinicaltrials.gov | Ricerca di sperimentazioni cliniche nelle pagine SMART: solo quando la richiede, i nomi del farmaco e dell’indicazione vengono inviati all’API di ClinicalTrials.gov | [Politiche web della NLM](https://www.nlm.nih.gov/web_policies.html) |
| rxnav.nlm.nih.gov | App SMART: i codici RxNorm dei farmaci letti dalla sua cartella clinica elettronica vengono inviati all’API RxNav della NLM per ricavare il nome del principio attivo (nessun identificativo del paziente) | [Politiche web della NLM](https://www.nlm.nih.gov/web_policies.html) |

Quando avvii attivamente l'app SMART on FHIR, questa richiede i dati sui farmaci al tuo sistema di cartella
clinica elettronica. L'identità del paziente e i dati della cartella clinica <strong>non vengono inviati ai server di questo
sito</strong> (è un sito statico, senza backend) e questo sito non li conserva. Per abbinare i nomi dei farmaci, l'app invia i
loro codici RxNorm al servizio RxNav della National Library of Medicine statunitense; questi codici non contengono dati
identificativi del paziente. Quando richiedi gli studi clinici, il nome del farmaco e l'indicazione vengono inviati a
ClinicalTrials.gov.

---

<!-- privacy-law:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改；法規與連結見 .claude/privacy_text_20261119.py）-->
## Normativa applicabile

Per i visitatori in Italia si applicano il [Regolamento generale sulla protezione dei dati (GDPR)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) e il [Codice in materia di protezione dei dati personali (d.lgs. 196/2003)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2003-06-30;196); i cookie analitici rientrano anche nell'art. 122 del Codice. L'autorità di controllo è il [Garante per la protezione dei dati personali](https://www.garanteprivacy.it/). Il titolare ha sede a Taiwan e non ha stabilimenti nell'UE; il trattamento riguarda i dati di utilizzo raccolti da Google Analytics 4 tramite cookie.

## I vostri diritti e come esercitarli

- Diritto di accesso (art. 15) e di rettifica (art. 16).
- Diritto alla cancellazione (art. 17) e alla limitazione (art. 18).
- Diritto di opposizione (art. 21), anche all'analisi statistica.
- Diritto di proporre reclamo al Garante (art. 77).

Richieste e domande: service@yao.care. Poiché il sito non ha account, possiamo intervenire sui dati di Google Analytics solo se ci fornite dettagli sufficienti (ad esempio data e pagine della visita); potete anche bloccare o cancellare i cookie analitici nel browser.

## Diritto d'autore e fonti dei dati

I testi del sito sono protetti dalla [legge sul diritto d'autore (L. 633/1941)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1941-04-22;633). Il codice del sito è pubblicato con licenza MIT nel [repository GitHub](https://github.com/yao-care/ITTxGNN); i testi dei rapporti sono © 藥提醒科技有限公司 (yao.care).

Fonti dei dati di questo sito e relative condizioni:

- Dati di previsione **TxGNN** (Harvard Dataverse): dedicati al pubblico dominio (CC0 1.0); citare Huang et al., *Nature Medicine* 2024.
- **ClinicalTrials.gov** e **PubMed**: National Library of Medicine degli Stati Uniti; si vedano le [condizioni di ClinicalTrials.gov](https://clinicaltrials.gov/about-site/terms-conditions) e le [politiche NCBI](https://www.ncbi.nlm.nih.gov/home/about/policies/) (alcuni abstract di PubMed restano protetti dal diritto d'autore dell'editore).
- Identificativi e dati **DrugBank**: secondo i termini di licenza di [DrugBank](https://go.drugbank.com/) (uso non commerciale).
- **Set di dati locale**: [AIFA: liste dei farmaci di classe A e H](https://www.aifa.gov.it/en/liste-farmaci-a-h), pubblicato da Agenzia Italiana del Farmaco (AIFA); il riutilizzo è regolato dalle condizioni dell'editore e questo sito non concede ulteriori diritti.

<!-- privacy-law:end -->

---

## Modifiche a questa informativa

Eventuali modifiche saranno pubblicate direttamente in questa pagina.

---

## Informazioni sullo Sviluppatore

Questa piattaforma è sviluppata e gestita da **藥提醒科技有限公司** (yao.care). Le informazioni sull'azienda,
il contesto del modello TxGNN e l'elenco completo dei siti della linea di prodotti si trovano nella pagina
<a href="{{ '/about/' | relative_url }}">Informazioni</a>.

---

<div class="disclaimer">
<strong>Esclusione di responsabilità</strong><br>
Il presente rapporto ha finalità esclusivamente di ricerca accademica e <strong>non costituisce un parere medico</strong>. Seguire sempre le indicazioni del proprio medico; non modificare mai la terapia di propria iniziativa. Qualsiasi decisione di riposizionamento di un farmaco richiede una validazione clinica completa e una revisione regolatoria.
<br><br>
<small>Revisionato da: 藥提醒科技有限公司 (yao.care)</small>
</div>
