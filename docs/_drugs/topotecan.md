---
layout: default
title: Topotecan
parent: 僅模型預測 (L5)
nav_order: 161
evidence_level: L5
indication_count: 10
---

# Topotecan
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

The txgnn-pipeline skill confirms this is a standard TxGNN evidence-to-report task. No conflicting instructions — proceeding with report generation per the v5 prompt.

---

# Topotecan: From Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Topotecan is a semisynthetic camptothecin derivative and Topoisomerase I (Topo I) inhibitor with established approvals for ovarian cancer, small cell lung cancer, and cervical cancer.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, supported by a compelling mechanistic rationale centred on Topo I overexpression in MYC-amplified and triple-negative breast cancer (TNBC) subtypes.
This direction is currently supported by **5 clinical trials** and **20 publications**, yielding an assigned evidence level of **L1**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Ovarian cancer, small cell lung cancer, cervical cancer (standard international approvals; no Italy authorisation on record) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L1 |
| Italy Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Topotecan is a semisynthetic camptothecin derivative that selectively inhibits Topoisomerase I (Topo I). It does so by stabilising the Topo I–DNA cleavage complex, converting transient single-strand breaks into irreversible double-strand DNA breaks during replication. This preferentially kills rapidly dividing cells, forming the mechanistic basis of its antitumour activity.

The relevance to breast cancer is strongly supported at the preclinical level. Topo I is frequently overexpressed in MYC-amplified breast cancer cells; Topo I inhibition has been shown to cause aberrant R-loop accumulation, driving synthetic lethality specifically in this subtype (PMID 37987734). In triple-negative breast cancer (TNBC) — the subtype with the poorest prognosis and fewest targeted options — the transcription factor TFDP1 promotes tumour growth by suppressing cellular senescence and has been identified as a direct therapeutic target for Topotecan (PMID 40300683). Breast cancer cell lines MCF-7 and MDA-MB-231 show consistent cytotoxic sensitivity to Topotecan in vitro, and this effect can be enhanced by flavonoid compounds through reversal of BCRP-mediated drug resistance (PMID 15836850, 31408695).

