---
layout: default
title: Almotriptan
parent: Solo previsione del modello (L5)
nav_order: 22
evidence_level: L5
indication_count: 3
---

# Almotriptan
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **3** 
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

# ALMOTRIPTAN: Relazione di valutazione del riutilizzo di farmaci

## Riassunto in una frase

Almotriptano è un agonista selettivo del recettore 5-HT₁B/₁D, ampiamente noto per il trattamento acuto delle cefalee emicraniche. Il modello TxGNN attualmente **non presenta indicazioni nuove previste** per questo farmaco, e il pacchetto di prove contiene significative lacune nei dati riguardanti il meccanismo d'azione, la sicurezza e le informazioni normative. Prima di procedere con qualsiasi valutazione del riutilizzo sono necessari ulteriori raccolta di dati.

---

## Panoramica rapida

| Elemento | Contenuto |
|------|------|
| Nome del farmaco (INN) | Almotriptano |
| ID DrugBank | [DB00918](https://go.drugbank.com/drugs/DB00918) |
| Indicazione originale | Trattamento acuto dell'emicrania (secondo le conoscenze farmacologiche generali; non compilato nel pacchetto di prove) |
| Indicazione nuova prevista | — (Nessuna previsione TxGNN disponibile) |
| Punteggio di previsione TxGNN | N/A |
| Livello di evidenza | **L5** — Previsione del modello solo; nessuna indicazione prevista o studi di supporto |
| Stato del mercato taiwanese | ✗ Non commercializzato (Non commercializzato) |
| Numero di autorizzazioni TFDA | 0 |
| Decisione consigliata | **In sospeso** |

---

## Perché questa previsione è ragionevole?

Attualmente, il modello TxGNN non ha generato alcuna indicazione nuova prevista per Almotriptano, quindi non esiste alcuna ipotesi di riutilizzo da valutare in questo momento.

Dalle conoscenze farmacologiche generali, Almotriptano è un triptano di seconda generazione — un agonista selettivo del recettore 5-HT₁B/₁D. Funziona costringendo i vasi sanguigni intracranici dilatati e inibendo il rilascio di neuropeptidi pro-infiammatori, interrompendo così gli attacchi acuti di emicrania. La sua elevata selettività per i recettori 5-HT₁B/₁D (con attività minima su altri sottotipi di recettori della serotonina) gli conferisce un profilo di tollerabilità favorevole tra i triptani.

> ⚠️ **Lacuna nei dati:** Il campo `original_moa` del pacchetto di prove non è compilato. Il meccanismo descritto sopra si basa sulla letteratura farmacologica consolidata. Si consiglia una interrogazione formale dell'API di DrugBank per colmare questa lacuna (vedere piano di correzione DG002).

---

## Evidenza da studi clinici

Attualmente non esistono indicazioni previste da TxGNN per Almotriptano, quindi non è stata effettuata alcuna ricerca mirata di studi clinici per candidati di riutilizzo.

---

## Evidenza dalla letteratura

Attualmente non esistono indicazioni previste da TxGNN per Almotriptano, quindi non è stata effettuata alcuna ricerca mirata della letteratura per candidati di riutilizzo.

---

## Informazioni sul mercato taiwanese

Almotriptano **non è commercializzato a Taiwan**. Non sono state trovate licenze farmacologiche TFDA (data della query: 2026-03-29). Non ci sono prodotti autorizzati, forme farmaceutiche o indicazioni approvate registrate con la TFDA.

---

## Considerazioni di sicurezza

> Si prega di fare riferimento al foglio illustrativo per le informazioni sulla sicurezza.
>
> ⚠️ **Lacuna nei dati (Bloccante):** Le avvertenze e le controindicazioni del foglio illustrativo TFDA non potevano essere recuperate (DG001). Questa è classificata come una lacuna **Bloccante** — il candidato non può entrare nello screening di sicurezza S1 finché questo non sarà risolto.
>
> Non sono stati trovati dati su interazioni tra farmaci (DDI) nei database interrogati.

---

## Riepilogo delle lacune nei dati

Sono state identificate le seguenti lacune critiche nei dati che devono essere affrontate prima di qualsiasi valutazione del riutilizzo:

| ID lacuna | Elemento | Gravità | Impatto | Correzione |
|--------|------|----------|--------|-------------|
| DG001 | Avvertenze/Controindicazioni del foglio illustrativo TFDA | **Bloccante** | Non può entrare nello screening di sicurezza S1 | Scaricare e analizzare il PDF del foglio illustrativo dal sito web TFDA |
| DG002 | Meccanismo d'azione (MOA) | **Alto** | Influisce sull'analisi della relazione meccanismo-indicazione | Query API di DrugBank |
| — | Indicazioni previste da TxGNN | **Alto** | Nessun candidato di riutilizzo da valutare | Eseguire/rieseguire la pipeline di previsione TxGNN per DB00918 |
| — | Indicazioni originali (strutturate) | Medio | Tabella Panoramica rapida incompleta | Compilare da dati DrugBank o TFDA |

---

## Conclusione e prossimi passaggi

**Decisione: In sospeso**

**Motivazione:**
Almotriptano attualmente non ha indicazioni nuove previste da TxGNN, non è commercializzato a Taiwan e presenta molteplici lacune bloccanti nei dati. Non ci sono informazioni sufficienti per valutare qualsiasi ipotesi di riutilizzo in questo momento.

**Per procedere, è necessario quanto segue:**
1. **Eseguire/rieseguire la pipeline di previsione TxGNN** per Almotriptano (DB00918) al fine di generare indicazioni candidate
2. **Risolvere DG001 (Bloccante):** Ottenere le avvertenze e le controindicazioni del foglio illustrativo TFDA — obbligatorio prima dello screening di sicurezza S1
3. **Risolvere DG002 (Alto):** Query API di DrugBank per dati dettagliati sul meccanismo d'azione al fine di abilitare l'analisi della relazione meccanismo-indicazione
4. **Compilare i dati sull'indicazione originale** da DrugBank o riferimenti farmacologici autorevoli
5. **Rivalutare il percorso normativo taiwanese** — poiché Almotriptano non è commercializzato a Taiwan, qualsiasi sforzo di riutilizzo dovrebbe tenere conto dei requisiti iniziali di autorizzazione del mercato

---

*Relazione generata: 2026-04-03 | Versione del pacchetto di prove: v4 | ID candidato: TW-DB00918-multi*

*⚠️ Questa relazione è solo per riferimento di ricerca e non costituisce consiglio medico. Qualsiasi candidato di riutilizzo di farmaci richiede convalida clinica prima dell'applicazione.*

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

