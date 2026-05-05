---
layout: default
title: Captopril
parent: 僅模型預測 (L5)
nav_order: 45
evidence_level: L5
indication_count: 4
---

# Captopril
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

# Captopril: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Captopril is a first-generation ACE inhibitor with a long-established role in treating hypertension, heart failure, and diabetic nephropathy; however, the current dataset contains no formal approved indication records for Italy.
The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**, with **no registered clinical trials** and only **1 published case report** currently supporting this specific direction.
A closely related indication — **Malignant Renovascular Hypertension** (TxGNN rank #2, identical score) — carries a stronger mechanistic rationale and is backed by 20 publications (Evidence Level L3), warranting attention alongside the primary prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from Italy regulatory dataset (no approved licenses on record) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L4 |
| Italy Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data source. Based on established clinical pharmacology, Captopril is an angiotensin-converting enzyme (ACE) inhibitor that blocks the conversion of Angiotensin I to Angiotensin II (Ang II). By lowering Ang II levels, it reduces systemic vascular resistance, decreases glomerular capillary hypertension, and attenuates proteinuria — a profile that is mechanistically relevant to kidney damage driven by severe hypertension.

In malignant hypertensive renal disease, the RAAS is often pathologically overactivated, triggering a vicious cycle of high Ang II, progressive renal ischaemia, and further renin secretion. Captopril directly interrupts this axis, making the TxGNN prediction logically coherent. However, a critical clinical caveat exists: in patients with bilateral renal artery stenosis (BRAS) or stenosis of a solitary functioning kidney, ACE inhibition can acutely and severely compromise glomerular filtration by removing the Ang II-dependent efferent arteriole tone that is sustaining residual perfusion — a well-known contraindication class that must be screened for before any therapeutic application.

The closely related rank #2 prediction — **malignant renovascular hypertension** — follows the same mechanistic logic and has substantially more supporting literature. In renovascular hypertension driven by renal artery stenosis, high-renin/high-Ang II physiology is the defining lesion, and Captopril is both the mechanistic antidote and a long-used diagnostic probe (captopril renography). This convergence of diagnostic and therapeutic utility in the RAAS-driven hypertension spectrum strengthens the biological plausibility of both predictions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Captopril in malignant hypertensive renal disease or malignant renovascular hypertension.

---

## Literature Evidence

### Primary Indication: Malignant Hypertensive Renal Disease (Rank #1)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [28902735](https://pubmed.ncbi.nlm.nih.gov/28902735/) | 2017 | Case Report | Clinical Nuclear Medicine | Positive captopril renography in a patient with renin-dependent hypertension caused by chromophobe renal cell carcinoma (not renal artery stenosis); hypertension resolved after nephrectomy — illustrates renin-dependent mechanisms mimicking renovascular renal disease |

### Supplementary Evidence: Malignant Renovascular Hypertension (Rank #2)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [232024](https://pubmed.ncbi.nlm.nih.gov/232024/) | 1979 | Clinical Study | Clinical Science | Captopril and saralasin induced marked PRA elevation (>14 ng/h/mL) in 43/44 untreated renovascular hypertension patients; diastolic BP reduction ≥9% — establishes captopril as a diagnostic and mechanistic probe |
| [6145432](https://pubmed.ncbi.nlm.nih.gov/6145432/) | 1984 | Clinical Study (Non-RCT) | Biull Vsesoiuznogo Kardiologicheskogo Nauchnogo Tsentra | Direct clinical evaluation of captopril in both stable and malignant-phase arterial hypertension |
| [3894732](https://pubmed.ncbi.nlm.nih.gov/3894732/) | 1985 | Cohort / Review | Japanese Journal of Medicine | Significance of captopril test in diagnosing renovascular hypertension; sodium balance importance in RAAS evaluation |
| [2887673](https://pubmed.ncbi.nlm.nih.gov/2887673/) | 1987 | Experimental / Clinical Study | Japanese Heart Journal | Serial neurohormonal measurements (PRA, Ang I, Ang II, catecholamines, vasopressin) during benign and malignant phases of 2K2C Goldblatt hypertension in dogs; defines RAAS contribution to malignant transition |
| [2040938](https://pubmed.ncbi.nlm.nih.gov/2040938/) | 1991 | Review | Journal of Pediatrics | Pathophysiology and management of malignant hypertension including RAAS mechanisms |
| [1572120](https://pubmed.ncbi.nlm.nih.gov/1572120/) | 1992 | Case Report | Clinical Nuclear Medicine | False-positive captopril renal scintigraphy in malignant hypertension without anatomical renal artery stenosis; highlights RAAS over-activation as a standalone driver |
| [8070421](https://pubmed.ncbi.nlm.nih.gov/8070421/) | 1994 | Review / Case Series | Endocrinology & Metabolism Clinics of North America | JG-cell renin-secreting tumors; blood pressure drops consistently with ACE inhibitor treatment; captopril test shows variable plasma renin autonomy |
| [10955932](https://pubmed.ncbi.nlm.nih.gov/10955932/) | 2000 | Case Series | Pediatric Nephrology | NF1-associated renovascular hypertension in 27 paediatric patients evaluated with captopril test and Doppler ultrasonography |
| [11334320](https://pubmed.ncbi.nlm.nih.gov/11334320/) | 2001 | Case Report + Review | Clinical Nephrology | Two cases of renovascular hypertension in neurofibromatosis; captopril stimulation increased PRA from 2.8 to 12.6 ng/mL/h, confirming renin-dependent mechanism |
| [17008836](https://pubmed.ncbi.nlm.nih.gov/17008836/) | 2006 | Review | Minerva Medica | Clinical concepts in renovascular hypertension: RAAS pathophysiology, diagnostic workup, and treatment strategies; ACE inhibitor role discussed |

---

## Italy Market Information

Captopril is currently **not marketed in Italy**. No regulatory authorizations were found in the dataset. This is notable given that captopril is a generic ACE inhibitor off-patent worldwide; absence from Italy's market registry may reflect data completeness rather than a true market absence, and requires verification against the AIFA official database.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Class-level clinical note:** As an ACE inhibitor, Captopril carries well-established safety considerations that are particularly relevant for the predicted renal indications. Bilateral renal artery stenosis or unilateral stenosis in a solitary kidney is a **known contraindication** — ACE inhibition in these settings can precipitate acute kidney injury. Additional class effects include hyperkalaemia (risk amplified in CKD), ACE inhibitor-induced dry cough, and angioedema (rare but potentially severe). Formal safety documentation from the package insert or TFDA label should be obtained before proceeding.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
For the primary predicted indication (malignant hypertensive renal disease, rank #1), only a single case report is available and no clinical trials have been registered, placing the evidence squarely at Level L4. The mechanistic rationale is coherent but insufficient on its own to support a repurposing decision. The closely related rank #2 indication (malignant renovascular hypertension) presents a more actionable profile (L3 evidence, 20 publications, recommendation: Proceed with Guardrails) and should be elevated as the primary candidate for follow-up.

**To proceed, the following is needed:**

- **Systematic evidence review for rank #2**: Malignant renovascular hypertension has L3 evidence and a stronger mechanistic case — consider advancing this indication to formal evaluation
- **AIFA database verification**: Confirm Italy market status via direct AIFA query; current dataset shows zero licenses which may reflect a data gap
- **Package insert retrieval**: Obtain formal contraindications and warnings (TFDA/EMA label) to complete the S1 safety screen — currently blocking
- **MOA data retrieval**: Query DrugBank API for Captopril's full mechanism-of-action profile to strengthen the mechanistic linkage analysis
- **Renal imaging requirement definition**: For any clinical pathway involving ACE inhibitors in malignant hypertension, bilateral renal artery stenosis screening (Doppler ultrasound or MR angiography) must be defined as a prerequisite safety criterion
- **Rank #3 and #4 indications (pulmonary hypertension)**: Both are rated L5 with Hold recommendation and lack mechanistic support for Captopril — no further action recommended at this stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

