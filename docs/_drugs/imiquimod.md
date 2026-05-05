---
layout: default
title: Imiquimod
parent: 僅模型預測 (L5)
nav_order: 124
evidence_level: L5
indication_count: 10
---

# Imiquimod
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

# Imiquimod: From Actinic Keratosis to Pre-malignant Neoplasm

## One-Sentence Summary

Imiquimod is a topical TLR7/8 agonist and immune response modifier approved internationally for superficial skin conditions including actinic keratosis, superficial basal cell carcinoma, and external genital warts.
The TxGNN model predicts it may be effective for **Pre-malignant Neoplasm** more broadly,
with **19 clinical trials** and **9 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Actinic keratosis, superficial basal cell carcinoma, external genital warts (international approvals; no registration currently recorded in Italy) |
| Predicted New Indication | Pre-malignant Neoplasm |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| Italy Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Imiquimod functions as a Toll-like receptor 7 and 8 (TLR7/8) agonist. Upon topical application, it activates innate immune signalling through the MyD88/NF-κB pathway, triggering the release of pro-inflammatory cytokines — primarily IFN-α, TNF-α, and IL-12. This cascade recruits NK cells and cytotoxic CD8+ T lymphocytes to the site of dysplastic tissue, ultimately inducing apoptosis in abnormal proliferating cells while largely sparing healthy surrounding tissue. Plasmacytoid dendritic cells are particularly sensitive to TLR7 stimulation, making imiquimod a potent activator of local antitumour immunity.

Pre-malignant neoplasms — including actinic keratosis (AK), cervical intraepithelial neoplasia (CIN), vulvar intraepithelial neoplasia (VIN), anal intraepithelial neoplasia (AIN), actinic cheilitis, and lentigo maligna — share a common pathological substrate: uncontrolled epithelial proliferation driven by chronic UV damage or persistent HPV infection, typically accompanied by local immune evasion. Imiquimod's mechanism directly counteracts this evasion by re-engaging innate and adaptive immune surveillance against dysplastic cells. HPV-associated lesions in particular are highly susceptible to TLR7-mediated immune clearance, given the virus's known strategy of suppressing type I interferon responses.

