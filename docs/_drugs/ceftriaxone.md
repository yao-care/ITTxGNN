---
layout: default
title: Ceftriaxone
parent: 僅模型預測 (L5)
nav_order: 49
evidence_level: L5
indication_count: 7
---

# Ceftriaxone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

以下是根據 Evidence Pack 產生的評估報告：

---

# Ceftriaxone: From Serious Bacterial Infections to Infectious Otitis Media

## One-Sentence Summary

Ceftriaxone is a third-generation cephalosporin antibiotic with well-established global use for serious bacterial infections including meningitis, sepsis, and pneumonia.
The TxGNN model predicts it may be effective for **Infectious Otitis Media**,
with **3 clinical trials** and **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Serious bacterial infections (3rd-generation cephalosporin) |
| Predicted New Indication | Infectious Otitis Media |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L2 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on known pharmacological information, ceftriaxone is a third-generation cephalosporin that inhibits bacterial cell wall synthesis by binding to penicillin-binding proteins (PBPs) — particularly PBP2b and PBP2x — disrupting peptidoglycan cross-linking and causing bactericidal cell lysis. This mechanism confers broad-spectrum activity against both Gram-positive and Gram-negative pathogens.

The three primary organisms responsible for acute otitis media (AOM) — *Streptococcus pneumoniae*, *Haemophilus influenzae*, and *Moraxella catarrhalis* — are all highly susceptible to ceftriaxone. Two RCTs (PMID 8989332, 11099083) have demonstrated its efficacy in treatment-refractory AOM, particularly when first-line oral antibiotics have failed. Its long elimination half-life (~8 hours) supports single-dose or short-course intramuscular regimens (IM 50 mg/kg/day), which is especially practical in paediatric settings where oral adherence is poor or rapid clinical response is needed.

The mechanistic connection is direct: ceftriaxone targets the causative pathogens of infectious otitis media through the same antibacterial mechanism that underpins its broader infectious disease use. Pharmacokinetic data show adequate drug penetration into middle ear fluid, providing further biological plausibility for the TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01511107](https://clinicaltrials.gov/study/NCT01511107) | Phase 2 | Terminated | 520 | Randomised double-blind placebo-controlled trial comparing 5-day vs. 10-day antibiotic treatment for AOM in children aged 6–23 months — most directly relevant to antibiotic therapy duration in AOM; terminated early (reason not reported) |
| [NCT02567825](https://clinicaltrials.gov/study/NCT02567825) | NA | Completed | 250 | Tympanostomy tube placement vs. nonsurgical management for recurrent AOM — surgical RCT providing comparative framework and AOM burden data over 2 years |
| [NCT01272999](https://clinicaltrials.gov/study/NCT01272999) | N/A | Completed | 391 | Postmarketing observational study of Prevnar 13 impact on AOM incidence in children — confirms pneumococcal pathogen relevance in the AOM disease context |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [8989332](https://pubmed.ncbi.nlm.nih.gov/8989332/) | 1997 | RCT | *Pediatrics* | Prospective randomised single-blind trial: single-dose IM ceftriaxone vs. 10-day oral TMP-SMZ for AOM — ceftriaxone achieved comparable clinical efficacy |
| [11099083](https://pubmed.ncbi.nlm.nih.gov/11099083/) | 2000 | RCT | *Pediatric Infectious Disease Journal* | 1-day vs. 3-day IM ceftriaxone for non-responsive AOM in children — 3-day regimen demonstrated superior bacteriological and clinical outcomes |
| [39361280](https://pubmed.ncbi.nlm.nih.gov/39361280/) | 2024 | Clinical Guideline | *JAMA Network Open* | Optimal paediatric outpatient antibiotic prescribing — 50% of US prescriptions deemed unnecessary; ceftriaxone endorsed as appropriate salvage choice for AOM |
| [12166789](https://pubmed.ncbi.nlm.nih.gov/12166789/) | 2002 | Clinical Guideline | *Clinical Pediatrics* | Consensus recommendations for AOM management — ceftriaxone positioned as second-line agent when oral amoxicillin fails; provides prescribing decision criteria |
| [35841649](https://pubmed.ncbi.nlm.nih.gov/35841649/) | 2022 | Retrospective Cohort | *Int J Pediatric Otorhinolaryngology* | Ceftriaxone IM use for AOM in a large US academic primary care population — characterises real-world utilisation factors including rising IM use for otitis-conjunctivitis |
| [12237596](https://pubmed.ncbi.nlm.nih.gov/12237596/) | 2002 | Prospective Cohort | *Pediatric Infectious Disease Journal* | Nasopharyngeal carriage dynamics of *S. pneumoniae* after 3-day vs. 1-day IM ceftriaxone for non-responsive AOM — 3-day regimen better suppresses resistant strain carriage |
| [20802367](https://pubmed.ncbi.nlm.nih.gov/20802367/) | 2010 | Review | *Otology & Neurotology* | Prevention and treatment of AOM and meningitis in children with cochlear implants — ceftriaxone identified as preferred IV/IM agent for invasive pneumococcal AOM |
| [9877360](https://pubmed.ncbi.nlm.nih.gov/9877360/) | 1998 | Prospective | *Pediatric Infectious Disease Journal* | Bacteriological efficacy of 3-day IM ceftriaxone in non-responsive AOM — established pathogen eradication rates against drug-resistant *S. pneumoniae* |
| [30279114](https://pubmed.ncbi.nlm.nih.gov/30279114/) | 2019 | Surveillance Study | *Journal of Infection and Chemotherapy* | Antimicrobial susceptibility of AOM pathogens in Japan (2014–2017) — resistance trend data informing which cases warrant ceftriaxone escalation |
| [20660544](https://pubmed.ncbi.nlm.nih.gov/20660544/) | 2010 | Review | *Pediatrics* | Cochlear implant children: AOM and meningitis prevention and treatment guidelines — reinforces ceftriaxone as first-choice agent for complicated or invasive AOM |

---

## Italy Market Information

No marketing authorisations for Ceftriaxone were identified in the Italy (AIFA) regulatory database.

> **Note:** Ceftriaxone is widely available internationally under brand names such as Rocephin and is included in the WHO Model List of Essential Medicines. The absence of records in this dataset is likely a data gap rather than actual unavailability in Italy.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two independent RCTs and multiple clinical guidelines have established intramuscular ceftriaxone as an effective second-line agent for treatment-refractory acute otitis media, with a clear and direct mechanistic basis targeting the primary causative pathogens.

**To proceed, the following is needed:**
- Verify Italy (AIFA) regulatory status — absence of records likely reflects a data gap given ceftriaxone's global availability
- Retrieve and review full package insert warnings and contraindications (flagged as Data Gap in this dataset)
- Develop a paediatric dosing protocol with attention to neonatal safety given ceftriaxone's high protein binding (95–98%), which may displace bilirubin in neonates
- Conduct an antimicrobial stewardship assessment — ceftriaxone is a WHO Access-group antibiotic; expansion into AOM should be restricted to treatment-failure cases to limit resistance pressure
- Identify or commission a comparative RCT vs. high-dose amoxicillin in the European paediatric population to establish regional efficacy and formulary positioning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

