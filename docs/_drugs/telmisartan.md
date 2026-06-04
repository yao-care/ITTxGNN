---
layout: default
title: Telmisartan
parent: 僅模型預測 (L5)
nav_order: 192
evidence_level: L5
indication_count: 10
---

# Telmisartan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

The skill confirms this is a TxGNN pipeline report task. Now generating the evaluation report based on the Evidence Pack JSON:

---

# Telmisartan: From Hypertension to Prinzmetal Angina

## One-Sentence Summary

Telmisartan is an angiotensin II type 1 (AT1) receptor blocker with a well-established global track record in hypertension management, though it currently holds no marketing authorization in Italy.
The TxGNN model assigns it the highest repurposing score for **Prinzmetal Angina** (99.98%), predicting a potential role in reducing coronary vasospasm susceptibility.
At present, however, **no clinical trials** and **no published literature** directly support this indication, placing this prediction at the lowest evidence tier (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension (global approval; no Italy authorization on record) |
| Predicted New Indication | Prinzmetal Angina |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, telmisartan is an AT1 receptor blocker that selectively antagonizes angiotensin II (AngII) signaling — preventing AngII-mediated vasoconstriction, aldosterone release, and vascular smooth muscle proliferation. Distinctively among ARBs, telmisartan also acts as a partial PPARγ (peroxisome proliferator-activated receptor gamma) agonist, conferring additional anti-inflammatory and metabolic benefits that extend beyond simple blood pressure reduction. This dual mechanism has earned it the informal label "metabosartan."

Prinzmetal angina (variant angina) involves transient, reversible coronary artery spasm at rest, typically in the absence of significant obstructive atherosclerosis. The theoretical link is mechanistically plausible: AT1 blockade could dampen AngII-induced coronary smooth muscle contraction, potentially lowering vasospasm susceptibility. PPARγ activation may further attenuate endothelial inflammation — a recognized contributor to the endothelial dysfunction that underlies vasospastic episodes.

Despite this theoretical rationale, the mechanistic inference remains highly indirect. No preclinical animal model, observational study, or clinical trial has directly assessed telmisartan in Prinzmetal angina. The TxGNN model's high score (99.98%) most likely reflects broad shared connectivity between vascular disease nodes in the knowledge graph — coronary artery disease, hypertension, and vasomotor disorders are densely interconnected — rather than a validated, drug-specific relationship. This prediction should be treated as hypothesis-generating only and not interpreted as evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Telmisartan in Prinzmetal Angina.

---

## Literature Evidence

Currently no related literature available for Telmisartan in Prinzmetal Angina.

---

## Italy Market Information

Telmisartan currently holds no marketing authorizations in Italy. No approved products are registered in this dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN score (99.98%), there is zero direct evidence — neither clinical trials nor published literature — linking telmisartan to Prinzmetal angina. An L5 rating means this is a model-only prediction that requires substantial preclinical validation before any development pathway can be considered.

**To proceed, the following is needed:**

- **Preclinical validation**: Coronary vasospasm animal models (e.g., ergonovine-induced spasm) to directly test whether AT1 blockade or PPARγ activation reduces vasospastic events
- **Indirect literature survey**: Systematic review of existing AT1 blocker and PPARγ agonist studies for any signals in vasospastic angina or coronary endothelial dysfunction
- **MOA documentation**: Complete DrugBank mechanism of action profile for telmisartan (currently unavailable in this Evidence Pack)
- **Safety review**: Full package insert (TFDA/EMA) for key warnings, contraindications, and drug interactions — especially relevant given telmisartan's antihypertensive effect, which may require dose adjustment in normotensive Prinzmetal angina patients
- **Hemodynamic risk assessment**: Evaluate whether blood pressure reduction in a normotensive vasospasm population is clinically appropriate or potentially harmful

> **Note for reviewers:** While Prinzmetal angina ranks #1 by TxGNN score, the Evidence Pack also contains indications with substantially stronger clinical evidence. Notably, **intracerebral hemorrhage (rank #9)** is supported by a completed Phase 3 RCT (TRIDENT, NCT02699645, n=1,671) and achieves an L1 evidence rating with a "Proceed with Guardrails" recommendation. A separate report focused on that indication may be of greater immediate clinical value.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