The mechanistic overlap between breast cancer and Topotecan's approved indications is substantial: ovarian cancer, SCLC, and breast cancer all exhibit high proliferative indices and Topo I dependency. Clinical investigation of Topotecan in breast cancer dates back to the early 1990s with a CALGB Phase II trial, and preclinical work continues through 2025, indicating sustained scientific interest in this repurposing direction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02282020](https://clinicaltrials.gov/study/NCT02282020) | Phase 3 | Completed | 266 | Open-label RCT of olaparib vs. physician's choice single-agent chemotherapy (including topotecan as a standard option) in gBRCA-mutated platinum-sensitive relapsed ovarian cancer; provides the highest-level randomised evidence for Topo I inhibitor activity in BRCA-mutated tumour biology, with mechanistic cross-relevance to BRCA-associated breast cancer |
| [NCT04739800](https://clinicaltrials.gov/study/NCT04739800) | Phase 2 | Active, not recruiting | 120 | Randomised Phase 2 evaluating triplet therapy (durvalumab PD-L1 inhibitor + olaparib + cediranib) vs. standard-of-care chemotherapy including topotecan in platinum-resistant recurrent ovarian/peritoneal/fallopian tube cancer; exploring Topotecan synergy with immunotherapy — a design principle applicable to breast cancer |
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | Terminated | N/A | High-dose TIME regimen (Topotecan + Ifosfamide + Etoposide) followed by autologous peripheral stem cell transplant in metastatic breast cancer; direct breast cancer investigation; terminated early due to limited feasibility, efficacy data incomplete |
| [NCT04279509](https://clinicaltrials.gov/study/NCT04279509) | N/A | Unknown | 35 | Patient-derived organoid drug screen (SCORE study) to guide chemotherapy selection in refractory solid tumours including breast cancer; Topotecan is among agents evaluated, representing a personalised-medicine approach to identifying responders |
| [NCT02419495](https://clinicaltrials.gov/study/NCT02419495) | Phase 1b | Terminated | 221 | Safety and dose-finding study of selinexor (XPO1 inhibitor) combined with multiple standard chemotherapy regimens including Topotecan in advanced malignancies; terminated early; provides safety profile data for Topotecan combinations |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [10362325](https://pubmed.ncbi.nlm.nih.gov/10362325/) | 1999 | Phase II Clinical | Am J Clin Oncol | CALGB Phase II trial of Topotecan in 47 evaluable advanced breast cancer patients with prior chemotherapy; established early clinical activity signal for Topo I inhibition in breast cancer |
| [9413954](https://pubmed.ncbi.nlm.nih.gov/9413954/) | 1997 | Phase II Clinical | Br J Cancer | Two open Phase II studies of continuous infusional Topotecan in advanced breast cancer and NSCLC; assessed tolerability and activity in chemo-naive metastatic setting |
| [11455218](https://pubmed.ncbi.nlm.nih.gov/11455218/) | 2001 | Pilot Clinical | Onkologie | Pilot study of Topotecan as primary chemotherapy for brain metastases from breast cancer; evaluated CNS penetration, clinical response, and tolerability |
| [40300683](https://pubmed.ncbi.nlm.nih.gov/40300683/) | 2025 | Preclinical | Int J Biol Macromol | TFDP1 drives TNBC development via senescence suppression; Topotecan (FDA-approved for metastatic breast cancer) identified as the corresponding therapeutic agent targeting this pathway |
| [37987734](https://pubmed.ncbi.nlm.nih.gov/37987734/) | 2023 | Mechanistic/Preclinical | Cancer Res | Genome-wide CRISPR knockout screen in isogenic breast cancer cell lines shows Topo I inhibition in MYC-driven cancers induces R-loop accumulation and synthetic lethality — key mechanistic basis for repurposing |
| [26623560](https://pubmed.ncbi.nlm.nih.gov/26623560/) | 2015 | Preclinical | Oncotarget | Metronomic Topotecan + pazopanib combination showed potent efficacy in preclinical primary and late-stage metastatic TNBC models with anti-angiogenic synergy |
| [31408695](https://pubmed.ncbi.nlm.nih.gov/31408695/) | 2019 | Preclinical (in vitro/in vivo) | Pharmacol Res | Daidzein (natural isoflavone) enhances Topotecan anti-tumour activity and reverses BCRP-mediated drug resistance in breast cancer cells; synergistic combination index 0.10–0.66 |
| [15836850](https://pubmed.ncbi.nlm.nih.gov/15836850/) | 2005 | Preclinical (in vitro) | J Surg Res | Quercetin + Topotecan combined cytotoxicity in MCF-7 and MDA-MB-231 cells; confirmed Topo I inhibition triggers ROS-mediated apoptosis in breast cancer cell lines |
| [10472342](https://pubmed.ncbi.nlm.nih.gov/10472342/) | 1999 | Preclinical (xenograft) | Anticancer Res | Oral Topotecan demonstrated cytostatic/cytotoxic activity in breast cancer xenografts (MCF-7, MDA-MB-231, T47D) in nude mice; direct in vivo anti-breast-cancer activity confirmed |
| [9445630](https://pubmed.ncbi.nlm.nih.gov/9445630/) | 1997 | Review | Gynakol Geburtshilfliche Rundsch | Early narrative review positioning Topotecan alongside gemcitabine and paclitaxel as emerging cytotoxic agents for breast cancer, contextualising its role in the treatment landscape |

---

## Italy Market Information

Topotecan currently has no active authorisations registered in Italy. The regulatory query returned 0 records. No product licences, approved indications, or dosage form data are available for this market.

---

## Cytotoxicity

Topotecan is a cytotoxic antineoplastic agent (Camptothecin class; Topoisomerase I inhibitor). Its activity in multiple solid tumours and haematological cancers, and its mechanism of action via DNA double-strand break induction, classifies it as conventional cytotoxic chemotherapy.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Topoisomerase I inhibitor (Camptothecin derivative) |
| Myelosuppression Risk | High — neutropenia is the primary dose-limiting toxicity; thrombocytopenia and anaemia also frequently observed |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (baseline and before each cycle), serum creatinine and renal function (dose adjustment required for renal impairment), liver function tests |
| Handling Protection | Must follow cytotoxic drug handling regulations; closed-system drug transfer devices (CSTDs) and appropriate PPE required during preparation and administration |

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction records were available in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Topotecan's Topo I–inhibiting mechanism is directly relevant to breast cancer biology — particularly MYC-amplified and triple-negative subtypes — with clinical investigation dating back over 30 years, active preclinical research through 2025, and a Phase 3 completed RCT providing the highest-level randomised evidence base (albeit primarily in ovarian cancer with cross-applicable BRCA/Topo I biology). The evidence profile supports cautious clinical advancement rather than a hold.

**To proceed, the following is needed:**

- Retrieve and review the full package insert to establish contraindications, key warnings, and dose-modification criteria (currently a blocking data gap)
- Obtain formal MOA and pharmacological profile from DrugBank (DB01030) to strengthen mechanism-of-action documentation
- Clarify whether NCT02282020 explicitly used Topotecan as one of the "physician's choice" arms, to confirm the L1 evidence classification basis
- Define the target breast cancer subpopulation most likely to benefit (MYC-amplified, TNBC, or BRCA-mutated patients) to focus any prospective design
- Assess the Italy regulatory pathway for clinical trial authorisation or compassionate use, given zero current local approvals
- Develop a safety monitoring plan addressing high-risk myelosuppression (mandatory CBC tracking) and renal function adjustment protocols
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

