---
layout: default
title: Fenofibrate
parent: Solo previsione del modello (L5)
nav_order: 195
evidence_level: L5
indication_count: 1
monitor_inn: "Fenofibrate"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-10-28
description: "Fenofibrate: nuova indicazione prevista, Cholesterol-ester transfer protein deficiency (livello di evidenza L5). Indicazione originale: Non riportata nei dati locali"
---

# Fenofibrate
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

## Fenofibrate: Cholesterol-ester transfer protein deficiency
{: .text-alpha }

## Sintesi in una frase

Il fenofibrato è un agonista di PPARα utilizzato per ridurre i trigliceridi e il colesterolo nelle dislipidemie (relazioni registrate nel grafo di conoscenza: ipertrigliceridemia, iperlipidemia, iperlipidemia familiare). Il modello TxGNN ne prevede una possibile utilità nella **carenza di proteina di trasferimento degli esteri del colesterolo (CETP)**, ma al momento non sono disponibili **studi clinici** e le **3 pubblicazioni** reperite sono solo studi preclinici o meccanicistici, che non studiano direttamente questa malattia.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione prevista | Cholesterol-ester transfer protein deficiency |
| Punteggio di previsione TxGNN | 0.9961 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 12 su 12) |
| Numero di autorizzazioni | 12 (valide: 12) |
| Decisione raccomandata | Hold |

## Perché questa previsione è plausibile?

Non sono disponibili dati dettagliati sul meccanismo d'azione registrati per questo report. In base alle conoscenze note, il fenofibrato è un agonista di PPARα (confermato dai dati farmacologici sul bersaglio PPARA) che aumenta il colesterolo HDL e riduce i trigliceridi, in parte favorendo l'espressione di ApoA-I/ApoA-II e l'attività della lipoproteina lipasi. Nei topi induce inoltre il gene della proteina di trasferimento dei fosfolipidi (PLTP), con aumento delle dimensioni delle HDL (PMID 11342537).

Il legame con la carenza di CETP è biologicamente plausibile ma indiretto: entrambi riguardano il metabolismo delle HDL. Tuttavia, la carenza di CETP si presenta già con livelli di HDL-C molto elevati, per cui un ulteriore aumento delle HDL non offre un beneficio clinico evidente. L'alto punteggio TxGNN (0,9961) riflette la prossimità tra le vie metaboliche (lipidi e HDL), non un reale bisogno terapeutico.

La letteratura riguarda l'associazione tra inibizione di CETP e agonismo PPARα come strategia farmacologica in modelli murini (PMID 20332533), non il trattamento del deficit genetico. Uno studio del 2018 (PMID 30271349) indica inoltre che le HDL plasmatiche correlano poco con l'escrezione fecale di colesterolo e con la capacità di efflusso, indebolendo ulteriormente il razionale per trattare stati di HDL elevate.

## Evidenze dagli studi clinici

Attualmente non risultano studi clinici correlati registrati.

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [20332533](https://pubmed.ncbi.nlm.nih.gov/20332533/) | 2010 | Studio preclinico | J Cardiovasc Pharmacol Ther | In topi transgenici ApoB100/CETP umana, l'inibizione di CETP (torcetrapib) e l'agonismo PPARα (fenofibrato) modificano il profilo lipidico, con aumento di HDL-C e riduzione di LDL-C |
| [11342537](https://pubmed.ncbi.nlm.nih.gov/11342537/) | 2001 | Studio meccanicistico preclinico | J Biol Chem | Il fenofibrato induce il gene PLTP, che spiega l'ingrandimento delle HDL nei topi trattati |
| [30271349](https://pubmed.ncbi.nlm.nih.gov/30271349/) | 2018 | Studio preclinico/meccanicistico | Front Physiol | Le HDL plasmatiche non correlano con l'escrezione fecale di colesterolo né con la capacità di efflusso: conta la funzionalità delle HDL |

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 029257019 | LIPSIN 20 cps 200 mg | – | – |
| 033557036 | FENOFIBRATO 20 cps 200 mg (Zentiva) | – | – |
| 037160049 | LIPERIAL 30 cpr rivestite 145 mg | – | – |
| 048413025 | FENOFIBRATO 30 cpr rivestite 145 mg (Aurobindo) | – | – |
| 041071046 | FENOFIBRATO 30 cpr 145 mg (DOC Generici) | – | – |

Sono presenti 12 autorizzazioni valide, tutte per il principio attivo singolo; qui sono elencate le prime 5. Il testo delle indicazioni approvate non è presente nei dati compilati.

## Considerazioni sulla sicurezza

I dati del grafo di conoscenza (non derivati dal foglio illustrativo) registrano relazioni di controindicazione con: insufficienza epatica e malattie epatiche, pancreatite, malattie della colecisti e colelitiasi, miopatia e rabdomiolisi, trombocitopenia, leucopenia, neutropenia e agranulocitosi, anemia, e compromissione della funzione renale.

**Interazioni:** i dati compilati riportano solo interazioni farmacologiche con bersagli (PPARα e proteina legante gli acidi grassi 1), non interazioni con altri farmaci.

Per le avvertenze e le controindicazioni ufficiali si rimanda al foglio illustrativo.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
- Nessuno studio clinico o pubblicazione studia direttamente la carenza di CETP, quindi il livello di evidenza è L5. Poiché la carenza di CETP cursa già con HDL elevate, non è evidente un beneficio clinico.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione e sulla relazione con la malattia
- Testo del foglio illustrativo AIFA (indicazioni, avvertenze, controindicazioni)
- Dimostrazione di un bisogno clinico e di studi che affrontino direttamente la carenza di CETP
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

