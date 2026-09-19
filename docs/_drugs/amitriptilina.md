---
layout: default
title: Amitriptilina
parent: Solo previsione del modello (L5)
nav_order: 28
evidence_level: L5
indication_count: 0
---

# Amitriptilina
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

# Amitriptilina (AMITRIPTILINA): Rapporto di Valutazione del Riposizionamento di Farmaco

## Riassunto in una frase

L'amitriptilina (AMITRIPTILINA) è un ben noto antidepressivo triciclico ampiamente utilizzato per la depressione, il dolore neuropatico e la profilassi dell'emicrania. Il modello TxGNN **non ha generato alcuna indicazione nuova prevista** per questo composto nel ciclo di analisi attuale. Rimangono significative lacune nei dati, inclusi i dettagli del meccanismo d'azione, le informazioni sulla sicurezza normativa e i dati di autorizzazione al mercato per l'Italia.

---

## Panoramica rapida

| Elemento | Contenuto |
|----------|-----------|
| Farmaco (INN) | AMITRIPTILINA (Amitriptilina) |
| ID DrugBank | Non disponibile |
| Indicazione Originale | Non registrata nel pacchetto di evidenze (nota: depressione, dolore neuropatico) |
| Indicazione Prevista Nuova | **Nessuna** — nessuna indicazione prevista da TxGNN |
| Punteggio di Previsione TxGNN | N/A |
| Livello di Evidenza | **L5** — Nessuna previsione e nessuno studio di supporto in questo pacchetto |
| Stato di Mercato Italia | ❌ Non commercializzato (Non commercializzato) |
| Numero di Autorizzazioni | 0 |
| Decisione Consigliata | **Sospensione** |

---

## Perché questa previsione è ragionevole?

**Non esiste alcuna previsione TxGNN da valutare** per l'amitriptilina in questo ciclo di analisi. L'elenco delle indicazioni previste è vuoto, il che significa che il modello non ha elaborato questo farmaco o non ha identificato indicazioni che soddisfino la soglia di confidenza.

Attualmente, i dati dettagliati sul meccanismo d'azione non sono disponibili in questo pacchetto di evidenze. Sulla base della conoscenza farmacologica consolidata, l'amitriptilina è un antidepressivo triciclico (TCA) che inibisce principalmente il riassorbimento della serotonina e della noradrenalina. Possiede inoltre proprietà anticolinergiche, antistaminiche e di blocco dei canali del sodio, che spiegano la sua ampia utilità clinica nella depressione, nel dolore neuropatico, nella profilassi dell'emicrania e nei disturbi funzionali gastrointestinali. Tuttavia, nessuno di questi razionali meccanicistici può essere collegato a una nuova indicazione prevista perché non è stata generata alcuna previsione.

Prima che possa essere eseguita una valutazione significativa, la pipeline di previsione TxGNN dovrebbe essere rieseguita per l'amitriptilina al fine di determinare se emergono candidati di riposizionamento. La ricca polifarmacologia del farmaco lo rende un candidato plausibile per il riposizionamento multi-bersaglio una volta risolte le lacune nei dati.

---

## Evidenza da Studi Clinici

Attualmente nessuno studio clinico correlato registrato in questo pacchetto di evidenze — nessuna indicazione prevista era disponibile per la ricerca.

---

## Evidenza da Letteratura

Attualmente nessuna letteratura correlata disponibile in questo pacchetto di evidenze — nessuna indicazione prevista era disponibile per la ricerca.

---

## Informazioni di Mercato Italia

Nessuna autorizzazione di commercializzazione registrata. L'amitriptilina non sembra possedere licenze approvate AIFA attuali nel dataset esaminato (0 licenze trovate).

---

## Considerazioni sulla Sicurezza

> Si prega di fare riferimento al foglio illustrativo per le informazioni sulla sicurezza.

Tutti i campi di sicurezza (avvertenze principali, controindicazioni, interazioni farmacologiche) non hanno restituito dati nel pacchetto di evidenze attuale. La query DDI ha restituito `not_found` con 0 interazioni. Questo rappresenta una lacuna nei dati **Bloccante** (DG001) che deve essere risolta prima che possa procedere qualsiasi valutazione della sicurezza in Fase 1.

---

## Riepilogo delle Lacune nei Dati

Le seguenti lacune critiche sono state identificate e dovrebbero essere affrontate prima della rivalutazione:

| ID Lacuna | Categoria | Elemento | Gravità | Rimedio |
|-----------|-----------|----------|---------|---------|
| DG001 | Livello Farmaco | Avvertenze del foglio illustrativo / controindicazioni | **Bloccante** | Scaricare e analizzare il PDF del foglio illustrativo dal sito web dell'autorità normativa |
| DG002 | Livello Farmaco | Meccanismo d'Azione (MOA) | **Alto** | Interrogare l'API di DrugBank (nota: l'ID di DrugBank è attualmente mancante) |
| — | Previsione | Indicazioni previste da TxGNN | **Bloccante** | Rieseguire la pipeline di previsione TxGNN per l'amitriptilina |
| — | Livello Farmaco | ID DrugBank | Alto | Risolvere la mappatura DrugBank (DB00321 è l'ID noto per l'amitriptilina) |
| — | Normativa | Dati di autorizzazione di mercato Italia | Medio | Interrogare direttamente il database AIFA |

---

## Conclusione e Prossimi Passi

**Decisione: Sospensione**

**Razionale:**
Non è stata generata alcuna previsione TxGNN per l'amitriptilina, e molteplici lacune nei dati bloccanti (informazioni sulla sicurezza, MOA, dati normativi) impediscono qualsiasi valutazione significativa del riposizionamento. Il pacchetto di evidenze è essenzialmente vuoto in tutte le dimensioni chiave.

**Per procedere, è necessario quanto segue:**
- **Risolvere la mappatura DrugBank** — L'ID DrugBank noto dell'amitriptilina è DB00321; collegare questo sbloccherebbe i dati su MOA, tossicità e interazioni
- **Rieseguire la pipeline di previsione TxGNN** con l'identificatore del farmaco corretto per generare candidate indicazioni
- **Ottenere dati sulla sicurezza AIFA / normativi** — scaricare e analizzare il foglio illustrativo per colmare la lacuna bloccante DG001
- **Rieseguire le query del database DDI** una volta che l'ID DrugBank sia correttamente collegato
- **Rigenerare il pacchetto di evidenze** dopo che le lacune di cui sopra siano state colmate, quindi rivalutare

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

