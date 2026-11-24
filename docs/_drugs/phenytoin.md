---
layout: default
title: Phenytoin
parent: Solo previsione del modello (L5)
nav_order: 348
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
monitor_inn: "Phenytoin"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
description: "Phenytoin: nuova indicazione prevista, Neoplasia del nervo trigemino (trigeminal nerve neoplasm) (livello di evidenza L5). In Italia, confezioni AIFA: 1 (autorizzate: 1)"
---

# Phenytoin
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **3** 
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

## Phenytoin: Neoplasia del nervo trigemino (trigeminal nerve neoplasm)
{: .text-alpha }

## Sintesi

La fenitoina è un antiepilettico utilizzato per il controllo delle crisi tonico-cloniche e delle crisi parziali complesse. Il modello TxGNN la indica come potenzialmente efficace per il **Tumore del nervo trigemino** (punteggio molto alto), ma i dati compilati per questo report non contengono **alcuno studio clinico registrato** e la letteratura recuperata non riguarda affatto tumori del trigemino. Il punteggio proviene dal modello TxGNN (deep learning) e può riflettere somiglianze apprese dal modello tra malattie correlate, come la nevralgia del trigemino, non un reale segnale antitumorale né un'evidenza biologica. Tra le 10 predizioni, la più solida sul piano clinico è la **nevralgia del trigemino** (livello L3).

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione predetta | Neoplasia del nervo trigemino (trigeminal nerve neoplasm) |
| Punteggio di predizione TxGNN | 0.9999 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 1 su 1) |
| Numero di autorizzazioni | 1 (valide: 1) |
| Decisione raccomandata | Hold |

## Perché questa predizione è (poco) ragionevole?

Secondo la sezione «Mechanism of Action» delle informazioni di prescrizione approvate dalla FDA statunitense (Prescribing Information) per Phenytoin (traduzione non ufficiale): «Il meccanismo preciso con cui fenitoina esercita il suo effetto terapeutico non è stato stabilito, ma si ritiene che comporti il blocco voltaggio-dipendente dei canali del sodio di membrana, con conseguente riduzione delle scariche neuronali sostenute ad alta frequenza.» Testo originale in inglese: "The precise mechanism by which phenytoin exerts its therapeutic effect has not been established but is thought to involve the voltage-dependent blockade of membrane sodium channels resulting in a reduction in sustained high-frequency neuronal discharges." ([DailyMed: Extended Phenytoin Sodium (phenytoin sodium) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=363cd347-d25e-42b9-9ce7-30642f3cb353), versione del 2026-06-25; consultato il 2026-11-19). In base alle conoscenze note, la fenitoina blocca i canali del sodio voltaggio-dipendenti (la scheda farmacologica indica come bersaglio Nav1.2, gene SCN2A), il che riduce la propagazione delle crisi e le scariche neuronali ectopiche ad alta frequenza.

Questo meccanismo è pertinente a crisi epilettiche e dolore neuropatico, **non al controllo tumorale**. Non emerge un legame meccanicistico diretto con le neoplasie del nervo trigemino. La letteratura recuperata riguarda la nevralgia del trigemino e la sindrome di Sturge-Weber, non tumori. Il punteggio elevato proviene dal modello TxGNN (deep learning) e può riflettere somiglianze apprese dal modello tra malattie correlate, non evidenze biologiche.

### Altre predizioni esaminate

| Predizione | Punteggio TxGNN | Livello | Valutazione |
|------|------|------|------|
| Nevralgia del trigemino | 0,9997 | L3 | Meccanismo plausibile (stesso della carbamazepina, di prima linea); uso come opzione e.v. per le riacutizzazioni; linee guida EAN 2019 favorevoli a carbamazepina/oxcarbazepina |
| Deficit di beta-chetotiolasi | 0,9995 | L5 | Nessun legame meccanicistico; il punteggio proviene dal modello TxGNN (deep learning) e può riflettere somiglianze apprese tra malattie correlate, non evidenze biologiche |

## Evidenza dagli studi clinici

Attualmente non risultano studi clinici registrati correlati.

## Evidenza dalla letteratura

Per la predizione principale (neoplasia del nervo trigemino) sono state recuperate solo due pubblicazioni, nessuna sui tumori:

