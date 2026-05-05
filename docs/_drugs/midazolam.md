---
layout: default
title: Midazolam
parent: 僅模型預測 (L5)
nav_order: 147
evidence_level: L5
indication_count: 1
---

# Midazolam
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

Using the `txgnn-pipeline` skill to confirm context. The skill applies to this TxGNN drug repurposing report generation task. Now generating the report from the Evidence Pack.

---

# Midazolam: From Procedural Sedation to Insomnia

## One-Sentence Summary

Midazolam is a short-acting benzodiazepine widely used in clinical practice for procedural sedation, anesthesia induction, and ICU sedation.
The TxGNN model predicts it may be effective for **Insomnia**, with a prediction confidence of **99.74%**.
The evidence base includes **4 published RCTs** (1981–1990) directly studying midazolam for sleep disorders, alongside several comparative sedation trials, yielding an overall **L2** evidence level.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Procedural sedation / Anaesthesia induction (established clinical use; no Italy authorization on file) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L2 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Midazolam is a short-acting benzodiazepine that acts as a **positive allosteric modulator of the GABA-A receptor**, enhancing inhibitory GABAergic neurotransmission across the CNS. This mechanism shortens sleep-onset latency and prolongs NREM sleep — the same pathway exploited by approved benzodiazepine hypnotics such as triazolam and temazepam. The TxGNN score of 99.74% is therefore mechanistically well-grounded: midazolam shares its pharmacological class with drugs already on the market for insomnia.

From an indication-relatedness standpoint, procedural sedation and insomnia both involve the same molecular target (GABA-A receptor upregulation) and the same downstream goal (reduction of wakefulness). Published RCTs from the 1980s and early 1990s explicitly tested oral midazolam (10–30 mg) as a hypnotic in insomnia patients and confirmed efficacy, further validating the model's prediction.

