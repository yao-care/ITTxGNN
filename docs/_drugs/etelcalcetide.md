---
layout: default
title: Etelcalcetide
parent: 僅模型預測 (L5)
nav_order: 96
evidence_level: L5
indication_count: 4
---

# Etelcalcetide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

The skill confirms this is a TxGNN pipeline task. Now let me generate the report based on the Evidence Pack.

---

# Etelcalcetide: From Secondary Hyperparathyroidism to Hyperphosphatemia

## One-Sentence Summary

Etelcalcetide is an intravenous calcimimetic (calcium-sensing receptor agonist) approved in multiple countries for secondary hyperparathyroidism (SHPT) in adults with chronic kidney disease (CKD) on hemodialysis.
The TxGNN model predicts it may be effective for **Hyperphosphatemia**,
with **1 clinical trial** and **3 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Secondary hyperparathyroidism in CKD patients on hemodialysis (no Italian registration on record) |
| Predicted New Indication | Hyperphosphatemia |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L3 |
| Italy Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Etelcalcetide activates the calcium-sensing receptor (CaSR) on parathyroid chief cells, powerfully suppressing PTH secretion. By driving down circulating PTH, it reduces osteoclast-mediated bone resorption — one of the key sources of phosphate release into the bloodstream in CKD-mineral and bone disorder (CKD-MBD). This indirect chain — CaSR activation → PTH suppression → reduced bone phosphate efflux → lower serum phosphate — forms the mechanistic basis for TxGNN's prediction.

In CKD-MBD, secondary hyperparathyroidism and hyperphosphatemia are tightly coupled pathologies. Elevated PTH drives bone resorption, releasing phosphate into the circulation; simultaneously, impaired renal phosphate clearance compounds the burden. Because etelcalcetide directly tackles PTH excess, treating SHPT with this agent naturally produces a measurable downstream reduction in phosphate levels, making this prediction biologically coherent.

It is important to flag, however, that **hyperphosphatemia is not etelcalcetide's direct pharmacological target** — phosphate reduction is a secondary benefit rather than the primary mechanism. Clinical guidelines for CKD-MBD recommend combining calcimimetics with phosphate binders for optimal phosphate control, which suggests etelcalcetide is unlikely to be sufficient as standalone therapy for hyperphosphatemia and would need to be positioned as part of a multimodal regimen.

> Currently, detailed mechanism of action data has not been retrieved from DrugBank (Data Gap DG002). The above mechanistic reasoning is based on the drug class (calcimimetic / CaSR agonist) and supporting literature found in this Evidence Pack.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03527511](https://clinicaltrials.gov/study/NCT03527511) | N/A | Completed | 21 | Mechanistic study examining the effect of active vitamin D and etelcalcetide on osteoclast activity in CKD-MBD patients. Hyperphosphatemia is a feature of the study population but not the primary endpoint; results provide supportive mechanistic evidence for the PTH–phosphate axis, though not direct efficacy data for hyperphosphatemia as an indication. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [33305109](https://pubmed.ncbi.nlm.nih.gov/33305109/) | 2020 | Phase 2/3 RCT | Kidney International Reports | DUET trial — prospective randomised study of etelcalcetide in hemodialysis patients with SHPT. Evaluated a multilateral CKD-MBD treatment strategy; phosphate control is a secondary outcome, providing indirect evidence that etelcalcetide contributes to phosphate reduction as part of SHPT management. |
| [29440923](https://pubmed.ncbi.nlm.nih.gov/29440923/) | 2018 | Review | International Journal of Nephrology and Renovascular Disease | Expert review of etelcalcetide's role in SHPT management in hemodialysis. Discusses PTH reduction mechanism, clinical trial results, and downstream effects on phosphate and bone metabolism; contextualises etelcalcetide within the broader CKD-MBD treatment landscape. |
| [33211001](https://pubmed.ncbi.nlm.nih.gov/33211001/) | 2021 | Case Report | Clinical Nephrology | Case of temporary metastatic pulmonary calcification in a peritoneal dialysis patient with SHPT. Illustrates the severe clinical consequences of uncontrolled hyperparathyroidism and hyperphosphatemia; indirect support for aggressive CaSR-targeted intervention in mineral disorder management. |

---

## Safety Considerations

Please refer to the package insert (SmPC) for safety information. Full warnings, contraindications, and drug interaction data were not available in this Evidence Pack (Data Gaps DG001 and DG002).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction is mechanistically grounded — etelcalcetide's suppression of PTH indirectly reduces phosphate load in CKD-MBD patients, and this effect is corroborated by the DUET Phase 2/3 RCT and supporting review literature (L3). However, phosphate reduction is a downstream secondary benefit rather than a primary pharmacological action, the drug is not currently registered in Italy, and critical safety data remain unresolved.

**To proceed, the following is needed:**

- **Regulatory clarification**: Verify the AIFA registration status; etelcalcetide is approved in the EU as Parsabiv® (EMA) — confirm whether this covers Italy and reconcile with the zero-license finding.
- **Full safety dossier**: Retrieve the SmPC / package insert to assess key warnings, contraindications, hypocalcaemia risk, and monitoring requirements (DG001).
- **MOA data**: Pull complete mechanism of action from DrugBank (DG002) to strengthen the mechanistic rationale.
- **Dedicated hyperphosphatemia endpoint study**: Existing evidence uses hyperphosphatemia only as a secondary outcome; a prospective study with phosphate as the primary endpoint is needed to formally support this new indication.
- **Combination strategy evaluation**: Assess the clinical value of etelcalcetide + phosphate binder regimens specifically designed to target hyperphosphatemia, rather than repurposing a SHPT dosing protocol.
- **Specialist review**: Consult a nephrologist to evaluate clinical feasibility in Italy, particularly for CKD-MBD patients not yet on hemodialysis (current IV administration requires dialysis access).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

