---
layout: default
title: Lanadelumab
parent: 僅模型預測 (L5)
nav_order: 129
evidence_level: L5
indication_count: 10
---

# Lanadelumab
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

Using the `txgnn-pipeline` skill as context — this is an Italy-market evaluation for a drug not yet registered in Italy. The skill confirms standard TxGNN workflow applies. Now generating the full report based on the Evidence Pack:

---

# Lanadelumab: From Hereditary Angioedema to C1 Inhibitor Deficiency

## One-Sentence Summary

Lanadelumab (Takhzyro) is a fully human monoclonal antibody globally approved since 2018 for preventing acute attacks of Hereditary Angioedema (HAE) due to C1 inhibitor deficiency, but not yet registered in Italy.
The TxGNN model predicts it highly effective for **C1 Inhibitor Deficiency (HAE Type I/II)** in the Italian market, backed by **22 clinical trials** and **20 publications**.
This represents one of the strongest evidence bases encountered in rare disease drug evaluation, with multiple completed Phase 3 RCTs and a pivotal publication in JAMA confirming efficacy.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HAE Type I/II attack prevention (globally approved; no Italian registration found) |
| Predicted New Indication | C1 Inhibitor Deficiency |
| TxGNN Prediction Score | 99.9955% |
| Evidence Level | L1 |
| Italy Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Lanadelumab is a fully human IgG1 monoclonal antibody that selectively inhibits plasma kallikrein (pKal), a serine protease at the centre of the contact activation pathway. In patients with HAE Type I or II, mutations in the *SERPING1* gene lead to deficiency or dysfunction of C1 inhibitor (C1-INH). C1-INH is the principal brake on the contact activation cascade — without it, pKal activity runs unchecked, cleaving high-molecular-weight kininogen (HMWK) to release excessive bradykinin. Bradykinin then acts on B2 receptors to cause fluid extravasation into subcutaneous and submucosal tissues, producing the painful, potentially life-threatening swelling episodes that define HAE. By directly blocking pKal upstream, lanadelumab prevents bradykinin overproduction before an attack begins, rather than treating it after the fact.

C1 inhibitor deficiency is not merely related to HAE Type I/II — it *is* its biochemical definition. The predicted indication and the drug's established mechanism are therefore a direct one-to-one match. The pivotal HELP Phase 3 RCT (NCT02586805, published in JAMA 2018) demonstrated statistically significant and clinically meaningful reductions in attack frequency versus placebo, leading to FDA approval in August 2018 and EMA approval shortly thereafter. Phase 3 studies across Japanese, Chinese, and paediatric populations have since replicated these findings, while multiple large real-world programmes (ENABLE, EMPOWER, INTEGRATED) confirm sustained effectiveness in routine clinical practice.

