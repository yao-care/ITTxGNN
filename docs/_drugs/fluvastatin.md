---
layout: default
title: Fluvastatin
parent: Solo previsione del modello (L5)
nav_order: 209
evidence_level: L5
indication_count: 10
---

# Fluvastatin
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

# Fluvastatina: dall'ipercolesterolemia/aterosclerosi all'ipercolesterolemia familiare

## Sintesi in una frase

La fluvastatina è una statina (inibitore dell'HMG-CoA reduttasi) originariamente usata per le dislipidemie e l'aterosclerosi. Il modello TxGNN prevede che possa essere efficace per l'**ipercolesterolemia familiare** (indicazione con il supporto più solido tra quelle previste), con **1 studio clinico di fase 3 completato direttamente sul farmaco** e **oltre 20 pubblicazioni** a sostegno di questa direzione. Si tratta però di un utilizzo molto vicino a quello già noto, più che di un vero riposizionamento.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Aterosclerosi e disturbi arteriosclerotici; iperlipidemia familiare combinata (testo di indicazione AIFA non disponibile) |
| Nuova indicazione prevista | Ipercolesterolemia familiare (tra le 10 previsioni, quella con le evidenze più solide; la prima in graduatoria è l'iperlipoproteinemia) |
| Punteggio di predizione TxGNN | 99,89% (ipercolesterolemia familiare); 99,99% per l'iperlipoproteinemia |
| Livello di evidenza | L1 (nota: lo studio di fase 3 completato è uno solo, quindi il livello è da considerare con cautela) |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 8 (tutte cancellate) |
| Decisione raccomandata | Proceed with Guardrails (procedere con cautele) |

---

## Perché questa previsione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione nei dati compilati per questo report. In base alle informazioni note, la fluvastatina appartiene alla classe delle statine e inibisce l'HMG-CoA reduttasi (target HMGCR), riducendo la sintesi epatica di colesterolo e aumentando l'espressione dei recettori delle LDL.

L'ipercolesterolemia familiare eterozigote conserva recettori LDL funzionanti, quindi l'azione delle statine è meccanicisticamente appropriata. Per questo motivo l'indicazione è molto vicina a quelle originarie (iperlipidemie, aterosclerosi) e non rappresenta un riposizionamento innovativo.

Altre previsioni hanno una base molto più debole: nella forma omozigote la funzione del recettore LDL è scarsa o assente, per cui l'efficacia delle statine è attesa limitata; per il deficit di CETP, i disturbi del neurosviluppo, le infezioni da SIV/FIV e il fibroma prostatico esistono solo previsioni del modello, senza studi né letteratura.

---

## Evidenze da studi clinici

Per l'ipercolesterolemia familiare:

| Numero studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT00171236](https://clinicaltrials.gov/study/NCT00171236) | Fase 3 | Completato | 84 | Sicurezza ed efficacia della fluvastatina in bambini con ipercolesterolemia familiare eterozigote (**studio diretto sul farmaco**) |
| [NCT03510884](https://clinicaltrials.gov/study/NCT03510884) | Fase 3 | Completato | 153 | Alirocumab vs placebo in bambini/adolescenti con FH eterozigote (non riguarda la fluvastatina) |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Fase 3 | Completato | 18 | Alirocumab in bambini/adolescenti con FH omozigote (non riguarda la fluvastatina) |
| [NCT01890967](https://clinicaltrials.gov/study/NCT01890967) | Fase 2 | Completato | 527 | LY3015014 (anticorpo anti-PCSK9) in ipercolesterolemia primaria (non riguarda la fluvastatina) |

Solo NCT00171236 testa direttamente la fluvastatina; gli altri tre sono studi su altri farmaci e forniscono soltanto un contesto indiretto.

---

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [17062478](https://pubmed.ncbi.nlm.nih.gov/17062478/) | 2006 | Studio clinico pediatrico | Acta Paediatr | Efficacia e sicurezza della fluvastatina in bambini e adolescenti con FH eterozigote |
| [8157036](https://pubmed.ncbi.nlm.nih.gov/8157036/) | 1993 | Studio clinico in doppio cieco | Eur J Clin Pharmacol | Fluvastatina ad alte dosi in 52 pazienti con FH |
| [8192170](https://pubmed.ncbi.nlm.nih.gov/8192170/) | 1994 | Studio clinico (combinazione) | Am J Med | Fluvastatina + bezafibrato vs fluvastatina + colestiramina nella FH |
| [7604807](https://pubmed.ncbi.nlm.nih.gov/7604807/) | 1995 | Studio clinico (terapia tripla) | Am J Cardiol | Fluvastatina-bezafibrato-colestiramina nella FH grave (22 pazienti) |
| [7604804](https://pubmed.ncbi.nlm.nih.gov/7604804/) | 1995 | Studio clinico | Am J Cardiol | Fluvastatina ad alte dosi con bezafibrato nella FH eterozigote |
| [8198022](https://pubmed.ncbi.nlm.nih.gov/8198022/) | 1994 | Analisi di coorte | Am J Cardiol | Risposta alla terapia di combinazione con fluvastatina nella FH |
| [7604789](https://pubmed.ncbi.nlm.nih.gov/7604789/) | 1995 | Studio clinico | Am J Cardiol | Effetti sul profilo lipidico in 31 pazienti cinesi ipercolesterolemici |
| [11219479](https://pubmed.ncbi.nlm.nih.gov/11219479/) | 2001 | Studio randomizzato | Clin Ther | Formulazione a rilascio prolungato vs immediato nell'ipercolesterolemia primaria |
| [16002074](https://pubmed.ncbi.nlm.nih.gov/16002074/) | 2006 | Studio genetico | Atherosclerosis | Polimorfismi CETP e MDR1 e risposta lipidica alla fluvastatina nella FH |
| [8462179](https://pubmed.ncbi.nlm.nih.gov/8462179/) | 1993 | Studio genetico | Circulation | Determinanti genetici della risposta alla fluvastatina nella FH eterozigote |

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 029199041 | LIPAXAN 28 cpr 80 mg rilascio prolungato (Ethyx Pharmaceuticals) | Compresse a rilascio prolungato | Non disponibile (cancellata) |
| 038581029 | Fluvastatina 28 cpr 80 mg rilascio prolungato (Teva Italia) | Compresse a rilascio prolungato | Non disponibile (cancellata) |
| 038580027 | Fluvastatina 28 cpr 80 mg rilascio prolungato (DOC Generici) | Compresse a rilascio prolungato | Non disponibile (cancellata) |
| 038602037 | Fluvastatina 28 cpr 80 mg rilascio prolungato (Aurobindo Pharma Italia) | Compresse a rilascio prolungato | Non disponibile (cancellata) |
| 038582021 | Fluvastatina 28 cpr 80 mg rilascio prolungato (EG SpA) | Compresse a rilascio prolungato | Non disponibile (cancellata) |

Tutte le 8 autorizzazioni risultano cancellate; ne sono mostrate 5 su 8 (le altre: Zentiva, Mylan, Lescol di Ethyx).

---

## Considerazioni sulla sicurezza

- **Controindicazioni (da relazioni tra malattie e farmaco nella base di conoscenza, non dal foglio illustrativo)**: malattia epatica, malattia della colecisti, miopatia, malattie muscolari e dello muscolo scheletrico, paralisi periodica familiare, disturbi ipotensivi, abuso/dipendenza da sostanze, rabdomiolisi, fascite nodulare, traumi.
- **Interazioni farmacologiche**: la ricerca è stata completata; l'unica voce rilevata è il target farmacologico (HMG-CoA reduttasi), non un'interazione con altri farmaci. Dalla letteratura si ricorda che la fluvastatina, metabolizzata soprattutto da CYP2C9, ha meno interazioni mediate da CYP3A4 con gli inibitori delle proteasi rispetto ad altre statine.

Per le avvertenze complete si rimanda al foglio illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Proceed with Guardrails**

**Motivazione:**
Esiste uno studio di fase 3 completato con la fluvastatina in bambini con FH eterozigote, oltre a numerosi studi clinici su adulti, e il meccanismo è coerente con le indicazioni originarie. Tuttavia le prove sono datate, spesso su piccoli campioni, e tutte le autorizzazioni italiane sono cancellate; le altre previsioni (FH omozigote, deficit di CYP7A1, CETP, HIV, SIV/FIV, disturbo del neurosviluppo, fibroma prostatico) vanno mantenute in "Hold" o come domande di ricerca.

**Per procedere sono necessari:**
- Verificare la disponibilità effettiva del prodotto in Italia (tutte le autorizzazioni cancellate)
- Acquisire il foglio illustrativo AIFA con avvertenze e controindicazioni (lacuna bloccante per lo screening di sicurezza)
- Dati sul meccanismo d'azione da DrugBank
- Limitare le conclusioni alla forma eterozigote; valutare confronti con le statine più recenti
- Monitoraggio di funzione epatica e di eventuali sintomi muscolari (rischio di miopatia/rabdomiolisi)
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

