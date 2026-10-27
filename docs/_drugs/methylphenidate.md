---
layout: default
title: Methylphenidate
parent: Solo previsione del modello (L5)
nav_order: 292
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Methylphenidate: nuova indicazione prevista, Sindrome faciodigitogenitale (livello di evidenza L5). Indicazione originale: ADHD…"
monitor_inn: "methylphenidate"
predicted_indications: ["faciodigitogenital syndrome", "chondromyxoid fibroma", "specific developmental disorder", "dysthymic disorder"]
---

# Methylphenidate
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **4** 
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

## Metilfenidato: dal disturbo da deficit di attenzione e iperattività al disturbo specifico dello sviluppo
{: .text-alpha }

## Sintesi in una frase

Il metilfenidato è uno stimolante del sistema nervoso centrale, utilizzato originariamente per il disturbo da deficit di attenzione e iperattività (ADHD) e per la narcolessia.
Il modello TxGNN prevede che possa essere efficace per il **disturbo specifico dello sviluppo** (la predizione con il punteggio più alto, la faciodigitogenital syndrome, non è supportata da alcuna evidenza), ma al momento sono disponibili **0 studi clinici** e **18 pubblicazioni**, per lo più indirette e riferite all'ADHD.

Nota metodologica: il rapporto è costruito sulla prima predizione in ordine di rank (sindrome faciodigitogenitale, nota anche come sindrome di Aarskog-Scott), priva di qualsiasi evidenza. Per completezza, la sezione sulle evidenze considera anche le predizioni successive, che dispongono di letteratura (disturbo specifico dello sviluppo e disturbo distimico).

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | ADHD, narcolessia (le autorizzazioni AIFA non riportano il testo dell'indicazione; le indicazioni derivano dal grafo di conoscenza TxGNN) |
| Nuova indicazione prevista (rank 1) | Sindrome faciodigitogenitale |
| Punteggio di predizione TxGNN | 99,998% |
| Livello di evidenza | L5 (solo predizione del modello) |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 9 (tutte cancellate) |
| Decisione raccomandata | Hold (sospendere) |

Altre predizioni esaminate:

| Rank | Indicazione prevista | Punteggio TxGNN | Livello di evidenza | Raccomandazione |
|------|------|------|------|------|
| 2 | Fibroma condromixoide | 99,991% | L5 | Hold |
| 3 | Disturbo specifico dello sviluppo | 99,988% | L4 | Domanda di ricerca |
| 4 | Disturbo distimico | 99,109% | L4 | Domanda di ricerca |

---

## Perché questa predizione è plausibile?

I dati compilati per questo report non contengono una descrizione dettagliata del meccanismo d'azione. In base alle informazioni note, il metilfenidato inibisce i trasportatori della dopamina (DAT) e della noradrenalina (NET), e la sua efficacia nell'ADHD è consolidata. Uno studio PET del 2026 (PMID 41128391) ha caratterizzato gli effetti del metilfenidato a rilascio prolungato su DAT e NET negli adulti con ADHD.

**Sindrome faciodigitogenitale (rank 1).** È una malattia dello sviluppo legata al cromosoma X, causata da varianti di FGD1. Alcuni pazienti presentano tratti comportamentali simili all'ADHD, e questo potrebbe collegarsi all'azione dopaminergica e noradrenergica del metilfenidato. Tuttavia, non sono stati forniti studi o pubblicazioni a supporto: il punteggio molto alto è una predizione del modello, senza un legame meccanicistico dimostrato.

**Disturbo specifico dello sviluppo (rank 3).** Si sovrappone ampiamente all'ADHD, quindi la predizione appare soprattutto come un'estensione dell'indicazione esistente più che come una vera nuova opportunità di riposizionamento. Uno studio clinico del 2022 sulla sindrome da delezione 22q11.2 (PMID 34453525) riporta effetti selettivi su attenzione e inibizione, suggerendo un possibile beneficio in popolazioni neuroevolutive geneticamente definite.

**Disturbo distimico (rank 4).** La disfunzione dopaminergica e noradrenergica è coinvolta nei sintomi depressivi, quindi l'uso di uno psicostimolante come terapia aggiuntiva è plausibile. La letteratura, però, riguarda solo contesti di comorbidità con l'ADHD.

**Fibroma condromixoide (rank 2).** Non è stato identificato alcun legame meccanicistico plausibile: si tratta di un tumore osseo benigno raro e il punteggio elevato è probabilmente un artefatto del grafo di conoscenza.

---

## Evidenze da studi clinici

Al momento non risultano studi clinici registrati correlati.

---

## Evidenze dalla letteratura

Le pubblicazioni sotto elencate riguardano la predizione del rank 3 (disturbo specifico dello sviluppo) e del rank 4 (disturbo distimico). Per il rank 1 non è disponibile alcuna letteratura. Sono riportate le più rilevanti, con priorità a RCT e studi di coorte.

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [34453525](https://pubmed.ncbi.nlm.nih.gov/34453525/) | 2022 | RCT | Int J Neuropsychopharmacol | Effetti selettivi del metilfenidato su attenzione e inibizione nella sindrome da delezione 22q11.2 |
| [40527386](https://pubmed.ncbi.nlm.nih.gov/40527386/) | 2025 | Coorte | Prog Neuropsychopharmacol Biol Psychiatry | Effetti dell'esposizione cumulativa al metilfenidato su struttura cerebrale e sintomi in giovani con ADHD (studio MRI longitudinale) |
| [41128391](https://pubmed.ncbi.nlm.nih.gov/41128391/) | 2026 | Coorte | Psychiatry Clin Neurosci | Effetti del metilfenidato a rilascio prolungato su DAT e NET in adulti con ADHD (PET con doppio tracciante) |
| [41655471](https://pubmed.ncbi.nlm.nih.gov/41655471/) | 2026 | Coorte | Psychiatry Res | Predizione poligenica della risposta al trattamento nell'ADHD |
| [24045603](https://pubmed.ncbi.nlm.nih.gov/24045603/) | 2013 | Coorte | Clin Neuropharmacol | Impatto del metilfenidato sull'umore in giovani con ADHD e depressione subsindromica |
| [14609500](https://pubmed.ncbi.nlm.nih.gov/14609500/) | 2003 | Coorte | Curr Psychiatry Rep | Effetti di antidepressivi e psicostimolanti sulla percezione interpersonale in depressione e disforia |
| [19627998](https://pubmed.ncbi.nlm.nih.gov/19627998/) | 2009 | Revisione | Neuropharmacology | Neurobiologia dell'ADHD |
| [22923783](https://pubmed.ncbi.nlm.nih.gov/22923783/) | 2015 | Revisione | J Atten Disord | Efficacia, sicurezza e meccanismi del metilfenidato nel cervello adulto e giovanile |
| [1351794](https://pubmed.ncbi.nlm.nih.gov/1351794/) | 1992 | Revisione | Clin Ther | ADHD negli adulti |
| [11563573](https://pubmed.ncbi.nlm.nih.gov/11563573/) | 2001 | Revisione | Am Fam Physician | Valutazione e trattamento dell'ADHD |

---

## Informazioni sul mercato italiano

Tutte le 9 autorizzazioni risultano cancellate. Il testo dell'indicazione approvata e la forma farmaceutica non sono riportati nei dati. Sono elencate le prime 5.

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 041438045 | MEDIKINET 30 cps 10 mg rilascio modificato | Medice Arzneimittel Pütter GmbH | Cancellata |
| 041889041 | EQUASYM 30 cps 10 mg rilascio modificato | Takeda Pharmaceuticals International AG Ireland Branch | Cancellata |
| 041438108 | MEDIKINET 30 cps 40 mg rilascio modificato | Medice Arzneimittel Pütter GmbH | Cancellata |
| 041438060 | MEDIKINET 30 cps 20 mg rilascio modificato | Medice Arzneimittel Pütter GmbH | Cancellata |
| 035040017 | RITALIN 30 cpr 10 mg | Infectopharm Arzneimittel und Consilium GmbH | Cancellata |

---

## Considerazioni sulla sicurezza

Il testo del foglio illustrativo AIFA non è disponibile; di seguito si riportano le informazioni ricavate dal grafo di conoscenza e dalle banche dati di interazioni.

- **Controindicazioni nel grafo di conoscenza (non dal foglio illustrativo)**: ipertensione, epilessia, disturbo bipolare e disturbi affettivi maggiori, disturbi psicotici (inclusi schizoaffettivo e schizofreniforme), abuso/dipendenza da sostanze, malattia coronarica, ictus e malattie cerebrovascolari, infarto miocardico, arresto cardiaco improvviso, malattie della conduzione cardiaca, trombocitopenia, leucopenia, anemie ed emoglobinopatie, anoressia nervosa, glaucoma, ipertiroidismo (malattia di Graves, tireotossicosi).
- **Interazioni farmacologiche**: sono state identificate 137 interazioni. Tra quelle di livello **maggiore** figura il **bupropione**. Interazioni di livello **moderato** sono riportate con isometeptene, efedrina, adrenalina, polietilenglicole con elettroliti, acido picosolfurico e sodio solfato. Molte altre sono di livello non classificato (ad esempio metformina, omeprazolo, pantoprazolo, morfina, simvastatina, prednisone).

Per avvertenze e controindicazioni ufficiali si rimanda al foglio illustrativo.

---

## Conclusioni e prossimi passi

**Decisione: Hold (sospendere)**

**Motivazione:**
- La predizione principale (sindrome faciodigitogenitale) si basa solo sul modello (L5), senza studi clinici né letteratura. Inoltre, tutte le autorizzazioni italiane sono cancellate, quindi non vi è un prodotto attualmente commercializzato.
- Le predizioni con letteratura (disturbo specifico dello sviluppo e disturbo distimico, livello L4) sono più adatte come domande di ricerca: le prove sono indirette e riguardano soprattutto l'ADHD e le sue comorbidità.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione dettagliato (MOA).
- Il testo del foglio illustrativo AIFA con avvertenze e controindicazioni, necessario per lo screening di sicurezza.
- Una revisione sistematica mirata della letteratura sulla sindrome faciodigitogenitale (sintomi di tipo ADHD) e sul disturbo distimico.
- Se ritenuto opportuno, un piccolo studio esplorativo in popolazioni neuroevolutive geneticamente definite, con attenzione al profilo cardiovascolare e di abuso degli stimolanti.
- Chiarimento sullo stato regolatorio (autorizzazioni cancellate) e sulle formulazioni disponibili.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

