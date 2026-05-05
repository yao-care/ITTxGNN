---
layout: default
title: Pimozide
parent: 僅模型預測 (L5)
nav_order: 164
evidence_level: L5
indication_count: 10
---

# Pimozide
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

The `txgnn-pipeline` skill confirms this is part of the TxGNN reporting workflow. Now I'll generate the full evaluation report based on the Evidence Pack.

---

# Pimozide: From Tourette Syndrome to Trichotillomania

## One-Sentence Summary

Pimozide is a diphenylbutylpiperidine-class antipsychotic, approved as a backup treatment for Gilles de la Tourette syndrome in the US (currently not marketed in Taiwan).
The TxGNN model predicts it may be effective for **Trichotillomania**,
with **0 clinical trials** and **10 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gilles de la Tourette Syndrome (FDA backup treatment; not registered in Taiwan) |
| Predicted New Indication | Trichotillomania |
| TxGNN Prediction Score | 99.996% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on known information from published literature, Pimozide belongs to the diphenylbutylpiperidine class of antipsychotics and acts primarily as a **D2 dopamine receptor antagonist**. Its efficacy in suppressing motor and vocal tics in Tourette syndrome has been established through decades of clinical use and international guideline endorsement.

Trichotillomania (TTM) is classified within the **obsessive-compulsive spectrum disorders**, in which both dopaminergic and serotonergic pathways are jointly implicated in the pathophysiology. First-line pharmacological treatment currently centers on serotonin reuptake inhibitors (SRIs), yet a substantial proportion of patients fail to achieve adequate response on SRI monotherapy alone.

This treatment gap is precisely where pimozide's D2 antagonism may offer mechanistic complementarity. As demonstrated in PMID 1532960 (Stein & Hollander, 1992), low-dose pimozide augmentation of SRI therapy produced benefit in SRI-refractory trichotillomania patients — mirroring the same augmentation logic already validated in refractory OCD and Tourette syndrome. The phenomenological overlap among TTM, OCD, and Tourette syndrome further reinforces the biological plausibility of this repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [36802832](https://pubmed.ncbi.nlm.nih.gov/36802832/) | 2023 | Systematic Evidence Mapping | J Cutan Med Surg | Identified and appraised RCT evidence for pharmacological treatment of primary psychodermatologic disorders (PPDs), including TTM; highlights persistent evidence gaps and the limited number of high-quality trials |
| [1532960](https://pubmed.ncbi.nlm.nih.gov/1532960/) | 1992 | Open-label Augmentation Study | J Clin Psychiatry | Low-dose pimozide added to SRI therapy showed clinical benefit in SRI-refractory trichotillomania, drawing on mechanistic parallels with Tourette syndrome and OCD |
| [15554735](https://pubmed.ncbi.nlm.nih.gov/15554735/) | 2004 | Comprehensive Review | Am J Clin Dermatol | Comprehensive review of pimozide in dermatology; discusses monosymptomatic hypochondriacal psychoses and compulsive body-focused repetitive behaviours |
| [30446201](https://pubmed.ncbi.nlm.nih.gov/30446201/) | 2018 | Review | Clin Dermatol | Reviews antipsychotic drug use in dermatology; explains both central D2-blocking and peripheral receptor effects relevant to psychodermatologic conditions |
| [27320510](https://pubmed.ncbi.nlm.nih.gov/27320510/) | 2016 | Review | Tijdschr Psychiatr | Reviews pharmacotherapy options for paediatric trichotillomania; notes that pharmacological research investment has been limited and that TTM can become chronic if untreated |
| [10357517](https://pubmed.ncbi.nlm.nih.gov/10357517/) | 1999 | Case Series | J Child Adolesc Psychopharmacol | Three TTM patients who had previously benefited from low-dose pimozide augmentation were switched to risperidone; all showed robust improvement, supporting D2 augmentation as a viable strategy |
| [28225970](https://pubmed.ncbi.nlm.nih.gov/28225970/) | 2017 | Case Report | An Bras Dermatol | Case report of TTM with dermatoscopic differential from alopecia areata; notes N-acetylcysteine evidence and highlights absence of standardised treatment protocols |
| [11475941](https://pubmed.ncbi.nlm.nih.gov/11475941/) | 2001 | Review | CNS Drugs | Proposes diagnostic criteria for psychogenic excoriation (compulsive skin picking) and reviews pharmacotherapy options within the OCD-spectrum framework |
| [10497682](https://pubmed.ncbi.nlm.nih.gov/10497682/) | 1999 | Review | Ann Acad Med Singapore | Reviews trichotillomania as an underdiagnosed chronic psychiatric condition; discusses epidemiology, comorbidities, and management strategies |
| [10900563](https://pubmed.ncbi.nlm.nih.gov/10900563/) | 2000 | Case Series / Observational | Int J Psychiatry Med | Clinical profile of delusional parasitosis (monosymptomatic hypochondriacal psychosis) — a related OCD-spectrum condition — providing contextual evidence for pimozide's role in this disorder cluster |

---

## Taiwan Market Information

Pimozide is currently **not registered or marketed in Taiwan**. No authorization records are available from TFDA.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for clinical teams:** Pimozide is known to carry a risk of QTc interval prolongation, which warrants particular attention in any future indication expansion or research design. Complete contraindication and drug interaction data should be retrieved from the official package insert before any clinical planning.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence base for pimozide in trichotillomania currently sits at **L4** — comprising primarily narrative reviews, case reports, and a single open-label augmentation study from 1992. Although the mechanistic rationale (D2 blockade as SRI augmentation within the OCD-spectrum) is scientifically coherent and has precedent in related conditions, no prospective clinical trial has yet directly evaluated pimozide for TTM as a primary indication.

**To proceed, the following is needed:**

- **Clinical evidence:** A prospective randomised controlled trial or at minimum a rigorous open-label pilot study evaluating low-dose pimozide augmentation in SRI-partial-responders with trichotillomania
- **MOA data:** Complete mechanism of action information from DrugBank (currently a High-severity data gap)
- **Safety data:** Full safety profile including QTc prolongation risk parameters, contraindications, and drug–drug interactions from the package insert (currently a Blocking data gap)
- **Regulatory pathway:** TFDA registration assessment — pimozide has zero current Taiwan approvals; a regulatory pathway must be mapped before any local clinical application
- **Comparator benchmarking:** Assessment against newer atypical antipsychotics (e.g., aripiprazole, risperidone) that share the D2 augmentation rationale but may offer a more favourable cardiac safety profile, to determine whether pimozide remains the best candidate in this mechanistic class
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

