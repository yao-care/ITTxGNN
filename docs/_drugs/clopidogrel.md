---
layout: default
title: Clopidogrel
parent: Prove elevate (L1-L2)
nav_order: 121
evidence_level: L2
indication_count: 8
last_modified_at: 2026-10-15
description: "Clopidogrel: nuova indicazione prevista, Disturbo emicranico (migraine disorder) (livello di evidenza L2). Indicazione originale: Sindrome coronarica acuta, embolia intracranica…"
monitor_inn: "CLOPIDOGREL"
predicted_indications: ["migraine with brainstem aura", "migraine disorder", "osteoarthritis", "tendinitis", "myositis fibrosa", "idiopathic granulomatous myositis", "rheumatoid arthritis", "osteoarthritis susceptibility"]
---

# Clopidogrel
{: .fs-9 }

Livello di evidenza: **L2** | Indicazioni previste: **8** 
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

# Clopidogrel: Dall'infarto miocardico e sindrome coronarica acuta all'emicrania

## Sintesi

Clopidogrel è un antiaggregante piastrinico, originariamente impiegato nella sindrome coronarica acuta, nell'embolia intracranica e nell'infarto miocardico con sopraslivellamento del tratto ST. Il modello TxGNN prevede che possa essere efficace per il **disturbo emicranico** (*migraine disorder*), con **6 studi clinici** e **20 pubblicazioni** reperiti. Il segnale più solido riguarda l'emicrania associata a shunt destro-sinistro (ad esempio forame ovale pervio).

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Sindrome coronarica acuta, embolia intracranica, infarto miocardico con sopraslivellamento ST (da grafo di conoscenza; i testi autorizzativi AIFA non riportano l'indicazione) |
| Nuova indicazione prevista | Disturbo emicranico (*migraine disorder*) |
| Punteggio di predizione TxGNN | 99,44% |
| Livello di evidenza | L2 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 20 (tutte cancellate) |
| Decisione raccomandata | Proceed with Guardrails |

**Nota sulla scelta dell'indicazione:** tra le 8 predizioni disponibili è stata selezionata la seconda in classifica (emicrania), perché ha il livello di evidenza più alto (L2). La prima in classifica, l'emicrania con aura del tronco encefalico (punteggio 99,44%, L3), ha evidenza solo indiretta, derivata dall'emicrania con aura in presenza di PFO. Le altre predizioni (osteoartrosi, tendinite, miosite fibrosa, miosite granulomatosa idiopatica, artrite reumatoide, suscettibilità all'osteoartrosi) hanno evidenza L4-L5 e sono in Hold.

## Perché questa predizione è plausibile?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. In base alle informazioni note, clopidogrel inibisce il recettore piastrinico P2Y12 e l'aggregazione piastrinica; la sua efficacia in ambito cardio e cerebrovascolare è consolidata.

Nell'emicrania, in particolare nei pazienti con forame ovale pervio (PFO) o altri shunt destro-sinistro, microemboli paradossi e mediatori vasoattivi di origine piastrinica (come la serotonina) potrebbero innescare la depressione corticale diffusa. Ridurre l'attivazione piastrinica potrebbe quindi diminuire questi fattori scatenanti. Dati preclinici suggeriscono inoltre un ruolo dei recettori P2Y12 in modelli animali di emicrania.

Il legame è però limitato a un sottogruppo (emicrania associata a shunt). Nell'emicrania non selezionata i risultati non sono consolidati.

## Evidenze da studi clinici