The critical limitation, however, is **pharmacokinetic**: midazolam has an elimination half-life of only approximately 1.5–2.5 hours. This enables reliable sleep initiation but provides poor coverage of sleep maintenance, and rapid clearance can cause rebound anxiety or early-morning awakening. This property — not any mechanistic gap — explains why midazolam has not been developed as a standard hypnotic, and is the primary reason the recommendation remains **Hold** pending modern trial data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT02142595](https://clinicaltrials.gov/study/NCT02142595) | Phase 4 | Completed | 111 | Direct RCT comparing dexmedetomidine vs midazolam combined with spinal anaesthesia on **postoperative sleep quality** in TURP patients — the most directly relevant trial in this dataset |
| [NCT06407518](https://clinicaltrials.gov/study/NCT06407518) | Phase NA | Recruiting | 280 | Prospective RCT of **preoperative oral midazolam** in colorectal cancer patients with sleep disturbance or anxiety; primary endpoint includes sleep quality improvement and postoperative pain |
| [NCT04082767](https://clinicaltrials.gov/study/NCT04082767) | Phase 3 | Unknown | 120 | Dexmedetomidine vs midazolam for sedation in critically ill paediatric patients; provides Phase 3 comparative data on midazolam's sedation–sleep continuum |
| [NCT05606315](https://clinicaltrials.gov/study/NCT05606315) | Phase 4 | Unknown | 285 | Remimazolam besylate (a midazolam-class benzodiazepine derivative) vs midazolam for ICU sedation; provides class-level Phase 4 evidence |
| [NCT01050699](https://clinicaltrials.gov/study/NCT01050699) | Phase 4 | Completed | 90 | Dexmedetomidine vs GABA agonist (midazolam) sedation on sleep and inflammation in ALI/ARDS patients; Phase 4 polysomnographic outcomes |
| [NCT01966315](https://clinicaltrials.gov/study/NCT01966315) | N/A | Terminated | 5 | 24-hour polysomnography comparing dexmedetomidine vs midazolam sleep quality in ICU patients; terminated early (n=5), minimal evidence value |
| [NCT00826553](https://clinicaltrials.gov/study/NCT00826553) | Phase 1 | Terminated | 6 | Polysomnographic comparison of α₂ agonist vs GABA agonist (midazolam class) on sleep stages; terminated early with very small sample |
| [NCT04879771](https://clinicaltrials.gov/study/NCT04879771) | N/A | Unknown | 100 | Comparison of morning vs afternoon sedated gastrointestinal endoscopy (midazolam used) on postoperative sleep quality |
| [NCT01791296](https://clinicaltrials.gov/study/NCT01791296) | Phase 4 | Completed | 100 | Dexmedetomidine nocturnal sleep protocol vs standard care (benzodiazepine/midazolam baseline) in ICU; measures delirium and sleep outcomes |
| [NCT05466279](https://clinicaltrials.gov/study/NCT05466279) | N/A | Completed | 131 | Remimazolam general anaesthesia vs propofol + midazolam control; includes sleep-quality outcomes in cancer surgery patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [6120704](https://pubmed.ncbi.nlm.nih.gov/6120704/) | 1981 | Phase 2 RCT (Dose-Finding) | Arzneimittel-Forschung | Oral midazolam 10–30 mg in 75 hospitalised insomnia patients; established optimal dose range for sleep–sedation efficacy |
| [6138072](https://pubmed.ncbi.nlm.nih.gov/6138072/) | 1983 | RCT | British Journal of Clinical Pharmacology | Double-blind placebo-controlled trial of midazolam 15 mg vs Vesparax in 30 insomnia patients; midazolam effective and better tolerated with no hangover |
| [2121802](https://pubmed.ncbi.nlm.nih.gov/2121802/) | 1990 | Multicenter RCT (14-day) | Journal of Clinical Psychopharmacology | Introduction to large multicentre study examining sleep, performance, and plasma levels in chronic insomniacs treated with flurazepam vs midazolam over 14 days |
| [2229461](https://pubmed.ncbi.nlm.nih.gov/2229461/) | 1990 | Multicenter RCT (14-day) | Journal of Clinical Psychopharmacology | Executive summary of above multicentre trial; confirms midazolam efficacy in chronic insomnia with assessment of performance and mood effects |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Clinical Review | Acta Psychiatrica Scandinavica (Suppl.) | Review of benzodiazepine hypnotics for insomnia subtypes; discusses midazolam among available agents with comparative pharmacokinetic and clinical profiles |
| [36615100](https://pubmed.ncbi.nlm.nih.gov/36615100/) | 2022 | Observational / Pilot | Journal of Clinical Medicine | Pilot study contrasting lemborexant with benzodiazepines (including midazolam class) for insomnia in high-risk endoscopy patients; benzodiazepine-induced delirium risk highlighted |
| [17988972](https://pubmed.ncbi.nlm.nih.gov/17988972/) | 2007 | Review / Case Series | Orvosi Hetilap | Review on insomnia pathogenesis and cerebral hypoperfusion; contextualises pharmacological targets including GABAergic agents |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key warnings, contraindications, and drug–drug interaction data were not available in this Evidence Pack. Given midazolam's benzodiazepine class, clinicians should be aware of the general class risks including dependence, tolerance, withdrawal, rebound insomnia, CNS/respiratory depression, and interactions with other CNS depressants — all of which must be verified from the current approved labelling before any repurposing decision.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the mechanistic link is clear and historical RCTs confirm hypnotic efficacy, the supporting evidence is over 30 years old and does not meet modern insomnia trial standards (polysomnography, Insomnia Severity Index, WASO endpoints). Midazolam has no current Italy marketing authorization, and no modern Phase 3 RCT for an insomnia indication is registered or completed. The pharmacokinetic profile (short T½) also raises questions about sleep-maintenance adequacy that have not been addressed by contemporary studies.

**To proceed, the following is needed:**

- **MOA and PK confirmation**: Retrieve full DrugBank data to formally document GABA-A mechanism and half-life implications for sleep maintenance vs. sleep onset
- **Modern clinical evidence**: A contemporary randomized controlled trial using accepted insomnia endpoints (ISI, PSG, sleep efficiency, WASO) would be required to upgrade to L1
- **Italy regulatory pathway**: Assess AIFA requirements for a new indication without an existing national authorization; consider whether a new MAA or a label extension is feasible
- **Benzodiazepine-specific safety review**: Formally document dependence potential, tolerance development, rebound insomnia, withdrawal syndrome, and respiratory depression risk — especially relevant for chronic insomnia management
- **Comparative positioning**: Evaluate whether midazolam offers any advantage over already-approved short-acting benzodiazepine hypnotics (e.g., triazolam) given near-identical mechanism and pharmacokinetics
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

