---
layout: default
title: Entecavir
parent: 僅模型預測 (L5)
nav_order: 93
evidence_level: L5
indication_count: 10
---

# Entecavir
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

The txgnn-pipeline skill confirms this is a TxGNN project report task. Now I'll write the full evaluation report per the v5 prompt specification.

---

# Entecavir: From Hepatitis B to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

Entecavir is a potent guanosine nucleoside analogue antiviral, globally established as a first-line oral therapy for chronic hepatitis B (HBV) infection.
The TxGNN model assigns its highest prediction score to **chronic hepatitis C virus (HCV) infection** (99.98%), placing it at rank 1 among all predicted new indications.
However, **no dedicated clinical trials or direct mechanistic evidence** support anti-HCV activity for entecavir; the high score reflects knowledge graph co-infection neighbourhood overlap rather than true pharmacological repurposing potential.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Italy; globally established for chronic hepatitis B (HBV) infection |
| Predicted New Indication | Chronic Hepatitis C Virus Infection |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Entecavir is a deoxyguanosine nucleoside analogue that, after intracellular triphosphorylation, competitively inhibits three sequential functions of the HBV DNA polymerase: base-primer synthesis, reverse transcription of pregenomic RNA into minus-strand DNA, and positive-strand DNA synthesis. Its selectivity for HBV replication is exceptionally high (IC₅₀ ≈ 0.004 µM). Multiple completed Phase 3 RCTs have established it as a first-line antiviral with a high genetic barrier to resistance, and it is recommended in all major international HBV treatment guidelines.

The TxGNN model's assignment of a 99.98% score for chronic HCV infection is primarily driven by knowledge graph topology: in the disease co-occurrence graph, HBV and HCV nodes share a dense neighbourhood owing to co-infection, shared transmission routes, and overlapping clinical management contexts. Entecavir appears frequently alongside HCV in the literature precisely because it is used to *prevent HBV reactivation* in patients receiving direct-acting antiviral (DAA) therapy for HCV — not because it treats HCV itself. HCV is a positive-sense RNA virus that replicates exclusively through an RNA-dependent RNA polymerase (NS5B RdRp), which is structurally and functionally distinct from the HBV reverse transcriptase/DNA polymerase targeted by entecavir. No in vitro or clinical data document any anti-HCV NS5B activity for entecavir or its metabolites.

