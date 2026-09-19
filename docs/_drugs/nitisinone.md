---
layout: default
title: Nitisinone
parent: Prove moderate (L3-L4)
nav_order: 155
evidence_level: L4
indication_count: 10
---

# Nitisinone
{: .fs-9 }

Livello di evidenza: **L4** | Indicazioni previste: **10** 
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

# Nitisinone: Dalla Tirossinemia Ereditaria di Tipo 1 all'Acidosi Tubulare Renale

## Riassunto in una frase

Nitisinone (NTBC) è un inibitore dell'enzima HPPD originariamente approvato per la Tirossinemia Ereditaria di Tipo 1 (HT-1), una rara malattia metabolica congenita del catabolismo della tirosina che causa danno epatico e renale progressivo.
Il modello TxGNN predice che potrebbe essere efficace per l'**Acidosi Tubulare Renale**, con **0 trial clinici** e **2 pubblicazioni** attualmente a supporto di questa direzione — entrambe le quali descrivono il recupero della funzione tubulare renale specificamente in pazienti con HT-1 trattati con NTBC, piuttosto che evidenze di efficacia nell'acidosi tubulare renale primaria.

## Panoramica Rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione Originale | Tirossinemia Ereditaria di Tipo 1 (HT-1) — derivata da contesto clinico; nessuna registrazione italiana in archivio |
| Indicazione Prevista | Acidosi Tubulare Renale |
| Punteggio di Previsione TxGNN | 99.96% |
| Livello di Evidenza | L4 |
| Stato del Mercato Italiano | Non commercializzato |
| Numero di Autorizzazioni | 0 |
| Decisione Consigliata | Sospendere |

## Perché questa Previsione è Ragionevole?

Attualmente, i dati dettagliati del meccanismo d'azione non sono disponibili in questo pacchetto di evidenze. Sulla base della farmacologia nota, nitisinone inibisce la **4-idrossifenil piruvato diossigenasi (HPPD)**, un enzima del percorso di degradazione della tirosina. Nell'HT-1, un enzima a valle difettoso (fumarilacetoacetato idrolasi, FAH) causa l'accumulo di metaboliti tossici — principalmente **succinylacetone** —. Bloccando HPPD a monte, nitisinone previene la produzione di succinylacetone e arresta la cascata del danno epatico e renale.

Il collegamento previsto all'acidosi tubulare renale deriva dal fenotipo renale dell'HT-1: succinylacetone danneggia direttamente i tubuli renali prossimali, producendo sindrome di Fanconi secondaria con caratteristiche di acidosi tubulare. Le osservazioni cliniche confermano che la terapia con NTBC migliora questa disfunzione tubulare nei pazienti con HT-1 — spiegando perché il grafo di conoscenza TxGNN ha collegato nitisinone al nodo di acidosi tubulare renale.

Tuttavia, questo ponte meccanicistico è **strettamente specifico per l'HT-1**. L'acidosi tubulare renale primaria (guidata da mutazioni in SLC4A1, ATP6V1B1, CA2 o altri trasportatori tubulari) non ha alcun percorso metabolico a monte condiviso con l'HT-1. Nitisinone non offre alcuna razionale farmacologica contro l'acidosi tubulare renale primaria. La previsione TxGNN molto probabilmente riflette una vicinanza condivisa nel grafo ("accumulo di metaboliti tossici → danno tubulare") piuttosto che un genuino nuovo percorso indicativo.

## Evidenze da Trial Clinici

Attualmente nessun trial clinico correlato registrato.

## Evidenze da Letteratura

| PMID | Anno | Tipo | Rivista | Risultati Principali |
|------|------|------|---------|----------------------|
| [25172236](https://pubmed.ncbi.nlm.nih.gov/25172236/) | 2014 | Studio Osservazionale | Molecular Genetics and Metabolism | Follow-up prospettico in pazienti con HT-1 che mostra che la terapia con NTBC produce un miglioramento precoce e misurabile della disfunzione tubulare renale prossimale (marcatori della sindrome di Fanconi) entro settimane dall'inizio del trattamento |
| [27109516](https://pubmed.ncbi.nlm.nih.gov/27109516/) | 2016 | Serie di Casi | Indian Journal of Gastroenterology | Quattro casi pediatrici di HT-1 trattati con NTBC: tre mantennero la funzione epatica normale, succinylacetone non rilevabile nelle urine, e nessun segno di ipertensione portale o disfunzione tubulare renale residua dopo ~3 anni di terapia |

> **Nota:** Entrambe le pubblicazioni riportano gli esiti renali come risultati secondari nella gestione dell'HT-1, non come studi autonomi di nitisinone nell'acidosi tubulare renale.

## Informazioni sul Mercato Italiano

Nitisinone non è registrato in Italia. Nessuna autorizzazione al commercio è in archivio. Orfadin® (la formulazione brandizzata) detiene designazione di farmaco orfano EMA ed è approvato nell'UE per l'HT-1, ma i dati di autorizzazione specifici per l'Italia non erano disponibili in questo pacchetto di evidenze.

## Considerazioni sulla Sicurezza

Si prega di fare riferimento al foglio illustrativo per le informazioni sulla sicurezza.

## Conclusione e Passi Successivi

**Decisione: Sospendere**

**Razionale:**
La previsione TxGNN per l'acidosi tubulare renale è biologicamente spiegabile, ma solo nel contesto della malattia HT-1 — entrambe le pubblicazioni di supporto descrivono miglioramento renale secondario in pazienti con HT-1, non attività terapeutica contro l'acidosi tubulare renale primaria o idiopatica. Senza un meccanismo plausibile al di fuori dell'HT-1 e con zero trial clinici registrati, questa indicazione non giustifica uno sviluppo attivo come bersaglio terapeutico.

**Per procedere, è necessario:**

- Un'ipotesi meccanicistica per l'attività di NTBC nell'acidosi tubulare renale primaria (ad es., trasportopatie ereditarie o acidosi tubulare renale secondaria tossica da altre cause metaboliche)
- Identificazione di sottotipi di acidosi tubulare renale dove i metaboliti tossici della tirosina, o un blocco di enzima analogo a monte, potrebbero essere operativi
- Dati preclinici (cellulari o modelli animali di acidosi tubulare renale primaria) che testano nitisinone
- Recupero del foglio illustrativo completo (TFDA / SmPC EMA) per valutare controindicazioni, avvertenze chiave e interazioni farmacologiche prima che possa procedere qualsiasi valutazione di sicurezza
- Revisione di esperti da parte di uno specialista di malattie metaboliche per valutare la plausibilità predetta dal grafo rispetto alla realtà clinica

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

