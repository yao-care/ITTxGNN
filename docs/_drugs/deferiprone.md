---
layout: default
title: Deferiprone
parent: Solo previsione del modello (L5)
nav_order: 67
evidence_level: L5
indication_count: 9
---

# Deferiprone
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **9** 
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

# Deferiprone: farmaco per il sovraccarico di ferro — Valutazione del riposizionamento (dati insufficienti)

## Sintesi in una frase

Deferiprone (DB08826) è un chelante del ferro noto utilizzato storicamente per trattare il sovraccarico di ferro trasfusionale in pazienti con sindromi talassemiche. Tuttavia, l'attuale Pacchetto di evidenze **non contiene alcuna nuova indicazione predetta da TxGNN** e **non ha autorizzazioni di mercato a Taiwan**, rendendo una valutazione standard del riposizionamento impossibile in questa fase. Numerosi gap critici dei dati — inclusa la documentazione mancante del MOA, gli avvertimenti del foglio illustrativo e le controindicazioni — devono essere risolti prima che qualsiasi percorso di riposizionamento possa essere valutato.

---

## Panoramica rapida

| Voce | Contenuto |
|------|-----------|
| Indicazione originaria | Sovraccarico di ferro (talassemia; non formalmente acquisita in questo Pacchetto di evidenze) |
| Nuova indicazione predetta | Nessuna — le previsioni TxGNN non sono disponibili in questo Pacchetto di evidenze |
| Punteggio di previsione TxGNN | N/A |
| Livello di evidenza | L5 (previsione del modello non disponibile; nessuno studio di supporto recuperabile) |
| Stato di mercato a Taiwan | ✗ Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | **Mantenere in sospeso** |

---

## Perché non è disponibile alcuna previsione

Il Pacchetto di evidenze per Deferiprone è stato costruito solo da dati DrugBank (`inputs_received: ["drugbank"]`). Due gap critici o ad alta gravità dei dati bloccano direttamente la previsione e l'analisi:

1. **Avvertimenti e controindicazioni del foglio illustrativo a Taiwan mancanti (DG001 — Bloccante):** Senza questo documento, la fase di pre-screening della sicurezza (S1) non può iniziare. Il percorso di rimedio è scaricare il relativo PDF del foglio illustrativo dal sito ufficiale della TFDA e analizzarlo.

2. **Dati del meccanismo d'azione mancanti (DG002 — Alto):** Senza un MOA confermato, la plausibilità meccanicistica che collega la farmacologia di Deferiprone a qualsiasi nuova indicazione target non può essere valutata. Una query API a DrugBank dovrebbe recuperare questo.

Fino a quando entrambi i gap non saranno risolti, il punteggio TxGNN per questo candidato non può essere considerato affidabile o interpretato.

---

## Informazioni sul mercato a Taiwan

Nessuna autorizzazione di prodotto per Deferiprone è stata trovata nel database di Taiwan (TFDA) al cutoff dei dati (2026-04-20). Il farmaco è attualmente **non commercializzato** a Taiwan.

> Se i dati di autorizzazione di commercializzazione esistono in altre giurisdizioni (ad es. approvazione EMA/FDA per Ferriprox), devono essere recuperati separatamente e incorporati in un Pacchetto di evidenze revisionato.

---

## Considerazioni sulla sicurezza

I dati di sicurezza non potevano essere recuperati per questa valutazione. Si prega di fare riferimento al foglio illustrativo ufficiale (ottenibile da TFDA o EMA) per le avvertenze complete, le controindicazioni e le informazioni sulle interazioni farmacologiche prima di procedere.

---

## Conclusione e passaggi successivi

**Decisione: Mantenere in sospeso**

**Razionale:**
Il Pacchetto di evidenze è incompleto in due dimensioni bloccanti — nessuna previsione TxGNN è stata generata e la documentazione di sicurezza critica (foglio illustrativo) è assente — rendendo impossibile valutare la fattibilità del riposizionamento o la sicurezza del paziente in questa fase.

**Per procedere, è necessario quanto segue:**

- **[DG001 — Bloccante]** Scarica e analizza il foglio illustrativo di Deferiprone dal sito web della TFDA per estrarre avvertimenti e controindicazioni approvati; questo sblocca la fase di pre-screening della sicurezza S1
- **[DG002 — Alto]** Interroga l'API DrugBank per il meccanismo d'azione confermato di Deferiprone (percorso di chelazione del ferro, proteine target) per consentire l'analisi della plausibilità meccanicistica
- **Esegui nuovamente la pipeline TxGNN** dopo che i gap dei dati sono stati risolti in modo che venga generato un elenco classificato delle nuove indicazioni predette
- **Espandi i dati normativi di input** per includere i record di autorizzazione EMA/FDA (Deferiprone/Ferriprox detiene approvazioni al di fuori di Taiwan che possono informare il contesto di riposizionamento)
- Una volta disponibili le previsioni, **rigenerare questo report** utilizzando il Pacchetto di evidenze completo (v5+)

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