| Numero studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT00799045](https://clinicaltrials.gov/study/NCT00799045) | Fase 4 | Completato | 220 | CANOA: clopidogrel in aggiunta ad aspirina per prevenire l'emicrania di nuova insorgenza dopo chiusura transcatetere di difetto interatriale |
| [NCT05546320](https://clinicaltrials.gov/study/NCT05546320) | Fase 2 | Completato | 1000 | COMPETE: anticoagulanti vs antiaggreganti vs terapia specifica per emicrania nei pazienti con PFO |
| [NCT02938182](https://clinicaltrials.gov/study/NCT02938182) | Fase 4 | Sconosciuto | 50 | Efficacia profilattica di clopidogrel nell'emicrania con shunt destro-sinistro; piccolo, stato non verificato |
| [NCT04946734](https://clinicaltrials.gov/study/NCT04946734) | Fase 3 | Attivo, non in arruolamento | 440 | SPRING: chiusura del PFO vs terapia medica; il farmaco è solo comparatore (evidenza indiretta) |
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Fase 3 | Completato | 664 | CLOSE: chiusura del PFO vs anticoagulanti vs antiaggreganti per prevenire la recidiva di ictus; l'emicrania non è l'endpoint primario |
| [NCT04100135](https://clinicaltrials.gov/study/NCT04100135) | N/D | Terminato | 7 | Dispositivo GORE CARDIOFORM per l'emicrania; clopidogrel non è l'intervento |

I due studi più pertinenti (CANOA e COMPETE) non sono studi di fase 3 su clopidogrel nell'emicrania stabilita; gli studi di fase 3 reperiti riguardano la chiusura del PFO.

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [42526943](https://pubmed.ncbi.nlm.nih.gov/42526943/) | 2026 | RCT | BMJ | Studio multicentrico randomizzato, in aperto, con controllo attivo sul trattamento antitrombotico per prevenire l'emicrania nei pazienti con PFO |
| [26551304](https://pubmed.ncbi.nlm.nih.gov/26551304/) | 2015 | RCT | JAMA | CANOA: clopidogrel più aspirina vs sola aspirina contro l'emicrania dopo chiusura di difetto interatriale |
| [32965476](https://pubmed.ncbi.nlm.nih.gov/32965476/) | 2021 | RCT | JAMA Cardiology | Risultati a un anno di CANOA, dopo sospensione di clopidogrel a 3 mesi |
| [24836213](https://pubmed.ncbi.nlm.nih.gov/24836213/) | 2014 | RCT pilota | Cephalalgia | Studio pilota randomizzato su clopidogrel come profilassi dell'emicrania |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Revisione sistematica | Headache | Ruolo dei farmaci antitrombotici nella prevenzione dell'emicrania |
| [40144614](https://pubmed.ncbi.nlm.nih.gov/40144614/) | 2025 | Revisione sistematica | Indian J Thorac Cardiovasc Surg | Cefalea di nuova insorgenza dopo chiusura transcatetere di difetto interatriale |
| [38109984](https://pubmed.ncbi.nlm.nih.gov/38109984/) | 2024 | Protocollo di studio | Am Heart J | Disegno e razionale di COMPETE |
| [32848048](https://pubmed.ncbi.nlm.nih.gov/32848048/) | 2020 | Coorte osservazionale | J Investig Med | Clopidogrel come profilassi complementare nell'emicrania refrattaria con PFO |
| [24770421](https://pubmed.ncbi.nlm.nih.gov/24770421/) | 2014 | Revisione retrospettiva | Cephalalgia | Clopidogrel come terapia primaria in emicranici con shunt destro-sinistro |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Osservazionale | Heart | Clopidogrel riduce l'emicrania con aura dopo chiusura di PFO e difetto interatriale |

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate; non esistono autorizzazioni valide. Il testo dell'indicazione approvata non è disponibile nei dati compilati. Principali autorizzazioni (tutte compresse rivestite da 75 mg, 28 unità):

| Numero autorizzazione | Nome prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 034128013 | PLAVIX (Sanofi Winthrop Industrie) | Compresse rivestite | Non disponibile |
| 039643022 | Clopidogrel (DOC Generici) | Compresse rivestite | Non disponibile |
| 042557114 | Clopidogrel (Aurobindo Pharma Italia) | Compresse rivestite | Non disponibile |
| 039494024 | CLOPINOVO (Errekappa Euroterapici) | Compresse rivestite | Non disponibile |
| 040215016 | NOGREG (S.F. Group) | Compresse rivestite | Non disponibile |

## Considerazioni di sicurezza

- **Controindicazioni (da grafo di conoscenza, non da scheda tecnica):** insufficienza epatica acuta, epatite, disturbi della coagulazione, traumi/lesioni, porpora trombocitopenica, ulcera peptica attiva, emorragia intracranica.
- **Interazioni farmacologiche:** 100 interazioni identificate. Di gravità maggiore: inibitori di pompa protonica (omeprazolo, esomeprazolo, rabeprazolo), pioglitazone, loperamide e repaglinide. Di gravità moderata, tra le altre: acido acetilsalicilico (rilevante per il rischio emorragico), morfina, bupropione, cimetidina, claritromicina, lansoprazolo e pantoprazolo.
- **Rischio emorragico:** per una condizione cronica e non letale come l'emicrania, il rischio di sanguinamento è la principale preoccupazione. La letteratura segnala anche casi di emorragia in associazione con altri farmaci.

Per le avvertenze complete fare riferimento alla scheda tecnica del prodotto.

## Conclusione e prossimi passi

**Decisione: Proceed with Guardrails**

**Motivazione:**
Esistono un RCT pilota, lo studio CANOA (RCT in un contesto di prevenzione post-chiusura) e una recente pubblicazione multicentrica randomizzata (BMJ 2026), che suggeriscono un beneficio nel sottogruppo di emicrania associata a PFO. Mancano però studi di fase 3 su clopidogrel nell'emicrania non selezionata, e il rischio emorragico richiede cautela in una condizione non letale.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione (MOA) e sulla scheda tecnica AIFA (avvertenze e controindicazioni), attualmente mancanti
- Verifica dei risultati completi di COMPETE e della pubblicazione BMJ 2026, e dello stato di NCT02938182
- Definizione della popolazione target (emicrania con PFO/shunt destro-sinistro) e valutazione del rapporto beneficio/rischio emorragico
- Chiarimento della situazione regolatoria: tutte le autorizzazioni italiane risultano cancellate, quindi serve verificare la disponibilità del farmaco sul mercato
- Per l'emicrania con aura del tronco encefalico, evidenza solo indiretta: trattarla come ipotesi di ricerca
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

