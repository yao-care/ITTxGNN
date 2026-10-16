---
layout: default
title: Turoctocog Alfa
parent: Solo previsione del modello (L5)
nav_order: 455
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Turoctocog Alfa: nuova indicazione prevista, Disturbo primario del rilascio piastrinico (livello di evidenza L5). Indicazione originale: Emofilia"
---

# Turoctocog Alfa
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

# Turoctocog alfa: dall'emofilia a un disturbo di rilascio piastrinico primario

## Riepilogo in una frase

Turoctocog alfa è un fattore VIII della coagulazione ricombinante umano, utilizzato originariamente per il trattamento dell'emofilia (inclusa la forma sintomatica nelle portatrici di sesso femminile). Il modello TxGNN prevede una possibile efficacia nel **disturbo primario del rilascio piastrinico**, ma attualmente **non risulta alcuno studio clinico né alcuna pubblicazione** a sostegno di questa direzione: si tratta di una previsione puramente computazionale.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Emofilia; forma sintomatica di emofilia nelle portatrici di sesso femminile (testo di indicazione AIFA non disponibile) |
| Nuova indicazione prevista | Disturbo primario del rilascio piastrinico |
| Punteggio di previsione TxGNN | 99,99% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 6 (tutte cancellate) |
| Decisione raccomandata | Hold |

## Perché questa previsione è ragionevole?

Allo stato attuale i dati dettagliati sul meccanismo d'azione non sono disponibili. Sulla base delle informazioni note, turoctocog alfa è un fattore VIII ricombinante che sostituisce il fattore carente nell'emofilia A e partecipa al complesso tenasi della cascata coagulativa.

Nel caso specifico, il collegamento meccanicistico è **debole**. I disturbi del rilascio piastrinico sono dovuti a difetti intrinseci della secrezione piastrinica e non a una carenza di fattore VIII, quindi la sostituzione del FVIII non corregge il difetto di base. L'elevato punteggio TxGNN riflette probabilmente la vicinanza nel grafo di conoscenza tra i disturbi della coagulazione e quelli emorragici, più che una reale plausibilità biologica.

Tra le altre previsioni di rilievo, la più plausibile dal punto di vista meccanicistico è la **carenza acquisita di fattori della coagulazione** (punteggio 99,95%), in cui la sostituzione del FVIII potrebbe in teoria essere utile. La categoria è però ampia ed eterogenea e, ad esempio, nell'emofilia acquisita gli autoanticorpi neutralizzano il FVIII e sono preferiti altri agenti. Altre previsioni (trombastenia di Glanzmann, pseudo-malattia di von Willebrand, sindrome di Scott) non hanno un supporto meccanicistico diretto. La **porpora trombotica trombocitopenica** (PTT) solleva invece una preoccupazione di sicurezza: un fattore procoagulante potrebbe in principio aggravare la trombosi.

## Evidenze da studi clinici

Attualmente non risultano studi clinici correlati registrati.

## Evidenze dalla letteratura

Attualmente non risulta alcuna letteratura correlata disponibile.

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Stato | Indicazione approvata |
|---------|------|------|-----------|
| 043153067 | NOVOEIGHT 3.000 UI + siringa solvente 4 ml | Cancellata | Non disponibile |
| 043153030 | NOVOEIGHT 1.000 UI + siringa solvente 4 ml | Cancellata | Non disponibile |
| 043153028 | NOVOEIGHT 500 UI + siringa solvente 4 ml | Cancellata | Non disponibile |
| 043153055 | NOVOEIGHT 2.000 UI + siringa solvente 4 ml | Cancellata | Non disponibile |
| 043153016 | NOVOEIGHT 250 UI + siringa solvente 4 ml | Cancellata | Non disponibile |

Titolare: Novo Nordisk A/S. Esiste una sesta autorizzazione cancellata (043153042, 1.500 UI), non riportata nella tabella per il limite di 5 voci. Nessuna autorizzazione risulta attualmente valida.

## Considerazioni sulla sicurezza

Le informazioni su avvertenze e controindicazioni dal foglio illustrativo AIFA non sono disponibili nei dati compilati per questo report, e non sono state identificate interazioni farmacologiche. Si rimanda al foglio illustrativo per le informazioni di sicurezza.

Si segnala inoltre, sul piano teorico, che l'uso di un fattore procoagulante in condizioni trombotiche (come la PTT) o con piastrine elevate (come la trombocitosi ereditaria) potrebbe aumentare il rischio trombotico.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
Tutte le previsioni si fondano esclusivamente sul modello (livello L5), senza studi clinici né letteratura. Per la previsione principale manca un razionale meccanicistico, e il prodotto non ha attualmente autorizzazioni valide in Italia.

**Per procedere sono necessari:**
- Foglio illustrativo AIFA con avvertenze e controindicazioni (lacuna bloccante per la valutazione di sicurezza)
- Dati sul meccanismo d'azione (MOA) da DrugBank
- Verifica della denominazione di alcune malattie previste (ad esempio «flood factor deficiency») rispetto a ontologie standard come MONDO o Orphanet
- Valutazione prioritaria della «carenza acquisita di fattori della coagulazione» come candidato più plausibile, con revisione della letteratura e degli studi esistenti
- Chiarimento dello stato regolatorio (cancellazione delle autorizzazioni) e della disponibilità di prodotti alternativi
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

