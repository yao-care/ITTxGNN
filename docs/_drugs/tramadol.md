---
layout: default
title: Tramadol
parent: Solo previsione del modello (L5)
nav_order: 445
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
monitor_inn: "tramadol"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "juvenile idiopathic arthritis", "juvenile arthritis due to defect in LACC1", "rheumatoid nodulosis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis"]
description: "Tramadol: nuova indicazione prevista, Displasia acromesomelica, tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type) (livello di evidenza L5)."
---

# Tramadol
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **9** 
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

## Tramadol: Displasia acromesomelica, tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type)
{: .text-alpha }

## Sintesi

Il tramadolo è un analgesico oppioide ad azione centrale, originariamente associato a osteoartrosi e artropatie.
Il modello TxGNN prevede una possibile efficacia per la **displasia acromesomelica, tipo Hunter-Thompson**,
ma per questa indicazione **non risultano sperimentazioni cliniche né pubblicazioni** a supporto: la predizione è esclusivamente computazionale.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originaria | Osteoartrosi, artropatie (derivata dal knowledge graph; nessun testo di indicazione approvata disponibile nelle autorizzazioni AIFA) |
| Nuova indicazione prevista | Displasia acromesomelica, tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type) |
| Punteggio di predizione TxGNN | 0.9999 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: almeno 20) |
| Numero di autorizzazioni | 20 (tutte cancellate) |
| Decisione raccomandata | Hold |

## Perché questa predizione potrebbe essere (o non essere) ragionevole?

I dati compilati per questo report non contengono una descrizione dettagliata del meccanismo d'azione. In base alle conoscenze generali, il tramadolo è un agonista dei recettori oppioidi mu con inibizione della ricaptazione di serotonina e noradrenalina, con effetto analgesico.

La displasia acromesomelica di tipo Hunter-Thompson è una displasia scheletrica genetica (difetto di CDMP1/GDF5). Non è stato individuato alcun legame meccanicistico con l'azione del tramadolo. L'elevato punteggio TxGNN sembra riflettere la vicinanza nella rete di conoscenza ai disturbi scheletrici e articolari, più che una motivazione biologica. Al massimo, il tramadolo potrebbe offrire sollievo sintomatico del dolore, che non costituisce una modifica della malattia.

Anche le altre predizioni nella top 10 (brachiolmia, sindrome brachiolmia-amelogenesi imperfetta, miosclerosi, pseudoacondroplasia, spondiloartropatie, artrite idiopatica giovanile e sottotipi, noduolosi reumatoide) mostrano lo stesso quadro: nessun legame meccanicistico diretto, al più un ruolo analgesico sintomatico.

## Evidenze da sperimentazioni cliniche

Attualmente non risultano sperimentazioni cliniche correlate registrate.

## Evidenze dalla letteratura

Per l'indicazione principale attualmente non è disponibile letteratura correlata.

Nota: per un'altra predizione (artrite idiopatica giovanile, rank 7) è presente un solo lavoro (PMID [20799760](https://pubmed.ncbi.nlm.nih.gov/20799760/), 2010, rassegna, *Paediatric Drugs*), che riguarda però il ketoprofene, un FANS, e non il tramadolo: non costituisce evidenza diretta.

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 049093014 | CONTRAMAL 20 cpr 100 mg rilascio prolungato | GMM FARMA Srl | Valida |
| 028878092 | FORTRADOL 20 cpr 100 mg rilascio prolungato | ALFASIGMA SpA | Valida |
| 036672020 | TRAFLASH 20 cpr orodispersibili 50 mg | VIATRIS HEALTHCARE LIMITED | Valida |
| 033998030 | TRAMADOLO 5 fiale 100 mg 2 ml | SANDOZ SpA | Valida |
| 028878155 | FORTRADOL 10 cpr 200 mg rilascio prolungato | ALFASIGMA SpA | Valida |

Sono state registrate in totale 20 autorizzazioni, tutte cancellate; non è disponibile il testo delle indicazioni approvate.

## Considerazioni sulla sicurezza

- **Controindicazioni secondo il knowledge graph** (non derivate dal foglio illustrativo): ipertensione, insufficienza epatica, epilessia, disturbi d'ansia, epatopatie, cirrosi, diabete, chetoacidosi diabetica, abuso/dipendenza da sostanze, insufficienza respiratoria, avvelenamento da paracetamolo, sindrome serotoninergica, ipertensione intracranica, astinenza da alcol, sindrome di Wernicke-Korsakoff, infezioni del sistema nervoso centrale, tra le altre.
- **Interazioni farmacologiche**: sono note 321 interazioni. Tra quelle di livello **maggiore**: alvimopan, bupropione, cisapride, destrofenfluramina, dietilpropione, dolasetron, dronabinolo, efedrina, fenfluramina. Tra quelle di livello **moderato**: atropina, bisacodile, cimetidina, claritromicina, famotidina, eliglustat, eluxadolina, glicerina, e altre.
- Nella popolazione pediatrica (rilevante per l'artrite idiopatica giovanile) l'uso del tramadolo presenta restrizioni regolatorie e rischi, tra cui la depressione respiratoria.

Per avvertenze e controindicazioni ufficiali si rimanda al foglio illustrativo.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione è puramente computazionale (livello L5), senza sperimentazioni né letteratura, senza legame meccanicistico plausibile con una malattia genetica dello scheletro. Inoltre, in Italia tutte le autorizzazioni sono cancellate e il profilo di interazioni è ampio.

**Per procedere sarebbe necessario:**
- Dati sul meccanismo d'azione e un'ipotesi biologica che colleghi il tramadolo alla malattia
- Acquisizione e analisi del foglio illustrativo AIFA (avvertenze e controindicazioni), attualmente mancante e bloccante per la valutazione di sicurezza
- Evidenze precliniche o cliniche specifiche per l'indicazione prevista
- Valutazione della compatibilità di via di somministrazione e della situazione autorizzativa (in commercio, 20 autorizzazioni valide)
- Se l'obiettivo è il controllo sintomatico del dolore, valutare l'indicazione come gestione generale del dolore anziché come riposizionamento
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

