---
layout: default
title: Acitretin
parent: Prove moderate (L3-L4)
nav_order: 21
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-15
description: "Acitretin: nuova indicazione prevista, Acne (livello di evidenza L4). Indicazione originale: Non disponibile (i testi delle indicazioni nelle autorizzazioni AIFA…"
monitor_inn: "acitretin"
predicted_indications: ["acne (disease)", "pediatric systemic lupus erythematosus", "fetal erythroblastosis", "familial cutaneous telangiectasia and oropharyngeal predisposition cancer syndrome"]
---

# Acitretin
{: .fs-9 }

Livello di evidenza: **L4** | Indicazioni previste: **4** 
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

## Acitretina: dall'uso dermatologico sistemico all'acne (indicazione predetta)
{: .text-alpha }

## Sintesi in una frase

L'acitretina è un retinoide sistemico di seconda generazione, noto per l'impiego nelle patologie cutanee ipercheratosiche. Il modello TxGNN prevede una possibile efficacia nell'**acne**, ma l'evidenza a supporto è molto limitata: **1 sola sperimentazione clinica** (solo indirettamente correlata, su un'altra patologia) e **nessuna pubblicazione** nei dati compilati per questo report.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non disponibile (i testi delle indicazioni nelle autorizzazioni AIFA sono vuoti) |
| Nuova indicazione predetta | Acne |
| Punteggio di predizione TxGNN | 0,9994 |
| Livello di evidenza | L4 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 4 su 4) |
| Numero di autorizzazioni | 4 (valide: 4) |
| Decisione raccomandata | Hold |

---

## Perché questa predizione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione registrato per il farmaco. In base alle conoscenze generali, l'acitretina è un retinoide sistemico che modula la differenziazione e la proliferazione dei cheratinociti ed esercita effetti antinfiammatori attraverso la segnalazione dei recettori dell'acido retinoico (RAR) e dei retinoidi X (RXR).

Questi stessi percorsi sono bersaglio di altri retinoidi, come l'isotretinoina, usati nell'acne e nei disturbi da occlusione follicolare. Esiste quindi un legame biologico plausibile a livello di classe, coerente con l'alto punteggio TxGNN. Tuttavia, non è stata reperita alcuna evidenza clinica o bibliografica specifica per l'acne.

Vanno inoltre considerati limiti pratici rilevanti: la teratogenicità, il lungo periodo di washout (nelle donne in età fertile comporta un obbligo di contraccezione protratto per anni) e la disponibilità dell'isotretinoina, che ne limitano il posizionamento.

---

## Evidenza dalle sperimentazioni cliniche

| Numero studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT07708480](https://clinicaltrials.gov/study/NCT07708480) | Fase 4 | Completato | 70 | Studio randomizzato che confronta apremilast (30 mg due volte al giorno) e acitretina (25 mg due volte al giorno) per 12 settimane nell'idrosadenite suppurativa moderata-grave; endpoint primario: punteggio IHS4. Non riguarda l'acne e l'acitretina è usata come comparatore; nessun risultato disponibile |

---

## Evidenza dalla letteratura

Attualmente non sono disponibili pubblicazioni correlate.

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata | Stato |
|---------|------|------|-----------|------|
| 027480019 | NEOTIGASON 30 cps 10 mg | n.d. | n.d. | Valida |
| 027480021 | NEOTIGASON 20 cps 25 mg | n.d. | n.d. | Valida |
| 041619014 | ZORIAS 30 cps 10 mg | n.d. | n.d. | Valida |
| 041619065 | ZORIAS 20 cps 25 mg | n.d. | n.d. | Valida |

Tutte e quattro le autorizzazioni (Aurobindo Pharma Italia e Difa Cooper) risultano cancellate: al momento non vi sono autorizzazioni valide in Italia.

---

## Considerazioni sulla sicurezza

I dati sulla sicurezza tratti dal foglio illustrativo non sono disponibili; si rimanda al foglio illustrativo ufficiale.

- **Possibili controindicazioni (da grafo di conoscenza, non da etichetta)**: insufficienza epatica, danno epatico da farmaci, pancreatite, diabete mellito e chetoacidosi diabetica, ipertrigliceridemia, ipoalfalipoproteinemia, obesità, pseudotumor cerebri, ipertensione intracranica, disturbi della vista (inclusa cecità e cecità notturna), iperostosi, disturbi d'ansia, nevrosi, disturbo distimico e abuso/dipendenza da sostanze.
- **Interazioni farmacologiche**: individuate 113 interazioni. Le principali di livello **maggiore** riguardano **doxiciclina, minociclina, tetraciclina e vitamina A**. Di livello **moderato**: sulfoniluree (acetoesamide, clorpropamide, glimepiride, glipizide, gliburide, tolazamide, tolbutamide) e naltrexone.
- **Teratogenicità**: l'acitretina è un noto potente teratogeno, controindicato in gravidanza, con un lungo periodo di washout.

---

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
Il legame meccanicistico con l'acne è plausibile a livello di classe, ma non esistono studi clinici o pubblicazioni specifici (l'unico studio è su un'altra patologia e usa l'acitretina come comparatore). Il profilo di sicurezza (teratogenicità, epatotossicità, alterazioni lipidiche) e l'esistenza di alternative consolidate come l'isotretinoina ne limitano il valore, mentre tutte le autorizzazioni italiane sono cancellate.

**Per procedere sono necessari:**
- Dati di avvertenze e controindicazioni dal foglio illustrativo AIFA (lacuna bloccante per lo screening di sicurezza)
- Dati sul meccanismo d'azione da DrugBank
- Evidenza clinica diretta nell'acne e confronto con l'isotretinoina
- Chiarimento dello stato regolatorio in Italia (autorizzazioni cancellate) e di un eventuale piano di gestione del rischio teratogeno

**Note sulle altre predizioni** (tutte L5, Hold): lupus eritematoso sistemico pediatrico (punteggio 0,9935; legame speculativo e rischi pediatrici come chiusura precoce delle epifisi), eritroblastosi fetale (0,9928; il punteggio proviene dal modello TxGNN (deep learning) e può riflettere similarità apprese dal modello tra malattie correlate, non evidenza biologica; clinicamente inappropriata per la teratogenicità) e sindrome familiare da teleangectasia cutanea e predisposizione al cancro orofaringeo (0,9910; legame teorico debole, richiederebbe un approccio specialistico caso per caso).
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