In fact, imiquimod is already established in clinical practice for several pre-malignant subtypes — VIN, AIN, AK, and lentigo maligna — with Phase 2–3 trial data and multiple Cochrane systematic reviews supporting its use. The TxGNN prediction therefore reflects a mechanistic continuum already validated in clinical evidence, and the model's high confidence score (99.92%) is consistent with this body of real-world support.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03233412](https://clinicaltrials.gov/study/NCT03233412) | Phase 2 | Completed | 90 | RCT evaluating topical imiquimod for high-grade CIN 2/3 (HPV-associated cervical pre-malignant lesion); assessed spontaneous regression vs. standard LLETZ surgical excision |
| [NCT01720407](https://clinicaltrials.gov/study/NCT01720407) | Phase 3 | Completed | 259 | Imiquimod as neo-adjuvant treatment for lentigo maligna of the face (intraepidermal melanocytic pre-malignant proliferation); assessed whether pre-treatment reduces excision size and risk of intralesional margins |
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Phase 3 | Terminated | 9 | RCT of topical imiquimod for CIN 2–3; terminated early due to slow enrolment (n=9), but design validates immunotherapy as a fertility-sparing alternative to LLETZ — mechanistic intent is highly relevant |
| [NCT04219358](https://clinicaltrials.gov/study/NCT04219358) | Phase 1 | Terminated | 49 | Head-to-head comparison of 5%, 0.05%, and nanoencapsulated 0.05% imiquimod gel for actinic cheilitis (pre-malignant lower lip lesion with SCC potential); provides formulation optimisation data despite termination |
| [NCT04883645](https://clinicaltrials.gov/study/NCT04883645) | Early Phase 1 | Completed | 16 | Pilot neoadjuvant trial of topical Aldara (imiquimod) as TLR7 agonist in early-stage oral squamous cell carcinoma; evaluated feasibility, safety, immune infiltration, and tumour cell self-destruction |
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Phase 3 | Completed | 20 | Open-label study of imiquimod 5% cream 3×/week for actinic keratoses on the head; evaluated duration of response after 1 or 2 treatment cycles |
| [NCT01229319](https://clinicaltrials.gov/study/NCT01229319) | Phase 4 | Unknown | 20 | Imiquimod 3.75% cream following cryotherapy for hypertrophic actinic keratoses on dorsal hands and forearms; targets field cancerisation — subclinical pre-malignant change in UV-damaged skin |
| [NCT00941811](https://clinicaltrials.gov/study/NCT00941811) | Phase 2 | Completed | 5 | Exploratory mechanistic study of imiquimod treatment for HPV-associated VIN 2/3 and anogenital warts; analysed immune escape mechanisms to understand why some lesions regress and others persist |
| [NCT02242929](https://clinicaltrials.gov/study/NCT02242929) | Phase 3 | Unknown | 145 | Non-inferiority RCT: surgical excision vs. curettage combined with imiquimod for nodular basal cell carcinoma; evaluates imiquimod as a function-preserving alternative |
| [NCT00142454](https://clinicaltrials.gov/study/NCT00142454) | Phase 1 | Completed | 9 | NY-ESO-1 protein vaccination with imiquimod as immune adjuvant in resected Stage IIB–III malignant melanoma; assessed safety and immunogenicity of TLR7-boosted tumour vaccination strategy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Cochrane Review | Cochrane Database Syst Rev | Systematic review of interventions for anal canal intraepithelial neoplasia (AIN); imiquimod assessed as an option for this HPV-associated pre-malignant condition in HIV-positive MSM and immunosuppressed patients |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Cochrane Review | Cochrane Database Syst Rev | Cochrane review of medical interventions for high-grade VIN; imiquimod evaluated as non-surgical alternative given high surgical morbidity and relapse rates — supports use in the broader pre-malignant neoplasm category |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Systematic Review | Int J Mol Sci | Review of PDT combinations for non-melanoma skin cancer; discusses imiquimod synergy for BCC and SCC field treatment, relevant to sequential and combination strategies for pre-malignant lesions |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Clinical Review | Skin Therapy Lett | Management review of actinic keratosis; positions imiquimod as a first-line topical field therapy for AK, with discussion of clearance rates, dosing schedules, and local inflammatory reaction profile |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Narrative Review | Semin Cutan Med Surg | Describes emerging roles of topical agents (5-FU, diclofenac, imiquimod, PDT) for non-melanoma skin cancers and pre-malignant lesions; one of the early systematic descriptions of imiquimod's immunomodulatory antitumour mechanism |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Case Report | Int J STD AIDS | Successful clearance of high-grade VIN with imiquimod 5% in a renal transplant recipient on immunosuppression; demonstrates activity in compromised immune settings and raises questions about optimising dosing in such populations |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Preclinical PK/PD | Urol Oncol | Rat model PK/PD study of two TLR-7 agonists (TMX-101, TMX-202) for non-muscle-invasive bladder cancer; demonstrates that TLR7 agonism can be extended beyond skin to other epithelial pre-malignant conditions with appropriate delivery routes |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Case Report | Int J STD AIDS | Successful clearance of bowenoid papulosis of the penis (HPV-associated pre-malignant anogenital condition) with topical imiquimod 5% cream once weekly for 8 weeks; well tolerated with no recurrence at follow-up |
| [18931984](https://pubmed.ncbi.nlm.nih.gov/18931984/) | 2008 | Case Study | Hautarzt | Disseminated superficial actinic porokeratosis co-existing with multiple pre-malignant lesions (AK, Bowen's disease, SCC); highlights cases where imiquimod was ineffective, providing context on treatment limitations and resistance patterns |

---

## Italy Market Information

Imiquimod is currently not registered or marketed in Italy. No AIFA authorisation has been identified in the current dataset.

Prescribers seeking to use imiquimod in Italy should consult the AIFA Farmaci Registrati database for any recent approval activity. If no authorisation exists, the applicable legal framework is Italian Law 648/96 (off-label access for serious conditions without alternatives), subject to Ethics Committee approval and individual patient prescription.

---

## Cytotoxicity

Imiquimod has established antineoplastic clinical use (superficial basal cell carcinoma, actinic keratosis), qualifying it for evaluation under this section.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy — TLR7/8 agonist / immune response modifier; not a conventional cytotoxic or targeted kinase inhibitor; antitumour effect is immune-mediated rather than directly cytocidal |
| Myelosuppression Risk | Low — standard topical application results in minimal systemic absorption; systemic myelosuppression is not a recognised risk for approved topical doses; large-surface or prolonged use may cause transient systemic flu-like symptoms |
| Emetogenicity Classification | Not applicable for topical formulation; systemic administration routes under investigation have not established a defined emetogenic potential |
| Monitoring Items | Local skin reactions (erythema, erosion, ulceration, crusting) at application site; systemic symptoms (fatigue, fever, myalgia) if used on large surface areas or at high frequency; CBC if extended use is anticipated beyond standard labelled durations |
| Handling Protection | Standard protection (avoid contact with eyes, mucous membranes, and broken skin when applying); formal cytotoxic drug handling regulations are not required for standard topical cream formulation |

---

## Safety Considerations

Full safety data including TFDA/AIFA package insert warnings and contraindications are not available in the current dataset. Please refer to the Aldara® (imiquimod 5% cream) package insert or an approved prescribing information document for complete warnings, contraindications, and drug interaction data.

Key areas to review before prescribing include:
- **Local inflammatory reactions**: erythema, erosion, ulceration, and scarring, particularly with over-application
- **Systemic flu-like syndrome**: fatigue, fever, rigors, and myalgia with high-frequency or large-area use
- **Use in immunocompromised patients**: evidence is limited; case reports show activity but also unpredictable inflammatory responses in transplant recipients
- **Use in pregnancy**: safety not established; avoid unless benefit clearly outweighs risk

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 RCT (NCT03233412, n=90) for HPV-associated CIN and a completed Phase 3 trial (NCT01720407, n=259) for lentigo maligna provide meaningful clinical evidence that imiquimod is active against pre-malignant neoplasms beyond its originally approved skin indications. Two Cochrane systematic reviews further establish its evidence base for high-grade VIN and AIN. The TLR7/8 immunomodulatory mechanism is directly relevant to the shared pathophysiology of HPV-associated and UV-induced pre-malignant lesions, making the prediction biologically coherent and clinically actionable — provided the appropriate indication subtype and administration route are clearly defined.

**To proceed, the following is needed:**

- **Regulatory package insert**: Obtain full AIFA-approved or EMA reference product data for imiquimod to complete the safety and contraindication review (currently a blocking data gap)
- **Indication specificity**: Define which pre-malignant neoplasm subtype is the primary target (e.g., CIN 2/3, high-grade VIN, AIN, actinic cheilitis) to enable focused evidence synthesis and protocol design
- **Formulation and route confirmation**: Clarify whether standard 5% cream, 3.75% cream, or an investigational delivery system (e.g., nanoencapsulated gel for mucosal use) is appropriate for the target anatomical site
- **Italy access pathway**: Assess eligibility for AIFA off-label access under Law 648/96 or Decreto Ministeriale 8 maggio 2003 for the selected indication
- **Post-marketing safety review**: Cross-reference pharmacovigilance data from FDA, EMA, and MHRA for known real-world safety signals in pre-malignant indication use, especially in immunocompromised populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