The TxGNN model's near-perfect prediction score (>99.99%) reflects the strength of this mechanistic and clinical relationship within the drug–disease knowledge graph. This is not a novel repurposing hypothesis requiring speculative extrapolation — it is a strong computational confirmation of an established clinical reality that Italy has yet to formally register.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02586805](https://clinicaltrials.gov/study/NCT02586805) | Phase 3 | Completed | 125 | **HELP Study** — Pivotal Phase 3 double-blind RCT of DX-2930 (lanadelumab) vs placebo in HAE Type I/II. Demonstrated significant reduction in acute angioedema attack rate; primary basis for FDA and EMA regulatory approval. |
| [NCT02741596](https://clinicaltrials.gov/study/NCT02741596) | Phase 3 | Completed | 212 | **HELP OLE** — Long-term open-label extension; evaluated sustained safety and efficacy of lanadelumab over an extended treatment period (>4 years) in HAE Type I/II. |
| [NCT04070326](https://clinicaltrials.gov/study/NCT04070326) | Phase 3 | Completed | 21 | **SPRING Study** — Paediatric Phase 3 trial in children aged 2–<12 years; assessed pharmacokinetics, pharmacodynamics, safety, and reduction in HAE attack frequency. |
| [NCT05460325](https://clinicaltrials.gov/study/NCT05460325) | Phase 3 | Completed | 20 | Multicenter open-label study in Chinese patients with HAE; evaluated safety profile and pharmacokinetics over 26 weeks. |
| [NCT04180163](https://clinicaltrials.gov/study/NCT04180163) | Phase 3 | Completed | 12 | Japanese Phase 3 study; confirmed safety and efficacy of lanadelumab in Japanese HAE Type I/II patients. |
| [NCT04444895](https://clinicaltrials.gov/study/NCT04444895) | Phase 3 | Completed | 73 | Long-term open-label study in non-histaminergic angioedema with normal C1-INH; explored lanadelumab efficacy beyond classical HAE Type I/II. |
| [NCT04130191](https://clinicaltrials.gov/study/NCT04130191) | N/A | Completed | 140 | **ENABLE Study** — 3-year prospective real-world observational study comparing HAE attack rates before and after lanadelumab initiation in routine clinical practice across multiple countries. |
| [NCT03845400](https://clinicaltrials.gov/study/NCT03845400) | N/A | Completed | 168 | **EMPOWER Study** — US and Canada real-world cohort; compared HAE attack frequency pre- and post-lanadelumab initiation over ≥24 months, with data collected via smartphone application. |
| [NCT05147181](https://clinicaltrials.gov/study/NCT05147181) | N/A | Completed | 48 | Polish National Drug Program observational study; documented proportion of attack-free patients, attack characteristics, and rescue treatment use in real-life HAE care. |
| [NCT04861090](https://clinicaltrials.gov/study/NCT04861090) | N/A | Completed | 207 | Retrospective multicountry chart review; assessed real-world attack-free rates with lanadelumab dosed every 2 weeks and every 4 weeks. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [30480729](https://pubmed.ncbi.nlm.nih.gov/30480729/) | 2018 | RCT | JAMA | HELP trial primary results: lanadelumab significantly reduced HAE attack rate vs placebo across all dose regimens; the landmark publication underpinning global regulatory approval. |
| [34287942](https://pubmed.ncbi.nlm.nih.gov/34287942/) | 2022 | Extension Study | Allergy | HELP OLE: sustained reduction in HAE attacks confirmed over ≥4 years of treatment; durable efficacy and acceptable long-term safety profile. |
| [39701274](https://pubmed.ncbi.nlm.nih.gov/39701274/) | 2025 | Real-World Study | J Allergy Clin Immunol Pract | INTEGRATED multicountry observational study: real-world effectiveness of lanadelumab across multiple countries confirms phase 3 findings in everyday clinical practice. |
| [40434599](https://pubmed.ncbi.nlm.nih.gov/40434599/) | 2025 | Network Meta-Analysis | Drugs R&D | Network meta-analysis comparing lanadelumab, garadacimab, SC C1-INH, and berotralstat for HAE long-term prophylaxis; provides indirect head-to-head comparative efficacy and safety data. |
| [39508959](https://pubmed.ncbi.nlm.nih.gov/39508959/) | 2024 | Systematic Review | Clin Rev Allergy Immunol | Systematic review of breakthrough HAE attacks during long-term prophylaxis; characterises attack burden in patients on lanadelumab and other agents. |
| [32187470](https://pubmed.ncbi.nlm.nih.gov/32187470/) | 2020 | Review | N Engl J Med | Comprehensive NEJM review of hereditary angioedema: pathophysiology, diagnostic criteria, and current treatment landscape including lanadelumab. |
| [30267321](https://pubmed.ncbi.nlm.nih.gov/30267321/) | 2018 | Approval Review | Drugs | First Global Approval summary: mechanism of action, PK/PD profile, clinical trial results, and regulatory milestones for lanadelumab (Takhzyro). |
| [30539362](https://pubmed.ncbi.nlm.nih.gov/30539362/) | 2019 | Review | BioDrugs | Detailed review of preclinical and Phase I data supporting lanadelumab's mechanism validation, pharmacokinetics, and early clinical safety in C1-INH-HAE. |
| [39836016](https://pubmed.ncbi.nlm.nih.gov/39836016/) | 2025 | Indirect Comparison | J Comp Effectiveness Res | Indirect treatment comparison of lanadelumab vs C1-esterase inhibitor in paediatric HAE (aged <12 years); supports lanadelumab's relative efficacy and safety in children. |
| [37328263](https://pubmed.ncbi.nlm.nih.gov/37328263/) | 2023 | Real-World Study | Allergy Asthma Proc | Healthcare resource utilisation in new users of lanadelumab vs subcutaneous C1-INH in US real-world setting; includes demographics, cost data, and clinical outcomes. |

---

## Italy Market Information

No authorizations for lanadelumab are currently registered in Italy (0 AIFA licenses). Lanadelumab is globally marketed as **Takhzyro** (Takeda, formerly Shire), with centralised EMA approval since 2018 and FDA approval since August 2018, for prophylaxis of HAE attacks in patients aged ≥12 years. Approval has since been extended to children aged 2–<12 years in some jurisdictions. A formal regulatory submission to AIFA would be required for Italian market entry, though the EMA approval pathway may facilitate an expedited process.

---

## Safety Considerations

Please refer to the Takhzyro European Summary of Product Characteristics (SmPC) for complete safety information. Detailed Italian-specific safety data (AIFA package insert warnings, contraindications, and drug-drug interactions) could not be retrieved, as lanadelumab is not currently registered in Italy and no DDI data were identified in the available databases.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Lanadelumab has robust **L1-level evidence** for C1 inhibitor deficiency (HAE Type I/II), anchored by multiple completed Phase 3 RCTs — including the pivotal JAMA-published HELP trial — and reinforced by large real-world programmes across the US, Europe, Japan, and China. The TxGNN prediction score of >99.99% is a computational confirmation of a well-established clinical indication, not a speculative hypothesis. The sole barrier to use in Italy is regulatory registration, not evidence.

**To proceed, the following is needed:**
- Initiate AIFA regulatory review using the EMA centralised approval package (Takhzyro SmPC), leveraging the mutual recognition / decentralised procedure pathway
- Obtain and review the full EMA SmPC for complete contraindications, warnings, and drug-drug interaction data before clinical use
- Assess reimbursement eligibility for HAE Type I/II under the Italian NHS (SSN), including potential bridging access via Law 648/96 while formal approval is pending
- Identify accredited HAE specialist and angioedema reference centres in Italy to ensure appropriate patient selection, monitoring, and pharmacovigilance reporting
- Develop a risk management plan (RMP) consistent with EMA PASS requirements, particularly for paediatric and high-risk populations (e.g. renal transplant patients, as highlighted in recent literature)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

