---
layout: default
title: Omalizumab
parent: 僅模型預測 (L5)
nav_order: 157
evidence_level: L5
indication_count: 10
---

# Omalizumab
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

The txgnn-pipeline skill covers pipeline management (training/deployment), not report writing — the system prompt's v5 format is the correct guide here. Proceeding directly with the report generation.

---

# Omalizumab: From Allergic Asthma to Bronchitis

## One-Sentence Summary

Omalizumab is a recombinant humanized anti-IgE monoclonal antibody, approved in multiple countries for moderate-to-severe allergic asthma and chronic spontaneous urticaria.
The TxGNN model predicts it may also be effective for **Bronchitis**, with **2 clinical trials** and **8 publications** currently supporting this direction.
However, the mechanistic link is partial — applying specifically to the IgE-elevated, allergic subtype of bronchitis — and the existing evidence is insufficient to support a positive decision at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Moderate-to-severe allergic asthma (not approved in Italy; no Italy authorizations on file) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L3 |
| Italy Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information from the supporting literature, Omalizumab is a recombinant humanized monoclonal antibody that binds specifically to the Cε3 domain of IgE — the site where IgE attaches to its high-affinity receptor FcεRI on mast cells and basophils. By sequestering free IgE, omalizumab reduces FcεRI receptor expression and attenuates the downstream allergic inflammatory cascade, including histamine release, cytokine secretion, and airway inflammation.

Bronchitis is a heterogeneous condition. The allergic (eosinophilic) subtype of chronic bronchitis shares key pathophysiological features with asthma: elevated serum IgE, IgE-mediated mast cell activation, airway mucosal inflammation, and mucus hypersecretion. In this overlapping population, the theoretical basis for anti-IgE therapy is plausible. One completed Phase 2/3 trial (NCT02049294) directly studied omalizumab's steroid-sparing effect in patients with asthma and eosinophilic bronchitis, providing the most direct clinical link — albeit severely limited by sample size (n=11).

Critically, most cases of acute infectious bronchitis are driven by viral or bacterial triggers, and smoking-induced chronic bronchitis is governed by oxidative stress and neutrophilic inflammation — neither of which involves IgE. The TxGNN model's high prediction score most likely reflects shared airway biology with asthma (omalizumab's proven indication). Meaningful benefit is expected only in a carefully selected sub-population with documented IgE elevation and allergen sensitization, not across the broader bronchitis population.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Phase 2/3 | Completed | 11 | Double-blind placebo-controlled RCT evaluating omalizumab's steroid-sparing effect in patients with asthma and **eosinophilic bronchitis**. The most directly relevant trial for this indication, but severely underpowered (n=11). |
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Phase 2b | Completed | 382 | Dose-finding RCT of QGE031 (next-generation anti-IgE) vs omalizumab as active comparator in Chronic Spontaneous Urticaria; double-blind, placebo and active controlled. Not targeted at bronchitis, but provides dose–response characterization for the anti-IgE class. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | Clinical Trial | Current Medical Research and Opinion | Pooled safety analysis of omalizumab in children with IgE-mediated allergic asthma; characterizes the safety profile in a pediatric airway disease population closely related to allergic bronchitis. |
| [35369622](https://pubmed.ncbi.nlm.nih.gov/35369622/) | 2022 | Observational | Postepy Dermatologii i Alergologii | Omalizumab in middle-aged/older patients with severe allergic asthma–COPD overlap; reports meaningful clinical benefit in this chronic obstructive airway phenotype with IgE-mediated component. |
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Review | Clinical Reviews in Allergy & Immunology | Comprehensive review of omalizumab's FDA approval and post-approval experience; describes IgE-reducing mechanism and documented reduction of airway inflammation and exacerbations. |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Review | Expert Opinion on Pharmacotherapy | Reviews drug treatment challenges in smoking-induced airway diseases (chronic bronchitis, emphysema, asthma–COPD overlap); highlights the exclusion of smokers from most omalizumab trials as a key evidence gap. |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | Review | Masui — Japanese Journal of Anesthesiology | Preoperative management review covering both bronchial asthma and chronic bronchitis; mentions omalizumab as a treatment option for severe allergic bronchial asthma with chronic airway involvement. |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | Review | Allergologia et Immunopathologia | Overview of monoclonal antibodies in pediatrics including omalizumab for allergic diseases; provides mechanistic background on anti-IgE therapy across respiratory indications. |
| [21163396](https://pubmed.ncbi.nlm.nih.gov/21163396/) | 2010 | Review | Revue des Maladies Respiratoires | French expert panel review on adult asthma exacerbations; discusses pathophysiology, treatment escalation, and contextual overlap with acute-on-chronic bronchitis presentations. |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Case Report | Journal of Investigational Allergology & Clinical Immunology | Case of plastic bronchitis following bronchial thermoplasty; documents a rare bronchitis complication in a severe asthma patient — contextual signal for refractory airway disease management. |

---

## Italy Market Information

Omalizumab is currently **not approved or marketed in Italy**. No authorization records are on file in the regulatory dataset.

> **Note:** Omalizumab (brand name Xolair®) holds regulatory approval from the EMA and FDA for moderate-to-severe allergic asthma and chronic spontaneous urticaria. Italy-specific marketing authorization has not been identified in this dataset. Any clinical use in Italy would require an off-label framework or future AIFA authorization.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The two identified clinical trials do not provide adequately powered, bronchitis-specific evidence — the only directly relevant trial (NCT02049294) enrolled just 11 patients, and the mechanistic rationale applies exclusively to the IgE-elevated allergic/eosinophilic bronchitis subtype, which represents a minority of the overall bronchitis population. With no Italy marketing authorization and insufficient clinical data, this candidate does not yet meet the threshold for active development.

**To proceed, the following is needed:**
- Retrieve and confirm Omalizumab's full mechanism of action from DrugBank (current data gap)
- Obtain complete Italy package insert data for warnings, contraindications, and special populations
- Define a clear target sub-population: patients with chronic bronchitis, documented IgE elevation (≥30 IU/mL), and positive allergen sensitization
- Commission or identify a properly powered prospective cohort study or Phase 2 RCT specifically in allergic/eosinophilic chronic bronchitis
- Assess AIFA regulatory pathway for potential compassionate use or new indication filing
- Conduct a health economics analysis to justify investment given the availability of established alternatives (inhaled corticosteroids, dupilumab in overlapping atopic phenotypes)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

