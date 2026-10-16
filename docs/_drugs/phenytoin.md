---
layout: default
title: Phenytoin
parent: Solo previsione del modello (L5)
nav_order: 348
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Phenytoin: nuova indicazione prevista, Neoplasia del nervo trigemino (livello di evidenza L5). Indicazione originale: Epilessia (crisi tonico-cloniche generalizzate, crisi parziali…"
monitor_inn: "Phenytoin"
predicted_indications: ["trigeminal nerve neoplasm", "micturation-induced seizures", "audiogenic seizures", "orgasm-induced seizures", "thinking seizures", "startle epilepsy", "eating seizures", "reading seizures", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
---

# Phenytoin
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

# Fenitoina: Dall'epilessia alla neoplasia del nervo trigemino

## Sintesi

La fenitoina è un antiepilettico utilizzato per il controllo delle crisi tonico-cloniche e delle crisi parziali complesse. Il modello TxGNN la indica come potenzialmente efficace per la **neoplasia del nervo trigemino** (punteggio molto alto), ma i dati compilati per questo report non contengono **alcuno studio clinico registrato** e la letteratura recuperata non riguarda affatto tumori del trigemino. Il punteggio sembra riflettere la vicinanza nel grafo di conoscenza alla nevralgia del trigemino, non un reale segnale antitumorale. Tra le 10 predizioni, la più solida sul piano clinico è la **nevralgia del trigemino** (livello L3).

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Epilessia (crisi tonico-cloniche generalizzate, crisi parziali, stato epilettico, sindrome di Lennox-Gastaut), secondo gli archi di indicazione del grafo di conoscenza; il testo dell'indicazione AIFA non è disponibile |
| Nuova indicazione predetta | Neoplasia del nervo trigemino |
| Punteggio di predizione TxGNN | 99,99% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni annullate |
| Numero di autorizzazioni | 1 (annullata) |
| Decisione raccomandata | Hold |

## Perché questa predizione è (poco) ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione nei dati compilati. In base alle conoscenze note, la fenitoina blocca i canali del sodio voltaggio-dipendenti (la scheda farmacologica indica come bersaglio Nav1.2, gene SCN2A), il che riduce la propagazione delle crisi e le scariche neuronali ectopiche ad alta frequenza.

Questo meccanismo è pertinente a crisi epilettiche e dolore neuropatico, **non al controllo tumorale**. Non emerge un legame meccanicistico diretto con le neoplasie del nervo trigemino. La letteratura recuperata riguarda la nevralgia del trigemino e la sindrome di Sturge-Weber, non tumori. Il punteggio elevato è verosimilmente un artefatto di prossimità nel grafo.

### Altre predizioni esaminate

| Predizione | Punteggio TxGNN | Livello | Valutazione |
|------|------|------|------|
| Nevralgia del trigemino | 99,97% | L3 | Meccanismo plausibile (stesso della carbamazepina, di prima linea); uso come opzione e.v. per le riacutizzazioni; linee guida EAN 2019 favorevoli a carbamazepina/oxcarbazepina |
| Crisi audiogene | 99,98% | L4 | Evidenza quasi solo preclinica (modelli murini/ratto); non è un'indicazione umana consolidata |
| Crisi indotte da minzione | 99,98% | L4 | Meccanismo plausibile; solo un caso clinico indiretto (clobazam + fenitoina); già rientra nell'ambito delle crisi epilettiche |
| Epilessia da sussulto (startle) | 99,98% | L4 | Letteratura a favore della lamotrigina; nessuna evidenza clinica specifica per la fenitoina |
| Crisi indotte dal pensiero, dall'alimentazione, dalla lettura | 99,97–99,98% | L4 | Letteratura largamente non pertinente; evidenza indiretta |
| Crisi indotte dall'orgasmo | 99,98% | L5 | Solo predizione del modello, nessuna letteratura |
| Deficit di beta-chetotiolasi | 99,95% | L5 | Nessun legame meccanicistico; verosimile artefatto del grafo |

## Evidenza dagli studi clinici

Attualmente non risultano studi clinici registrati correlati.

## Evidenza dalla letteratura

Per la predizione principale (neoplasia del nervo trigemino) sono state recuperate solo due pubblicazioni, nessuna sui tumori:

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

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 002129017 | DINTOINA*30 cpr rivestite 100 mg (SIT Laboratorio Farmaceutico) | Compresse rivestite | Non disponibile — autorizzazione annullata |

Non risultano autorizzazioni attualmente valide in Italia (0 monocomponente, 0 combinazioni).

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
- Per la neoplasia del nervo trigemino non vi sono studi clinici né letteratura pertinente e non esiste un legame meccanicistico plausibile: il punteggio TxGNN sembra un artefatto di prossimità alla nevralgia del trigemino. Anche l'autorizzazione italiana è annullata e mancano i dati di sicurezza dell'etichetta.

**Per procedere sono necessari:**
- Scaricare e analizzare il foglio illustrativo AIFA (avvertenze e controindicazioni): lacuna bloccante per lo screening di sicurezza.
- Ottenere i dati sul meccanismo d'azione da DrugBank.
- Riorientare la valutazione verso la **nevralgia del trigemino** (L3): una revisione mirata sulla fenitoina e.v. nelle riacutizzazioni acute, con attenzione all'indice terapeutico ristretto e alla tossicità a lungo termine.
- Verificare la disponibilità attuale di formulazioni di fenitoina in Italia, dato che l'unica autorizzazione è annullata.
- Considerare le altre crisi riflesse (L4) solo come ipotesi di ricerca, dato che sono già comprese nell'ambito del trattamento delle crisi epilettiche.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

