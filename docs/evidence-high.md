---
layout: default
title: Prove elevate (L1-L2)
nav_order: 21
permalink: /evidence-high/
description: "Candidati al riposizionamento dei farmaci di livello L1-L2 in ITTxGNN, supportati da studi clinici o revisioni sistematiche."
---

# Prove elevate (L1-L2)

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Candidati che possono essere considerati prioritari per la valutazione clinica
</p>

---

## Criteri

| Livello | Definizione | Significato clinico |
|-------|------------|------------------|
| **L1** | Più RCT di Fase 3 / revisioni sistematiche | Supporto forte; l'uso clinico può essere preso in considerazione |
| **L2** | Un singolo RCT o più studi di Fase 2 | Supporto moderato; è possibile progettare studi di validazione |

---

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | sort: "title" %}

### L1 ({{ l1_drugs.size }} farmaci)

| Farmaco | Indicazioni | Collegamento |
|---------|---------|------|
{% for drug in l1_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Vedi la scheda]({{ drug.url | relative_url }}) |
{% endfor %}

### L2 ({{ l2_drugs.size }} farmaci)

| Farmaco | Indicazioni | Collegamento |
|---------|---------|------|
{% for drug in l2_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Vedi la scheda]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Esclusione di responsabilità</strong><br>
Il presente rapporto ha finalità esclusivamente di ricerca accademica e <strong>non costituisce un parere medico</strong>. Seguire sempre le indicazioni del proprio medico; non modificare mai la terapia di propria iniziativa. Qualsiasi decisione di riposizionamento di un farmaco richiede una validazione clinica completa e una revisione regolatoria.
<br><br>
<small>Revisionato da: 藥提醒科技有限公司 (yao.care)</small>
</div>
