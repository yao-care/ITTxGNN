---
layout: default
title: Vildagliptin
parent: 僅模型預測 (L5)
nav_order: 182
evidence_level: L5
indication_count: 10
---

# Vildagliptin
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

The txgnn-pipeline skill confirms this is a TxGNN report-writing task. Proceeding with the evaluation report using the Drug Repurposing Evaluation Report Prompt v5 guidelines.

---

# Vildagliptin: From Type 2 Diabetes to Classic Stiff Person Syndrome

## One-Sentence Summary

Vildagliptin is a selective DPP-4 (dipeptidyl peptidase-4) inhibitor established in the treatment of Type 2 Diabetes Mellitus, working by prolonging the activity of incretin hormones GLP-1 and GIP to improve glycemic control.
The TxGNN model's highest-ranked prediction is **Classic Stiff Person Syndrome** (99.88% score); however, this is currently supported by **no clinical trials and no publications**, making it a hypothesis-generating signal only.
Of note, **Type 1 Diabetes Mellitus** (rank 10, score 99.37%) carries the strongest real-world evidence in this analysis — including **1 Phase 2 double-blind RCT** and **20 publications** — and represents the most actionable repurposing signal in this pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus (established pharmacological use; no Italy regulatory record available) |
| Predicted New Indication | Classic Stiff Person Syndrome |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Italy Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Vildagliptin is a DPP-4 inhibitor — DPP-4 (also known as CD26) is a membrane-bound serine protease that rapidly degrades the incretin hormones GLP-1 and GIP after meal ingestion. By blocking this degradation, vildagliptin extends incretin activity, leading to glucose-dependent stimulation of insulin secretion and suppression of glucagon. This mechanism has proven efficacy in Type 2 Diabetes Mellitus.

The theoretical bridge to Classic Stiff Person Syndrome (SPS) runs through the immunological role of DPP-4/CD26. SPS is an autoimmune neurological disorder characterised by anti-GAD-65 antibody-mediated disruption of GABAergic interneuron function, resulting in progressive muscle rigidity and spasms. Because CD26 is highly expressed on activated T lymphocytes and modulates T-cell co-stimulation, DPP-4 inhibition could theoretically attenuate pathological T-cell activation, reducing autoimmune-driven neuronal damage. This immunomodulatory rationale has been explored in other autoimmune settings.

However, the mechanistic plausibility remains low for SPS specifically. Vildagliptin has no known direct action on the GABA system, and the core pathology of SPS is neurological rather than metabolic or broadly immunological. The identical TxGNN score shared between Classic SPS (rank 1) and Focal Stiff Limb Syndrome (rank 2, score 0.99884462…) strongly suggests these are treated as near-identical graph nodes by the model — reflecting shared ontology rather than independent biological signal. This prediction should be treated as a hypothesis only.

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
Classic Stiff Person Syndrome carries an L5 evidence classification — model prediction only — with zero supporting clinical trials or publications. The mechanistic link between DPP-4 inhibition and GABAergic autoimmune pathology is indirect and speculative, providing an insufficient basis for clinical investigation at this stage.

**To proceed, the following is needed:**
- Preclinical studies examining whether DPP-4/CD26 inhibition modulates anti-GAD-65 antibody production or T-cell autoreactivity in relevant animal models
- Mechanistic clarification of whether CD26 immunomodulation can meaningfully influence the GABAergic pathway disrupted in SPS
- A broader literature scan on DPP-4 inhibitors and autoimmune neurological disorders (e.g., multiple sclerosis, myasthenia gravis) to establish a class-level signal before focusing on SPS

---

> **⚠️ Advisory — Higher-Priority Signal Identified in This Pack**
>
> Among all 10 predicted indications, **Type 1 Diabetes Mellitus** (rank 10, TxGNN score 99.37%, Evidence Level **L2**) warrants a separate, dedicated evaluation. Supporting evidence includes:
> - **NCT02803892** (Phase 2 RCT, completed, n=55): *Rapamycin + Vildagliptin in long-standing T1DM* — the only direct Phase 2 double-blind trial of vildagliptin in T1DM, examining β-cell function recovery.
> - **PMID 33124663** (*J Clin Endocrinol Metab*, 2021): Double-blind RCT confirming β-cell function signals with Rapamycin + Vildagliptin.
> - **PMID 22855332** (*J Clin Endocrinol Metab*, 2012): Controlled clinical study showing vildagliptin reduces glucagon during hyperglycemia while preserving counterregulatory response during hypoglycemia in T1DM.
> - **PMID 30848158** (*Expert Opin Investig Drugs*, 2019): Systematic review on DPP-4 inhibitors in T1DM — β-cell protection and renal effects.
> - **20 publications in total**, including animal neogenesis studies, RCTs in adolescents with T1DM during Ramadan, and mechanistic human studies.
>
> The mechanistic rationale is substantially stronger: DPP-4 inhibition → ↑GLP-1 → β-cell neogenesis and survival, glucagon suppression, and potential CD26-mediated attenuation of autoimmune β-cell destruction. Recommended decision for this indication: **Research Question / Proceed with Guardrails** — a full evidence report for T1DM is advised.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

