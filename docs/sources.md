---
layout: default
title: Fonti dei dati
nav_order: 93
permalink: /sources/
description: "Le fonti dei dati alla base di ITTxGNN: liste AIFA dei farmaci di classe A e H e stato delle AIC (confezioni.csv), TxGNN, ClinicalTrials.gov, PubMed e DrugBank."
---

# Fonti dei dati

<div class="key-takeaway">
Ogni conclusione è riconducibile a una fonte di dati pubblica — nulla è una scatola nera.
</div>

---

<!-- local-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
## Italia: cosa coprono i dati locali

Dati locali: [AIFA: liste dei farmaci di classe A e H](https://www.aifa.gov.it/en/liste-farmaci-a-h). I dati locali sono le confezioni AIFA (codici AIC a 9 cifre) delle liste di classe A e H, verificate sul registro delle confezioni autorizzate. Un AIC che non figura più nel registro non è contato come autorizzato; la classe C non è inclusa.

| Voce | Valore |
|---|---|
| Medicinali presenti nei dati locali | {{ site.data.local_facts.licence.drugs_with_data }} |
| …con almeno una confezione autorizzate | {{ site.data.local_facts.licence.drugs_with_current }} |
| …con confezioni, ma nessuna autorizzate | {{ site.data.local_facts.licence.drugs_none_current }} |
| Medicinali assenti dai dati locali | {{ site.data.local_facts.licence.drugs_without_data }} |
| Voci locali (confezioni AIFA (AIC)) | {{ site.data.local_facts.licence.items_total }} |
| …di cui autorizzate | {{ site.data.local_facts.licence.items_current }} |

{% if site.data.local_facts.no_current.size > 0 %}Medicinali con confezioni AIFA (AIC) in questi dati, ma nessuna autorizzate: {% for r in site.data.local_facts.no_current %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}{% if site.data.local_facts.no_current_more > 0 %}, e altri {{ site.data.local_facts.no_current_more }}{% endif %}{% endif %}

{% if site.data.local_facts.recent_licence_reviews.size > 0 %}Ultime correzioni dei dati regolatori locali: {% for r in site.data.local_facts.recent_licence_reviews %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.d }}): {{ r.s }}{% unless forloop.last %}; {% endunless %}{% endfor %}{% endif %}

<!-- local-facts:end -->

## Panoramica delle fonti

<table class="comparison-table">
<thead>
<tr><th>Tipo</th><th>Fonte</th><th>Utilizzata per</th></tr>
</thead>
<tbody>
<tr><td>Dati di registrazione</td><td>AIFA: liste dei farmaci di <a href="https://www.aifa.gov.it/documents/20142/3442801/Classe_A_per_principio_attivo_30-09-2025.csv">classe A</a> e di <a href="https://www.aifa.gov.it/documents/20142/3442801/Classe_H_per_principio_attivo_30-09-2025.csv">classe H</a> per principio attivo (30/09/2025); open data <a href="https://drive.aifa.gov.it/farmaci/confezioni.csv">confezioni.csv</a></td><td>Farmaci di classe A e H e relativi principi attivi; stato amministrativo dell'AIC di ogni confezione</td></tr>
<tr><td>Modello di previsione</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Previsione delle associazioni farmaco&ndash;malattia</td></tr>
<tr><td>Studi clinici</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Classificazione delle prove (NCT)</td></tr>
<tr><td>Letteratura</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Classificazione delle prove (PMID)</td></tr>
<tr><td>Informazioni sui farmaci</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Mappatura dei principi attivi e dati sui bersagli</td></tr>
<tr><td>Interazioni</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>Dati sulle interazioni tra farmaci</td></tr>
</tbody>
</table>

L'elenco dei farmaci del sito comprende solo le classi A e H: i farmaci di classe C non sono inclusi.

---

## Licenze

Ogni fonte ha la propria licenza — si prega di verificarla prima di citarla:

- **TxGNN**: uso accademico; citare Huang et al. (2024)
- **ClinicalTrials.gov / PubMed**: dati pubblici del NIH statunitense
- **DrugBank**: uso non commerciale soggetto ai termini della relativa licenza
- **AIFA**: soggetta ai termini di open data dell'autorità regolatoria italiana

---

## Frequenza di aggiornamento

| Dati | Frequenza |
|------|-----------|
| Stato amministrativo delle AIC | Aggiornato automaticamente ogni settimana (lunedì) da confezioni.csv |
| Prove da studi clinici / letteratura | Raccolte nuovamente a intervalli periodici |
| Dati sulle interazioni | Riesaminati trimestralmente |

---

## Citazione accademica

> Huang, K., et al. (2024). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-024-03233-x](https://doi.org/10.1038/s41591-024-03233-x)

---

## Informazioni sullo Sviluppatore

Questa piattaforma è sviluppata e gestita da **藥提醒科技有限公司** (yao.care). Le informazioni sull'azienda,
il contesto del modello TxGNN e l'elenco completo dei siti della linea di prodotti si trovano nella pagina
<a href="{{ '/about/' | relative_url }}">Informazioni</a>.

---

<div class="disclaimer">
<strong>Esclusione di responsabilità</strong><br>
Il presente rapporto ha finalità esclusivamente di ricerca accademica e <strong>non costituisce un parere medico</strong>. Seguire sempre le indicazioni del proprio medico; non modificare mai la terapia di propria iniziativa. Qualsiasi decisione di riposizionamento di un farmaco richiede una validazione clinica completa e una revisione regolatoria.
<br><br>
<small>Revisionato da: 藥提醒科技有限公司 (yao.care)</small>
</div>
