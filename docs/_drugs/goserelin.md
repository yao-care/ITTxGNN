---
layout: default
title: Goserelin
parent: 僅模型預測 (L5)
nav_order: 120
evidence_level: L5
indication_count: 3
---

# Goserelin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

Using **txgnn-pipeline** to guide report generation structure. Now producing the evaluation report from the Evidence Pack.

---

# Goserelin: From Hormone-Sensitive Breast Cancer to Amenorrhea

## One-Sentence Summary

Goserelin (Zoladex) is a GnRH agonist with established clinical use in hormone-sensitive breast cancer and endometriosis, acting by suppressing pituitary gonadotropin secretion and inducing ovarian estrogen deprivation.
The TxGNN model predicts it may be effective for **Amenorrhea (disease)** — encompassing both therapeutic amenorrhea induction and chemotherapy-induced ovarian protection —
with **7 clinical trials** and **19 publications** currently supporting this direction, achieving an **L1** evidence level.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hormone-sensitive breast cancer; endometriosis (known clinical uses; no Italy/AIFA marketing authorization on record) |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Italy Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not retrievable from the DrugBank query for this report. Based on well-established pharmacology, Goserelin is a synthetic analogue of gonadotropin-releasing hormone (GnRH). Continuous administration paradoxically downregulates pituitary GnRH receptors through desensitisation, suppressing LH and FSH secretion, which in turn sharply reduces ovarian estrogen production in premenopausal women — directly inducing amenorrhea through a hormonal cascade.

This mechanistic pathway supports the TxGNN prediction from two clinically distinct angles. In the first, Goserelin deliberately induces **therapeutic amenorrhea**: suppressing the hormonal milieu is itself the treatment goal, as in hormone-sensitive breast cancer (reducing tumor-promoting estrogen), endometriosis (starving ectopic endometrial tissue), and uterine adenomyosis. In the second, pre-chemotherapy Goserelin administration temporarily drives ovarian follicles into a quiescent state, shielding them from cytotoxic damage — thereby **preventing** chemotherapy-induced amenorrhea and preserving fertility.

