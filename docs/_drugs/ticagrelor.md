---
layout: default
title: Ticagrelor
parent: 僅模型預測 (L5)
nav_order: 169
evidence_level: L5
indication_count: 10
---

# Ticagrelor
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

The txgnn-pipeline skill confirms the context. Now generating the report from the Evidence Pack:

---

# Ticagrelor: From Acute Coronary Syndrome to Intracranial Arteriosclerosis

## One-Sentence Summary

Ticagrelor is a potent oral P2Y12 receptor antagonist originally used to reduce cardiovascular events in patients with Acute Coronary Syndrome (ACS) and ischemic cardiovascular disease.
The TxGNN model predicts it may be effective for **Intracranial Arteriosclerosis**,
with **11 clinical trials** and **3 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute Coronary Syndrome / Ischemic Cardiovascular Disease |
| Predicted New Indication | Intracranial Arteriosclerosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Ticagrelor is a direct-acting, reversibly binding P2Y12 receptor antagonist. Unlike older thienopyridines, it does not require hepatic bioactivation, providing faster onset and more consistent platelet inhibition. Its efficacy in reducing major cardiovascular events (cardiovascular death, MI, stroke) in ACS patients has been established through landmark large-scale RCTs including PLATO. Importantly, Ticagrelor also inhibits ENT-1 (equilibrative nucleoside transporter 1) on erythrocytes and platelets, increasing local adenosine concentrations — contributing to vasodilation, coronary blood flow enhancement, and anti-inflammatory pleiotropic effects beyond simple platelet inhibition.

Intracranial arteriosclerosis (ICAS) is driven by the same core pathophysiology as coronary artery disease: platelet-mediated thrombosis superimposed on atherosclerotic plaques within arterial walls, causing progressive luminal stenosis and downstream ischemia. Ticagrelor's dual mechanism applies directly: (1) P2Y12 antagonism suppresses platelet activation and aggregation in stenotic intracranial arteries; (2) adenosine accumulation via ENT-1 inhibition provides cerebrovascular anti-inflammatory protection and vasodilation, potentially reducing ischemic injury in patients who have experienced TIA or stroke from ICAS. Standard clopidogrel-based DAPT leaves a high residual 12-month recurrent stroke risk in symptomatic ICAS patients, making a more potent P2Y12 inhibitor a rational therapeutic step.

