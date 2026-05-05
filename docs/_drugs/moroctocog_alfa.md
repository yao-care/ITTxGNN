---
layout: default
title: Moroctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 152
evidence_level: L5
indication_count: 8
---

# Moroctocog Alfa
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

Using `txgnn-pipeline` to confirm project context — confirmed. Now generating the report from the Evidence Pack.

---

# Moroctocog Alfa: From Hemophilia A to Primary Release Disorder of Platelets

## One-Sentence Summary

Moroctocog alfa is a B-domain deleted recombinant human coagulation Factor VIII (rFVIII), used in multiple countries for the treatment and prophylaxis of bleeding in patients with Hemophilia A.
The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**, however this prediction is supported by **no directly relevant clinical trials** and **no publications** — all 7 identified trials concern unrelated indications.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hemophilia A (Factor VIII deficiency); not registered in Italy |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, moroctocog alfa is a B-domain deleted recombinant human Factor VIII — a component of the intrinsic coagulation pathway. Its efficacy in Hemophilia A (congenital FVIII deficiency) is well established through factor replacement therapy.

Primary release disorder of platelets refers to defective α-granule or dense granule secretion, a primary hemostasis defect. This is mechanistically distinct from the secondary coagulation cascade where FVIII operates. FVIII replacement therapy restores thrombin generation via the intrinsic tenase complex, but it cannot correct the platelet secretory machinery. As the Evidence Pack's own mechanistic analysis notes, "FVIII replacement cannot repair platelet secretory granule function."

The high TxGNN score most likely results from knowledge graph generalisation through shared "bleeding phenotype" nodes (e.g., common ICD-10 hemorrhagic disorder co-classification), rather than a true pharmacological connection. This prediction should be treated as a model artefact pending further mechanistic investigation.

---

## Clinical Trial Evidence

Seven trials were identified, but **all are classified Grade C** — none directly test moroctocog alfa in primary release disorder of platelets.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04161495](https://clinicaltrials.gov/study/NCT04161495) | Phase 3 | Completed | 159 | BIVV001 (rFVIIIFc-VWF-XTEN fusion protein) prophylaxis in severe Hemophilia A — unrelated to platelet release disorders |
| [NCT04759131](https://clinicaltrials.gov/study/NCT04759131) | Phase 3 | Completed | 74 | BIVV001 safety and efficacy in pediatric severe Hemophilia A — same indication, different drug |
| [NCT01913405](https://clinicaltrials.gov/study/NCT01913405) | Phase 3 | Completed | 30 | PEGylated rFVIII (BAX 855) perioperative use in severe Hemophilia A — different drug, unrelated indication |
| [NCT07343687](https://clinicaltrials.gov/study/NCT07343687) | N/A | Not Yet Recruiting | 80 | Clinicohaematological and coagulation profiles in newly diagnosed AML patients on induction chemotherapy — no FVIII intervention |
| [NCT07400848](https://clinicaltrials.gov/study/NCT07400848) | N/A | Recruiting | 200 | Clinical assessment of Post-COVID-19 Vaccination Syndrome — completely unrelated |
| [NCT07329036](https://clinicaltrials.gov/study/NCT07329036) | N/A | Recruiting | 25 | Artificial liver support system (DPMAS + TPE) in acute-on-chronic liver failure — no FVIII intervention |
| [NCT07439939](https://clinicaltrials.gov/study/NCT07439939) | N/A | Recruiting | 45 | Portal and systemic hemostasis during TIPS placement — observational only, no FVIII intervention |

> ⚠️ None of these trials constitute direct evidence for moroctocog alfa in primary release disorder of platelets.

---

## Literature Evidence

Currently no related literature available.

---

## Italy Market Information

Moroctocog alfa is **not registered or marketed in Italy**. No marketing authorizations have been identified.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic connection between FVIII replacement (moroctocog alfa) and primary release disorder of platelets is not pharmacologically supported — platelet granule secretion defects are independent of the coagulation Factor VIII pathway. Furthermore, there are zero directly relevant clinical trials and zero publications; the 7 trials identified all concern unrelated conditions.

**To proceed, the following is needed:**
- Establish a credible mechanistic hypothesis explaining how FVIII supplementation would address platelet granule release dysfunction (currently none exists)
- Consult a specialist in platelet function disorders to assess whether any patient subgroup could plausibly benefit
- Investigate whether the high TxGNN score reflects a data artefact (shared ICD bleeding-phenotype node) rather than a biological signal — consider reviewing the knowledge graph edges connecting moroctocog alfa to this disease node
- Obtain the full package insert (EMA SmPC or TFDA 仿單) to complete the safety gap assessment before any further clinical evaluation
- If interest in FVIII repurposing for bleeding disorders persists, redirect analysis to **Rank 4: Acquired Coagulation Factor Deficiency** (Evidence Level L3, 13 clinical trials including Grade B studies, recommendation: Research Question), which has a substantially more credible mechanistic rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

