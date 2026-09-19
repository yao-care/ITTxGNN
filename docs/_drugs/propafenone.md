---
layout: default
title: Propafenone
parent: Solo previsione del modello (L5)
nav_order: 173
evidence_level: L5
indication_count: 8
---

# Propafenone
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **8** 
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

# Propafenone: Dall'aritmia cardiaca al disturbo bipolare affettivo maniacale

## Sintesi in una frase

Propafenone è un farmaco antiaritmico di classe IC utilizzato in clinica per gestire le aritmie cardiache, inclusa la fibrillazione atriale e la tachicardia ventricolare.
Il modello TxGNN prevede che potrebbe essere efficace per il **disturbo bipolare affettivo maniacale**, con **0 trial clinici** e **3 pubblicazioni** nel set di dati — tuttavia, queste pubblicazioni descrivono eventi avversi e interazioni farmacologiche piuttosto che qualsiasi uso terapeutico.
In questa fase, questa previsione è considerata biologicamente implicabile e la raccomandazione complessiva è **Sospendere**.

---

## Panoramica rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione originale | Aritmia cardiaca (farmaco antiaritmico di classe IC; nessun record normativo italiano disponibile) |
| Nuova indicazione prevista | Disturbo bipolare affettivo maniacale |
| Punteggio di previsione TxGNN | 99.80% |
| Livello di evidenza | L5 |
| Stato del mercato italiano | ✗ Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Sospendere |

---

## Perché questa previsione è ragionevole?

Attualmente, i dati dettagliati del meccanismo d'azione non sono disponibili in questo Evidence Pack. In base alla farmacologia nota, propafenone è un farmaco antiaritmico di classe IC che blocca principalmente i canali del sodio cardiaci (Nav1.5). Possiede inoltre un blando blocco adrenergico beta e deboli proprietà antagoniste dei canali del calcio. Crucialmente, la sua penetrazione nel SNC è molto bassa a causa dell'insufficiente lipofilicità — e nessun meccanismo noto di stabilizzazione dell'umore o anti-maniacale è stato identificato per questo farmaco.

L'aritmia cardiaca e il disturbo bipolare affettivo maniacale sono condizioni meccanisticamente non correlate. Il modello TxGNN sembra aver identificato erroneamente un segnale di co-occorrenza nel suo grafo della conoscenza: la letteratura "di supporto" disponibile descrive propafenone *causante* mania come un evento avverso (PMID 2579063) e documenta interazioni dannose tra farmaci cardiovascolari e antipsicotici (PMID 32124390) — non evidenza di beneficio terapeutico nel disturbo bipolare. Questo è un noto modo di fallimento nei modelli basati su grafi, dove la direzione causale tra un nodo farmaco e un nodo malattia non è adeguatamente risolta.

In sintesi, questa previsione di rango 1 non ha una razionale biologicamente plausibile. Il modello ha confuso una relazione di evento avverso (propafenone → mania) con una terapeutica. Nessuna investigazione aggiuntiva per questa indicazione è consigliata.

---

## Evidenza da trial clinici

Attualmente nessun trial clinico correlato è registrato.

---

## Evidenza da letteratura

