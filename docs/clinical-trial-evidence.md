---
layout: default
title: "Farmaci con evidenze da studi per una nuova indicazione"
nav_order: 25
permalink: /clinical-trial-evidence/
description: "Farmaci di classe A e H (liste AIFA) la cui nuova indicazione prevista da TxGNN ha evidenze da studi clinici (L1-L2): indicazione, livello, studi."
last_modified_at: 2026-11-03
---
{%- comment -%}
2026-11-03：回答 AI 搜尋常問的「本國藥物中，哪些新適應症有臨床試驗證據」。全表由 Liquid 從藥物頁產生，不寫死藥名或數字。
收錄＝公開藥物頁（排除 id_redirect 與 noindex）中 evidence_level 為 L1 或 L2（本站 evidence-high 標準：L1 多個 Phase 3 RCT／系統性回顧，
L2 單一 RCT 或多個 Phase 2 試驗）。預測新適應症與等級註記取自各藥物頁快速總覽表；下列欄名是本站藥物頁實際用到的寫法（建頁時逐頁核對），
新寫法抓不到時顯示「vedi report」、等級仍取 front matter。試驗數＝該藥物頁引用的不重複 NCT 編號數。
{%- endcomment -%}
{%- assign ind_labels = "Nuova indicazione prevista|Nuova indicazione predetta" | split: "|" -%}
{%- assign lev_labels = "Livello di evidenza" | split: "|" -%}
{%- assign listed = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" -%}
{%- assign l1 = listed | where: "evidence_level", "L1" | sort: "title" -%}
{%- assign l2 = listed | where: "evidence_level", "L2" | sort: "title" -%}
{%- assign trial_drugs = l1 | concat: l2 -%}
{%- assign latest = trial_drugs | sort: "last_modified_at" | last -%}
{%- assign latest_date = latest.last_modified_at | date: "%Y-%m-%d" -%}

# Farmaci di classe A e H con evidenze da studi clinici per una nuova indicazione

<p class="key-answer" data-question="Quali farmaci in Italia hanno evidenze da studi clinici per una nuova indicazione?">
<strong>{{ trial_drugs.size }}</strong> dei {{ listed.size }} farmaci con un report ITTxGNN hanno una nuova indicazione prevista da TxGNN con livello di evidenza <strong>L1 o L2</strong> ({{ l1.size }} di livello L1, {{ l2.size }} di livello L2): per essa sono quindi state trovate evidenze da studi clinici (studi randomizzati, studi di fase 2–3 o revisioni sistematiche).
</p>

I farmaci provengono da le [liste AIFA dei farmaci di classe A e H](https://www.aifa.gov.it/en/liste-farmaci-a-h) (classi di rimborsabilità; la classe C non è inclusa); l'elenco riflette i report sui farmaci aggiornati l'ultima volta il {{ latest_date }}.

<div class="key-takeaway">
Le evidenze da studi per un'indicazione prevista non dimostrano l'efficacia. Ogni candidato qui sotto <strong>richiede ancora una validazione clinica</strong> e una valutazione regolatoria prima di qualsiasi uso clinico.
</div>

---

## Farmaci con evidenze da studi (L1–L2)

<div class="table-wrapper"><table>
<thead>
<tr><th>Farmaco</th><th>Nuova indicazione prevista</th><th>Livello di evidenza</th><th>Studi registrati citati (NCT)</th></tr>
</thead>
<tbody>
{%- for drug in trial_drugs -%}
{%- assign indication = "" -%}
{%- for lab in ind_labels -%}{%- if indication == "" -%}{%- assign needle = "<td>" | append: lab | append: "</td>" -%}{%- assign qo = drug.content | split: needle -%}{%- if qo.size > 1 -%}{%- assign indication = qo[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign level_cell = "" -%}
{%- for lab in lev_labels -%}{%- if level_cell == "" -%}{%- assign needle = "<td>" | append: lab | append: "</td>" -%}{%- assign lv = drug.content | split: needle -%}{%- if lv.size > 1 -%}{%- assign level_cell = lv[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign parts = drug.content | split: "NCT" -%}
{%- capture nct_ids -%}{%- for p in parts offset: 1 -%}{%- assign id = p | slice: 0, 8 -%}{%- assign rest = id | remove: "0" | remove: "1" | remove: "2" | remove: "3" | remove: "4" | remove: "5" | remove: "6" | remove: "7" | remove: "8" | remove: "9" -%}{%- if id.size == 8 and rest == "" -%}{{ id }},{%- endif -%}{%- endfor -%}{%- endcapture -%}
{%- assign nct_count = nct_ids | split: "," | uniq | size %}
<tr><td><a href="{{ drug.url | relative_url }}">{{ drug.title }}</a></td><td>{% if indication != "" %}{{ indication }}{% else %}vedi report{% endif %}</td><td>{{ drug.evidence_level }}{% if level_cell != "" and level_cell != drug.evidence_level %} <a href="{{ drug.url | relative_url }}" title="{{ level_cell | strip_html | escape }}">(con riserva)</a>{% endif %}</td><td>{{ nct_count }}</td></tr>
{%- endfor %}
</tbody>
</table></div>

## Come leggere questo elenco

- **Livello di evidenza** segue i [criteri]({{ '/evidence-high/' | relative_url }}) del sito: L1 = Più RCT di Fase 3 / revisioni sistematiche; L2 = Un singolo RCT o più studi di Fase 2. «(con riserva)» indica che il report precisa il livello con una riserva; leggete la nota del report prima di basarvi su di esso.
- **Nuova indicazione prevista** è la previsione principale di ciascun report. Le indicazioni e controindicazioni già registrate nel grafo di conoscenza di TxGNN sono escluse, ma alcune previsioni possono comunque sovrapporsi a un uso consolidato; il report lo spiega quando è il caso.
- **Studi registrati citati** conta i numeri ClinicalTrials.gov (NCT) citati nel report. I report citano una selezione degli studi trovati; 0 significa che il report non cita alcuno studio registrato e la sezione sulle evidenze dalla letteratura mostra la base del livello.
- Per tutti i livelli e il metodo completo, vedere [Prove elevate (L1-L2)]({{ '/evidence-high/' | relative_url }}), [Tutti i farmaci]({{ '/drugs/' | relative_url }}) e la [metodologia]({{ '/methodology/' | relative_url }}).

---

<div class="disclaimer">
<strong>Esclusione di responsabilità</strong><br>
Il presente rapporto ha finalità esclusivamente di ricerca accademica e <strong>non costituisce un parere medico</strong>. Seguire sempre le indicazioni del proprio medico; non modificare mai la terapia di propria iniziativa. Qualsiasi decisione di riposizionamento di un farmaco richiede una validazione clinica completa e una revisione regolatoria.
<br><br>
<small>Revisionato da: 藥提醒科技有限公司 (yao.care)</small>
</div>
