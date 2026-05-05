---
layout: default
title: Ezetimibe
parent: 僅模型預測 (L5)
nav_order: 102
evidence_level: L5
indication_count: 4
---

# Ezetimibe
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Ezetimibe: From Cholesterol Absorption Inhibitor to Hyperlipoproteinemia

## One-Sentence Summary

Ezetimibe is a selective cholesterol absorption inhibitor that blocks intestinal uptake of dietary and biliary cholesterol via the NPC1L1 transporter, directly lowering circulating LDL-C levels.
The TxGNN model predicts it may be effective for **Hyperlipoproteinemia**, with **50 clinical trials** and **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indications on record (not registered in Italy) |
| Predicted New Indication | Hyperlipoproteinemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| Italy Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the regulatory dataset. Based on known pharmacological evidence, Ezetimibe selectively inhibits the NPC1L1 (Niemann-Pick C1-Like 1) transporter located on intestinal brush-border epithelial cells. This transporter is responsible for absorbing both dietary and biliary cholesterol from the gut lumen. By blocking NPC1L1, Ezetimibe reduces intestinal cholesterol absorption by approximately 54%, which directly lowers circulating LDL-C levels without affecting bile acid synthesis or triglyceride-rich lipoprotein pathways — a mechanism that is fundamentally distinct from, and complementary to, statin therapy.

The mechanistic link to hyperlipoproteinemia is exceptionally direct: elevated lipoprotein levels — particularly LDL — are driven in part by excessive intestinal cholesterol absorption delivering substrate for hepatic lipoprotein assembly. Ezetimibe addresses this at the supply side, while statins reduce hepatic synthesis. Combination therapy has consistently demonstrated additive LDL-C reductions of 15–25% beyond what statins achieve alone, underscoring the clinical rationale for Ezetimibe in patients who cannot achieve LDL-C targets on monotherapy.