<!-- review:begin it-lic-20261106-phenytoin-1 -->

> **Correzione di verifica (2026-11-06)**: Testo originale: «Non risultano autorizzazioni attualmente valide in Italia (0 monocomponente, 0 combinazioni).» Rimosso: l'indicazione di prodotti monocomponente o in associazione non corrispondeva ai dati delle autorizzazioni (AIFA, elenco delle confezioni autorizzate, al 2026-11-06). Fonte: [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv).

<!-- review:end it-lic-20261106-phenytoin-1 -->

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Revisione | Expert Review of Neurotherapeutics | Panoramica dei trattamenti medici e chirurgici della nevralgia del trigemino; non riguarda neoplasie |
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Serie di casi | Anales Españoles de Pediatría | Esperienza su 14 casi di sindrome di Sturge-Weber; non riguarda neoplasie del trigemino |

### Letteratura pertinente per la nevralgia del trigemino (predizione correlata più solida)

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Linea guida | Eur J Neurol | Linee guida EAN: carbamazepina e oxcarbazepina di prima scelta |
| [35469475](https://pubmed.ncbi.nlm.nih.gov/35469475/) | 2022 | Studio clinico retrospettivo (144 casi) | Cephalalgia | Lacosamide e fenitoina e.v. nelle riacutizzazioni acute |
| [32981076](https://pubmed.ncbi.nlm.nih.gov/32981076/) | 2020 | Coorte retrospettiva | Headache | Fenitoina e.v. come trattamento di salvataggio nella crisi |
| [28761370](https://pubmed.ncbi.nlm.nih.gov/28761370/) | 2017 | Revisione | J Pain Res | Fenitoina e carbamazepina: trattamento basato sul marketing o sull'evidenza |
| [22592741](https://pubmed.ncbi.nlm.nih.gov/22592741/) | 2012 | Revisione Cochrane | Cochrane Database Syst Rev | Fenitoina nel dolore neuropatico e nella fibromialgia dell'adulto |
| [11803299](https://pubmed.ncbi.nlm.nih.gov/11803299/) | 2002 | Revisione | Clin J Pain | Farmacoterapia della nevralgia del trigemino; carbamazepina con evidenza controllata |

## Informazioni sul mercato italiano

<!-- licenses:begin -->

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|------|------|------|------|
| 002129017 | DINTOINA\*30 cpr rivestite 100 mg | SIT LABORATORIO FARMAC. Srl | Autorizzata |

Fonte: AIFA, elenco delle confezioni autorizzate (open data), stato amministrativo; confezioni autorizzate per prime.

<!-- licenses:end -->

## Considerazioni sulla sicurezza

I dati compilati non includono avvertenze o controindicazioni tratte dal foglio illustrativo AIFA. Dal grafo di conoscenza (non dal testo dell'etichetta) risultano le seguenti condizioni associate a controindicazione:

- **Cardiovascolari**: sindrome del QT lungo (anche familiare), torsione di punta, ipotensione
- **Epatiche**: insufficienza epatica, malattie epatiche e della colecisti, encefalopatia/coma epatico
- **Renali**: malattia renale
- **Ematologiche**: trombocitopenia, neutropenia, agranulocitosi
- **Metaboliche**: iperglicemia, diabete mellito, chetoacidosi diabetica, porfirie (ereditarie e del metabolismo delle porfirine)
- **Immunologiche**: lupus eritematoso sistemico (anche pediatrico)
- **Psichiatriche/altre**: disturbi d'ansia, disturbo nevrotico, disturbo distimico, abuso/dipendenza da sostanze
- **Respiratorie/sonno**: sindrome delle apnee notturne (anche ostruttiva), sindrome da ipoventilazione centrale congenita, sindrome di Haddad

La letteratura recuperata segnala inoltre casi di trombocitopenia, iperglicemia/chetoacidosi, sindrome EMPACT (eritema multiforme associato a fenitoina e radioterapia cranica), oftalmoplegia e neuropatia periferica indotte da fenitoina.

**Interazioni**: l'unica voce è di tipo farmacologico (non una interazione tra farmaci): bersaglio Nav1.2 (SCN2A), coerente con il meccanismo di blocco dei canali del sodio. Non sono disponibili dati sulle interazioni con altri farmaci.

Per le informazioni complete di sicurezza si rimanda al foglio illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
- Per la neoplasia del nervo trigemino non vi sono studi clinici né letteratura pertinente e non esiste un legame meccanicistico plausibile: il punteggio TxGNN sembra un artefatto di prossimità alla nevralgia del trigemino. Mancano i dati di sicurezza dell'etichetta.

<!-- review:begin it-lic-20261106-phenytoin-2 -->

> **Correzione di verifica (2026-11-24)**: Testo originale: «Anche l'autorizzazione italiana è annullata e mancano i dati di sicurezza dell'etichetta.» Rimosso: l'affermazione che le autorizzazioni fossero revocate, annullate o non valide non corrispondeva ai dati delle autorizzazioni (AIFA, elenco delle confezioni autorizzate, al 2026-11-06). I numeri aggiornati delle autorizzazioni sono nella panoramica rapida e nella tabella delle informazioni sul mercato. Fonte: [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv).

<!-- review:end it-lic-20261106-phenytoin-2 -->

**Per procedere sono necessari:**
- Scaricare e analizzare il foglio illustrativo AIFA (avvertenze e controindicazioni): lacuna bloccante per lo screening di sicurezza.
- Ottenere i dati sul meccanismo d'azione da DrugBank.
- Riorientare la valutazione verso la **nevralgia del trigemino** (L3): una revisione mirata sulla fenitoina e.v. nelle riacutizzazioni acute, con attenzione all'indice terapeutico ristretto e alla tossicità a lungo termine.
- Verificare la disponibilità attuale di formulazioni di fenitoina in Italia.
- Considerare le altre crisi riflesse (L4) solo come ipotesi di ricerca, dato che sono già comprese nell'ambito del trattamento delle crisi epilettiche.

<!-- review:begin it-lic-20261106-phenytoin-3 -->

> **Correzione di verifica (2026-11-24)**: Testo originale: «Verificare la disponibilità attuale di formulazioni di fenitoina in Italia, dato che l'unica autorizzazione è annullata.» Rimosso: l'affermazione che le autorizzazioni fossero revocate, annullate o non valide non corrispondeva ai dati delle autorizzazioni (AIFA, elenco delle confezioni autorizzate, al 2026-11-06). I numeri aggiornati delle autorizzazioni sono nella panoramica rapida e nella tabella delle informazioni sul mercato. Fonte: [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv).

<!-- review:end it-lic-20261106-phenytoin-3 -->

<!-- review:begin log -->

## Registro delle verifiche

Di seguito il registro delle verifiche di questa pagina: affermazioni controllate sui dati ufficiali delle autorizzazioni (AIFA, elenco delle confezioni autorizzate). Le correzioni riguardano solo dati di base; le previsioni del modello, i livelli di evidenza e le conclusioni non sono stati riscritti. La frase secondo cui non erano disponibili dati sul meccanismo d'azione è stata sostituita da un estratto delle informazioni di prescrizione ufficiali citate (con traduzione non ufficiale).

| Data di verifica | Voce | Intervento | Fonte |
|------|------|------|------|
| 2026-11-06 | Rimosso: «Non risultano autorizzazioni attualmente valide in Italia (0 monocomponente, 0 combinazioni)» | Corretto | [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv) |
| 2026-11-24 | Rimosso: «Anche l'autorizzazione italiana è annullata e m» | Corretto (rivisto il 2026-11-24; versione precedente conservata nel registro) | [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv) |
| 2026-11-24 | Rimosso: «dato che l'unica autorizzazione è annullata» | Corretto (rivisto il 2026-11-24; versione precedente conservata nel registro) | [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv) |
| 2026-11-19 | Frase «dati sul meccanismo d'azione non disponibili» sostituita da un estratto del foglietto statunitense | Frase sull'assenza di dati sul meccanismo d'azione sostituita da un estratto con fonte | [DailyMed: Extended Phenytoin Sodium (phenytoin sodium) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=363cd347-d25e-42b9-9ce7-30642f3cb353) |

<!-- review:end log -->

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

