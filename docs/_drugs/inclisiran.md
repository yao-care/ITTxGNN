---
layout: default
title: Inclisiran
parent: 僅模型預測 (L5)
nav_order: 125
evidence_level: L5
indication_count: 10
---

# Inclisiran
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

Using **txgnn-pipeline** for report context. Now analyzing the Evidence Pack and generating the evaluation report.

**Key analytical decisions:**
- `predicted_indications[0]` (potassium deficiency disease, rank 1) is explicitly flagged as a **typical false positive** in `repurposing_rationale` — building a primary report around it would be misleading
- Rank 8 "aortic malformation" has the only clinically meaningful evidence: 2 Phase 3 RCTs, L1 scoring, and a plausible mechanistic link via LDL-C/PCSK9 → aortic vascular disease
- Literature retrieved for rank 7 is exclusively about epilepsy genetics — irrelevant to inclisiran or migraine
- Inclisiran is a lipid-lowering siRNA, **not** antineoplastic → Cytotoxicity section omitted
- No Italian market authorizations → Italy Market Information table omitted per prohibition rules

---

# Inclisiran: From Hypercholesterolemia to Aortic Malformation

## One-Sentence Summary

Inclisiran is a hepatocyte-targeted siRNA that silences PCSK9 expression, originally developed to lower LDL cholesterol in patients with hypercholesterolemia and high cardiovascular risk.
The TxGNN model's highest-scored prediction (potassium deficiency disease, 99.93%) was assessed as a likely false positive with no mechanistic basis; the most clinically relevant prediction is **aortic malformation** (rank 8, 99.76%), with **2 active Phase 3 clinical trials** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypercholesterolemia / LDL-C reduction (global approval; not yet registered in Italy) |
| Predicted New Indication | Aortic Malformation (best-evidenced prediction, rank 8) |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L1 (2 recruiting Phase 3 RCTs) |
| Italy Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this evidence pack. Based on known information, inclisiran is a double-stranded siRNA that is taken up selectively by hepatocytes via GalNAc conjugation, where it directs RNA-induced silencing complex (RISC) to degrade PCSK9 mRNA. By reducing hepatic PCSK9 protein, LDL receptors on the hepatocyte surface are recycled rather than degraded, resulting in sustained LDL-C reductions of approximately 50% with just twice-yearly subcutaneous dosing. This is pharmacologically equivalent to PCSK9 antibody inhibitors (evolocumab, alirocumab) but with a fundamentally different delivery modality.

**A note on the full prediction landscape**: The top TxGNN-scored prediction (rank 1: potassium deficiency disease) was assessed by the evidence pipeline as a typical false positive — the PCSK9/LDL metabolic pathway has no known mechanistic intersection with renal or intestinal potassium homeostasis. The high score reflects graph-structural co-occurrence patterns in the knowledge graph rather than pharmacological plausibility. Ranks 2–7 and 9–10 are similarly unsupported (L5, Hold), and the 20 literature items retrieved for rank 7 (migraine susceptibility) are exclusively epilepsy genetics papers with no relation to inclisiran.

Rank 8 "aortic malformation" represents the most clinically actionable prediction. The disease label likely reflects an ontology mapping artifact: familial hypercholesterolemia (HoFH/HeFH) causes severe and accelerated atherosclerotic changes in the aorta that can register as structural aortic pathology in disease classification systems. Mechanistically, PCSK9 inhibition is plausible here on multiple grounds: substantial LDL-C lowering slows atherosclerotic progression in the aortic wall; PCSK9 protein is expressed in aortic valve interstitial cells, where its inhibition may attenuate BMP2/Wnt-mediated osteogenic and calcification signaling; and endothelial function improvement from reduced LDL-C burden may reduce aortic wall inflammation.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06597006](https://clinicaltrials.gov/study/NCT06597006) | Phase 3 | Recruiting | 9 | Double-blind inclisiran vs. placebo (Year 1) followed by open-label inclisiran (Year 2) in children aged 2–<12 years with homozygous familial hypercholesterolemia (HoFH) and elevated LDL-C; evaluates safety, tolerability, and efficacy |
| [NCT06597019](https://clinicaltrials.gov/study/NCT06597019) | Phase 3 | Recruiting | 51 | Same two-part double-blind/open-label design as NCT06597006; targets children aged 6–<12 years with heterozygous familial hypercholesterolemia (HeFH) and elevated LDL-C; anticipated completion April 2029 |

> **Caution**: Both trials are still recruiting with small sample sizes (n=9 and n=51). The disease label "aortic malformation" in the TxGNN mapping requires verification against the actual trial primary endpoints — the trials target familial hypercholesterolemia, not structural aortic malformation per se. Confidence in the L1 rating reflects inclisiran's established Phase 3 evidence base in adults (ORION program), not these pediatric trials alone.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two active Phase 3 trials directly test inclisiran in pediatric familial hypercholesterolemia — a condition with well-documented aortic and cardiovascular consequences — and inclisiran already holds EMA approval in adults, providing a substantial established safety and efficacy foundation. However, both pediatric trials are still recruiting with limited enrollment, the "aortic malformation" disease label requires ontology clarification, and Italy-specific regulatory authorization has not yet been established.

**To proceed, the following is needed:**

- **Clarify disease mapping**: Confirm whether "aortic malformation" in TxGNN maps to aortic atherosclerosis, aortic valve calcification, or familial hypercholesterolemia-related structural aortic pathology — this determines whether the prediction is a true repurposing signal or an extension-of-label finding
- **Obtain MOA data**: Retrieve full DrugBank mechanism-of-action record for inclisiran (Data Gap DG002) to support mechanistic-link analysis
- **Obtain safety data**: Download and parse the full package insert from EMA/AIFA (Data Gap DG001) to complete safety screening, including pregnancy/lactation, hepatic impairment, and injection-site reaction profile
- **Monitor trial completion**: NCT06597006 and NCT06597019 both have estimated completion in April 2029; interim data releases should be tracked
- **Italy market pathway**: Inclisiran (Leqvio®) holds EMA approval; AIFA registration and reimbursement classification (Fascia A/H) should be evaluated separately from this repurposing analysis
- **Re-evaluate rank 1–7 predictions**: A secondary literature sweep specifically combining "inclisiran" + each disease term is recommended to confirm absence of any emerging signals, particularly for migraine (rank 4/6/7) given the theoretical PCSK9 neuronal expression hypothesis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

