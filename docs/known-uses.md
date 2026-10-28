---
layout: default
title: "Solo usi noti (nessuna nuova previsione)"
nav_order: 24
permalink: /known-uses/
description: "Per questi farmaci tutti i candidati del modello TxGNN sono già usi noti (registrati nel grafo di conoscenza o in un'autorizzazione), quindi non esiste alc…"
---

# Solo usi noti (nessuna nuova previsione)

Per questi farmaci tutti i candidati del modello TxGNN sono già usi noti (registrati nel grafo di conoscenza o in un'autorizzazione), quindi non esiste alcuna nuova indicazione prevista. Ogni pagina riporta gli usi noti e lo stato di commercializzazione locale.

{% assign known_drugs = site.drugs | where: "evidence_level", "N/A" | sort: "title" %}

**{{ known_drugs.size }} farmaci**

| Farmaco | Report |
|------|------|
{% for drug in known_drugs %}| **{{ drug.title }}** | [Vedi pagina]({{ drug.url | relative_url }}) |
{% endfor %}
