---
layout: default
title: Prove moderate (L3-L4)
nav_order: 22
permalink: /evidence-medium/
description: "41 medicinali con livello di evidenza L3–L4 su questo sito (Italia), ad es. Calcipotriol, Citalopram, Clobetasol, con indicazione principale prevista, confezioni AIFA (AIC) e verifiche per ciascuno."
---

# Prove moderate (L3-L4)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
Questa pagina elenca **{{ site.data.evidence_tier_facts.medium.count }}** dei **{{ site.data.drug_stats.total_drugs }}** medicinali con un rapporto pubblicato su questo sito ({{ site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%): L3 **{{ site.data.evidence_tier_facts.medium.by_level.L3 }}**, L4 **{{ site.data.evidence_tier_facts.medium.by_level.L4 }}**.
Quota mediana dei livelli L3–L4 nei 30 siti TxGNN: {{ site.data.evidence_tier_facts.medium.cross.median_share }}%. {% if ev_share > site.data.evidence_tier_facts.medium.cross.median_share %}Questo sito è sopra la mediana.{% elsif ev_share < site.data.evidence_tier_facts.medium.cross.median_share %}Questo sito è sotto la mediana.{% else %}Questo sito è alla mediana.{% endif %}

{% if site.data.evidence_tier_facts.medium.count > 0 %}
Nei dati locali (confezioni AIFA (AIC)), **{{ site.data.evidence_tier_facts.medium.with_current }}** di questi medicinali hanno almeno una confezione autorizzate, **{{ site.data.evidence_tier_facts.medium.none_current }}** hanno confezioni ma nessuna autorizzate e **{{ site.data.evidence_tier_facts.medium.without_data }}** non figurano nei dati locali. **{{ site.data.evidence_tier_facts.medium.with_reviews }}** hanno voci nel registro delle verifiche (correzioni dei dati regolatori nella pagina del medicinale). **{{ site.data.evidence_tier_facts.medium.cross.unique_drugs }}** hanno un'indicazione prevista che nessun altro sito TxGNN riporta per lo stesso medicinale.
{% if site.data.evidence_tier_facts.medium.none_current_list.size > 0 %}

Con confezioni, ma nessuna autorizzate: {% for r in site.data.evidence_tier_facts.medium.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}
{% endif %}

Definizione di tutti i livelli: [Metodologia]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

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

### L3 ({{ site.data.evidence_tier_facts.medium.by_level.L3 }} farmaci)

<!-- tier-table:start L3（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Medicinale | Livello | Principale nuova indicazione prevista | confezioni AIFA (AIC): autorizzate / totale | Registro verifiche | Solo su questo sito |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.medium.rows %}{% if r.l == "L3" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}sì ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

### L4 ({{ site.data.evidence_tier_facts.medium.by_level.L4 }} farmaci)

<!-- tier-table:start L4（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Medicinale | Livello | Principale nuova indicazione prevista | confezioni AIFA (AIC): autorizzate / totale | Registro verifiche | Solo su questo sito |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.medium.rows %}{% if r.l == "L4" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}sì ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

<div class="disclaimer">
<strong>Esclusione di responsabilità</strong><br>
Il presente rapporto ha finalità esclusivamente di ricerca accademica e <strong>non costituisce un parere medico</strong>. Seguire sempre le indicazioni del proprio medico; non modificare mai la terapia di propria iniziativa. Qualsiasi decisione di riposizionamento di un farmaco richiede una validazione clinica completa e una revisione regolatoria.
<br><br>
<small>Revisionato da: 藥提醒科技有限公司 (yao.care)</small>
</div>