Both directions are mechanistically coherent and have been directly tested in large RCTs. The OPTION trial (n=400), IBCSG Trial VIII, and multiple supporting Phase 3 studies represent the strongest possible evidence base. The TxGNN model's top-ranked prediction for Goserelin precisely mirrors its validated pharmacodynamic fingerprint, making this one of the model's most mechanistically transparent predictions.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00427245](https://clinicaltrials.gov/study/NCT00427245) | Phase 3 | Completed | 400 | OPTION trial: large RCT testing goserelin vs no goserelin to prevent early menopause (chemotherapy-induced amenorrhea) in premenopausal women with stages I–III breast cancer |
| [NCT00068601](https://clinicaltrials.gov/study/NCT00068601) | Phase 3 | Completed | 257 | Phase 3 RCT with ovarian failure (amenorrhea) as primary endpoint; evaluated whether goserelin prevents early menopause in HR-negative breast cancer patients receiving chemotherapy |
| [NCT02483767](https://clinicaltrials.gov/study/NCT02483767) | Phase 3 | Completed | 98 | Prospective RCT directly assessing GnRH agonist (goserelin) for ovarian function preservation during chemotherapy in premenopausal breast cancer; sufficient data on amenorrhea outcomes |
| [NCT01218581](https://clinicaltrials.gov/study/NCT01218581) | Phase 2/3 | Completed | 32 | RCT comparing aromatase inhibitors vs GnRH agonists in uterine adenomyosis; amenorrhea is a secondary outcome in fertility-preserving management |
| [NCT02132390](https://clinicaltrials.gov/study/NCT02132390) | Phase 3 | Unknown | 300 | Adjuvant toremifene ± goserelin in premenopausal HR+ stages I–IIIA breast cancer; goserelin-induced amenorrhoea explicitly incorporated into study design |
| [NCT03475758](https://clinicaltrials.gov/study/NCT03475758) | Phase 2 | Unknown | 100 | Goserelin for ovarian protection in premenopausal patients on cyclophosphamide-containing chemotherapy; menstruation outcome is the primary endpoint |
| [NCT00488722](https://clinicaltrials.gov/study/NCT00488722) | N/A | Unknown | N/A | Single-arm study of Zoladex + CEF neoadjuvant chemotherapy; explicitly notes goserelin's capacity to induce reversible amenorrhea equivalent to ovarian ablation |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28472240](https://pubmed.ncbi.nlm.nih.gov/28472240/) | 2017 | Meta-analysis / Systematic Review of RCTs | Annals of Oncology | OPTION trial final results: GnRH agonist co-administration significantly reduced chemotherapy-induced premature ovarian insufficiency (POI) and amenorrhea in early breast cancer |
| [12488406](https://pubmed.ncbi.nlm.nih.gov/12488406/) | 2002 | RCT | Journal of Clinical Oncology | ZEBRA study: goserelin vs CMF chemotherapy as adjuvant therapy in premenopausal node-positive breast cancer; long-term amenorrhea and premature menopause directly compared |
| [8513962](https://pubmed.ncbi.nlm.nih.gov/8513962/) | 1993 | RCT | Fertility and Sterility | Goserelin vs low-dose oral contraceptive for endometriosis-associated pelvic pain; amenorrhea induction is the primary therapeutic mechanism evaluated |
| [14679153](https://pubmed.ncbi.nlm.nih.gov/14679153/) | 2003 | RCT | Journal of the National Cancer Institute | IBCSG Trial VIII: sequential chemotherapy + goserelin vs either alone for premenopausal node-negative breast cancer; ovarian suppression and amenorrhea as core treatment outcomes |
| [17159194](https://pubmed.ncbi.nlm.nih.gov/17159194/) | 2007 | Secondary analysis of RCT | Journal of Clinical Oncology | IBCSG Trial VIII QoL analysis: differential impact of chemotherapy, goserelin, and their combination on amenorrhea, hot flashes, and quality of life by age group |
| [25187267](https://pubmed.ncbi.nlm.nih.gov/25187267/) | 2015 | Prospective Cohort | Cancer Research and Treatment | Goserelin ovarian ablation improved survival in HR+ stages II/III breast cancer patients without chemotherapy-induced amenorrhea; highlights amenorrhea status as prognostic stratifier |
| [12734855](https://pubmed.ncbi.nlm.nih.gov/12734855/) | 2003 | Review / Meta-analysis | British Journal of Surgery | Comprehensive review of ovarian ablation methods for adjuvant breast cancer treatment; GnRH agonists including goserelin assessed as reversible, effective amenorrhea-inducing strategy |
| [12353820](https://pubmed.ncbi.nlm.nih.gov/12353820/) | 2002 | Review | Breast Cancer Research and Treatment | Overview of LHRH agonists in early breast cancer; goserelin's reversible ovarian ablation and amenorrhea induction highlighted as equivalent to CMF in hormone-sensitive disease |
| [1533675](https://pubmed.ncbi.nlm.nih.gov/1533675/) | 1992 | Review | Journal of the Royal Army Medical Corps | Early review on therapeutic amenorrhea induction; goserelin identified as highly effective for controlled elimination of menstruation with fewer side effects than continuous oral contraceptives |
| [10730389](https://pubmed.ncbi.nlm.nih.gov/10730389/) | 1999 | Clinical Study | Akusherstvo i Ginekologiia | GnRH agonist (Zoladex depot) used to manage severe uterine haemorrhage in adolescents with congenital aplastic/hypoplastic anaemia; amenorrhea induction stopped bleeding within 2–4 days |

---

## Cytotoxicity

Goserelin is used in the treatment of hormone-sensitive cancers (breast cancer, prostate cancer) and qualifies as an antineoplastic hormonal agent.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal / Endocrine therapy — GnRH agonist (not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Low — mechanism is hormonal, not myelotoxic; bone marrow effects not expected |
| Emetogenicity Classification | Minimal — injection site reactions more common than nausea |
| Monitoring Items | Serum estradiol or testosterone (to confirm suppression), LH/FSH, bone mineral density (with use >6 months), liver function |
| Handling Protection | Standard pharmaceutical handling; cytotoxic drug handling precautions are not required |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction is mechanistically transparent — Goserelin's core pharmacodynamic action directly modulates amenorrhea — and is backed by multiple completed Phase 3 RCTs (including the 400-patient OPTION trial and IBCSG Trial VIII), placing this indication firmly at evidence level L1. The clinical goal must be clearly defined before proceeding, as Goserelin both induces and prevents amenorrhea depending on context.

**To proceed, the following is needed:**
- Confirm clinical intent: therapeutic amenorrhea induction (e.g., adenomyosis, endometriosis) vs. chemotherapy-induced amenorrhea prevention (ovarian protection) — these are pharmacologically opposite applications requiring separate clinical pathways
- Retrieve full MOA documentation from DrugBank to complete the mechanistic dossier
- Verify Italy/AIFA registration status for Goserelin (marketed globally as Zoladex; current query returned 0 results, which may reflect a data gap rather than true non-approval)
- Develop a long-term safety monitoring plan covering bone mineral density loss (hypo-estrogenic state) and cardiovascular effects with prolonged use
- Assess fertility preservation and paediatric use cases separately, as these require dedicated clinical and ethical review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

