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

Questo sito pubblica rapporti su **{{ site.data.drug_stats.total_drugs }}** medicinali presenti nelle [liste AIFA dei farmaci di classe A e H](https://www.aifa.gov.it/en/liste-farmaci-a-h) (Italia); la classe C non è inclusa.

Set di dati: [AIFA: liste dei farmaci di classe A e H](https://www.aifa.gov.it/en/liste-farmaci-a-h); viene scaricato e confrontato automaticamente ogni settimana (il lunedì). Dettagli: [Fonti dei dati]({{ '/sources/' | relative_url }}).

Rapporti per livello di evidenza:

| Livello di evidenza | Rapporti | Quota |
|---|---|---|
| L1 | {{ site.data.drug_stats.level_counts.L1 }} | {{ site.data.drug_stats.level_counts.L1 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L2 | {{ site.data.drug_stats.level_counts.L2 }} | {{ site.data.drug_stats.level_counts.L2 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L3 | {{ site.data.drug_stats.level_counts.L3 }} | {{ site.data.drug_stats.level_counts.L3 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L4 | {{ site.data.drug_stats.level_counts.L4 }} | {{ site.data.drug_stats.level_counts.L4 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L5 | {{ site.data.drug_stats.level_counts.L5 }} | {{ site.data.drug_stats.level_counts.L5 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
{% assign na = site.data.drug_stats.total_drugs | minus: site.data.drug_stats.level_counts.L1 | minus: site.data.drug_stats.level_counts.L2 | minus: site.data.drug_stats.level_counts.L3 | minus: site.data.drug_stats.level_counts.L4 | minus: site.data.drug_stats.level_counts.L5 %}{% if na > 0 %}| N/A | {{ na }} | {{ na | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |{% endif %}

2 coppie farmaco–malattia previste su questo sito non compaiono in nessun altro dei 30 siti TxGNN.

### Medicinali con il livello di evidenza più alto su questo sito

| Medicinale | Livello di evidenza |
|---|---|
| [Bupropion](/drugs/bupropion/) | L1 |
| [Cefprozil](/drugs/cefprozil/) | L1 |
| [Imiquimod](/drugs/imiquimod/) | L1 |
| [Ribavirin](/drugs/ribavirin/) | L1 |
| [Clomipramine](/drugs/clomipramine/) | L1 |
| [Ketorolac](/drugs/ketorolac/) | L1 |
| [Tacrolimus](/drugs/tacrolimus/) | L1 |
| [Solriamfetol](/drugs/solriamfetol/) | L2 |
| [Flecainide](/drugs/flecainide/) | L2 |
| [Everolimus](/drugs/everolimus/) | L2 |

### Medicinali coperti solo da questo sito tra i 30 siti TxGNN

| Medicinale | Livello di evidenza |
|---|---|
| [Gliquidone](/drugs/gliquidone/) | L5 |

<!-- local-home:end -->

## Informazioni sullo Sviluppatore

Questa piattaforma è sviluppata e gestita da **藥提醒科技有限公司** (yao.care). Le informazioni sull'azienda,
il contesto del modello TxGNN e l'elenco completo dei siti della linea di prodotti si trovano nella pagina
<a href="{{ '/about/' | relative_url }}">Informazioni</a>.
