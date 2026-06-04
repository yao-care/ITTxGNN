---
layout: default
title: Tadalafil
parent: 僅模型預測 (L5)
nav_order: 191
evidence_level: L5
indication_count: 8
---

# Tadalafil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

The skill confirms this is the EU (Italy) deployment of the TxGNN pipeline. Now generating the report.

---

# TADALAFIL: From Erectile Dysfunction / Pulmonary Arterial Hypertension to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Tadalafil is a selective PDE5 inhibitor widely approved for erectile dysfunction, pulmonary arterial hypertension (PAH), and benign prostatic hyperplasia.
The TxGNN model assigns its highest score to **Ambras Type Hypertrichosis Universalis Congenita**, with **0 clinical trials** and **0 supporting publications** — and the mechanistic evidence strongly suggests this is a **false positive**: tadalafil is itself a documented cause of excessive hair growth (trichomegaly) as an adverse effect, meaning the model has likely learned a drug–side-effect association and misclassified it as a treatment signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Erectile dysfunction, pulmonary arterial hypertension, benign prostatic hyperplasia (known from pharmaceutical literature; no Italy regulatory record available) |
| Predicted New Indication | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Italy Market Status | ✗ Not Marketed (0 registered licenses in data) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

> ⚠️ **Data Note**: Tadalafil (Cialis®, Adcirca®) is commercially available across the EU, including Italy. The zero-license result likely reflects a data retrieval gap rather than true absence from the Italian market. Regulatory confirmation via AIFA should be obtained before drawing conclusions about market status.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not present in the Evidence Pack. Based on established pharmaceutical knowledge, Tadalafil selectively inhibits phosphodiesterase type 5 (PDE5), preventing degradation of cyclic guanosine monophosphate (cGMP). The resulting rise in intracellular cGMP promotes smooth muscle relaxation and vasodilation — the basis for its approved uses in penile vasculature (erectile dysfunction), pulmonary vasculature (PAH), and prostatic smooth muscle (BPH).

Ambras type hypertrichosis universalis congenita is a rare autosomal dominant disorder caused by mutations in the *TRPS1* gene. It is characterized by diffuse, excessive growth of terminal hair over the entire body surface. The pathology is rooted in abnormal hair follicle development driven by TRPS1 dysfunction, with **no known intersection with the PDE5/cGMP signaling pathway**.

The mechanistic direction here is, in fact, **reversed**: trichomegaly (excessive eyelash elongation) is a recognized adverse effect of PDE5 inhibitors including tadalafil, documented in multiple pharmacovigilance reports. This means that elevated cGMP likely *promotes* hair follicle growth rather than suppressing it — precisely the opposite of what would be needed to treat hypertrichosis. The TxGNN model appears to have encoded this drug–side-effect co-occurrence as a positive treatment association, a known failure mode in knowledge graph–based repurposing algorithms. **This prediction should be classified as a false positive and excluded from further development.**

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Italy Market Information

No Italy regulatory authorizations are on record for Tadalafil in the current dataset. As noted above, this is likely a data gap. Tadalafil is EU-authorized under Cialis® (erectile dysfunction, BPH) and Adcirca® (pulmonary arterial hypertension); AIFA records should be queried directly to confirm the active authorization list.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Additional note relevant to the predictions in this pack: PDE5 inhibitors are known to trigger headache and, in documented cases, migraine aura via the NO–cGMP pathway activating the trigeminovascular system. One case report (PMID [17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/)) records tadalafil-associated typical migraine aura without headache. This is directly relevant because rank-8 prediction (migraine with brainstem aura) represents a *safety risk*, not a treatment opportunity.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All top-ranked TxGNN predictions for tadalafil exhibit a systematic pattern of false positives — hair-related disorders (ranks 1, 2, 5, 6) that reflect a drug–adverse-effect inversion, a structural brain malformation with no mechanistic link (rank 4), a periodontal condition where 20 retrieved publications are disease-general literature entirely unrelated to tadalafil (rank 3), and a migraine subtype where the sole relevant publication documents tadalafil as the *cause* of the aura (rank 8). None of the top 8 predictions constitutes a viable repurposing candidate based on current evidence.

**The one direction worth formal investigation:**

Rank 7 — **kyphoscoliotic heart disease** — is the only prediction with an indirect but biologically coherent rationale: severe thoracic kyphoscoliosis can cause restrictive lung disease → chronic hypoxia → secondary pulmonary arterial hypertension, and tadalafil (Adcirca®) is FDA- and EMA-approved for PAH. While no dedicated clinical trials exist for this subgroup, tadalafil's use in scoliosis-associated PAH falls within the scope of its approved mechanism.

**To proceed, the following is needed:**

- **Data gap remediation**: Retrieve MOA data from DrugBank API (DG002) and package insert warnings/contraindications (DG001) to enable a complete safety evaluation.
- **AIFA regulatory verification**: Confirm current Tadalafil authorization status in Italy (Cialis® and Adcirca® are expected to be listed; absence from current data is likely a retrieval error).
- **Model audit**: Flag the tadalafil predictions as a test case for PDE5i false-positive filtering. The model appears to systematically confuse side-effect graph edges with therapeutic edges for this drug class. Consider adding a side-effect exclusion layer to the post-processing pipeline.
- **Research question (rank 7 only)**: Design a retrospective case series or sub-group analysis examining PDE5 inhibitor use in patients with kyphoscoliosis-associated PAH, using existing PAH registry data.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

