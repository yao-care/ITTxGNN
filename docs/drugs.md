---
layout: default
title: Tutti i farmaci
nav_order: 20
permalink: /drugs/
description: "Tutte le schede di validazione dei farmaci e le statistiche sui livelli di prova in ITTxGNN."
---
{% assign l1_count = site.drugs | where: "evidence_level", "L1" | size %}
{% assign l2_count = site.drugs | where: "evidence_level", "L2" | size %}
{% assign l3_count = site.drugs | where: "evidence_level", "L3" | size %}
{% assign l4_count = site.drugs | where: "evidence_level", "L4" | size %}
{% assign l5_count = site.drugs | where: "evidence_level", "L5" | size %}

# Tutti i farmaci

{{ site.drugs.size }} schede di validazione dei farmaci

---

## Ripartizione per livello di prova

| Livello di prova | Farmaci | Descrizione |
|---------|--------|------|
| **L1** | {{ l1_count }} | Più RCT / revisioni sistematiche |
| **L2** | {{ l2_count }} | Singolo RCT / studi di Fase 2 |
| **L3** | {{ l3_count }} | Studi osservazionali / ampie serie di casi |
| **L4** | {{ l4_count }} | Studi preclinici / meccanicistici |
| **L5** | {{ l5_count }} | Solo previsione del modello |

---

## Elenco completo dei farmaci

{% assign all_drugs = site.drugs | sort: 'title' %}

| Farmaco | Livello di prova | Indicazioni |
|---------|---------|---------|
{% for drug in all_drugs %}| [{{ drug.title }}]({{ drug.url | relative_url }}) | {{ drug.evidence_level }} | {{ drug.indication_count }} |
{% endfor %}

---

<div class="disclaimer">
<strong>Esclusione di responsabilità</strong><br>
Il presente rapporto ha finalità esclusivamente di ricerca accademica e <strong>non costituisce un parere medico</strong>. Seguire sempre le indicazioni del proprio medico; non modificare mai la terapia di propria iniziativa. Qualsiasi decisione di riposizionamento di un farmaco richiede una validazione clinica completa e una revisione regolatoria.
<br><br>
<small>Revisionato da: 藥提醒科技有限公司 (yao.care)</small>
</div>
