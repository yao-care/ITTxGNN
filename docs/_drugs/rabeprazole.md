---
layout: default
title: Rabeprazole
parent: Solo previsione del modello (L5)
nav_order: 371
evidence_level: L5
indication_count: 2
---

# Rabeprazole
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **2** 
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

# Rabeprazolo: dalla malattia da reflusso gastroesofageo alla mastocitosi sistemica indolente (smouldering)

## Sintesi

Rabeprazolo è un inibitore di pompa protonica (PPI) utilizzato per ulcera peptica, malattia da reflusso gastroesofageo ed esofagite. Il modello TxGNN prevede una possibile efficacia nella **mastocitosi sistemica smouldering**, con un punteggio molto alto (99,44%). Al momento **non risultano studi clinici né pubblicazioni** a supporto: si tratta di una predizione puramente computazionale.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Malattia ulcerosa peptica, malattia da reflusso gastroesofageo, esofagite, ulcera duodenale, sindrome di Zollinger-Ellison (il testo delle indicazioni nelle autorizzazioni AIFA non è disponibile; elenco tratto dal knowledge graph) |
| Nuova indicazione prevista | Mastocitosi sistemica smouldering |
| Punteggio di predizione TxGNN | 99,44% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 20 (tutte cancellate) |
| Decisione raccomandata | Hold |

---

## Perché questa predizione è plausibile?

I dati compilati per questo report non contengono il meccanismo d'azione registrato del farmaco. Si può comunque dire che rabeprazolo, come PPI, riduce la secrezione acida gastrica inibendo la pompa protonica.

Nella mastocitosi sistemica, i mediatori dei mastociti (in particolare l'istamina) causano iperacidità gastrica e sintomi gastrointestinali. La soppressione acida è già una terapia sintomatica consolidata e la mastocitosi è già tra le indicazioni originali associate al farmaco nel knowledge graph.

Va però chiarito che l'effetto atteso sarebbe **di controllo dei sintomi** (ipersecrezione acida), non modificante la malattia clonale dei mastociti. Il punteggio elevato riflette verosimilmente la vicinanza alle indicazioni di mastocitosi già presenti nel grafo, più che nuove evidenze per questo specifico sottotipo. Il collegamento meccanicistico non ha potuto essere verificato rispetto a dati di bersaglio farmacologico.

Una seconda predizione, la **mastocitosi linfoadenopatica con eosinofilia** (punteggio 99,35%), segue lo stesso ragionamento: eventuale uso solo come terapia di supporto accanto alle terapie dirette contro la malattia. Anche qui non vi sono studi o letteratura.

---

## Evidenze da studi clinici

Attualmente non risultano studi clinici correlati registrati.

---

## Evidenze dalla letteratura

Attualmente non risulta letteratura correlata disponibile.

---

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate; non vi sono autorizzazioni valide. Il testo delle indicazioni approvate e la forma farmaceutica non sono riportati nei dati. Esempi delle principali autorizzazioni:

| N. autorizzazione | Nome prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 034216022 | PARIET 14 cpr gastroresistenti 10 mg | Janssen Cilag SpA | Cancellata |
| 041599186 | Rabeprazolo 28 cpr gastroresistenti 20 mg | Zentiva Italia Srl | Cancellata |
| 041110141 | Rabeprazolo 28 cpr gastroresistenti 20 mg | Sandoz SpA | Cancellata |
| 041984016 | AKIRAB 14 cpr gastroresistenti 10 mg | So.Se.Pharm Srl | Cancellata |
| 041970029 | RABEX 14 cpr gastroresistenti 20 mg | S.F. Group Srl | Cancellata |

---

## Considerazioni di sicurezza

- **Controindicazioni segnalate nel knowledge graph** (non derivate dal foglietto illustrativo): malattia epatica, malattia della colecisti, osteoporosi, osteoporosi postmenopausale, frattura ossea.
- **Interazioni farmacologiche**: sono state identificate 486 interazioni. Tra quelle di livello **maggiore** figurano **acalabrutinib** e **atazanavir**. Tra quelle di livello moderato: amikacina, amfotericina B (varie formulazioni), anfetamina, aprepitant, armodafinil, apalutamide, bosutinib, bendroflumetiazide e benztiazide. Un'interazione minore è riportata con acido acetilsalicilico e assitinib.

Per le avvertenze e le controindicazioni ufficiali, consultare il foglietto illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione è solo computazionale (L5), senza studi né pubblicazioni, e il beneficio atteso sarebbe limitato al controllo sintomatico dell'iperacidità. In più, in Italia non vi sono attualmente autorizzazioni valide.

**Per procedere sono necessari:**
- Scaricare e analizzare il foglietto illustrativo AIFA per avvertenze e controindicazioni
- Dati sul meccanismo d'azione da DrugBank
- Revisione della letteratura sull'uso dei PPI nella mastocitosi come terapia di supporto
- Verifica dello stato regolatorio e della disponibilità commerciale in Italia
- Valutazione delle interazioni di livello maggiore (acalabrutinib, atazanavir), rilevanti per i pazienti oncoematologici
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

