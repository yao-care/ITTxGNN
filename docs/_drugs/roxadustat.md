---
layout: default
title: Roxadustat
parent: Solo previsione del modello (L5)
nav_order: 391
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Roxadustat: nuova indicazione prevista, Sindrome dell'occhio secco (livello di evidenza L5). Indicazione originale: Anemia refrattaria (dal grafo di conoscenza TxGNN"
---

# Roxadustat
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **4** 
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

# Roxadustat: Dall'anemia refrattaria alla sindrome dell'occhio secco

## Sintesi in una frase

Roxadustat è un inibitore della prolil-idrossilasi del fattore inducibile dall'ipossia (HIF-PH), originariamente associato al trattamento dell'anemia refrattaria. Il modello TxGNN prevede una possibile efficacia nella **sindrome dell'occhio secco**, ma al momento **non risultano studi clinici né pubblicazioni** a sostegno di questa direzione: l'unico elemento a favore è il punteggio del modello.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Anemia refrattaria (dal grafo di conoscenza TxGNN; il testo dell'indicazione nelle autorizzazioni AIFA non è disponibile) |
| Nuova indicazione prevista | Sindrome dell'occhio secco |
| Punteggio di predizione TxGNN | 99,51% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni annullate |
| Numero di autorizzazioni | 5 (tutte annullate) |
| Decisione raccomandata | Hold |

## Perché questa predizione potrebbe essere ragionevole?

Roxadustat stabilizza i fattori HIF-1α e HIF-2α inibendo le prolil-idrossilasi (EGLN). Questo meccanismo spiega l'aumento dell'eritropoietina e l'impiego nell'anemia associata a malattia renale cronica, per la quale l'EMA lo ha approvato nell'agosto 2021. I dati compilati per questo report non contengono una descrizione dettagliata del meccanismo d'azione; quanto segue deriva dalle conoscenze generali sulla classe del farmaco.

Il legame con l'occhio secco è **speculativo**. L'attivazione di HIF potrebbe in teoria influire su infiammazione della superficie oculare, riparazione epiteliale e angiogenesi. Tuttavia, la stessa segnalazione pro-angiogenica e pro-infiammatoria potrebbe risultare dannosa per la superficie oculare. Anemia refrattaria e occhio secco sono inoltre condizioni molto distanti, e la similarità con l'indicazione originale non è stata valutata.

Il punteggio elevato (0,995, posizione 2841 nella classifica del modello) è quindi da interpretare come un'associazione di rete, non come prova di beneficio.

## Evidenze da studi clinici

Al momento non risultano studi clinici correlati registrati.

## Evidenze dalla letteratura

Al momento non risulta letteratura correlata.

## Informazioni sul mercato italiano

| N. autorizzazione | Nome prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 049685050 | EVRENZO 12 compresse rivestite 150 mg | Compressa rivestita | Non disponibile |
| 049685047 | EVRENZO 12 compresse rivestite 100 mg | Compressa rivestita | Non disponibile |
| 049685035 | EVRENZO 12 compresse rivestite 70 mg | Compressa rivestita | Non disponibile |
| 049685023 | EVRENZO 12 compresse rivestite 50 mg | Compressa rivestita | Non disponibile |
| 049685011 | EVRENZO 12 compresse rivestite 20 mg | Compressa rivestita | Non disponibile |

Tutte le autorizzazioni (titolare: Astellas Pharma Europe B.V.) risultano annullate; non esiste quindi attualmente alcun prodotto valido sul mercato italiano.

## Considerazioni di sicurezza

- **Interazioni**: la ricerca ha individuato una sola voce, di natura farmacologica e non una interazione tra farmaci: l'interazione con il bersaglio EGLN2 (egl-9 family hypoxia inducible factor 2), coerente con il meccanismo d'azione di inibizione delle HIF-PH.
- **Preoccupazione teorica**: la stabilizzazione di HIF è associata a progressione tumorale, adattamento all'ipossia e angiogenesi. Questo è particolarmente rilevante per le predizioni oncologiche (ad esempio il carcinoma squamocellulare), dove costituirebbe un rischio di promozione tumorale più che una logica terapeutica. Anche per l'occhio la segnalazione pro-angiogenica richiede cautela.

Per avvertenze e controindicazioni complete, consultare il foglio illustrativo.

## Altre predizioni del modello (per contesto)

| Posizione | Malattia prevista | Punteggio | Evidenze | Commento |
|------|------|------|------|------|
| 2 | Malattia ossea di Paget | 99,12% | Nessuna | HIF influenza il rimodellamento osseo, ma la direzione dell'effetto è incerta e la terapia con bisfosfonati è già efficace |
| 3 | Dentinogenesi imperfetta | 99,06% | Nessuna | Malattia genetica (tipicamente DSPP) senza un percorso meccanicistico plausibile |
| 4 | Carcinoma squamocellulare | 99,02% | Nessuna | Rischio teorico di promozione tumorale; richiede prima una valutazione di sicurezza |

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione si basa solo sul punteggio TxGNN (livello L5), senza studi clinici né letteratura. Il razionale meccanicistico è speculativo e potrebbe addirittura essere sfavorevole, e senza autorizzazioni valide in Italia né dati di sicurezza dal foglio illustrativo non è possibile procedere alla valutazione di sicurezza.

**Per procedere sono necessari:**
- Recupero e analisi del foglio illustrativo AIFA (avvertenze e controindicazioni), attualmente un limite bloccante
- Dati dettagliati sul meccanismo d'azione (ad esempio da DrugBank)
- Studi preclinici sull'effetto della stabilizzazione di HIF sulla superficie oculare (infiammazione, riparazione epiteliale, angiogenesi)
- Ricerca sistematica di letteratura e studi registrati sull'occhio secco
- Valutazione della compatibilità della via di somministrazione (probabile necessità di una formulazione oftalmica topica, oggi inesistente) e della similarità con l'indicazione originale
- Valutazione del rischio teorico legato all'attivazione di HIF
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

