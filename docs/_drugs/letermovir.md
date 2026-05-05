---
layout: default
title: Letermovir
parent: 僅模型預測 (L5)
nav_order: 134
evidence_level: L5
indication_count: 1
---

# Letermovir
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

# Letermovir: From CMV Prophylaxis to Vulvovaginal Candidiasis

## One-Sentence Summary

Letermovir is an antiviral agent specifically developed for prophylaxis against cytomegalovirus (CMV) infection in hematopoietic stem cell transplant recipients.
The TxGNN model predicts it may be effective for **Vulvovaginal Candidiasis**, yet **zero clinical trials** and **zero publications** currently support this direction — evidence sits at the lowest level (L5), and mechanistic analysis strongly suggests this is a knowledge graph topological false positive rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | CMV prophylaxis in hematopoietic stem cell transplant recipients |
| Predicted New Indication | Vulvovaginal Candidiasis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Italy Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not formally available in this Evidence Pack. Based on known pharmacology, Letermovir selectively inhibits the **CMV viral terminase complex** (subunits UL51/UL56/UL89) — an enzyme the virus uses to cleave and package newly replicated DNA into virion capsids. This mechanism is exquisitely specific to human herpesvirus 5 (CMV) and has no documented activity against any fungal pathogen.

Vulvovaginal candidiasis is caused by *Candida* spp. (predominantly *C. albicans*), whose pathogenesis involves ergosterol biosynthesis and β-1,3-glucan cell wall synthesis — biochemical pathways entirely unrelated to viral DNA terminase enzymes. There is no established or plausible biological bridge between Letermovir's antiviral mechanism and antifungal activity.

The strikingly high TxGNN score (99.88%) almost certainly reflects a **knowledge graph topological false positive**: immunosuppressed hematopoietic stem cell transplant recipients receive Letermovir for CMV prophylaxis while simultaneously carrying elevated risk for opportunistic fungal infections, including candidiasis. This patient-level co-occurrence creates spurious node co-association in the knowledge graph — a statistical artifact, not a pharmacological relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction linking Letermovir to vulvovaginal candidiasis is assessed as a knowledge graph topological false positive with no mechanistic basis, no clinical trial support, and no literature evidence (Evidence Level L5). Pursuing this indication without any biological rationale would not be a responsible use of development resources.

**To revisit this decision, the following would be needed:**
- In vitro data demonstrating any Letermovir activity against *Candida* species
- A credible mechanistic hypothesis explaining how CMV terminase inhibition could produce antifungal effects
- At minimum one preclinical study (animal model or cell-based) showing efficacy in a fungal infection setting
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

