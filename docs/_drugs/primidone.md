---
layout: default
title: Primidone
parent: 僅模型預測 (L5)
nav_order: 171
evidence_level: L5
indication_count: 10
---

# Primidone
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

The skill confirms this is the right TxGNN drug repurposing context. Now generating the evaluation report based on the Evidence Pack.

---

# Primidone: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Primidone is a barbiturate-class antiepileptic drug with a long history of use in seizure disorders and essential tremor management.
The TxGNN model predicts it may be effective for **Trigeminal Nerve Neoplasm** with a score of **99.99%**, yet **0 clinical trials** and **0 publications** directly support this direction.
The evidence pack's own analysis strongly suggests this prediction reflects semantic leakage in the knowledge graph rather than a genuine therapeutic signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Italy; established pharmacological use for epilepsy and essential tremor |
| Predicted New Indication | Trigeminal Nerve Neoplasm |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Italy Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established pharmacological knowledge, Primidone is a barbiturate-class antiepileptic drug that is metabolised in vivo to phenobarbital and phenylethylmalonamide (PEMA). These active metabolites primarily enhance GABA-A receptor-mediated inhibitory neurotransmission and stabilise neuronal voltage-gated sodium channels, thereby suppressing pathological hyperexcitability. This dual mechanism underpins Primidone's established efficacy in generalised tonic-clonic seizures, partial seizures, and essential tremor.

Trigeminal nerve neoplasm is a structural, proliferative lesion of the trigeminal nerve — a fundamentally different pathophysiology from the electrophysiological dysregulation that Primidone addresses. Tumour growth is driven by uncontrolled cellular proliferation and survival signalling (e.g., growth factor receptors, apoptosis evasion), processes entirely outside the scope of GABA-A enhancement or sodium channel blockade. Neither Primidone nor its metabolites possess any known cytotoxic, antiproliferative, or antiangiogenic properties.

The 99.99% TxGNN prediction score almost certainly arises from **semantic leakage**: in the biomedical knowledge graph, the node "trigeminal nerve neoplasm" sits adjacent to "trigeminal neuralgia" — an indication where anticonvulsants (particularly carbamazepine) have well-documented efficacy. The model conflates structural proximity in graph space with therapeutic relevance, producing a high score that does not correspond to a real treatment signal. This prediction should therefore be treated as a known artefact of graph-based modelling rather than a drug repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Italy Market Information

Primidone is not currently authorised or marketed in Italy. No AIFA license records are on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Trigeminal nerve neoplasm is a proliferative disease with no mechanistic connection to Primidone's antiepileptic pharmacology; the extremely high TxGNN score is almost certainly a false positive caused by knowledge-graph semantic leakage between "trigeminal nerve neoplasm" and the adjacent "trigeminal neuralgia" node, and there is zero clinical trial or literature evidence to support this indication.

**To proceed, the following is needed:**
- Do not pursue trigeminal nerve neoplasm as a repurposing target unless independent preclinical data directly demonstrate an effect of Primidone or its metabolites on trigeminal nerve tumour biology
- Redirect analysis to mechanistically defensible indications within the same prediction set — **trigeminal neuralgia** (rank 9, L3 evidence, S2 Proceed with Guardrails), **audiogenic seizures** (rank 3, L4), **startle epilepsy** (rank 7, L4), and **reading seizures** (rank 8, L4) are more promising candidates
- Retrieve Primidone's complete MOA data from DrugBank API to fill the current data gap (DG002) and enable proper mechanistic-link scoring across all predicted indications
- Obtain and parse the TFDA/AIFA package insert (DG001) to complete the safety profile before any clinical feasibility assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

