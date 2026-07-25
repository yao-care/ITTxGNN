---
layout: default
title: Solo previsione del modello (L5)
nav_order: 23
permalink: /evidence-low/
description: "Candidati di livello L5 in ITTxGNN: solo previsione del modello, ancora senza prove cliniche o di letteratura."
---

# Solo previsione del modello (L5)

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Candidati con la sola previsione del modello e ancora senza prove sull'uomo
</p>

---

## Criteri

| Livello | Definizione | Significato clinico |
|-------|------------|------------------|
| **L5** | Solo previsione del modello | Fase ipotetica; nessuna prova sull'uomo |

---

{% assign l5_drugs = site.drugs | where: "evidence_level", "L5" | sort: "title" %}

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
