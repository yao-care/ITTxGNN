---
layout: default
title: Ciclesonide
parent: 僅模型預測 (L5)
nav_order: 51
evidence_level: L5
indication_count: 6
---

# Ciclesonide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Using the `txgnn-pipeline` skill confirmed the context. Now generating the report from the Evidence Pack.

---

# Ciclesonide: From Asthma to Atopic Eczema

## One-Sentence Summary

Ciclesonide is an inhaled corticosteroid (ICS) approved for asthma, acting as a glucocorticoid receptor (GR) agonist that suppresses airway inflammation via pulmonary enzymatic activation to its active metabolite, des-ciclesonide.
The TxGNN model predicts it may be effective for **Atopic Eczema**, but with **no clinical trials** and **no published literature** currently supporting this specific direction.
A critical barrier exists: ciclesonide is a pulmonary prodrug with no topical dermatological formulation, making route compatibility a fundamental unresolved challenge for skin indications.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma (inhaled corticosteroid) |
| Predicted New Indication | Atopic Eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ciclesonide is a glucocorticoid receptor (GR) agonist engineered specifically as an inhaled prodrug. After inhalation, pulmonary esterases convert it to its active metabolite, des-ciclesonide, which inhibits NF-κB activation in airway epithelial cells and suppresses pro-inflammatory cytokines including IL-6, IL-8, and TNF-α. This highly targeted pulmonary activation mechanism is a deliberate design feature intended to reduce systemic corticosteroid side effects.

Atopic eczema is driven primarily by Th2-mediated immune dysregulation, characterized by overactivation of IL-4, IL-13, and IgE pathways leading to chronic skin barrier dysfunction and inflammation. At the class level, GR agonists are central to atopic eczema management — topical corticosteroids remain a first-line standard of care. The TxGNN model likely captures this broad corticosteroid-class mechanistic overlap, which accounts for the high prediction score.

However, there is a **fundamental route compatibility barrier**: ciclesonide is pharmacologically engineered to be activated by lung-specific esterases, not skin enzymes. No topical or transdermal formulation of ciclesonide currently exists, and it is unclear whether cutaneous esterases can sufficiently convert ciclesonide to des-ciclesonide at therapeutically relevant concentrations. Without a viable delivery route, the mechanistic rationale cannot translate to clinical application without significant pharmaceutical development. The 99.96% TxGNN score should therefore be interpreted as reflecting **class-level plausibility**, not ciclesonide-specific evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Ciclesonide has no approved drug licenses on record in Taiwan (0 authorizations). No authorization table is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.96%), the evidence for ciclesonide in atopic eczema is L5 (model prediction only) with zero supporting clinical trials or literature, and — more critically — ciclesonide's prodrug pharmacology poses a fundamental route compatibility barrier that cannot be resolved without new formulation development.

**To proceed, the following is needed:**

- **Formulation feasibility study**: Determine whether a topical or transdermal ciclesonide formulation can deliver therapeutically active des-ciclesonide to the skin (requires pharmaceutical R&D investment before any clinical step)
- **Skin esterase assessment**: Characterize whether human cutaneous esterases can activate ciclesonide to des-ciclesonide at relevant tissue concentrations — this single data point would dramatically change the plausibility of skin indications
- **Preclinical proof-of-concept**: In vitro keratinocyte models and in vivo atopic dermatitis mouse models using ciclesonide to establish basic efficacy signal before any human study
- **MOA data confirmation**: Obtain full DrugBank mechanism data to strengthen mechanistic rationale documentation

> **Strategic note — consider reprioritizing to Bronchitis (Rank 4):** Among all six predicted indications, bronchitis/COPD presents the most immediately actionable research question. Ciclesonide is already an ICS with established airway anti-inflammatory action; GOLD guidelines support ICS use in COPD; and Finnish COPD treatment guidelines ([PMID 25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/)) cite ICS pharmacotherapy in this context. No new formulation development is needed, and the route of administration is identical to the approved indication.

> **Caution — Contact Dermatitis (Rank 5) carries counter-evidence:** The only available literature for this indication ([PMID 22957490](https://pubmed.ncbi.nlm.nih.gov/22957490/)) is a case report documenting ciclesonide as a **cross-reactive allergen** in systemic allergic dermatitis caused by inhaled budesonide — not a therapeutic agent. This indication should not be pursued.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

