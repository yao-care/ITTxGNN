---
layout: default
title: Tiapride
parent: 僅模型預測 (L5)
nav_order: 198
evidence_level: L5
indication_count: 1
---

# Tiapride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Tiapride: From Movement Disorders to Migraine Disorder

## One-Sentence Summary

Tiapride is a selective dopamine D2/D3 receptor antagonist of the benzamide class, primarily used for movement disorders (dyskinesia, choreiform movements in Huntington's disease), alcohol withdrawal syndrome, and agitation in elderly patients.
The TxGNN model predicts it may be effective for **Migraine Disorder**,
with **0 registered clinical trials** and **10 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Movement disorders (dyskinesia, chorea), alcohol withdrawal, agitation |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L2 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, tiapride is a selective D2/D3 dopamine receptor antagonist of the benzamide class, whose efficacy in movement disorders and alcohol withdrawal syndrome is well established in the literature.

Mechanistically, the link to migraine is well-supported: dopaminergic signalling abnormalities play a documented role in migraine pathophysiology, particularly in premonitory symptoms such as yawning, nausea, and mood changes. D2/D3 receptor antagonism may (1) suppress dopamine-mediated premonitory symptoms, (2) modulate central pain sensitisation through downstream CGRP pathway effects, and (3) exert antiemetic actions that reduce the overall burden of migraine attacks.

This rationale is further reinforced by the established use of closely related benzamide drugs — particularly sulpiride — in migraine prevention, suggesting a class effect. Multiple historical controlled trials and a 2022 randomised pilot study directly comparing tiapride with topiramate (a guideline-recommended first-line prophylactic agent) provide convergent clinical support for the TxGNN prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered on ClinicalTrials.gov or ICTRP.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35548913](https://pubmed.ncbi.nlm.nih.gov/35548913/) | 2022 | RCT | Revista de neurologia | Randomised double-blind pilot study: tiapride vs. topiramate as prophylaxis for chronic migraine — head-to-head comparison of efficacy and safety |
| [6256904](https://pubmed.ncbi.nlm.nih.gov/6256904/) | 1980 | Controlled Study | La semaine des hopitaux | Placebo-controlled study (n=40): tiapride clearly demonstrated efficacy in migraine, with concurrent improvement of associated dyspeptic symptoms |
| [6266020](https://pubmed.ncbi.nlm.nih.gov/6266020/) | 1981 | Controlled Trial | La semaine des hopitaux | Controlled trial (n=25) in intractable migraine and facial vascular pain: excellent response in 10/25 cases; tiapride recommended when standard therapy has failed |
| [7323625](https://pubmed.ncbi.nlm.nih.gov/7323625/) | 1981 | Clinical Study | Rivista di patologia nervosa e mentale | Double-blind trial (n=50, including classical migraine subgroup): 65% of patients showed clinical benefit in headache intensity and frequency |
| [6293072](https://pubmed.ncbi.nlm.nih.gov/6293072/) | 1982 | Clinical Study | La semaine des hopitaux | Prospective study (n=180 headache patients): 71% achieved good or excellent results with tiapride 300 mg/day, irrespective of headache aetiology |
| [6528587](https://pubmed.ncbi.nlm.nih.gov/6528587/) | 1984 | Comparative Review | Wiadomosci lekarskie | Review of benzamides (sulpiride, tiapride) in preventive migraine treatment; supports a class-level D2 antagonist effect in migraine prophylaxis |
| [211624](https://pubmed.ncbi.nlm.nih.gov/211624/) | 1978 | Review | La semaine des hopitaux | Treatment overview: tiapride's combined analgesic, antiemetic, and mild anticompulsive actions favour its use in headache associated with masked depression |
| [39344](https://pubmed.ncbi.nlm.nih.gov/39344/) | 1979 | Case Series | La semaine des hopitaux | 4 migraine patients treated for ≥6 months: all showed excellent or very good outcomes; headache frequency and severity markedly reduced or resolved |
| [229563](https://pubmed.ncbi.nlm.nih.gov/229563/) | 1979 | Case Series | La semaine des hopitaux | Geriatric cohort (n=47): tiapride effective across multiple indications including headache, with doses up to 800 mg/day for refractory cases |
| [35831](https://pubmed.ncbi.nlm.nih.gov/35831/) | 1978 | Review | La semaine des hopitaux | Clinical practice review of chronic headache treatment: psychotropic agents including tiapride noted for definite, well-tolerated efficacy |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple historical controlled trials and a 2022 randomised head-to-head pilot study versus topiramate provide convergent support for tiapride's efficacy in migraine prophylaxis, underpinned by a mechanistically coherent D2/D3 antagonism hypothesis; however, much of the existing evidence predates modern trial standards, pilot-scale RCT data requires replication, and tiapride holds no current marketing authorisation in Italy.

**To proceed, the following is needed:**
- Obtain and review the full package insert (AIFA/EMA-equivalent) to characterise contraindications, warnings, and drug interactions (currently blocking data gap DG001)
- Retrieve mechanism of action details via DrugBank API to complete the mechanistic evidence dossier (data gap DG002)
- Clarify regulatory status in the EU: tiapride holds authorisations in France and other EU member states — verify whether an AIFA recognition or MRP/DCP pathway is applicable
- Commission or identify a well-powered Phase 2/3 RCT to upgrade evidence from pilot-level L2 to L1
- Establish a targeted safety monitoring plan covering QTc prolongation risk (class effect for dopamine antagonists), extrapyramidal symptoms, hyperprolactinaemia, and sedation — particularly relevant in the migraine patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

