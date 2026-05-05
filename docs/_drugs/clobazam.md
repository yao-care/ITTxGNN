---
layout: default
title: Clobazam
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L5
indication_count: 10
---

# Clobazam
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

以下是依照 Evidence Pack 生成的完整評估報告：

---

# Clobazam: From Lennox-Gastaut Syndrome (Adjunctive Therapy) to Febrile Infection-Related Epilepsy Syndrome

## One-Sentence Summary

Clobazam is a 1,5-benzodiazepine with established use as an anxiolytic and as adjunctive antiseizure therapy — most notably for Lennox-Gastaut syndrome (LGS), for which it holds FDA approval.
The TxGNN model predicts it may be effective for **Febrile Infection-Related Epilepsy Syndrome (FIRES)**,
with **0 clinical trials** and **2 publications** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anxiolytic; adjunctive antiseizure treatment in LGS (no Italy authorization on file) |
| Predicted New Indication | Febrile Infection-Related Epilepsy Syndrome (FIRES) |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, clobazam is a 1,5-benzodiazepine — structurally distinct from classical 1,4-benzodiazepines (such as diazepam and clonazepam). Published literature consistently describes it as a positive allosteric modulator of GABA-A receptors with a reported preference for α2/α3 subunits over α1, which may translate to a broader antiseizure spectrum and relatively lower sedation burden. This has supported its role not only as an anxiolytic but as an adjunctive antiseizure agent in drug-resistant syndromes, including LGS and Dravet syndrome (where it forms part of the approved stiripentol protocol).

FIRES is an ultra-refractory form of new-onset status epilepticus triggered by a febrile illness, predominantly affecting previously healthy children. Clinical management centres on pharmacological coma with IV midazolam or other general anaesthetics — agents that share the same GABA-A modulatory mechanism as clobazam. The TxGNN prediction is mechanistically grounded: as seizures in FIRES are driven by GABA-A circuit failure, enhancing inhibitory tone via GABA-A modulation is both the established acute strategy and the logical target for maintenance. Clobazam's oral and enteral bioavailability gives it a distinct advantage as a potential transition agent during the critical weaning phase, when patients must be shifted away from IV sedation. One case series in the evidence base (PMID 35770765) demonstrates enteral lorazepam as an effective weaning substitute in midazolam-dependent FIRES patients, directly illustrating the clinical rationale that could extend to clobazam.

It should be noted that no clinical trials have been registered specifically investigating clobazam in FIRES, and the disease is extremely rare and severe. The TxGNN score of 99.82% most likely reflects the strong mechanistic overlap within the benzodiazepine–GABA-A landscape rather than disease-specific efficacy data. The prediction should currently be treated as a hypothesis to be explored rather than a clinical recommendation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35770765](https://pubmed.ncbi.nlm.nih.gov/35770765/) | 2022 | Case Series | Epileptic Disorders | Enteral lorazepam used as a successful weaning substitute in midazolam-dependent FIRES patients; supports the concept of oral/enteral benzodiazepine transition therapy during BZD weaning phase |
| [39958143](https://pubmed.ncbi.nlm.nih.gov/39958143/) | 2025 | Case Report | Cureus | Perampanel reduced barbiturate dependency in a 13-year-old with FIRES; highlights the unmet clinical need for non-anaesthetic weaning agents and the relevance of non-IV antiseizure options |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between clobazam's GABA-A modulation and FIRES pathophysiology is plausible, but the current evidence base consists of only 2 case-level publications involving related benzodiazepines — not clobazam itself. No clinical trials have been registered, and the evidence level is L4. Italy has no marketing authorization for clobazam, and safety data is unavailable for formal evaluation.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) from DrugBank to formally confirm GABA-A subunit binding profile
- Italy/TFDA package insert warnings and contraindications to complete the safety profile
- Prospective case series or pilot trial evaluating clobazam specifically as an enteral weaning agent in FIRES or NORSE (New-Onset Refractory Status Epilepticus)
- Drug-drug interaction profile with agents commonly co-administered in FIRES ICU management (e.g., ketamine, phenobarbital, valproate, topiramate)
- Clarification of regulatory pathway: clobazam is currently not marketed in Italy, so any clinical use would require compassionate use or off-label authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

