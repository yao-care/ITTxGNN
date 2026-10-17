---
layout: default
title: Octreotide
parent: Solo previsione del modello (L5)
nav_order: 325
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
monitor_inn: "OCTREOTIDE"
predicted_indications: ["vulvar inverted follicular keratosis", "seborrheic keratosis"]
description: "Octreotide: nuova indicazione prevista, Cheratosi follicolare invertita vulvare (livello di evidenza L5)."
---

# Octreotide
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **2** 
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

# Octreotide: Dall'acromegalia alla cheratosi follicolare invertita vulvare

## Sintesi in una frase

L'octreotide è un analogo della somatostatina, originariamente utilizzato per il trattamento di acromegalia, iperpituitarismo e sindrome da carcinoide.
Il modello TxGNN ne prevede una possibile efficacia per la **cheratosi follicolare invertita vulvare** (e, in seconda posizione, per la **cheratosi seborroica**), ma al momento **non risulta alcuna sperimentazione clinica né alcuna pubblicazione** a sostegno di questa direzione: si tratta di una predizione puramente computazionale.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originaria | Acromegalia, iperpituitarismo, sindrome da carcinoide (da grafo di conoscenza; il testo delle indicazioni AIFA non è disponibile) |
| Nuova indicazione predetta | Cheratosi follicolare invertita vulvare |
| Punteggio di predizione TxGNN | 99,58% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 20 (tutte cancellate; nessuna valida) |
| Decisione raccomandata | Hold |

## Perché questa predizione potrebbe essere ragionevole?

I dati compilati per questo report non contengono informazioni dettagliate sul meccanismo d'azione. In base alle conoscenze generali, l'octreotide è un analogo della somatostatina che agisce principalmente sui recettori della somatostatina SSTR2 e SSTR5, e la sua efficacia nelle patologie neuroendocrine e ipersecretive originarie è nota.

Non vi è però alcuna evidenza, nei dati forniti, che questi recettori abbiano un ruolo nella cheratosi follicolare invertita, una lesione epiteliale benigna. Il collegamento meccanicistico non è quindi supportato. Il punteggio TxGNN (0,996) è una predizione derivata dal modello e non è corroborato da studi.

Anche la seconda predizione, la **cheratosi seborroica** (punteggio 99,55%), è una proliferazione epidermica benigna senza evidenze a supporto. I due punteggi sono molto vicini, il che suggerisce che condividano lo stesso segnale basato sul grafo: non vanno considerati come supporti indipendenti.

## Evidenze da sperimentazioni cliniche

Attualmente non risultano sperimentazioni cliniche correlate registrate.

## Evidenze dalla letteratura

Attualmente non è disponibile alcuna letteratura correlata.

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate; il testo delle indicazioni approvate e la forma farmaceutica non sono disponibili. Si elencano le prime 5 a titolo informativo:

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 040014021 | Octreotide, 10 fiale SC/EV 1 ml 0,1 mg/ml | Bioindustria L.I.M. SpA | Cancellata |
| 040014033 | Octreotide, 10 fiale SC/EV 1 ml 0,5 mg/ml | Bioindustria L.I.M. SpA | Cancellata |
| 041156011 | Octreotide, 5 fiale EV/SC 0,05 mg 1 ml | Sun Pharmaceutical Ind. Eu. B.V. | Cancellata |
| 027083094 | Sandostatina LAR, 1 flacone IM 20 mg + siringa 2 ml + ago | Novartis Farma SpA | Cancellata |
| 039101011 | Siroctid, 5 siringhe 1 ml 50 mcg/ml | Chemi SpA | Cancellata |

## Considerazioni di sicurezza

- **Controindicazioni suggerite dal grafo di conoscenza** (relazioni farmaco-malattia di PrimeKG, non testo del foglietto illustrativo): iperglicemia, ipotiroidismo, mixedema, ipotiroidismo congenito, cirrosi epatica, diabete mellito, chetoacidosi diabetica, malattia della colecisti, malattie epatiche, ileo, occlusione intestinale, arresto cardiaco improvviso, malattie della conduzione cardiaca, ipoglicemia, colelitiasi, colecistolitiasi, coledocolitiasi, insufficienza renale, uremia, carenza di vitamina B12.
- **Interazioni farmacologiche**: la ricerca ha individuato 100 interazioni; quelle mostrate sono tutte di livello **moderato**, soprattutto con antidiabetici (acarbosio, metformina, glimepiride, clorpropamide, linagliptin, alogliptin), agonisti GLP-1 (albiglutide, dulaglutide, semaglutide), inibitori SGLT2 (canagliflozin, dapagliflozin, empagliflozin) e varie insuline (aspart, degludec, detemir, glargine, glulisine, umana regolare e isofano, inalatoria). È necessario un monitoraggio della glicemia in caso di associazione.

Per avvertenze e controindicazioni ufficiali, consultare il foglietto illustrativo.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione si basa unicamente sul modello (livello L5), senza sperimentazioni né pubblicazioni, e non esiste un collegamento meccanicistico plausibile con una lesione epiteliale benigna. Inoltre, tutte le autorizzazioni italiane sono cancellate e i dati di sicurezza ufficiali mancano.

**Per procedere, sono necessari:**
- Dati sul meccanismo d'azione (MOA) e verifica del ruolo dei recettori SSTR2/SSTR5 nella cheratosi follicolare invertita
- Foglietto illustrativo AIFA con avvertenze e controindicazioni (lacuna bloccante per lo screening di sicurezza)
- Una revisione della letteratura e dei registri di sperimentazioni per la nuova indicazione
- Valutazione della compatibilità della via di somministrazione e della disponibilità commerciale attuale in Italia, dato che non esistono autorizzazioni valide
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

