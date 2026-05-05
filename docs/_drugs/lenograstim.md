---
layout: default
title: Lenograstim
parent: 僅模型預測 (L5)
nav_order: 133
evidence_level: L5
indication_count: 4
---

# Lenograstim
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

# Lenograstim: From Neutropenia / Stem Cell Mobilization to Primary Release Disorder of Platelets

## One-Sentence Summary

Lenograstim is a recombinant glycosylated granulocyte colony-stimulating factor (G-CSF), primarily known for reducing chemotherapy-induced neutropenia and mobilizing hematopoietic stem cells (HSC) prior to transplantation.
The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**, with **13 clinical trials** identified (all of indirect relevance only) and **no published literature** currently supporting this direction.
The evidence base is thin: all trial connections trace through HSCT mobilization use rather than direct treatment of platelet release defects, making this a knowledge-graph inference rather than clinical evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no registered licenses in Italy) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| Italy Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not formally available in this Evidence Pack. Based on established pharmacology, lenograstim binds the G-CSF receptor (G-CSFR/CD114), stimulating the proliferation and differentiation of neutrophil progenitors. Crucially, G-CSFR is also expressed on megakaryocyte progenitor cells — the precursors to platelets — meaning lenograstim may exert a secondary, indirect influence on platelet production. However, its primary clinical role has always been neutrophil recovery and HSC mobilization, not platelet function.

Primary release disorder of platelets covers conditions where platelets fail to discharge their granule contents (dense granules, alpha granules) upon activation. These are structural or enzymatic defects in granule biology — distinct from platelet *quantity*. Lenograstim has no known mechanism to repair granule packaging or release machinery, so the link between the drug and this indication is mechanistically indirect at best.

The most plausible pathway captured by TxGNN is the following: severe, refractory platelet release disorders are theoretically curable by allogeneic HSCT, which replaces the defective megakaryocyte lineage with a donor's healthy progenitors. Lenograstim frequently appears in allo-HSCT clinical trials as an HSC mobilization adjunct. TxGNN's knowledge graph likely connected the dots via the shared node **hematology → allo-HSCT → lenograstim** — a legitimate but indirect association that should not be interpreted as direct therapeutic evidence for platelet release disorders.

---

## Clinical Trial Evidence

All 13 trials retrieved involve lenograstim in the context of hematopoietic stem cell transplantation. None directly study lenograstim for primary release disorder of platelets; all carry an indirect relevance grade (Grade C). The table below excludes two clearly off-topic trials (a COVID-19 antiviral trial and two CMV prophylaxis trials) that were returned as search noise.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00281879](https://clinicaltrials.gov/study/NCT00281879) | Phase 2 | Terminated | 200 | Unrelated donor HSCT for hematological malignancies; lenograstim used for donor HSC mobilization — no platelet release disorder endpoint |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Phase 2 | Completed | 60 | Allogeneic/syngeneic blood stem cell transplant for high-risk pediatric sarcomas; stem cell mobilization context only |
| [NCT00354172](https://clinicaltrials.gov/study/NCT00354172) | Phase 2 | Terminated | 16 | Umbilical cord blood transplant + NK cell infusion for myeloid leukemia not in CR; terminated early, unrelated to platelet function |
| [NCT00923364](https://clinicaltrials.gov/study/NCT00923364) | Phase 2 | Completed | 19 | Reduced-intensity HSCT feasibility study for GATA2 mutations; small pilot, no platelet release disorder focus |
| [NCT05436418](https://clinicaltrials.gov/study/NCT05436418) | Phase 1/2 | Recruiting | 260 | Optimizing post-transplant cyclophosphamide dose for GVHD prophylaxis after PBSCT; lenograstim is a mobilization adjunct, not the primary intervention |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Platform trial comparing GVHD prophylaxis regimens in mismatched unrelated donor PBSCT; lenograstim not the study drug |
| [NCT04047628](https://clinicaltrials.gov/study/NCT04047628) | Phase 3 | Recruiting | 156 | Autologous HSCT vs best available therapy for treatment-resistant relapsing MS; lenograstim role limited to mobilization |
| [NCT00076752](https://clinicaltrials.gov/study/NCT00076752) | Phase 2 | Completed | 9 | Autologous HSCT for severe SLE; very small pilot (n=9), disease and endpoints unrelated to platelet release disorders |
| [NCT00245037](https://clinicaltrials.gov/study/NCT00245037) | Phase 1/2 | Completed | 147 | Non-myeloablative allogeneic HSCT for hematological malignancies; lenograstim used in donor mobilization phase |
| [NCT05170828](https://clinicaltrials.gov/study/NCT05170828) | Phase 1 | Withdrawn | 0 | Cryopreserved mismatched unrelated donor bone marrow transplant study; withdrawn before enrolling any patients — no usable data |

---

## Literature Evidence

Currently no related literature available.

---

## Italy Market Information

Lenograstim has no registered product authorizations in Italy and is not currently marketed. There are no license records to display.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN score (99.91%), the prediction reflects a knowledge-graph inference via HSCT pathways rather than direct clinical evidence — no trial has tested lenograstim against platelet release disorders, no literature documents this use, and the drug's mechanism does not address the core pathophysiology of granule release defects. The absence of an Italian marketing authorization adds a further regulatory barrier before any clinical development could begin.

**To proceed, the following is needed:**
- Formal MOA documentation from DrugBank or an approved package insert to confirm whether any granule-biology or platelet-function effects are described
- Targeted literature review for case reports or mechanistic studies exploring G-CSF effects on platelet dense/alpha granule release
- Verification of whether allo-HSCT has documented curative outcomes specifically in primary platelet release disorders, and whether lenograstim was the mobilization agent used in those cases
- Preclinical (in vitro / murine) data assessing lenograstim's direct effect on megakaryocyte granule biogenesis
- Italian regulatory pathway assessment for pursuing a new indication from a currently non-marketed starting point
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

