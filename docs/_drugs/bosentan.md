---
layout: default
title: Bosentan
parent: 僅模型預測 (L5)
nav_order: 39
evidence_level: L5
indication_count: 9
---

# Bosentan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

Using the `txgnn-pipeline` skill for context on this TxGNN report generation task. Now generating the full evaluation report based on the Evidence Pack.

---

# Bosentan: From Pulmonary Arterial Hypertension to Rheumatoid Arthritis

## One-Sentence Summary

Bosentan is a dual endothelin receptor antagonist (ERA) internationally approved for pulmonary arterial hypertension (PAH) and prevention of digital ulcers in systemic sclerosis, though no local regulatory approval is currently on record in this market.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis (RA)**, with **1 clinical trial** (indirectly related, targeting Giant Cell Arteritis) and **16 publications** currently supporting this direction — predominantly preclinical mechanistic studies without direct human RA trial data.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pulmonary arterial hypertension (based on known pharmacology; no local regulatory approvals on file) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 |
| Italy Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, bosentan is a dual ETA/ETB endothelin receptor antagonist, and its efficacy in pulmonary arterial hypertension and systemic sclerosis has been well established internationally. The predicted bridge to RA rests on a shared biological pathway: endothelin-1 (ET-1) is both a potent vasoconstrictor and a pro-inflammatory mediator whose levels are significantly elevated in the synovial fluid and pannus tissue of RA patients. Acting through the ETA receptor, ET-1 promotes TNF-α release, amplifying synovial inflammation and driving the progressive joint destruction that characterises RA.

The key mechanistic argument is that blocking ETA and ETB receptors with bosentan could interrupt this ET-1 → TNF-α inflammatory loop while simultaneously improving synovial microcirculation. This hypothesis has direct preclinical support: in a collagen-induced arthritis (CIA) mouse model — the gold-standard animal model for RA — bosentan significantly ameliorated arthritis (PMID 22249931). Multiple additional animal studies confirm that endothelins modulate neutrophil accumulation, oedema formation, and articular pain sensitisation in models of inflammatory arthritis, and that IL-15 triggers a sequential endothelin-dependent hypernociception cascade relevant to RA pain pathophysiology.

Despite this mechanistic plausibility, direct clinical evidence in RA patients is entirely absent. The only clinical trial identified (NCT06957002) targets Giant Cell Arteritis (GCA), a large-vessel granulomatous vasculitis with a pathological mechanism distinct from RA's autoimmune synovial inflammation; results from this trial cannot be extrapolated to RA. The evidence therefore remains at Level L4, warranting further mechanistic investigation before clinical translation can be considered.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06957002](https://clinicaltrials.gov/study/NCT06957002) | Phase 2 | Not Yet Recruiting | 40 | Bosentan + glucocorticoids vs. glucocorticoids alone in Giant Cell Arteritis; primary endpoint is failure-free survival at 12 months. ⚠️ Indication is GCA (large-vessel vasculitis), **not RA** — results cannot be directly extrapolated to rheumatoid arthritis. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|---------|
| [22249931](https://pubmed.ncbi.nlm.nih.gov/22249931/) | 2012 | Preclinical (CIA Mouse Model) | Inflammation Research | Bosentan directly ameliorates collagen-induced arthritis in mice; TNF-α drives ET system gene upregulation in joints, and bosentan suppresses this cascade — the most directly relevant evidence for RA repurposing |
| [18515326](https://pubmed.ncbi.nlm.nih.gov/18515326/) | 2008 | Preclinical (Animal Model) | Journal of Leukocyte Biology | Endothelins mediate neutrophil accumulation and oedema in zymosan-induced arthritis; ET-1 elevated in RA synovial membrane; ETA/ETB blockade reduces joint inflammation |
| [16766656](https://pubmed.ncbi.nlm.nih.gov/16766656/) | 2006 | Preclinical (Animal Model) | PNAS | IL-15 triggers sequential IFN-γ → endothelin → prostaglandin release causing articular hypernociception; dual ERA blockade inhibits this RA-relevant pain pathway |
| [19969421](https://pubmed.ncbi.nlm.nih.gov/19969421/) | 2010 | Preclinical (Animal Model) | Pain | IL-17 drives articular hypernociception in antigen-induced arthritis with confirmed ET-1 pathway involvement; supports endothelin's role in RA pain generation |
| [20054770](https://pubmed.ncbi.nlm.nih.gov/20054770/) | 2009 | Case Report | Kardiologia Polska | Juvenile RA co-occurring with Eisenmenger syndrome; bosentan initiated for Eisenmenger with clinical improvement noted — incidental observation, not a controlled RA study |
| [24268012](https://pubmed.ncbi.nlm.nih.gov/24268012/) | 2014 | Review | Rheumatic Disease Clinics of North America | PAH complicating CTDs including RA; bosentan role in CTD-PAH management; provides disease-overlap context for endothelin pathway relevance in RA |
| [19487226](https://pubmed.ncbi.nlm.nih.gov/19487226/) | 2009 | Review | Rheumatology (Oxford) | Vasculopathy and PAH in rheumatic CTDs; endothelin pathway central to vascular pathology in autoimmune diseases; contextual support for ERA use in rheumatic conditions |
| [16218473](https://pubmed.ncbi.nlm.nih.gov/16218473/) | 2005 | Review | Lupus | PAH as complication of CTDs including RA, dermatomyositis and Sjögren's syndrome; supports broad ET pathway relevance across the rheumatic disease spectrum |
| [21165350](https://pubmed.ncbi.nlm.nih.gov/21165350/) | 2010 | Review | Canadian Respiratory Journal | Targeted PH therapies including bosentan in CTD patients with concomitant ILD; real-world clinical use of ERA across rheumatic disease contexts |
| [19851110](https://pubmed.ncbi.nlm.nih.gov/19851110/) | 2010 | Review | Current Opinion in Rheumatology | Overview of rheumatic skin disease pathophysiology and emerging therapies; contextual background for endothelin antagonism in the broader rheumatic disease landscape |

---

## Italy Market Information

No regulatory authorizations for Bosentan are currently on record in this market.

> **Note:** Bosentan (Tracleer®) holds EMA approval for pulmonary arterial hypertension and prevention of new digital ulcers in systemic sclerosis. If the absence of local records reflects a data retrieval gap rather than a true lack of local approval, further verification with the relevant regulatory authority (AIFA) is recommended.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Bosentan has a mechanistically plausible and preclinically supported rationale for RA repurposing, with ET-1/ERA pathway involvement confirmed in collagen-induced and other animal arthritis models. However, no human clinical trials in RA patients have been conducted, placing this squarely at Evidence Level L4 — insufficient to support clinical translation without further dedicated investigation.

**To proceed, the following is needed:**
- Retrieve full MOA and safety profile data from DrugBank (currently unavailable in this evidence pack)
- Obtain the local package insert to assess TFDA/AIFA-specific warnings, contraindications, and approved dosing
- Conduct a dedicated systematic review of ET receptor antagonism in RA, focusing on human biomarker and translational data
- Evaluate bosentan's drug interaction profile with common RA therapies — particularly methotrexate and biologics — given bosentan's known CYP3A4/CYP2C9 induction capacity
- Design a Phase 1/2 proof-of-concept clinical study; a pragmatic entry point would be RA patients with comorbid PAH or systemic sclerosis overlap, where ERA therapy is already clinically justified
- Investigate hepatotoxicity risk in the context of concurrent DMARD use, as both bosentan and methotrexate carry hepatotoxic potential
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

