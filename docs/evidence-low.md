---
layout: default
title: Solo previsione del modello (L5)
nav_order: 23
permalink: /evidence-low/
description: "358 medicinali con livello di evidenza L5 su questo sito (Italia), ad es. Anastrozole, Aripiprazole, Bisoprolol, con indicazione principale prevista, confezioni AIFA (AIC) e verifiche per ciascuno."
---

# Solo previsione del modello (L5)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.low.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
Questa pagina elenca **{{ site.data.evidence_tier_facts.low.count }}** dei **{{ site.data.drug_stats.total_drugs }}** medicinali con un rapporto pubblicato su questo sito ({{ site.data.evidence_tier_facts.low.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%): L5 **{{ site.data.evidence_tier_facts.low.by_level.L5 }}**.
Quota mediana dei livelli L5 nei 30 siti TxGNN: {{ site.data.evidence_tier_facts.low.cross.median_share }}%. {% if ev_share > site.data.evidence_tier_facts.low.cross.median_share %}Questo sito è sopra la mediana.{% elsif ev_share < site.data.evidence_tier_facts.low.cross.median_share %}Questo sito è sotto la mediana.{% else %}Questo sito è alla mediana.{% endif %}

{% if site.data.evidence_tier_facts.low.count > 0 %}
Nei dati locali (confezioni AIFA (AIC)), **{{ site.data.evidence_tier_facts.low.with_current }}** di questi medicinali hanno almeno una confezione autorizzate, **{{ site.data.evidence_tier_facts.low.none_current }}** hanno confezioni ma nessuna autorizzate e **{{ site.data.evidence_tier_facts.low.without_data }}** non figurano nei dati locali. **{{ site.data.evidence_tier_facts.low.with_reviews }}** hanno voci nel registro delle verifiche (correzioni dei dati regolatori nella pagina del medicinale). **{{ site.data.evidence_tier_facts.low.cross.unique_drugs }}** hanno un'indicazione prevista che nessun altro sito TxGNN riporta per lo stesso medicinale.
{% if site.data.evidence_tier_facts.low.none_current_list.size > 0 %}

Con confezioni, ma nessuna autorizzate: {% for r in site.data.evidence_tier_facts.low.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}

I medicinali con una confezione locale autorizzate sono elencati per primi.
{% endif %}

Definizione di tutti i livelli: [Metodologia]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

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

### L5 ({{ site.data.evidence_tier_facts.low.by_level.L5 }} farmaci)

<!-- tier-table:start L5（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Medicinale | Livello | Principale nuova indicazione prevista | confezioni AIFA (AIC): autorizzate / totale | Registro verifiche | Solo su questo sito |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.low.rows %}{% if r.l == "L5" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}sì ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

<div class="disclaimer">
<strong>Esclusione di responsabilità</strong><br>
Il presente rapporto ha finalità esclusivamente di ricerca accademica e <strong>non costituisce un parere medico</strong>. Seguire sempre le indicazioni del proprio medico; non modificare mai la terapia di propria iniziativa. Qualsiasi decisione di riposizionamento di un farmaco richiede una validazione clinica completa e una revisione regolatoria.
<br><br>
<small>Revisionato da: 藥提醒科技有限公司 (yao.care)</small>
</div>
