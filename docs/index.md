---
layout: default
title: Previsioni di Riposizionamento dei Farmaci
nav_order: 1
description: "Previsioni di riposizionamento dei farmaci basate sull'IA per l'Italia. Analisi basata sulle evidenze di possibili nuove indicazioni terapeutiche dei farmaci autorizzati."
permalink: /
---

# Previsioni di Riposizionamento dei Farmaci — Italia

Questo progetto utilizza il modello TxGNN (apprendimento profondo) per prevedere potenziali nuovi utilizzi terapeutici per i farmaci approvati in Italia.

**Esclusione di Responsabilità**: Questo contenuto è solo a scopo di ricerca e non costituisce consulenza medica. Tutte le previsioni di riposizionamento dei farmaci richiedono la validazione clinica prima dell'applicazione.

---

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## Italia: cosa copre questo sito

Questo sito pubblica rapporti su **{{ site.data.drug_stats.total_drugs }}** medicinali presenti nei dati di autorizzazione ([AIFA](https://www.aifa.gov.it/), Italia).

Rapporti per livello di evidenza: L1 {{ site.data.drug_stats.level_counts.L1 }} · L2 {{ site.data.drug_stats.level_counts.L2 }} · L3 {{ site.data.drug_stats.level_counts.L3 }} · L4 {{ site.data.drug_stats.level_counts.L4 }} · L5 {{ site.data.drug_stats.level_counts.L5 }}

### Medicinali con il livello di evidenza più alto su questo sito

| Medicinale | Livello di evidenza |
|---|---|
| [Bupropion](/drugs/bupropion/) | L1 |
| [Cefprozil](/drugs/cefprozil/) | L1 |
| [Imiquimod](/drugs/imiquimod/) | L1 |
| [Lanadelumab](/drugs/lanadelumab/) | L1 |
| [Oteracil](/drugs/oteracil/) | L1 |
| [Rifabutin](/drugs/rifabutin/) | L1 |
| [Solriamfetol](/drugs/solriamfetol/) | L1 |
| [Tegafur](/drugs/tegafur/) | L1 |
| [Ribavirin](/drugs/ribavirin/) | L1 |
| [Clomipramine](/drugs/clomipramine/) | L1 |

### Medicinali coperti solo da questo sito tra i 30 siti TxGNN

| Medicinale | Livello di evidenza |
|---|---|
| [Gliquidone](/drugs/gliquidone/) | L5 |

<!-- local-home:end -->

## Informazioni sullo Sviluppatore

Questa piattaforma è sviluppata e gestita da **藥提醒科技有限公司** (yao.care, numero di registrazione
societaria 83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

ITTxGNN è il sito italiano della linea di prodotti "TxGNN Drug Repurposing" dell'azienda.
Lo stesso sistema è distribuito in 30 paesi e regioni, ciascuno denominato `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN e così via) all'indirizzo `{cc}txgnn.yao.care`.
Panoramica del prodotto: <https://www.yao.care/medical/txgnn/>.

Il modello TxGNN è stato sviluppato dallo Zitnik Lab della Harvard Medical School ed è stato pubblicato
su *Nature Medicine*. Questa piattaforma è il sistema di produzione che 藥提醒科技有限公司 ha costruito
su tale modello e comprende l'integrazione dei dati nazionali di registrazione dei farmaci, la previsione tramite deep learning che esclude gli usi già registrati nel grafo di conoscenza, la classificazione delle prove da
PubMed / ClinicalTrials e l'integrazione con le cartelle cliniche elettroniche tramite SMART on FHIR.
