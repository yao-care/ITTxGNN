---
layout: default
title: Atenolol
parent: Solo previsione del modello (L5)
nav_order: 55
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Atenolol: nuova indicazione prevista, Infarto miocardico posterolaterale (livello di evidenza L5). Indicazione originale: Ipertensione, infarto miocardico"
monitor_inn: "atenolol"
predicted_indications: ["malignant hypertensive renal disease", "chronic pulmonary heart disease"]
---

# Atenolol
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **9** 
{: .fs-6 .fw-300 }

---

## Indice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Relazione di valutazione farmaceutica

</div>

# Atenololo: dall'ipertensione e dall'infarto miocardico all'infarto miocardico posterolaterale

## Sintesi

L'atenololo è un beta-bloccante cardioselettivo (β1), usato originariamente per ipertensione, infarto miocardico e disturbi correlati. Il modello TxGNN lo indica come potenzialmente efficace per l'**infarto miocardico posterolaterale**, ma si tratta di una sotto-localizzazione di un'indicazione già nota e non di un vero riposizionamento. Per questa predizione sono disponibili **0 studi clinici** e **0 pubblicazioni**.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Ipertensione, infarto miocardico (il testo dell'indicazione autorizzata non è presente nei dati sulle licenze; indicazioni tratte dal grafo di conoscenza) |
| Nuova indicazione predetta | Infarto miocardico posterolaterale |
| Punteggio di predizione TxGNN | 99,87% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 20 (tutte cancellate) |
| Decisione raccomandata | Hold (sospendere) |

## Perché questa predizione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. In base alle conoscenze generali, l'atenololo è un antagonista dei recettori β1-adrenergici: riduce frequenza cardiaca, consumo miocardico di ossigeno e carico ischemico. La sua efficacia nell'infarto miocardico è già riconosciuta.

L'infarto posterolaterale è una variante per sede anatomica dell'infarto miocardico. Il punteggio elevato riflette probabilmente la vicinanza nel grafo al termine generale "infarto miocardico", più che una nuova evidenza specifica. Per questo motivo la predizione non rappresenta un riposizionamento in senso stretto.

Tra le altre predizioni del modello figurano l'infarto posteroinferiore e settale, l'ipertensione renale maligna e renovascolare, l'ipertensione polmonare e il cuore polmonare cronico. Per le forme polmonari le evidenze sono indirette o solo animali, e in parte contrastanti, e i beta-bloccanti richiedono cautela nelle patologie polmonari.

## Evidenze da studi clinici

Attualmente non risultano studi clinici correlati registrati.

## Evidenze dalla letteratura

Attualmente non è disponibile letteratura correlata per l'infarto posterolaterale. Per una sotto-localizzazione vicina (infarto posteroinferiore) esiste un solo lavoro:

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [3901170](https://pubmed.ncbi.nlm.nih.gov/3901170/) | 1985 | RCT (piccolo, cross-over, in cieco singolo) | La Revue de médecine interne | Confronto dell'attività anti-ischemica di atenololo (200 mg) e diltiazem (240 mg) in 23 pazienti a 4 settimane da un infarto posteroinferiore o anteriore; studio piccolo, datato e indiretto |

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate; nessuna è attualmente valida. Il testo dell'indicazione autorizzata non è riportato. Esempi:

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Titolare |
|---------|------|------|-----------|
| 024016038 | TENORMIN 42 cpr 100 mg | Compresse | Atnahs Pharma Netherlands BV |
| 029486014 | Atenololo 50 cpr rivestite 50 mg | Compresse rivestite | Sandoz SpA |
| 033378023 | Atenololo 42 cpr rivestite 100 mg | Compresse rivestite | ABC Farmaceutici SpA |
| 036541011 | TENSIBLOCK 42 cpr 100 mg | Compresse | Jakinmed Srl |
| 024325060 | SELES BETA 50 cpr 100 mg | Compresse | Teofarma Srl |

## Considerazioni sulla sicurezza

- **Controindicazioni (dal grafo di conoscenza, non dal foglietto illustrativo)**: asma (anche intrinseca e allergica), blocco atrioventricolare, malattia di Raynaud, anafilassi, diabete mellito (tipo 1 e 2) e chetoacidosi diabetica, insufficienza epatica, pancreatite, lupus eritematoso sistemico, psoriasi, gotta, anuria, ipercalcemia, nefrocalcinosi, carenza di potassio, disturbi d'ansia e nevrotici.
- **Interazioni farmacologiche**: sono state rilevate 294 interazioni. Tra quelle di livello moderato: epinefrina, idrocortisone, ioscina (iosciamina), bupropione, triamcinolone, morfina, acetoesamide, atropina, betametasone, budesonide e vari sali di calcio. Di livello lieve: acido acetilsalicilico, idrossido di alluminio e attapulgite.
- I beta-bloccanti richiedono cautela in presenza di patologie polmonari (rischio di broncospasmo) e nell'ipertensione polmonare.

Per avvertenze e controindicazioni ufficiali occorre consultare il foglietto illustrativo.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione è una sotto-localizzazione di un'indicazione già consolidata (infarto miocardico), non un vero riposizionamento, e non è supportata da studi o pubblicazioni specifiche (livello L5). Inoltre, tutte le autorizzazioni italiane risultano cancellate, quindi non esiste un prodotto attualmente commercializzato.

**Per procedere è necessario:**
- Acquisire dal sito AIFA il foglietto illustrativo (avvertenze e controindicazioni), attualmente mancante e bloccante per la valutazione di sicurezza
- Reperire i dati sul meccanismo d'azione
- Chiarire la situazione regolatoria in Italia (motivi delle cancellazioni ed eventuale disponibilità di prodotti validi)
- Valutare se l'infarto posterolaterale richieda una valutazione distinta da quella dell'indicazione generale già approvata
- Considerare candidati con maggior potenziale di riposizionamento reale (ad es. ipertensione renovascolare/maligna o cuore polmonare), con attenzione al profilo di sicurezza respiratorio
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

