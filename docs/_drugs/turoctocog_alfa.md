---
layout: default
title: Turoctocog Alfa
parent: Solo previsione del modello (L5)
nav_order: 208
evidence_level: L5
indication_count: 10
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

# Turoctocog alfa: dall'emofilia A al disturbo primario del rilascio piastrinico

## Riassunto in una sola frase

Turoctocog alfa (NovoEight®) è un Fattore VIII ricombinante umano troncato nel dominio B (rFVIII), originariamente sviluppato per la prevenzione e il trattamento degli episodi emorragici nell'emofilia A.
Il modello TxGNN prevede che potrebbe essere efficace per il **disturbo primario del rilascio piastrinico**, con un punteggio di predizione di **99.99%**.
Tuttavia, questa indicazione è attualmente supportata da **0 studi clinici** e **0 pubblicazioni** — la predizione si basa interamente sulla topologia del grafo di conoscenza e non dispone di alcuna evidenza clinica empirica.

---

## Panoramica rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione originaria | Emofilia A (deficienza congenita del Fattore VIII) |
| Nuova indicazione predetta | Disturbo primario del rilascio piastrinico |
| Punteggio di predizione TxGNN | 99.99% |
| Livello di evidenza | L5 |
| Stato di commercializzazione in Italia | ✗ Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Non procedere |

---

## Perché questa predizione è ragionevole?

Attualmente, i dati dettagliati sul meccanismo d'azione non sono disponibili nel pacchetto di evidenze. Sulla base della conoscenza farmacologica consolidata, turoctocog alfa è un Fattore VIII ricombinante umano troncato nel dominio B. Funziona come cofattore nel complesso tenasi intrinseco (FVIIIa + FIXa), amplificando notevolmente la generazione di trombina attraverso la cascata coagulativa intrinseca. La sua efficacia consolidata è nell'emofilia A — una malattia definita dalla deficienza di FVIII che porta a una compromissione dell'emostasi secondaria.

Il disturbo primario del rilascio piastrinico (malattia da carenza di riserve) implica il rilascio difettoso di contenuti dei granuli α e/o δ dalle piastrine, compromettendo l'emostasi primaria. Questo è un dominio fisiopatologico fondamentalmente diverso dal meccanismo del FVIII: il FVIII agisce sull'emostasi secondaria (cascata coagulativa), mentre i disturbi nel rilascio dei granuli piastrnici interessano l'emostasi primaria (formazione del tappo piastrinico). Il collegamento del modello TxGNN qui sembra derivare da nodi di convergenza a valle tra la cascata coagulativa e i percorsi di attivazione piastrinica nel grafo di conoscenza — un collegamento topologico indiretto piuttosto che una relazione meccanicistica diretta.

In sintesi, l'alto punteggio di predizione riflette la vicinanza nel grafo di conoscenza malattia-farmaco, non una relazione terapeutica meccanicistica diretta. L'integrazione di FVIII non affronta il difetto sottostante nella secrezione dei granuli piastrnici, e attualmente nessuna base biologica supporta un beneficio clinico in questa condizione.

---

## Evidenza da studi clinici

Attualmente non sono registrati studi clinici correlati.

---

## Evidenza bibliografica

Attualmente non è disponibile letteratura correlata.

---

## Considerazioni sulla sicurezza

Per le informazioni sulla sicurezza, si prega di consultare il foglio illustrativo.

---

## Conclusioni e prossimi passi

**Decisione: Non procedere**

**Razionale:**
La predizione è classificata come L5 (solo modello, senza supporto empirico), il collegamento meccanicistico tra l'integrazione di FVIII e i disturbi del rilascio piastrinico è indiretto e biologicamente implausibile come strategia terapeutica primaria, e non esistono studi clinici o pubblicazioni per convalidare questa ipotesi di riutilizzo. Il farmaco inoltre non è attualmente autorizzato in Italia, aggiungendo un ostacolo normativo a qualsiasi percorso di sviluppo.

**Per procedere, sarebbe necessario:**

- **Risoluzione dei gap di dati**: Ottenere il foglio illustrativo completo / il Riassunto delle Caratteristiche del Prodotto (RCP) per caratterizzare le avvertenze note, le controindicazioni e le indicazioni approvate
- **Chiarimento del meccanismo d'azione**: Confermare il meccanismo d'azione dettagliato da DrugBank o dalla letteratura sui prodotti dell'EMA
- **Rivalutazione della plausibilità meccanicistica**: Commissionare una revisione bibliografica mirata che valuti se alcuni effetti secondari correlati al FVIII (ad es., amplificazione della scarica di trombina) potrebbero teoricamente compensare i difetti del rilascio dei granuli piastrnici in modelli ex vivo o animali
- **Indicazioni alternative a priorità più elevata**: Tra le 10 indicazioni predette, **Deficienza acquisita del fattore coagulativo** (rank 5, include Emofilia A acquisita) rappresenta un candidato di riutilizzo molto più plausibile dal punto di vista meccanicistico e dovrebbe essere valutato per primo
- **Strategia normativa italiana**: Data l'assenza attuale di autorizzazioni in Italia, un'analisi del divario normativo (potenziale designazione di farmaco orfano EMA, framework di utilizzo off-label) sarebbe necessaria prima che qualsiasi sviluppo clinico venga avviato

---

> **⚠️ Nota sulla qualità dei dati — Rank 8 ("flood factor deficiency"):** Questo termine di malattia è probabilmente un artefatto OCR/di codifica di "blood factor deficiency". Questa entità dovrebbe essere corretta e rivalutata prima di essere inclusa in qualsiasi punteggio o presentazione normativa.
>
> **📌 Dichiarazione di esclusione di responsabilità:** Questo rapporto è a solo scopo di ricerca e non costituisce consulenza medica. Qualsiasi candidato di riutilizzo di farmaci deve subire validazione clinica prima dell'applicazione terapeutica.

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

