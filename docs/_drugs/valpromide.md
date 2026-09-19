---
layout: default
title: Valpromide
parent: Solo previsione del modello (L5)
nav_order: 209
evidence_level: L5
indication_count: 1
---

# Valpromide
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **1** 
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

# Valpromide: Dall'Anticonvulsivante/Disturbi dell'Umore all'Insonnia

## Sommario in una frase

Valpromide è un prodotto farmaceutico amidico dell'acido valproico, storicamente associato ad applicazioni anticonvulsivanti e stabilizzanti dell'umore — sebbene nessuna indicazione approvata sia formalmente registrata in Italia. Il modello TxGNN prevede che potrebbe essere efficace per l'insonnia, con 0 studi clinici e 1 pubblicazione attualmente a supporto di questa direzione. La base di evidenza complessiva rimane minima, posizionando questo candidato al più precoce stadio di esplorazione.

---

## Panoramica veloce

| Voce | Contenuto |
|------|---------|
| Indicazione originale | Nessuna indicazione registrata in Italia (farmaco non commercializzato) |
| Indicazione nuova prevista | Insonnia |
| Punteggio di previsione TxGNN | 99.79% |
| Livello di evidenza | L5 |
| Stato del mercato italiano | ✗ Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Hold |

---

## Perché questa previsione è ragionevole?

Attualmente, i dati dettagliati sul meccanismo d'azione non sono disponibili per valpromide. Sulla base delle informazioni farmacologiche note, valpromide è un prodotto farmaceutico amidico strutturale dell'acido valproico — durante il metabolismo viene convertito in acido valproico, che a sua volta potenzia la neurotrasmissione GABAergica nel sistema nervoso centrale. Questo meccanismo è ampiamente analogo a quello delle benzodiazepine, una classe importante di farmaci ipnotici approvati, fornendo una base teorica per un effetto sedativo/ipnotico.

Il collegamento concettuale tra farmaci anticonvulsivanti/stabilizzanti l'umore e l'insonnia non è senza precedenti: gli agenti della classe dei valproati sono talvolta osservati migliorare l'architettura del sonno come effetto secondario nei pazienti con epilessia o disturbo bipolare. L'insonnia si presenta frequentemente insieme ad agitazione e disturbi d'ansia, e il percorso di potenziamento GABAergico che sta alla base dell'attività anticonvulsivante della valpromide potrebbe plausibilmente ridurre la latenza di inizio del sonno o migliorare la continuità del sonno.

Tuttavia, è importante sottolineare che questo ragionamento meccanicistico è derivato indirettamente dalla classe dei valproati. Valpromide stessa non è stata direttamente validata per la promozione del sonno mediata da GABA in studi controllati sull'uomo. La previsione del modello TxGNN (punteggio 99.79%) riflette la plausibilità biologica basata su grafo, non l'evidenza clinica — e deve essere interpretata di conseguenza fino a quando non saranno disponibili dati prospettici.

---

## Evidenza da studi clinici

Attualmente non ci sono studi clinici correlati registrati.

---

## Evidenza dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati chiave |
|------|------|------|---------|-------------|
| [10370890](https://pubmed.ncbi.nlm.nih.gov/10370890/) | 1999 | Serie di casi (n=8) | L'Encephale | Valpromide e carbamazepina utilizzate per gestire l'agitazione aggressiva, l'ansia e l'insonnia in pazienti con demenza di Alzheimer; entrambi gli agenti hanno mostrato efficacia con un profilo di effetti collaterali più favorevole rispetto agli antipsicotici |

---

## Informazioni sul mercato italiano

Valpromide non ha attualmente autorizzazioni di commercializzazione in Italia e non è disponibile in commercio nel mercato italiano.

---

## Considerazioni di sicurezza

Si prega di fare riferimento al foglio illustrativo per le informazioni sulla sicurezza. Non sono stati recuperati dati su interazioni farmacologiche, controindicazioni o avvertenze chiave per valpromide in questo momento.

---

## Conclusioni e prossimi passi

**Decisione: Hold**

**Razionale:**
L'evidenza a supporto di valpromide per l'insonnia consiste in un'unica serie di casi del 1999 (n=8) in cui l'insonnia era un sintomo secondario — non un endpoint primario — in una popolazione con demenza. Non ci sono studi clinici registrati, nessuna approvazione normativa in Italia e nessun dato verificato sul meccanismo d'azione. Il punteggio TxGNN riflette la plausibilità meccanicistica attraverso l'inferenza su grafo, non la convalida clinica.

**Per procedere, sono necessari i seguenti elementi:**
- Recupero e revisione del foglio illustrativo di valpromide (fonti TFDA/EMA) per stabilire le avvertenze chiave e le controindicazioni prima che qualsiasi valutazione della sicurezza possa essere condotta
- Conferma del meccanismo d'azione tramite query API DrugBank (DG002)
- Studi prospettici di farmacocinetica/farmacodinamica che caratterizzano gli effetti ipnotici diretti della valpromide nel SNC indipendentemente dalla conversione dell'acido valproico
- Almeno uno studio clinico esplorativo di Fase 2 in pazienti con insonnia primaria (popolazione adulta generale, non solo coorti con demenza) prima di aggiornare il livello di evidenza
- Valutazione della fattibilità della via normativa italiana/UE dato zero autorizzazioni esistenti e nessuna indicazione approvata in nessun paese

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

