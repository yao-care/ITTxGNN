---
layout: default
title: Etoposide
parent: 僅模型預測 (L5)
nav_order: 97
evidence_level: L5
indication_count: 10
---

# Etoposide
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

Using the Drug Repurposing Evaluation Report format (v5) already loaded in the system prompt, I'll generate the report directly from the Evidence Pack.

---

# Etoposide: From Small Cell Lung Cancer & Germ Cell Tumors to Well-Differentiated Fetal Adenocarcinoma of the Lung

## One-Sentence Summary

Etoposide is a well-established cytotoxic chemotherapy agent internationally recognized for treating small cell lung cancer, germ cell tumors, and lymphomas, where it acts by inhibiting DNA topoisomerase II.
The TxGNN model predicts it may be effective for **Well-Differentiated Fetal Adenocarcinoma of the Lung (WDFA)**, an extremely rare lung malignancy within the pulmonary blastoma family.
This prediction is currently supported by only **1 indirect case report** and **no registered clinical trials**, placing this indication at a very early exploratory stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Italy; internationally used for SCLC, germ cell tumors, and lymphomas |
| Predicted New Indication | Well-Differentiated Fetal Adenocarcinoma of the Lung |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current regulatory dataset. Based on published pharmacological literature, etoposide is a semisynthetic epipodophyllotoxin that inhibits DNA topoisomerase II — an enzyme essential for unwinding double-stranded DNA during replication. By stabilising the topoisomerase II–DNA cleavage complex, etoposide causes irreversible double-strand DNA breaks, selectively targeting rapidly proliferating cells. It is a backbone component of established regimens including EPOCH, ICE, BEP, and IE, with proven efficacy across multiple cancer types.

Well-Differentiated Fetal Adenocarcinoma (WDFA) is a rare subtype within the pulmonary blastoma spectrum, characterised by glandular structures resembling embryonic lung at 10–16 weeks gestation and harbouring CTNNB1 mutations (β-catenin pathway activation). Because topoisomerase II activity is upregulated in embryonic and highly proliferative tumour cells, etoposide's mechanism is theoretically applicable. Related pulmonary blastoma subtypes share embryonic mesenchymal components that historically show sensitivity to genotoxic agents.

However, the mechanistic rationale remains theoretical for this specific histological subtype. The sole supporting publication (PMID 33107372) describes a classic biphasic pulmonary blastoma — a related but distinct entity — where etoposide was not part of the primary treatment. No direct clinical data targeting WDFA with etoposide exists, and no trials are currently registered. The TxGNN high score likely reflects structural similarity in the disease knowledge graph to other etoposide-sensitive embryonal tumour categories.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for well-differentiated fetal adenocarcinoma of the lung.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33107372](https://pubmed.ncbi.nlm.nih.gov/33107372/) | 2020 | Case Report | J Int Med Research | Classic biphasic pulmonary blastoma (closely related to WDFA); patient underwent surgical resection then nedaplatin + paclitaxel; disease recurred. Etoposide not used but the PB spectrum, including WDFA, is reviewed. Highlights absence of standard treatment guidelines for this tumour family. |

---

## Italy Market Information

Etoposide currently holds **no marketing authorization in Italy**. No license records are on file with the regulatory authority.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — Epipodophyllotoxin class (Topoisomerase II inhibitor) |
| Myelosuppression Risk | **High** — leukopenia and thrombocytopenia are dose-limiting toxicities; neutropenia nadir typically occurs 7–14 days post-administration |
| Emetogenicity Classification | Low to moderate (intravenous); low (oral) |
| Monitoring Items | CBC with differential (at each cycle), platelet count, hepatic enzymes (ALT/AST), serum creatinine, blood pressure during IV infusion |
| Handling Protection | Must comply with cytotoxic drug handling and disposal regulations; closed-system drug transfer devices recommended |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a TxGNN prediction score of 99.94%, the evidence base for etoposide in well-differentiated fetal adenocarcinoma of the lung is limited to a single indirect case report on a related tumour entity, with no clinical trials registered — insufficient to support clinical development or repurposing investment at this time.

**To proceed, the following is needed:**
- Preclinical studies (in vitro and in vivo models) specifically evaluating etoposide activity in WDFA cell lines or CTNNB1-mutated lung adenocarcinoma models
- Full mechanism of action profile (DrugBank API retrieval; currently flagged as Data Gap DG002)
- Package insert safety data for Italy-specific risk assessment (currently flagged as Data Gap DG001)
- Systematic case series review of all published pulmonary blastoma cases to identify any etoposide-containing regimens that achieved objective responses specifically in the WDFA subtype
- Genetic/molecular profiling (CTNNB1 mutation status, topoisomerase II expression in WDFA tumours) to validate mechanistic hypothesis
- Given extreme rarity of WDFA, consideration of an international registry or compassionate use framework rather than a standalone trial design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

