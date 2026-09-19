---
layout: default
title: Verapamil
parent: Solo previsione del modello (L5)
nav_order: 211
evidence_level: L5
indication_count: 7
---

# Verapamil
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **7** 
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

# Verapamil: da aritmia cardiaca / ipertensione a blocco di branca obsoleto

## Riassunto in una frase

Verapamil è un bloccante consolidato dei canali del calcio di tipo L (CCB) utilizzato clinicamente per la tachicardia sopraventricolare, l'angina pectoris e l'ipertensione; nessun record di autorizzazione formale dell'Italia (AIFA) è stato trovato in questo set di dati.
La principale previsione del modello TxGNN lo collega al **blocco di branca obsoleto** — un concetto clinico ritirato da SNOMED/OMOP — **senza studi clinici** e **nessuna pubblicazione di supporto** identificati.
⚠️ Questa previsione merita una cautela particolare: l'etichetta della malattia non è più in uso clinico attivo, e Verapamil è farmacologicamente considerato controindicato nel blocco di branca a causa del rischio di indurre un blocco cardiaco completo.

---

## Panoramica rapida

| Voce | Contenuto |
|------|-----------|
| Indicazione originale | Aritmia cardiaca, ipertensione, angina pectoris (basato su conoscenze farmacologiche consolidate; nessun record di licenza AIFA trovato nel set di dati) |
| Indicazione prevista nuova | Blocco di branca obsoleto |
| Punteggio di previsione TxGNN | 99.62% |
| Livello di evidenza | L5 |
| Stato del mercato italiano | ✗ Non commercializzato (nessun record AIFA trovato) |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Hold |

---

## Perché questa previsione è ragionevole?

Verapamil appartiene alla classe delle fenilalchilammine tra i bloccanti dei canali del calcio voltaggio-dipendenti di tipo L. Bloccando l'ingresso del calcio nelle cellule cardiache e della muscolatura liscia, rallenta la conduzione attraverso il nodo atrioventricolare (AV), riduce la frequenza cardiaca e la contrattilità, e dilata la vascolatura periferica. Queste proprietà supportano i suoi ruoli clinici consolidati nella tachicardia sopraventricolare (controllo della frequenza), fibrillazione atriale, angina stabile e ipertensione. I dati dettagliati del meccanismo d'azione non sono stati recuperabili dalla pipeline dei dati per questo rapporto (segnalato come data gap DG002), ma il profilo elettrofisiologico cardiaco di Verapamil è ben caratterizzato nella letteratura.

A livello superficiale, il collegamento meccanicistico al blocco di branca (BBB) esiste — Verapamil agisce sul tessuto di conduzione cardiaca, che è il substrato anatomico del BBB. Tuttavia, questa relazione è una di rischio farmacologico, non di beneficio terapeutico: il rallentamento della conduzione nodale AV in un paziente con BBB preesistente rischia una progressione verso un blocco cardiaco completo (di terzo grado), una condizione potenzialmente fatale. Le linee guida cliniche quindi elencano il BBB — specialmente il blocco bifascicolare o trifascicolare — come controindicazione o cautela ad alto rischio per l'uso di Verapamil.

Un ulteriore problema critico mina completamente questa previsione: l'etichetta della malattia porta un prefisso "obsoleto", indicando che questo concetto è stato formalmente ritirato dall'ontologia SNOMED CT / OMOP CDM. Il grafo di conoscenza TxGNN probabilmente conserva questo nodo legacy, il che potrebbe spiegare l'alto punteggio del modello. In pratica, il "blocco di branca obsoleto" non corrisponde più a nessuna categoria diagnostica attiva, e la traduzione clinica di questa previsione non è significativa.

---

## Evidenza da studi clinici

Attualmente nessuno studio clinico correlato registrato.

---

## Evidenza da letteratura

Attualmente nessuna letteratura correlata disponibile.

---

## Informazioni sul mercato italiano

Nessuna autorizzazione AIFA per Verapamil è stata identificata in questo set di dati. Il farmaco è registrato come non commercializzato in Italia secondo i record interrogati (0 licenze, dati al 2026-03-29).

> **Nota:** Verapamil (commercializzato a livello globale come Isoptin®, Calan®, Veramil® e generici) ha approvazioni normative in molti paesi per aritmia, angina e ipertensione. Si consiglia un'interrogazione mirata del database AIFA per confermare lo stato del mercato italiano prima che qualsiasi valutazione formulare o di licenza sia finalizzata.

---

## Considerazioni sulla sicurezza

Si prega di fare riferimento al foglio illustrativo per le informazioni sulla sicurezza.

> **Nota clinica derivata dall'analisi meccanicistica:** In tutte le 7 indicazioni previste in questo Evidence Pack, il `repurposing_rationale` identifica esplicitamente preoccupazioni meccanicistiche per almeno 4 previsioni:
> - **Rank 1 (Blocco di branca obsoleto):** Verapamil è relativamente controindicato — rischio di blocco cardiaco completo.
> - **Rank 4 & 5 (Ipertensione polmonare, Gruppi 3 & 5):** I CCB non sono raccomandati nell'ipertensione polmonare Gruppo 3/5; possono peggiorare il disadattamento ventilazione-perfusione nel Gruppo 3.
> - **Rank 2 (Ipertensione renovascolare maligna):** La monoterapia con CCB è meno efficace degli inibitori del RAAS nel contesto della stenosi dell'arteria renale.
>
> Gli avvertimenti completi e le controindicazioni devono essere verificati contro il foglio illustrativo una volta ottenuti via TFDA/AIFA.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Fondamento:**
La principale previsione di TxGNN si rivolge a un concetto di ontologia ritirato senza rilevanza clinica attiva; la relazione meccanicistica tra Verapamil e il blocco di branca è una di controindicazione piuttosto che di opportunità terapeutica. Nessuno studio clinico o letteratura di supporto è stato identificato per nessuna delle 7 indicazioni previste, e tutte le previsioni portano il più basso grado di evidenza (L5) con raccomandazioni unanimi di "Hold" o equivalenti.

**Per procedere, è necessario quanto segue:**

- **Risolvere lo stato del mercato italiano:** Condurre un'interrogazione diretta del database AIFA per confermare se Verapamil mantiene autorizzazioni italiane — il set di dati corrente ha restituito zero record, il che potrebbe riflettere una limitazione della query piuttosto che un'assenza genuina dal mercato italiano.
- **Ottenere i dati MOA completi:** Interrogare l'API DrugBank per colmare il data gap DG002 e abilitare una corretta analisi meccanicistica tra le indicazioni.
- **Aggiornare il mapping dell'ontologia della malattia:** Rieseguire TxGNN con un mapping SNOMED CT / OMOP CDM corrente per escludere i nodi di malattia ritirati ("obsoleti") dagli output candidati e migliorare la qualità del segnale di previsione.
- **Esplorare il rank 7 come ipotesi di ricerca:** "Paralisi periodica con sindrome simile a compartimento transitoria" (rank 7) porta la sola raccomandazione di "Domanda di ricerca" e l'ipotesi meccanicistica più plausibile (mutazioni VGCC, sovrapposizione della sindrome di Andersen-Tawil). Questo è l'unico candidato in questo rapporto che merita un'immersione profonda mirata nella letteratura prima di un hold formale.

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

