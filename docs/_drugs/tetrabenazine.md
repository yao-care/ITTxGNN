---
layout: default
title: Tetrabenazine
parent: Solo previsione del modello (L5)
nav_order: 431
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Tetrabenazine: nuova indicazione prevista, Malattia policistica renale di tipo 3 con o senza malattia policistic… (livello di evidenza L5). Indicazione originale: Malattia di Huntington (e condizioni…"
---

# Tetrabenazine
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **10** 
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

# Tetrabenazina: dalla malattia di Huntington alla malattia policistica renale di tipo 3

## Riepilogo in breve

La tetrabenazina è un inibitore del trasportatore vescicolare delle monoamine (VMAT), utilizzato principalmente per il trattamento sintomatico dei disturbi ipercinetici, come la corea nella malattia di Huntington. Il modello TxGNN la indica come potenzialmente efficace per la **malattia policistica renale di tipo 3 con o senza malattia policistica epatica**, ma a oggi **non risulta alcuno studio clinico né alcuna pubblicazione** a sostegno di questa ipotesi. La predizione è puramente computazionale e priva di un razionale biologico identificabile.

---

## Quadro d'insieme

| Voce | Contenuto |
|------|------|
| Indicazione originale | Malattia di Huntington (e condizioni correlate: sindromi simil-Huntington, sindrome di McLeod) |
| Nuova indicazione predetta | Malattia policistica renale di tipo 3 con o senza malattia policistica epatica |
| Punteggio di predizione TxGNN | 99,90% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 3 (tutte cancellate) |
| Decisione raccomandata | Hold |

---

## Perché questa predizione potrebbe (o non potrebbe) essere ragionevole?

I dati compilati per questo report non includono una descrizione dettagliata del meccanismo d'azione. Sulla base delle conoscenze farmacologiche note, la tetrabenazina è un inibitore reversibile di VMAT2 (e, secondo i dati di farmacologia disponibili, interagisce anche con VMAT1): riduce le riserve presinaptiche di monoamine (dopamina, serotonina, noradrenalina) nel sistema nervoso centrale. Questo spiega la sua utilità nei disturbi del movimento ipercinetici.

La malattia policistica renale di tipo 3 (legata al gene GANAB) coinvolge invece un difetto nel ripiegamento delle glicoproteine e nella maturazione delle policistine nel reticolo endoplasmatico. **Non si riscontra alcun legame meccanicistico plausibile** tra la deplezione di monoamine e questa via patologica. L'elevato punteggio TxGNN sembra derivare dalla vicinanza topologica nel grafo di conoscenza, non da una via biologica credibile.

Lo stesso vale per le altre predizioni di rango elevato (ad esempio displasia renale-epatica-pancreatica, sindrome di Joubert con difetto renale, nefrite interstiziale cariomegalica, porfiria acuta intermittente): in nessun caso è stato individuato un collegamento meccanicistico o un'evidenza clinica.

---

## Evidenza clinica

Attualmente non risulta alcuno studio clinico registrato correlato.

---

## Evidenza dalla letteratura

Per l'indicazione predetta principale non è disponibile alcuna letteratura correlata.

*Nota:* per la predizione di rango 5 (malformazione toracica) è stato recuperato un solo lavoro, un case report su torcicollo spasmodico ed emangioma vertebrale (PMID [11293103](https://pubmed.ncbi.nlm.nih.gov/11293103/), 2001, Revista de neurologia). Si tratta di un'associazione incidentale, che non dimostra alcuna efficacia della tetrabenazina e non è pertinente all'indicazione principale.

---

## Informazioni sul mercato italiano

Tutte e tre le autorizzazioni risultano cancellate; non vi sono autorizzazioni valide.

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 046035010 | Tetrabenazina 112 cpr 25 mg flacone | Aristo Pharma GmbH | Cancellata |
| 044251027 | Tetrabenazina 112 cpr 25 mg flacone | Sun Pharmaceutical Ind. Europe B.V. | Cancellata |
| 036688012 | Xenazina 112 cpr div 25 mg | Pharmaswiss Ceska Republika s.r.o. | Cancellata |

---

## Considerazioni sulla sicurezza

I dati sul foglio illustrativo AIFA (avvertenze e controindicazioni) non sono disponibili. Di seguito si riportano le informazioni ricavate dal grafo di conoscenza, che **non derivano dal testo dell'etichetta** e vanno quindi verificate.

- **Condizioni associate a controindicazione nel grafo di conoscenza:**
  - Cardiovascolari: sindrome del QT lungo (anche familiare), torsione di punta, ipotensione ortostatica, sindrome da tachicardia posturale ortostatica, disturbi ipotensivi, atrofia multisistemica
  - Neuropsichiatriche: disturbo d'ansia, disturbo nevrotico, disturbo distimico
  - Motorie: discinesia tardiva, discinesia linguo-facciale-buccale, parkinsonismo, malattia di Parkinson, acatisia indotta da farmaci
  - Epatobiliari: malattia epatica, malattia della colecisti
  - Endocrine: iperprolattinemia (anche familiare e acquisita), tumore ipofisario secernente prolattina
- **Interazioni:** sono stati rilevati solo legami farmacologici con i trasportatori vescicolari delle monoamine 1 e 2 (VMAT1/SLC18A1 e VMAT2/SLC18A2); non sono disponibili dati su interazioni con altri farmaci.

Per le informazioni di sicurezza complete si rimanda al foglio illustrativo.

---

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione si basa unicamente sul punteggio del modello (evidenza L5), senza studi clinici, senza letteratura di supporto e senza un legame meccanicistico plausibile. Inoltre, in Italia non esistono autorizzazioni valide e il profilo di sicurezza è gravato da numerose controindicazioni segnalate nel grafo di conoscenza (in particolare QT lungo, depressione/disturbi dell'umore e parkinsonismo).

**Per procedere sarebbe necessario:**
- Acquisire e analizzare il foglio illustrativo AIFA (avvertenze e controindicazioni), lacuna attualmente bloccante per la valutazione di sicurezza
- Ottenere dati dettagliati sul meccanismo d'azione (ad esempio da DrugBank)
- Individuare un'ipotesi biologica plausibile che colleghi l'inibizione di VMAT2 alla fisiopatologia della malattia policistica renale (difetto GANAB), oppure validare la predizione con studi preclinici
- Valutare indicazioni predette alternative con un razionale più solido
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

