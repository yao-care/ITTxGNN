---
layout: default
title: Prove moderate (L3-L4)
nav_order: 22
permalink: /evidence-medium/
description: "Candidati al riposizionamento dei farmaci di livello L3-L4 in ITTxGNN, sostenuti da prove osservazionali o precliniche."
---

# Prove moderate (L3-L4)

<!-- page-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
{% assign pd_m = site.data.drug_stats.level_counts.L3 | plus: site.data.drug_stats.level_counts.L4 %}
Questa pagina elenca **{{ pd_m }}** dei **{{ site.data.drug_stats.total_drugs }}** medicinali con un rapporto pubblicato su questo sito ({{ pd_m | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%). Definizione dei livelli: [Metodologia]({{ '/methodology/' | relative_url }}).
<!-- page-data:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Candidati con prove preliminari che richiedono ulteriore validazione
</p>

---

## Criteri

| Livello | Definizione | Significato clinico |
|-------|------------|------------------|
| **L3** | Studi osservazionali / ampie serie di casi | Supporto preliminare; necessita di ulteriore validazione |
| **L4** | Studi preclinici / meccanicistici | Supporto teorico; lontano dall'uso clinico |

---

{% assign l3_drugs = site.drugs | where: "evidence_level", "L3" | where_exp: "d", "d.noindex != true" | sort: "title" %}
{% assign l4_drugs = site.drugs | where: "evidence_level", "L4" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L3 ({{ l3_drugs.size }} farmaci)

| Farmaco | Indicazioni | Collegamento |
|---------|---------|------|
{% for drug in l3_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Vedi la scheda]({{ drug.url | relative_url }}) |
{% endfor %}

### L4 ({{ l4_drugs.size }} farmaci)

| Farmaco | Indicazioni | Collegamento |
|---------|---------|------|
{% for drug in l4_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Vedi la scheda]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Esclusione di responsabilità</strong><br>
Il presente rapporto ha finalità esclusivamente di ricerca accademica e <strong>non costituisce un parere medico</strong>. Seguire sempre le indicazioni del proprio medico; non modificare mai la terapia di propria iniziativa. Qualsiasi decisione di riposizionamento di un farmaco richiede una validazione clinica completa e una revisione regolatoria.
<br><br>
<small>Revisionato da: 藥提醒科技有限公司 (yao.care)</small>
</div>