> ⚠️ **Avvertenza importante**: Le pubblicazioni seguenti **non** supportano propafenone come trattamento per il disturbo bipolare. Documentano eventi avversi e interazioni farmacologiche. Appaiono in questo set di dati perché propafenone e disturbo bipolare co-occorrono in un contesto di sicurezza, non terapeutico.

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|------|------|---------|--------|
| [32124390](https://pubmed.ncbi.nlm.nih.gov/32124390/) | 2020 | Revisione | Pharmacological Reports | Valuta le interazioni dannose tra antipsicotici e farmaci cardiovascolari; non supporta propafenone come trattamento per il disturbo bipolare |
| [11949740](https://pubmed.ncbi.nlm.nih.gov/11949740/) | 2001 | Case Report | Int J Psychiatry in Medicine | Riporta un caso di psicosi organica risultante da un'interazione farmacologica venlafaxina–propafenone in un paziente bipolare — questo è un evento avverso, non un'applicazione terapeutica |
| [2579063](https://pubmed.ncbi.nlm.nih.gov/2579063/) | 1985 | Case Report | J Clin Psychiatry | Descrive mania indotta dall'amministrazione di propafenone; nota la somiglianza chimica con bupropione (antidepressivo) come possibile meccanismo degli effetti collaterali psichiatrici |

---

## Considerazioni sulla sicurezza

Si prega di fare riferimento al foglio illustrativo per informazioni sulla sicurezza.

---

## Sintesi di tutte le indicazioni previste

Per contesto, la seguente tabella riassume tutte le 8 indicazioni previste da TxGNN e il loro stato di evidenza:

| Rango | Malattia | Punteggio TxGNN | Livello di evidenza | Decisione |
|-------|---------|-----------------|-------------------|----------|
| 1 | Disturbo bipolare affettivo maniacale | 99.80% | L5 | **Sospendere** — evento avverso interpretato erroneamente come terapeutico |
| 2 | Tachicardia ventricolare polimorca catecolaminergica (CPVT) | 99.79% | L3 | **Procedere con criteri di sicurezza** — meccanismo di inibizione diretta RyR2; 9 pubblicazioni |
| 3 | Paralisi periodica con sindrome compartimentale transitoria | 99.67% | L5 | **Sospendere** — mancata selettività del canale (Nav1.5 vs Nav1.4) |
| 4 | Angina di Prinzmetal | 99.45% | L5 | **Sospendere** — gli agenti di classe IC possono peggiorare l'aritmia correlata all'ischemia |
| 5 | Tachicardia ventricolare incessante nell'infanzia | 99.44% | L3 | **Procedere con criteri di sicurezza** — uso pediatrico registrato dal 1987; 5 pubblicazioni |
| 6 | Cardiomiopatia aritmogena del ventricolo destro (ARVC) | 99.42% | L3 | **Domanda di ricerca** — rischio proaritmico nella malattia cardiaca strutturale; 12 pubblicazioni |
| 7 | Sindrome nefrogena di inappropriata antidiuresi (NSIAD) | 99.23% | L5 | **Sospendere** — nessuna intersezione meccanistica |
| 8 | Tricotillomania | 99.17% | L5 | **Sospendere** — farmaco cardiaco periferico; penetrazione nel SNC trascurabile |

Il candidato al riposizionamento **più scientificamente convincente** è **CPVT (Rango 2)**: propafenone inibisce direttamente i canali di rilascio del calcio RyR2 — il driver patologico primario in CPVT — mentre il suo blocco Nav1.5 e le proprietà blande di blocco beta forniscono soppressione complementare delle aritmie triggeriate.

---

## Conclusione e prossimi passi

**Decisione: Sospendere** *(per il Rango 1: Disturbo bipolare affettivo maniacale)*

**Razionale:**
La previsione di rango 1 di TxGNN è biologicamente implicabile. La penetrazione del SNC molto bassa di propafenone, l'assenza di qualsiasi via di stabilizzazione dell'umore e il fatto che l'unica letteratura disponibile documenta propafenone *causante* effetti avversi psichiatrici collettivamente rendono questo un chiaro falso positivo. Il modello sembra aver invertito la direzione causale di una nota reazione avversa ai farmaci.

**Per procedere con ulteriore valutazione:**
- **Non perseguire** il disturbo bipolare affettivo maniacale come target di riposizionamento per propafenone
- **Pivot consigliato**: Avviare una sintesi completa di evidenza per **CPVT (Rango 2)**, che ha fondamenti meccanistici (inibizione RyR2, PMID 21270101, 26121139), supporto da coorti osservazionali e un rapporto di caso a lungo termine di trattamento di successo di 35 anni (PMID 30820400)
- **Ottenere foglio illustrativo / dati normativi**: Recuperare le informazioni di prescrizione dell'Italia (AIFA) e di Taiwan (TFDA) per colmare il divario nei dati di sicurezza prima di qualsiasi pianificazione clinica
- **Ottenere documentazione formale del meccanismo d'azione**: Consultare l'API di DrugBank per DB01182 per completare l'analisi del meccanismo d'azione
- **Per ARVC (Rango 6)**: Commissionare una revisione sistematica della sicurezza che esamini specificamente il rischio proaritmico degli agenti di classe IC nella malattia cardiaca strutturale prima di procedere ulteriormente

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

