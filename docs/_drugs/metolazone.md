---
layout: default
title: Metolazone
parent: 僅模型預測 (L5)
nav_order: 146
evidence_level: L5
indication_count: 5
---

# Metolazone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

以下為根據 Evidence Pack 產生的完整評估報告：

---

# Metolazone: From Hypertension and Oedema to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Metolazone is a thiazide-like diuretic traditionally used to manage hypertension and oedema, including diuretic-resistant volume overload in combination with loop diuretics.
The TxGNN model predicts it may have a role in **Malignant Hypertensive Renal Disease**,
however there are currently **0 clinical trials** and **0 disease-specific publications** supporting this direction — the prediction rests entirely on knowledge-graph modelling.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension and oedema (thiazide-like diuretic by pharmacological class; no Italian authorisation record available) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the regulatory package. Based on known pharmacological classification, Metolazone belongs to the quinazoline sulfonamide (thiazide-like) diuretic class. It inhibits sodium reabsorption in the distal convoluted tubule, reducing intravascular volume and consequently lowering systemic blood pressure. Notably, Metolazone retains diuretic activity at lower GFR levels compared to conventional thiazides, which explains its frequent off-label use in patients with moderate renal impairment alongside loop diuretics.

Malignant hypertensive renal disease (accelerated-phase hypertension with acute renal injury) is characterised by severely elevated blood pressure driving progressive glomerular ischaemia and arteriolar fibrinoid necrosis. In this context, a volume-reducing agent that lowers blood pressure could theoretically relieve haemodynamic stress on the glomerulus. This forms the indirect mechanistic rationale that the TxGNN knowledge graph likely captured: Metolazone's antihypertensive node is well-connected to hypertension-related renal disease nodes in the graph.

However, the mechanistic plausibility is low to moderate in practice. Malignant hypertension requires rapid, controlled BP reduction and is primarily managed with RAAS inhibitors, calcium channel blockers, or intravenous agents as first-line therapy. Thiazide-like diuretics are not considered standard of care for this acute, high-severity phenotype, and their efficacy diminishes substantially when GFR falls significantly — a common finding precisely in malignant hypertensive nephrosclerosis. The high TxGNN score therefore most likely reflects broad graph topology connectivity rather than a targeted disease-modifying mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns a high numerical score (99.84%), there is zero disease-specific clinical or literature evidence, the mechanistic link is indirect and partially contradicted by the pathophysiology of malignant hypertension, and no Italian marketing authorisation exists. This prediction does not meet the minimum threshold to advance beyond model-output stage.

**To proceed, the following is needed:**
- Retrieve and parse the full package insert (SmPC/仿單) to obtain confirmed MOA, boxed warnings, contraindications, and special-population restrictions
- Conduct a targeted literature search to determine whether any observational, retrospective, or case-series data supports thiazide-like diuretics specifically in malignant hypertension with renal involvement
- Clarify the GFR threshold below which Metolazone's antihypertensive and diuretic efficacy becomes clinically insufficient
- Assess whether the TxGNN signal is an artefact of graph proximity between "antihypertensive" and "hypertensive renal disease" nodes, or reflects a genuine unmet-need gap
- If evidence retrieval yields ≥1 supporting study, re-triage as L4 and repeat decision assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

