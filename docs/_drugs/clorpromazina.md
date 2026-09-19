---
layout: default
title: Clorpromazina
parent: Solo previsione del modello (L5)
nav_order: 59
evidence_level: L5
indication_count: 0
---

# Clorpromazina
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **0** 
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

# Clorpromazina: Valutazione della Riproposizione Incompleta — Previsioni di TxGNN Non Disponibili

## Riassunto in una Riga

Clorpromazina (chlorpromazine) è un antipsicoptico fenotiazinico di prima generazione con un uso consolidato nelle patologie psichiatriche.
Tuttavia, questo Evidence Pack non contiene **alcun'indicazione nuova prevista da TxGNN** e mancano campi critici — indicazioni originarie, meccanismo d'azione e dati di sicurezza — rendendo impossibile al momento una valutazione completa della riproposizione.
La pipeline dei dati ha confermato che le fonti DrugBank e del foglio illustrativo hanno ciascuna restituito un risultato, ma il loro contenuto non era ancora stato integrato nell'Evidence Pack.

---

## Panoramica Rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione Originaria | Non disponibile nell'Evidence Pack |
| Indicazione Nuova Prevista | Nessuna — previsioni di TxGNN non popolate |
| Punteggio di Previsione TxGNN | N/A |
| Livello di Evidenza | N/A |
| Stato nel Mercato Italiano | Non commercializzato |
| Numero di Autorizzazioni | 0 |
| Decisione Consigliata | In sospeso |

---

## Considerazioni di Sicurezza

Si prega di consultare il foglio illustrativo per le informazioni di sicurezza.

---

## Conclusione e Prossimi Passi

**Decisione: In sospeso**

**Razionale:**
L'Evidence Pack per Clorpromazina è criticamente incompleto — senza previsioni di TxGNN, indicazioni originarie, meccanismo d'azione o dati di sicurezza, nessuna ipotesi di riproposizione può essere formulata o valutata.

**Per procedere, è necessario il seguente:**

- **Output del modello TxGNN** — l'array `predicted_indications` è vuoto; il modello deve essere eseguito o i risultati caricati per questo farmaco prima che possa iniziare qualsiasi valutazione
- **Indicazioni Originarie Approvate** — `original_indications` è vuoto; recuperare dal database AIFA o dal foglio illustrativo
- **Meccanismo d'azione** — la query DrugBank ha restituito 1 risultato il 2026-03-29 ma i dati non sono stati integrati in `drug.original_moa`; estrarre e popolare
- **Informazioni sulla Sicurezza** — la query del foglio illustrativo ha restituito 1 risultato il 2026-03-29 ma `key_warnings` e `contraindications` rimangono non compilati; analizzare e integrare
- **Dati di Interazione Farmacologica** — la query DDI non ha restituito risultati; considerare l'interrogazione di un database DDI alternativo (ad es., interazioni DrugBank, Drugs.com)
- **Verifica del Mercato Italiano** — Confermare se Clorpromazina possiede autorizzazioni AIFA; 0 licenze è inaspettato per un composto di questa classe

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