The TxGNN score of 0.9963 (ranked #2,407 globally) reflects a very strong structural connection between Ezetimibe's molecular target nodes and the disease nodes associated with hyperlipoproteinemia in the knowledge graph. This is powerfully corroborated by the clinical evidence base: multiple completed Phase 3 trials have deployed Ezetimibe as both the primary investigational drug and the active comparator benchmark — indicating it is considered the clinical reference standard for cholesterol absorption inhibition in this disease area.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Phase 3 | Completed | 611 | Ezetimibe/Simvastatin + Fenofibrate coadministration in mixed hyperlipidemia (elevated cholesterol + triglycerides); core efficacy and safety evaluation of combination lipid-lowering strategy |
| [NCT01763827](https://clinicaltrials.gov/study/NCT01763827) | Phase 3 | Completed | 615 | Evolocumab vs. Ezetimibe vs. placebo over 12 weeks in low-risk hypercholesterolemic adults; Ezetimibe served as the active comparator, establishing the clinical LDL-C benchmark |
| [NCT01043380](https://clinicaltrials.gov/study/NCT01043380) | Phase 4 | Completed | 245 | PRECISE-IVUS: Ezetimibe (absorption inhibitor) vs. statin (synthesis inhibitor) on coronary plaque regression measured by intravascular ultrasound; assessed atherosclerotic outcomes beyond LDL-C |
| [NCT06005597](https://clinicaltrials.gov/study/NCT06005597) | Phase 3 | Completed | 407 | Obicetrapib 10mg + Ezetimibe 10mg fixed-dose combination vs. placebo in HeFH/ASCVD patients on maximally tolerated lipid-lowering therapy; evaluated adjunct LDL-C reduction |
| [NCT00092560](https://clinicaltrials.gov/study/NCT00092560) | Phase 3 | Completed | 587 | Fenofibrate and Ezetimibe coadministration in mixed hyperlipidemia; comprehensive evaluation of cholesterol-lowering effectiveness and safety of the dual combination |
| [NCT00349284](https://clinicaltrials.gov/study/NCT00349284) | Phase 3 | Completed | 181 | Fenofibrate vs. Ezetimibe vs. their combination in Type IIb dyslipidemia with metabolic syndrome features; assessed complementary improvement of the atherogenic lipid profile |
| [NCT04433533](https://clinicaltrials.gov/study/NCT04433533) | Phase 4 | Unknown | 200 | Rosuvastatin/Ezetimibe combination vs. Rosuvastatin monotherapy in Korean patients with left ventricular diastolic dysfunction and hyperlipidemia (LDL ≥ 100 mg/dL) |
| [NCT00092833](https://clinicaltrials.gov/study/NCT00092833) | Phase 3 | Terminated | 49 | Open-label treatment use study: Ezetimibe 10mg/day in homozygous familial hypercholesterolemia and sitosterolemia; early access program with safety data collection (terminated; interpret with caution) |
| [NCT00843661](https://clinicaltrials.gov/study/NCT00843661) | Phase 4 | Unknown | 60 | Ezetimibe + Fenofibrate vs. Pravastatin monotherapy in HIV-infected patients on protease inhibitors with hyperlipidemia; addressed drug interaction challenges in complex clinical settings |
| [NCT04862260](https://clinicaltrials.gov/study/NCT04862260) | Early Phase 1 | Active, Not Recruiting | 3 | Exploratory cholesterol metabolism reprogramming (Evolocumab + Atorvastatin + Ezetimibe) with standard of care in advanced pancreatic adenocarcinoma; investigates cholesterol's role in cancer progression |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | Phase 3 RCT | Lancet | TANDEM trial: Obicetrapib + Ezetimibe fixed-dose combination significantly reduced LDL-C vs. placebo in patients on maximally tolerated lipid-lowering therapy; validates Ezetimibe's central role in novel combination lipid management |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | Phase 3 RCT | JAMA | Oral PCSK9 inhibitor enlicitide vs. placebo in HeFH adults; participants were already on background therapy including Ezetimibe, establishing its role as the standard foundation of LDL-C management |
| [23956253](https://pubmed.ncbi.nlm.nih.gov/23956253/) | 2013 | Guideline/Review | European Heart Journal | EAS consensus: familial hypercholesterolemia underdiagnosed and undertreated globally; Ezetimibe explicitly recommended in the treatment algorithm to prevent coronary heart disease |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Review | Cardiology Clinics | FH management overview: Ezetimibe is a proven treatment to lower LDL-C; early combination therapy with statins substantially reduces cardiovascular events and mortality |
| [34480646](https://pubmed.ncbi.nlm.nih.gov/34480646/) | 2021 | Review | Current Cardiology Reports | FH global burden and current management; Ezetimibe positioned as a key second-line agent for patients not reaching LDL-C targets on statin monotherapy |
| [29219151](https://pubmed.ncbi.nlm.nih.gov/29219151/) | 2017 | Review | Nature Reviews Disease Primers | Definitive FH review covering LDLR/APOB/PCSK9 mutation pathophysiology, clinical spectrum, and treatment strategy including Ezetimibe in the therapeutic algorithm |
| [37762244](https://pubmed.ncbi.nlm.nih.gov/37762244/) | 2023 | Review | Int J Molecular Sciences | Postprandial hyperlipidemia pathophysiology, atherogenesis, and treatment; Ezetimibe reduces postprandial lipemia by inhibiting intestinal NPC1L1, addressing a distinct atherogenic risk window |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Review | Molecular Medicine Reports | Comprehensive review of drugs targeting hyperlipidemia; Ezetimibe's intestinal cholesterol absorption mechanism, clinical efficacy data, and current role in ASCVD prevention reviewed in modern context |
| [38599725](https://pubmed.ncbi.nlm.nih.gov/38599725/) | 2024 | Review | Indian Heart Journal | FH management and cascade screening importance; Ezetimibe is a standard add-on to statin therapy, particularly critical in populations with high FH prevalence and underdiagnosis |
| [19654419](https://pubmed.ncbi.nlm.nih.gov/19654419/) | 2009 | Review | Drug and Therapeutics Bulletin | Ezetimibe update: reduces plasma LDL-C and total cholesterol as monotherapy or combined with statins; discusses cardiovascular outcome evidence as of that period and clinical positioning |

---

## Italy Market Information

Ezetimibe is **not currently registered** in Italy. The regulatory database returns 0 active authorizations and no approved indication records. Evaluation of a market authorization pathway via AIFA would be required before any clinical use in Italy.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs and a broad body of peer-reviewed literature confirm Ezetimibe's well-established efficacy in reducing LDL-C in patients with hyperlipoproteinemia — the TxGNN prediction is strongly validated and reflects existing clinical practice in most markets. The absence of Italian market authorization is the primary operational barrier, not a lack of clinical evidence.

**To proceed, the following is needed:**
- Submission of a market authorization application to AIFA (Agenzia Italiana del Farmaco) for the hyperlipoproteinemia indication
- Resolution of the mechanism of action data gap via DrugBank (DG002, High severity)
- Full package insert review for safety warnings, contraindications, and drug interactions (DG001, Blocking severity — required before S1 safety evaluation)
- Drug-drug interaction assessment, particularly for concomitant use with statins, fibrates, cyclosporine, and HIV protease inhibitors
- Pediatric subpopulation protocol: dedicated review for children aged 6–17 with familial hypercholesterolemia, where Phase 3 evidence (NCT00867165, n=138) is available
- Long-term cardiovascular outcomes monitoring plan, including hepatic function surveillance during chronic use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

