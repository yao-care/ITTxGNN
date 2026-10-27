---
layout: default
title: Carteolol
parent: Solo previsione del modello (L5)
nav_order: 90
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Carteolol: nuova indicazione prevista, Glaucoma ereditario primario (livello di evidenza L5). Indicazione originale: Glaucoma ad angolo aperto…"
---

# Carteolol
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **1** 
{: .fs-6 .fw-300 }

---

## Indice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Relazione di valutazione farmaceutica

</div>

## Carteololo: dall'ipertensione e glaucoma ad angolo aperto al glaucoma ereditario primario
{: .text-alpha }

## Sintesi in una frase

Il carteololo è un beta-bloccante non selettivo, utilizzato in origine per il glaucoma ad angolo aperto e l'ipertensione oculare (oltre che per l'ipertensione arteriosa, secondo la base di conoscenza del modello).
Il modello TxGNN prevede che possa essere efficace per il **glaucoma ereditario primario**, ma al momento **non risultano studi clinici né pubblicazioni** a supporto di questa indicazione: la previsione si basa solo sul modello.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Glaucoma ad angolo aperto, ipertensione oculare (e disturbi ipertensivi, secondo la base di conoscenza TxGNN); il testo autorizzativo AIFA non riporta l'indicazione |
| Nuova indicazione prevista | Glaucoma ereditario primario |
| Punteggio di predizione TxGNN | 99,92% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 10 |
| Decisione raccomandata | Hold |

---

## Perché questa predizione è ragionevole?

Il carteololo è un antagonista beta-adrenergico non selettivo con attività simpaticomimetica intrinseca. Riduce la pressione intraoculare (IOP) diminuendo la produzione di umore acqueo nel corpo ciliare, meccanismo alla base dell'uso approvato nel glaucoma ad angolo aperto e nell'ipertensione oculare. I dati compilati per questo report non contengono una descrizione dettagliata del meccanismo d'azione originale; quanto sopra deriva dalle conoscenze farmacologiche generali.

Il glaucoma ereditario primario (ad esempio il glaucoma congenito primario o le forme legate a MYOC e CYP1B1) è anch'esso caratterizzato da pressione intraoculare elevata, per cui un meccanismo ipotensivo oculare è plausibilmente rilevante.

Occorre però cautela. Il punteggio TxGNN molto alto (0,999) riflette con ogni probabilità la vicinanza nella rete di conoscenza alle indicazioni già approvate per il glaucoma, e non un'evidenza indipendente. Le forme ereditarie spesso comportano difetti strutturali delle vie di deflusso (disgenesia del trabecolato) e sono frequentemente trattate in modo chirurgico; i beta-bloccanti topici hanno in genere un ruolo di supporto. Nei pazienti pediatrici l'assorbimento sistemico dei beta-bloccanti pone ulteriori problemi di sicurezza (bradicardia, broncospasmo).

---

## Informazioni sul mercato italiano

Tutte le 10 autorizzazioni risultano cancellate: non vi sono prodotti a base di carteololo attualmente validi in Italia. Il testo dell'indicazione approvata e la forma farmaceutica non sono riportati nei dati. Autorizzazioni principali (collirio):

| N. autorizzazione | Nome prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 026057048 | CARTEOL collirio 30 monodosi 0,3 ml 20 mg/ml | SIFI SpA | Cancellata |
| 038373027 | FORTINOL collirio 3 ml 2% rilascio prolungato | Bausch & Lomb-IOM SpA | Cancellata |
| 038373015 | FORTINOL collirio 3 ml 1% rilascio prolungato | Bausch & Lomb-IOM SpA | Cancellata |
| 026057024 | CARTEOL collirio 5 ml 20 mg/ml | SIFI SpA | Cancellata |
| 039626027 | FORTIDOSE collirio 30 flaconcini 0,2 ml 1% rilascio prolungato | Bausch & Lomb-IOM SpA | Cancellata |

---

## Considerazioni sulla sicurezza

I dati compilati non includono avvertenze e controindicazioni dal foglio illustrativo. Per queste informazioni si rimanda al foglio illustrativo.

- **Condizioni associate a controindicazione (base di conoscenza TxGNN, non testo di etichetta)**: asma (incluse le forme intrinseca e allergica), bronchite, enfisema polmonare, insufficienza cardiaca (inclusa congestizia), blocco atrioventricolare, diabete mellito, chetoacidosi diabetica, miastenia gravis e malattie della giunzione neuromuscolare, anafilassi.
- **Interazioni farmacologiche**: sono state identificate 137 interazioni in totale. Tra quelle di livello **maggiore** figurano **epinefrina** e **dolasetron**. Tra quelle di livello moderato: corticosteroidi (idrocortisone, desametasone, betametasone, triamcinolone, budesonide), anticolinergici (atropina, iosciamina, metscopolamina, diciclomina), bupropione, cimetidina, canagliflozin, dapagliflozin, clorpropamide e sali di calcio. Acido acetilsalicilico e ossido di magnesio hanno interazioni minori.
- **Popolazione pediatrica**: il rischio di assorbimento sistemico (bradicardia, broncospasmo) richiede particolare attenzione, dato che il glaucoma ereditario si manifesta spesso nell'infanzia.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione si fonda esclusivamente sul modello (livello L5), senza studi clinici né letteratura a supporto. Tutte le autorizzazioni italiane sono cancellate e i dati di sicurezza dal foglio illustrativo mancano, il che impedisce di procedere alla valutazione di sicurezza. Inoltre, la gestione del glaucoma ereditario è spesso chirurgica e il profilo di rischio in età pediatrica è critico.

**Per procedere sono necessari:**
- Acquisizione e analisi del foglio illustrativo AIFA (avvertenze e controindicazioni), attualmente un vuoto di dati bloccante
- Dati sul meccanismo d'azione dettagliato (ad esempio da DrugBank)
- Revisione sistematica della letteratura e ricerca di studi clinici sui beta-bloccanti topici nel glaucoma ereditario/congenito
- Valutazione della compatibilità di via di somministrazione e formulazione, e dello stato commerciale (nessuna autorizzazione valida in Italia)
- Piano di monitoraggio della sicurezza per la popolazione pediatrica e per i pazienti con condizioni cardiorespiratorie o metaboliche
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