In summary, the rank-1 TxGNN prediction for chronic HCV should be interpreted as a **knowledge graph false positive** arising from disease co-occurrence signal, not a pharmacologically grounded repurposing hypothesis. The more actionable finding in this evidence pack is the rank-2 prediction — **hepatitis B virus infection** — which carries L1 evidence from multiple completed Phase 3 RCTs and corresponds to entecavir's already-established global indication. The drug is simply not yet registered in Italy, which may represent a regulatory and commercialisation opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Prospective study of DAA therapy in HCV/HBV co-infected patients; entecavir was used to manage HBV reactivation risk during anti-HCV treatment — not as treatment for HCV itself. Most directly relevant trial in this dataset. |
| [NCT03662568](https://clinicaltrials.gov/study/NCT03662568) | Phase 1 | Completed | 56 | DDI and pharmacokinetics study of Morphothiadine Mesilate/Ritonavir (an investigational HCV agent) combined with entecavir or tenofovir in healthy subjects; no HCV efficacy data for entecavir. |
| [NCT00065507](https://clinicaltrials.gov/study/NCT00065507) | Phase 3 | Completed | 195 | Pivotal Phase 3 RCT of entecavir vs. adefovir in chronic HBV with hepatic decompensation; core HBV efficacy data, no HCV relevance. |
| [NCT00371150](https://clinicaltrials.gov/study/NCT00371150) | Phase 4 | Completed | 131 | Observational study of entecavir antiviral effect in Black/African-American and Hispanic HBV patients; HBV-focused, no HCV data. |
| [NCT01020565](https://clinicaltrials.gov/study/NCT01020565) | Phase 2 | Completed | 60 | Safety and antiviral activity of entecavir (0.1 mg and 0.5 mg) in Japanese adults with chronic HBV at 52 weeks; HBV-focused. |
| [NCT03272009](https://clinicaltrials.gov/study/NCT03272009) | Phase 1 | Completed | 73 | Safety, PK, and pharmacodynamics of FXR agonist EYP001a in chronic HBV subjects (some receiving entecavir background therapy); HBV-focused. |
| [NCT01270178](https://clinicaltrials.gov/study/NCT01270178) | N/A | Unknown | 420 | Prospective trial of entecavir in HBV-positive HCC patients after radiofrequency ablation; abstract references HCV-related HCC but the enrolled population is HBV patients. |
| [NCT01848743](https://clinicaltrials.gov/study/NCT01848743) | Phase 3 | Unknown | 120 | Tenofovir vs. lamivudine for chronic HBV with severe acute exacerbation; HBV-focused, status unknown. |
| [NCT01354652](https://clinicaltrials.gov/study/NCT01354652) | Phase 4 | Terminated | 5 | Lactic acidosis incidence during entecavir treatment in HBV patients with severe cirrhosis; terminated early due to very low enrollment (n=5). |
| [NCT05416008](https://clinicaltrials.gov/study/NCT05416008) | N/A | Unknown | 150 | Observational study investigating whether long-term nucleoside analogues (including entecavir) promote hepatic steatosis in chronic HBV patients; HBV-focused. |

> **Important caveat:** None of the above trials evaluate entecavir as a treatment for HCV infection. NCT02555943 is the only trial with contextual HCV relevance, and in that study entecavir's role is strictly HBV suppression. No Phase 2 or later trial has prospectively tested entecavir against HCV replication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Retrospective Cohort | *Viruses* | In 66 anti-HCV antibody-positive CHB patients receiving nucleos(t)ide analogues (including entecavir), HCV RNA was detectable at baseline in many; HCV reactivation was observed during/after anti-HBV therapy. Entecavir suppresses HBV but does not suppress HCV — HCV RNA was not reduced by entecavir treatment. |
| [28230928](https://pubmed.ncbi.nlm.nih.gov/28230928/) | 2017 | Observational | *Journal of Gastroenterology and Hepatology* | HBV reactivation risk investigated in CHC patients receiving DAA therapy; supports the practice of entecavir prophylaxis in HBV/HCV co-infected patients starting anti-HCV treatment. Entecavir role = HBV protector, not HCV treatment. |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Review | *Expert Opinion on Pharmacotherapy* | Comprehensive review of HBV/HCV co-infection treatment; discusses entecavir for the HBV component in co-infected patients. Highlights the high risk of cirrhosis and HCC in co-infection and the need for effective HBV suppression. |
| [22959099](https://pubmed.ncbi.nlm.nih.gov/22959099/) | 2013 | Review + Case | *Clinics and Research in Hepatology and Gastroenterology* | HBV/HCV co-infection is a therapeutic challenge; presents a case managed with sequential treatment. Entecavir is identified as the appropriate HBV component; no anti-HCV activity is attributed to it. |
| [35327336](https://pubmed.ncbi.nlm.nih.gov/35327336/) | 2022 | Review | *Biomedicines* | Panoramic review of chronic viral hepatitis therapy (HBV, HCV, HDV); discusses how entecavir and tenofovir achieve viral suppression in HBV but emphasises that HBV and HCV require entirely different drug classes. |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | *Wiener Medizinische Wochenschrift* | Early narrative review comparing HBV and HCV treatment landscapes; pegylated interferon discussed for both, while nucleoside analogues including entecavir are identified as HBV-specific. |
| [32173307](https://pubmed.ncbi.nlm.nih.gov/32173307/) | 2020 | Review | *Clinics and Research in Hepatology and Gastroenterology* | Management of HBV and HCV in children; entecavir referenced as an approved HBV therapy for paediatric use. No pediatric or adult HCV indication discussed for entecavir. |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | *Minerva Gastroenterologica e Dietologica* | Reviews renal effects of antivirals for HBV and HCV; classifies entecavir as a nucleoside analogue for HBV. For HCV, separate drug classes (protease inhibitors, NS5B inhibitors) are discussed. |
| [21497740](https://pubmed.ncbi.nlm.nih.gov/21497740/) | 2011 | Review | *Best Practice & Research Clinical Gastroenterology* | Fibrosis progression in chronic viral hepatitis; demonstrates that entecavir treatment leads to histological improvement and fibrosis regression in HBV patients, supporting sustained HBV viral suppression as the mechanism. |
| [24868325](https://pubmed.ncbi.nlm.nih.gov/24868325/) | 2014 | Review | *World Journal of Hepatology* | HBV and HCV management in liver and kidney transplant recipients; entecavir and tenofovir identified as preferred HBV agents with high genetic barrier to resistance. HCV treated separately with interferon-based or DAA regimens. |

---

## Italy Market Information

Entecavir is currently **not marketed in Italy** (AIFA database records 0 authorizations; `market_status: 未上市`). No product licenses exist to tabulate.

Entecavir is commercially available in numerous other markets under brand names such as **Baraclude®** (Bristol-Myers Squibb), with approvals from the FDA (USA, 2005), EMA, PMDA (Japan), and other regulatory agencies for the treatment of chronic HBV infection in adults and children ≥2 years. Its absence from the Italian AIFA register may reflect a historical commercial or regulatory decision rather than a safety or efficacy barrier.

---

## Safety Considerations

Please refer to the package insert (e.g., Baraclude® SmPC or FDA label) for complete safety information, as Italian labeling data is unavailable (no AIFA authorization on file).

**Critical safety flag — HIV co-infection (based on published literature):**
Entecavir must **not** be used as monotherapy in patients with HIV/HBV co-infection who are not receiving a fully suppressive antiretroviral (ART) regimen. A 2007 landmark case series demonstrated that entecavir exerts partial anti-HIV-1 reverse transcriptase activity and can select for the M184V lamivudine-resistance mutation in HIV, severely compromising future HIV treatment options (the "Entecavir surprise," PMID 17582071). This is a class-defining safety restriction applicable to all prescribers.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN rank-1 prediction for chronic HCV is a knowledge-graph false positive: entecavir's mechanism of action (HBV DNA polymerase inhibition) has no cross-reactivity with the HCV NS5B RNA polymerase, and no clinical trial or pre-clinical study has documented any anti-HCV activity. Pursuing entecavir as an HCV treatment would be scientifically unwarranted given the availability of highly curative DAA regimens already approved for HCV.

**Contextual note — the more actionable finding:**
The rank-2 TxGNN prediction, **hepatitis B virus infection** (score 99.85%, evidence level L1), corresponds to entecavir's well-established global approved indication. Multiple completed Phase 3 RCTs confirm its superiority over comparators in treatment-naïve and treatment-experienced HBV populations. The drug is simply absent from the Italian market. An AIFA registration pathway for the HBV indication may represent a more clinically meaningful and immediately actionable opportunity than any HCV repurposing hypothesis.

**To close data gaps before any further evaluation:**

- Obtain entecavir package insert (EMA SmPC or FDA label) to resolve DG001 (safety warnings/contraindications) and DG002 (formal MOA documentation)
- Confirm AIFA registration status and identify any historical EU withdrawal or non-submission rationale
- If HCV repurposing is to be formally assessed despite the above, conduct in vitro HCV replicon assays to determine whether any NS5B inhibitory activity exists at clinically achievable entecavir concentrations before committing to clinical resources
- Implement mandatory HIV co-infection screening protocol in any future Italian clinical use plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

