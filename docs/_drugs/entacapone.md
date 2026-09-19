---
layout: default
title: Entacapone
parent: Solo previsione del modello (L5)
nav_order: 92
evidence_level: L5
indication_count: 10
---

# Entacapone
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

# Entacapone: dalla Malattia di Parkinson alla Neurodegenrazione Associata a PLA2G6

## Riassunto in una Frase

L'entacapone è un inibitore della catecolo-O-metiltransferasi (COMT), farmaco clinicamente consolidato come adiuvante della terapia con levodopa/carbidopa negli adulti con malattia di Parkinson che presentano episodi "off".
Il modello TxGNN predice che possa essere efficace nella **Neurodegenrazione Associata a PLA2G6 (PLAN)**, un raro disturbo neurodegenerativo con accumulo di ferro che presenta caratteristiche simili al Parkinson.
Attualmente, **nessuno studio clinico** e **nessuna letteratura pubblicata** supportano questa specifica direzione di ripurposing — rimane una predizione solo da modello.

---

## Panoramica Rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione Originale | Malattia di Parkinson (adiuvante della levodopa, per la gestione dei periodi "off") |
| Indicazione Predetta | Neurodegenrazione Associata a PLA2G6 (PLAN) |
| Punteggio di Predizione TxGNN | 99.76% |
| Livello di Evidenza | L5 |
| Stato di Mercato Italia | Non commercializzato |
| Numero di Autorizzazioni | 0 |
| Decisione Consigliata | In Sospeso |

---

## Perché questa Predizione è Ragionevole?

Attualmente, i dati dettagliati sul meccanismo d'azione non sono disponibili dall'Evidence Pack. Sulla base delle conoscenze farmacologiche consolidate, l'entacapone è un inibitore selettivo e reversibile della COMT periferica. Bloccando la degradazione enzimatica della levodopa nel sangue, aumenta la frazione di ogni dose di levodopa che attraversa la barriera emato-encefalica e viene convertita in dopamina nella via nigrostriatale. Nella malattia di Parkinson, questo estende la durata dell'effetto terapeutico della levodopa e riduce le fluttuazioni motorie ("wearing-off").

La Neurodegenrazione Associata a PLA2G6 (PLAN) è causata da mutazioni loss-of-function nel gene *PLA2G6* che codifica la fosfolipasi A2, un sottotipo di Neurodegenrazione con Accumulo di Ferro Cerebrale (NBIA). Un sottogruppo clinicamente significativo di pazienti con PLAN — in particolare quelli con fenotipo Parkinson ad esordio nell'adulto — presenta degenerazione dopaminergica nigrostriatale indistinguibile dalla malattia di Parkinson idiopatica. Questa vulnerabilità neuroanatomica condivisa è la base più plausibile per la predizione TxGNN.

Tuttavia, la somiglianza fenotipica non equivale all'equivalenza terapeutica. Il deficit dopaminergico in PLAN nasce da una causa a monte fondamentalmente diversa (disregolazione della membrana fosfolipidica e tossicità del ferro) piuttosto che dalla patologia dell'α-sinucleina aggregata. Se i sintomi motori dei pazienti con PLAN siano responsivi alla levodopa — un prerequisito affinché l'inibizione della COMT aggiunga qualche beneficio — è incoerente nei case report pubblicati. Il punteggio TxGNN molto probabilmente riflette il clustering di prossimità nel grafo di conoscenza tra i nodi PLAN e Parkinson classico, non evidenza meccanicistica diretta. Al presente, questa connessione è puramente ipotetica.

---

## Evidenza da Studi Clinici

Attualmente nessuno studio clinico registrato correlato all'entacapone nella neurodegenrazione associata a PLA2G6.

---

## Evidenza dalla Letteratura

Attualmente nessuna letteratura disponibile correlata all'entacapone nella neurodegenrazione associata a PLA2G6.

---

## Informazioni di Mercato Italia

L'entacapone non ha autorizzazioni di commercializzazione approvate in Italia e non è attualmente disponibile sul mercato italiano.

---

## Considerazioni di Sicurezza

Si prega di fare riferimento al foglio illustrativo per informazioni sulla sicurezza.

---

## Conclusioni e Prossimi Passi

**Decisione: In Sospeso**

**Razionale:**
Nonostante un alto punteggio di predizione TxGNN (99.76%), questo punteggio riflette la sovrapposizione fenotipica nel grafo di conoscenza tra PLAN e malattia di Parkinson — non l'evidenza terapeutica effettiva. Non esiste alcun dato clinico, osservazionale o preclinico che valuti specificamente l'entacapone in PLAN, e il collegamento meccanicistico è al massimo indiretto.

**Per procedere, è necessario il seguente:**

- **Dati su MOA**: Recuperare il meccanismo d'azione completo dall'API DrugBank (attualmente mancante; blocca l'analisi di plausibilità meccanicistica)
- **Dati di sicurezza**: Ottenere il foglio illustrativo approvato da EMA/AIFA per valutare controindicazioni e avvertenze chiave prima di qualsiasi ulteriore valutazione
- **Dati di responsività alla levodopa in PLAN**: Revisione sistematica dei case report pubblicati su PLAN per determinare quale proporzione di pazienti con fenotipo ad esordio nell'adulto risponde alla levodopa — questo è il gate di prerequisito affinché l'inibizione della COMT sia clinicamente rilevante
- **Segnale preclinico**: Identificare qualsiasi studio in vitro o su modelli animali che utilizzi l'inibizione della COMT in modelli knockout di NBIA/PLA2G6
- **Consulenza di esperti**: Neurologo specializzato in disturbi del movimento rari per valutare la plausibilità clinica prima dell'investimento di risorse

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

