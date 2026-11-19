---
layout: default
title: Prove elevate (L1-L2)
nav_order: 21
permalink: /evidence-high/
description: "20 medicinali con livello di evidenza L1–L2 su questo sito (Italia), ad es. Bupropion, Cefprozil, Clomipramine, con indicazione principale prevista, confezioni AIFA (AIC) e verifiche per ciascuno."
---

# Prove elevate (L1-L2)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.high.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
Questa pagina elenca **{{ site.data.evidence_tier_facts.high.count }}** dei **{{ site.data.drug_stats.total_drugs }}** medicinali con un rapporto pubblicato su questo sito ({{ site.data.evidence_tier_facts.high.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%): L1 **{{ site.data.evidence_tier_facts.high.by_level.L1 }}**, L2 **{{ site.data.evidence_tier_facts.high.by_level.L2 }}**.
Quota mediana dei livelli L1–L2 nei 30 siti TxGNN: {{ site.data.evidence_tier_facts.high.cross.median_share }}%. {% if ev_share > site.data.evidence_tier_facts.high.cross.median_share %}Questo sito è sopra la mediana.{% elsif ev_share < site.data.evidence_tier_facts.high.cross.median_share %}Questo sito è sotto la mediana.{% else %}Questo sito è alla mediana.{% endif %}

{% if site.data.evidence_tier_facts.high.count > 0 %}
Nei dati locali (confezioni AIFA (AIC)), **{{ site.data.evidence_tier_facts.high.with_current }}** di questi medicinali hanno almeno una confezione autorizzate, **{{ site.data.evidence_tier_facts.high.none_current }}** hanno confezioni ma nessuna autorizzate e **{{ site.data.evidence_tier_facts.high.without_data }}** non figurano nei dati locali. **{{ site.data.evidence_tier_facts.high.with_reviews }}** hanno voci nel registro delle verifiche (correzioni dei dati regolatori nella pagina del medicinale). **{{ site.data.evidence_tier_facts.high.cross.unique_drugs }}** hanno un'indicazione prevista che nessun altro sito TxGNN riporta per lo stesso medicinale.
{% if site.data.evidence_tier_facts.high.none_current_list.size > 0 %}

Con confezioni, ma nessuna autorizzate: {% for r in site.data.evidence_tier_facts.high.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}
{% endif %}

Definizione di tutti i livelli: [Metodologia]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Candidati che possono essere considerati prioritari per la valutazione clinica
</p>

Quali di questi farmaci hanno evidenze da studi per la nuova indicazione prevista e quanti studi registrati sono citati? Vedere [Farmaci di classe A e H con evidenze da studi clinici per una nuova indicazione]({{ '/clinical-trial-evidence/' | relative_url }}).

---

## Criteri

| Livello | Definizione | Significato clinico |
|-------|------------|------------------|
| **L1** | Più RCT di Fase 3 / revisioni sistematiche | Supporto forte; l'uso clinico può essere preso in considerazione |
| **L2** | Un singolo RCT o più studi di Fase 2 | Supporto moderato; è possibile progettare studi di validazione |

---

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | where_exp: "d", "d.noindex != true" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L1 ({{ site.data.evidence_tier_facts.high.by_level.L1 }} farmaci)

<!-- tier-table:start L1（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Medicinale | Livello | Principale nuova indicazione prevista | confezioni AIFA (AIC): autorizzate / totale | Registro verifiche | Solo su questo sito |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.high.rows %}{% if r.l == "L1" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}sì ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

### L2 ({{ site.data.evidence_tier_facts.high.by_level.L2 }} farmaci)

<!-- tier-table:start L2（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Medicinale | Livello | Principale nuova indicazione prevista | confezioni AIFA (AIC): autorizzate / totale | Registro verifiche | Solo su questo sito |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.high.rows %}{% if r.l == "L2" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}sì ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

<div class="disclaimer">
<strong>Esclusione di responsabilità</strong><br>
Il presente rapporto ha finalità esclusivamente di ricerca accademica e <strong>non costituisce un parere medico</strong>. Seguire sempre le indicazioni del proprio medico; non modificare mai la terapia di propria iniziativa. Qualsiasi decisione di riposizionamento di un farmaco richiede una validazione clinica completa e una revisione regolatoria.
<br><br>
<small>Revisionato da: 藥提醒科技有限公司 (yao.care)</small>
</div>
