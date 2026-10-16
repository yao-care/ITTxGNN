---
layout: default
title: Elbasvir
parent: Solo previsione del modello (L5)
nav_order: 167
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Elbasvir: nuova indicazione prevista, Infezione da virus dell'epatite B (livello di evidenza L5). Indicazione originale: Infezione cronica da virus dell'epatite C (dalle indicazioni del graf…"
---

# Elbasvir
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

# Elbasvir: Dall'epatite C cronica all'infezione da virus dell'epatite B

## Sintesi in una frase

Elbasvir è un inibitore della proteina virale NS5A, utilizzato in associazione con grazoprevir per il trattamento dell'infezione cronica da virus dell'epatite C (HCV). Il modello TxGNN lo indica come possibile candidato per l'**infezione da virus dell'epatite B**, ma i **2 studi clinici** e le pubblicazioni raccolte riguardano l'HCV e non forniscono prove dirette di attività anti-HBV: il supporto è quindi essenzialmente solo computazionale.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Infezione cronica da virus dell'epatite C (dalle indicazioni del grafo di conoscenza; il testo autorizzativo AIFA non è disponibile) |
| Nuova indicazione prevista | Infezione da virus dell'epatite B |
| Punteggio di predizione TxGNN | 99,71% |
| Livello di evidenza | L5 (predizione del modello, senza studi diretti sull'HBV) |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 1 (cancellata) |
| Decisione raccomandata | Hold |

*Nota: i dati compilati assegnano a questa indicazione il livello L4; qui si applica L5 perché non esiste alcuno studio clinico o preclinico sull'HBV.*

## Perché questa predizione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. Sulla base delle informazioni note, elbasvir è un inibitore di NS5A dell'HCV, la cui efficacia nell'epatite C è documentata, ma il suo uso nell'epatite B non ha una chiara base meccanicistica.

L'HBV non possiede una proteina NS5A, quindi non c'è omologia diretta con il bersaglio di elbasvir. L'elevato punteggio TxGNN riflette probabilmente la vicinanza, nella rete di conoscenza, tra virus epatotropi (HCV e HBV) e non un'attività antivirale dimostrata.

Va inoltre segnalato che tra le altre indicazioni previste l'unica con un segnale biologico reale è l'**epatite E**: uno studio in vitro del 2026 (PMID 42347219) riporta che elbasvir inibisce l'internalizzazione del virus HEV e, in associazione con ribavirina, ne ottiene una soppressione prolungata. Si tratta di evidenza preclinica, quindi non dimostra efficacia nell'uomo, ma è il filone più promettente per ulteriori approfondimenti.

## Evidenze dagli studi clinici

| Numero studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT02940496](https://clinicaltrials.gov/study/NCT02940496) | Fase 2 | Completato | 15 | Pembrolizumab come terapia di seconda linea nel carcinoma epatocellulare, in pazienti HCV positivi e negativi; elbasvir non è l'agente in studio e l'HBV non è il bersaglio |
| [NCT02115321](https://clinicaltrials.gov/study/NCT02115321) | Fase 2/3 | Completato | 40 | Grazoprevir + elbasvir in HCV con cirrosi avanzata (Child-Pugh B); studio sull'HCV, nessun dato sull'HBV |

Entrambi gli studi sono stati valutati come non pertinenti all'HBV.

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [26904396](https://pubmed.ncbi.nlm.nih.gov/26904396/) | 2016 | Revisione | Acta Pharm Sin B | Panoramica degli antivirali ad azione diretta anti-HCV; l'HBV è citato solo per confronto |
| [25529080](https://pubmed.ncbi.nlm.nih.gov/25529080/) | 2015 | Revisione | Liver Int | Verso l'eradicazione dell'HCV e la guarigione dall'HBV; discussione generale sull'epatite virale |
| [34902265](https://pubmed.ncbi.nlm.nih.gov/34902265/) | 2022 | Coorte (fase 4) | Antimicrob Agents Chemother | Grazoprevir/elbasvir in trapiantati di fegato o rene con HCV genotipo 1b |
| [32039536](https://pubmed.ncbi.nlm.nih.gov/32039536/) | 2020 | Real-world | J Viral Hepat | Esperienza a Taiwan con elbasvir/grazoprevir, con focus sugli eventi avversi epatici e renali |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Revisione | Clin Pharmacokinet | Aspetti farmacocinetici e farmacodinamici dei regimi anti-HCV |
| [32306039](https://pubmed.ncbi.nlm.nih.gov/32306039/) | 2020 | Studio clinico | J Antimicrob Chemother | Grazoprevir/elbasvir nell'HCV acuto in MSM |
| [29077864](https://pubmed.ncbi.nlm.nih.gov/29077864/) | 2018 | Studio randomizzato | Clin Infect Dis | Ritrattamento con sofosbuvir + grazoprevir/elbasvir + ribavirina dopo fallimento di DAA (studio ANRS HC34 REVENGE) |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) | 2025 | Retrospettivo | Klin Mikrobiol Infekc Lek | Terapia antivirale dell'epatite virale B e C nei bambini a Ostrava |

Nessuna pubblicazione dimostra attività di elbasvir contro l'HBV.

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 044929014 | ZEPATIER 28 cpr rivestite 50 mg + 100 mg | Compresse rivestite | Autorizzazione cancellata |

## Cytotoxicity

Elbasvir non è un farmaco antineoplastico: sezione omessa.

## Considerazioni sulla sicurezza

**Interazioni farmacologiche** (15 interazioni segnalate; una di livello maggiore, le altre moderate):
- **Maggiore**: ozanimod
- **Moderate**: warfarin, dicumarolo, betrixaban, lusutrombopag, metreleptina, griseofulvina, elagolix, somatrem, somatropina, alpelisib, aminoglutetimide, binimetinib, ivosidenib, talazoparib

Per avvertenze e controindicazioni si rimanda al foglio illustrativo.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
Non esistono studi clinici o preclinici su elbasvir nell'HBV, che non ha un bersaglio NS5A; il punteggio TxGNN elevato non è sufficiente a giustificare uno sviluppo. Inoltre in Italia l'unica autorizzazione risulta cancellata.

**Per procedere sono necessari:**
- Studi in vitro di attività anti-HBV di elbasvir
- Dati sul meccanismo d'azione (non disponibili al momento)
- Avvertenze e controindicazioni dal foglio illustrativo AIFA, indispensabili per la valutazione della sicurezza
- Verifica del testo completo dello studio sull'HEV (PMID 42347219) e valutazione dell'epatite E come indicazione prioritaria alternativa
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

