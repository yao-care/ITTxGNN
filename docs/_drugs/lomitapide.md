---
layout: default
title: Lomitapide
parent: 僅模型預測 (L5)
nav_order: 138
evidence_level: L5
indication_count: 10
---

# Lomitapide
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

The TxGNN pipeline skill is noted. This task is a report generation task — proceeding to write the evaluation report based on the Evidence Pack.

---

# Lomitapide: From Homozygous Familial Hypercholesterolemia to Hyperlipoproteinemia

## One-Sentence Summary

Lomitapide is an oral microsomal triglyceride transfer protein (MTP) inhibitor with established approval in the US (2012) and EU (2013) for treating Homozygous Familial Hypercholesterolemia (HoFH), a rare genetic disorder causing severely elevated LDL cholesterol and premature cardiovascular disease.
The TxGNN model predicts it may be effective for **Hyperlipoproteinemia** (rank 9, score 99.74%) — the broader disease category that encompasses HoFH — with **12 clinical trials** and **19 publications** currently supporting this direction.
Notably, TxGNN's highest-ranked predictions (ranks 1–8 and 10) are all rare platelet disorders; these lack any established mechanistic or clinical connection to Lomitapide and are rated **L5 / Hold** pending further investigation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Homozygous Familial Hypercholesterolemia (HoFH) — approved in US/EU; no Italian marketing authorization on record |
| Predicted New Indication | Hyperlipoproteinemia (TxGNN rank 9) |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L1 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Lomitapide inhibits microsomal triglyceride transfer protein (MTP), an enzyme in the hepatocyte endoplasmic reticulum that is essential for loading triglycerides onto apolipoprotein B (ApoB) to assemble VLDL particles. When MTP is blocked, VLDL secretion drops sharply, and circulating LDL-C and ApoB levels fall substantially — even in patients who lack functional LDL receptors. This receptor-independent mechanism is precisely what separates Lomitapide from statins and PCSK9 inhibitors.

Homozygous Familial Hypercholesterolemia is the most severe subtype of Hyperlipoproteinemia type IIa. Patients carry two defective LDLR alleles, making receptor-dependent therapies largely futile and leaving Lomitapide as one of the few agents capable of achieving clinically meaningful LDL-C reductions (typically 40–50%). HoFH is nosologically classified within Hyperlipoproteinemia, so TxGNN's rank 9 prediction is a direct mechanistic match — not speculative repurposing, but a model-confirmed validation of established clinical use within a broader disease taxonomy.

