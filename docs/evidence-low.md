---
layout: default
title: Solo previsione del modello (L5)
nav_order: 23
permalink: /evidence-low/
description: "Candidati di livello L5 in ITTxGNN: solo previsione del modello, ancora senza prove cliniche o di letteratura."
---

# Solo previsione del modello (L5)

<!-- page-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
{% assign pd_m = site.data.drug_stats.level_counts.L5 %}
Questa pagina elenca **{{ pd_m }}** dei **{{ site.data.drug_stats.total_drugs }}** medicinali con un rapporto pubblicato su questo sito ({{ pd_m | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%). Definizione dei livelli: [Metodologia]({{ '/methodology/' | relative_url }}).
<!-- page-data:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Candidati con la sola previsione del modello e ancora senza prove sull'uomo
</p>

---

## Criteri

| Livello | Definizione | Significato clinico |
|-------|------------|------------------|
| **L5** | Solo previsione del modello | Fase ipotetica; nessuna prova sull'uomo |

---

{% assign l5_drugs = site.drugs | where: "evidence_level", "L5" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L5 ({{ l5_drugs.size }} farmaci)

| Farmaco | Indicazioni | Collegamento |
|---------|---------|------|
{% for drug in l5_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Vedi la scheda]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Esclusione di responsabilità</strong><br>
Il presente rapporto ha finalità esclusivamente di ricerca accademica e <strong>non costituisce un parere medico</strong>. Seguire sempre le indicazioni del proprio medico; non modificare mai la terapia di propria iniziativa. Qualsiasi decisione di riposizionamento di un farmaco richiede una validazione clinica completa e una revisione regolatoria.
<br><br>
<small>Revisionato da: 藥提醒科技有限公司 (yao.care)</small>
</div>