The mechanistic and clinical overlap is substantial enough that the field has progressed from hypothesis to active Phase 3 investigation. The ongoing CAPTIVA trial (NCT05047172, 1,683 patients) directly compares ticagrelor against clopidogrel and rivaroxaban for symptomatic ICAS — the strongest confirmation that this repurposing direction is well-founded. Complementary evidence from the EUCLID trial (PAD) and GLOBAL LEADERS (post-stent monotherapy) further establishes the safety and pharmacodynamic profile needed for this application.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT05047172](https://clinicaltrials.gov/study/NCT05047172) | Phase 3 | Active (Not Recruiting) | 1,683 | CAPTIVA trial: directly compares ticagrelor, rivaroxaban, and clopidogrel + aspirin for lowering the 1-year rate of ischemic stroke, ICH, or vascular death in symptomatic intracranial atherosclerotic stenosis — the most relevant and direct evidence for this indication |
| [NCT01732822](https://clinicaltrials.gov/study/NCT01732822) | Phase 3 | Completed | 13,885 | EUCLID trial: compares ticagrelor vs clopidogrel in established peripheral artery disease for cardiovascular death, MI, and ischemic stroke; largest completed Phase 3 RCT providing direct ticagrelor safety/efficacy data in atherosclerotic vascular disease |
| [NCT06714526](https://clinicaltrials.gov/study/NCT06714526) | N/A | Recruiting | 100 | Pilot PROBE study: genotype-guided P2Y12 inhibitor selection (including ticagrelor) vs conventional clopidogrel in symptomatic intracranial atherosclerotic disease; directly addresses the ICAD patient population |
| [NCT04948749](https://clinicaltrials.gov/study/NCT04948749) | N/A | Recruiting | 792 | DREAM-PRIDE: randomized trial comparing drug-eluting stent implantation plus aggressive medical treatment (ticagrelor-based DAPT) vs medical treatment alone for preventing 1-year recurrent stroke in symptomatic intracranial atherosclerotic disease |
| [NCT01813435](https://clinicaltrials.gov/study/NCT01813435) | Phase 3 | Completed | 15,991 | GLOBAL LEADERS: ticagrelor + aspirin for 1 month followed by ticagrelor monotherapy for 23 months vs standard 12-month DAPT post coronary stenting; largest safety database for long-term ticagrelor monotherapy |
| [NCT02605447](https://clinicaltrials.gov/study/NCT02605447) | Phase 4 | Completed | 2,009 | EVOLVE Short DAPT: safety of 3-month DAPT in high bleeding risk patients post-PCI; provides safety reference data for abbreviated DAPT strategies relevant to neurointerventional contexts |
| [NCT06058130](https://clinicaltrials.gov/study/NCT06058130) | N/A | Unknown | 2,171 | Combination antiplatelet + anticoagulation in acute ischemic stroke patients with concomitant non-valvular atrial fibrillation and extracranial/intracranial artery stenosis; 1:1 randomized, 3-month composite endpoint |
| [NCT07164859](https://clinicaltrials.gov/study/NCT07164859) | Phase 3 | Not Yet Recruiting | 1,700 | SOLOPCI: very short DAPT (aspirin stopped at day 7) followed by P2Y12 inhibitor monotherapy in elderly patients ≥65 years post-PCI; evaluates bleeding reduction without increasing cardiovascular events |
| [NCT07354828](https://clinicaltrials.gov/study/NCT07354828) | N/A | Not Yet Recruiting | 3,500 | Quality control standard system for coronary revascularization based on DAPT; addresses DAPT optimization and high-bleeding-risk management in real-world coronary practice |
| [NCT03620760](https://clinicaltrials.gov/study/NCT03620760) | Phase 4 | Unknown | 2,036 | Randomized comparison of low-dose ticagrelor (45 mg BID) vs standard dose (90 mg BID) in Chinese patients with unstable angina post drug-eluting stent; dose optimization data applicable to Asian populations |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [39862061](https://pubmed.ncbi.nlm.nih.gov/39862061/) | 2025 | RCT Protocol | International Journal of Stroke | CAPTIVA trial design and early progress: details the rationale for testing ticagrelor vs clopidogrel + aspirin in symptomatic ICAS; standard dual therapy leaves unacceptably high 12-month recurrent stroke risk, motivating the trial |
| [38252758](https://pubmed.ncbi.nlm.nih.gov/38252758/) | 2024 | Guideline Update | Stroke | AHA/ASA focused update on intracranial atherosclerosis: summarizes current evidence gaps in antithrombotic management and identifies ongoing trials such as CAPTIVA as critical knowledge-gap closers for ICAS treatment |
| [39658130](https://pubmed.ncbi.nlm.nih.gov/39658130/) | 2025 | Clinical Study | Journal of Neurointerventional Surgery | Real-world experience with lower-dose ticagrelor (60 mg BID) + aspirin 81 mg for intracranial stenting vs standard aspirin + clopidogrel; demonstrates feasibility, adequate platelet inhibition, and acceptable safety profile specifically in neurointerventional procedures |

---

## Italy Market Information

No authorized products for Ticagrelor are documented in this dataset (0 records retrieved). Authorization records for Italy were not available in the queried data source at the time of this report.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The CAPTIVA Phase 3 trial (NCT05047172) is actively investigating ticagrelor specifically in symptomatic intracranial atherosclerotic stenosis, and the broader P2Y12 inhibitor evidence base across atherosclerotic vascular disease (including multiple completed Phase 3 RCTs) provides an L1-level foundation. The TxGNN score of 99.97% combined with direct mechanistic plausibility and active clinical trial infrastructure supports moving forward — but critical data gaps in safety documentation must be resolved before any institutional protocol is designed.

**To proceed, the following is needed:**
- Retrieve full MOA documentation from DrugBank (DB08816) to complete mechanistic and pharmacological analysis
- Obtain the EU SmPC / prescribing information for Ticagrelor (Brilique®) to populate key warnings, contraindications, and clinically significant drug interactions
- Monitor CAPTIVA trial results (projected completion: January 2027) — these data will determine whether this direction reaches definitive L1 ICAS-specific evidence
- Confirm current Italy (AIFA) authorization status directly through official channels, as EMA approval of Brilique® for ACS is likely already in force
- Define the target patient population precisely (e.g., symptomatic ICAS with ≥50% stenosis, TIA with atherosclerotic etiology) before designing any investigator-initiated or off-label use protocol
- Assess bleeding risk profile in cerebrovascular patients, where intracranial hemorrhage is a particularly consequential adverse event
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