> **On TxGNN's top-ranked predictions (ranks 1–8 and 10):** The highest-ranked novel predictions are eight rare platelet conditions (thrombocytopenia subtypes, Glanzmann thrombasthenia, pseudo-von Willebrand disease, dense granule disease, etc.). MTP inhibition operates exclusively in hepatic lipoprotein metabolism and has no established mechanistic bridge to platelet production, granule biology, or platelet receptor function. The repurposing rationales in the Evidence Pack confirm this absence of a pathophysiological link. These predictions most likely reflect knowledge-graph topological proximity in the TxGNN network rather than genuine therapeutic signal. All are rated **L5** and are on **Hold**.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT06832371](https://clinicaltrials.gov/study/NCT06832371) | Observational | Active, Not Recruiting | 73 | Multicenter retrospective-prospective study evaluating the effect of Lomitapide on Major Adverse Cardiovascular Events (MACE) in HoFH patients — delivers real-world cardiovascular outcomes data |
| [NCT00943306](https://clinicaltrials.gov/study/NCT00943306) | Phase 3 | Completed | 19 | Long-term open-label follow-on study of Lomitapide (MTP inhibitor) in HoFH; assessed continued LDL-C efficacy and safety over multi-year treatment |
| [NCT00730236](https://clinicaltrials.gov/study/NCT00730236) | Phase 3 | Completed | 29 | Pivotal Phase 3 study of AEGR-733 (Lomitapide) in HoFH patients on current lipid-lowering therapy; evaluated LDL-C reduction and long-term safety — key registration trial |
| [NCT02173158](https://clinicaltrials.gov/study/NCT02173158) | Phase 3 | Completed | 9 | Single-arm open-label multicenter study of Lomitapide specifically in Japanese HoFH patients; confirmed cross-ethnic efficacy and safety |
| [NCT04681170](https://clinicaltrials.gov/study/NCT04681170) | Phase 3 | Completed | 46 | International multicenter Phase 3 study evaluating Lomitapide efficacy and long-term safety in **pediatric** HoFH patients on stable lipid-lowering therapy — supports age-range expansion |
| [NCT02135705](https://clinicaltrials.gov/study/NCT02135705) | Observational | Recruiting | 300 | LOWER Registry: global prospective cohort study monitoring long-term safety and effectiveness of Lomitapide across real-world clinical settings; ongoing through 2028 |
| [NCT00559962](https://clinicaltrials.gov/study/NCT00559962) | Phase 2 | Completed | 260 | Double-blind placebo-controlled RCT of low-dose MTP inhibitor ± atorvastatin/ezetimibe/fenofibrate; evaluated hepatic fat accumulation by MRI spectroscopy — largest Phase 2 cohort |
| [NCT00690443](https://clinicaltrials.gov/study/NCT00690443) | Phase 2 | Completed | 44 | Randomized double-blind study of AEGR-733 + atorvastatin 20 mg vs. atorvastatin monotherapy in moderate hypercholesterolemia; primary endpoint: % LDL-C change at 8 weeks |
| [NCT01556906](https://clinicaltrials.gov/study/NCT01556906) | Phase 2 | Completed | 6 | Open-label dose-escalation safety study of Lomitapide (BMS-201038) in HoFH; established the dose-response profile for LDL-C and VLDL-C reduction across four dose levels |
| [NCT05611528](https://clinicaltrials.gov/study/NCT05611528) | Phase 3 | Completed | 10 | Open-label real-world study of evinacumab added on top of background LMT (including Lomitapide) in Canadian HoFH patients — provides combination therapy and competitive context |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [39426393](https://pubmed.ncbi.nlm.nih.gov/39426393/) | 2024 | Phase 3 Study | The Lancet Diabetes & Endocrinology | APH-19 trial: Lomitapide significantly reduced LDL-C in pediatric HoFH patients on standard-of-care therapy — primary efficacy phase results |
| [37130090](https://pubmed.ncbi.nlm.nih.gov/37130090/) | 2023 | Expert Consensus / Guidelines | European Heart Journal | 2023 EAS Consensus update on HoFH: revised diagnostic criteria (LDL-C >10 mmol/L triggers HoFH workup), updated treatment algorithms including Lomitapide |
| [35148370](https://pubmed.ncbi.nlm.nih.gov/35148370/) | 2022 | Systematic Evidence Review | European Journal of Preventive Cardiology | Comprehensive synthesis of Lomitapide efficacy and safety in HoFH; integrates clinical trial and real-world evidence |
| [39751968](https://pubmed.ncbi.nlm.nih.gov/39751968/) | 2025 | Review | Current Atherosclerosis Reports | Latest review of novel HoFH pharmacotherapies; positions Lomitapide alongside evinacumab, inclisiran, and RNA-based agents in current treatment landscape |
| [36152419](https://pubmed.ncbi.nlm.nih.gov/36152419/) | 2022 | Clinical Study | Atherosclerosis | Lomitapide efficacy and safety evaluated in Familial Chylomicronaemia Syndrome (FCS) — signals a potential label extension beyond HoFH to severe hypertriglyceridemia |
| [31741187](https://pubmed.ncbi.nlm.nih.gov/31741187/) | 2019 | Mechanistic Review | Current Atherosclerosis Reports | In-depth mechanistic review of Lomitapide (MTP inhibition) and Mipomersen (ApoB100 antisense) as LDL-receptor-independent lipid-lowering strategies |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Expert Review | Journal of the American College of Cardiology | JACC Focus Seminar on emerging LDL-C lowering agents; contextualizes Lomitapide within inclisiran, bempedoic acid, and PCSK9i landscape |
| [28598687](https://pubmed.ncbi.nlm.nih.gov/28598687/) | 2017 | Review | Expert Opinion on Pharmacotherapy | Comprehensive clinical review of Lomitapide: mechanism, Phase 3 evidence, safety profile, drug interactions, and place in HoFH therapy |
| [25936301](https://pubmed.ncbi.nlm.nih.gov/25936301/) | 2015 | Review | Atherosclerosis Supplements | Comparison of Lomitapide and Mipomersen for HoFH patients who remain uncontrolled on maximal statin therapy plus apheresis |
| [25053660](https://pubmed.ncbi.nlm.nih.gov/25053660/) | 2014 | Consensus Statement | European Heart Journal | EAS Consensus Panel foundational position paper on HoFH: clinical diagnosis, genetic heterogeneity, and treatment recommendations anchoring Lomitapide's role |

---

## Italy Market Information

Lomitapide is currently **not registered** in Italy. No marketing authorizations were identified in the regulatory database.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | — | — | No Italian authorizations on record |

> Lomitapide (brand name **Lojuxta®**) holds a valid EMA marketing authorization for HoFH in adult patients, which provides a direct regulatory basis for AIFA submission. Clinicians requiring access for eligible HoFH patients in Italy may explore compassionate use or the named-patient exemption framework (Legge 648/96) while formal authorization is pending.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Lomitapide carries robust L1 evidence — multiple completed Phase 3 trials, an ongoing global observational registry, and a valid EMA approval — firmly supporting its use in Homozygous Familial Hypercholesterolemia, the most severe subtype of Hyperlipoproteinemia. The TxGNN prediction for Hyperlipoproteinemia is mechanistically coherent and evidence-backed, making the decision to advance straightforward. The primary guardrail is the absence of Italian market authorization and the need for a formal hepatic risk management plan, both of which are addressable through established regulatory pathways.

**To proceed, the following is needed:**
- Submit an AIFA marketing authorization application referencing the existing EMA approval for Lojuxta® (Lomitapide) for HoFH in adults
- Extend the pediatric dossier to AIFA, citing the completed APH-19 trial (NCT04681170 / PMID 39426393), to support authorization in patients under 18
- Establish a hepatic monitoring protocol (ALT/AST at baseline and at each dose escalation; hepatic steatosis imaging) equivalent to the EU Risk Management Plan
- Develop a patient and prescriber education program on mandatory low-fat diet adherence to minimize gastrointestinal dose-limiting adverse effects
- Investigate AIFA Legge 648/96 compassionate use for HoFH patients in urgent need while formal authorization is being processed
- Commission a formal knowledge-graph audit to explain why TxGNN ranks platelet disorders (ranks 1–8 and 10) above the drug's approved indication — this topological artifact warrants model calibration before further interpretation of those predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

