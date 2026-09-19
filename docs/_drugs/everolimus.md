---
layout: default
title: Everolimus
parent: Prove moderate (L3-L4)
nav_order: 99
evidence_level: L3
indication_count: 10
---

# Everolimus
{: .fs-9 }

Livello di evidenza: **L3** | Indicazioni previste: **10** 
{: .fs-6 .fw-300 }

---

## Indice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Relazione di valutazione farmaceutica

</div>

# Everolimus: da Carcinoma a Cellule Renali a Liposarcoma

## Riassunto in una frase

L'Everolimus è un analogo della rapamicina (rapalogo) e inibitore di mTOR, affermato a livello globale per il carcinoma a cellule renali, il carcinoma mammario con recettori ormonali positivi e i tumori neuroendocrini, sebbene non sia stata identificata un'autorizzazione al commercio nel set di dati normativo attuale. Il modello TxGNN predice che potrebbe essere efficace per **Liposarcoma**, con **1 studio clinico di Fase 2 attivo** e **5 pubblicazioni** che attualmente supportano questa linea di ricerca.

---

## Panoramica rapida

| Elemento | Contenuto |
|---|---|
| Indicazione originale | Carcinoma a cellule renali (affermato a livello globale; nessuna registrazione trovata nel set di dati attuale) |
| Indicazione nuova prevista | Liposarcoma |
| Punteggio di predizione TxGNN | 99.88% |
| Livello di evidenza | L3 |
| Stato del mercato italiano | ✗ Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Procedere con misure di salvaguardia |

---

## Perché questa previsione è ragionevole?

L'Everolimus è un inibitore di mTOR ben caratterizzato, sebbene i dati formali del suo meccanismo d'azione dal database DrugBank non siano stati inclusi in questo pacchetto di evidenze. Agisce inibendo mTORC1 (complesso 1 del bersaglio meccanistico di rapamicina), sopprimendo gli effettori a valle S6K1 e 4EBP1, che sono regolatori critici della sintesi proteica e della progressione del ciclo cellulare G1→S. Questo meccanismo è alla base del suo uso approvato nel carcinoma a cellule renali e nel carcinoma mammario con recettori ormonali positivi, dove la sovraattivazione della via PI3K/Akt/mTOR promuove la crescita tumorale.

Il liposarcoma dedifferenziato (DDLS) — il sottotipo primario mirato negli attuali studi clinici — è biologicamente rilevante per questo meccanismo. Uno studio clinicopatologico di 99 campioni di DDLS (PMID 26518767, 2016) ha fornito evidenza immunoistochimica dell'attivazione della via Akt/mTOR e MAPK, insieme alla dimostrazione in vitro degli effetti antitumorali degli inibitori di mTOR. Il DDLS è ulteriormente caratterizzato dall'amplificazione del gene CDK4, stabilendo una forte razionale biologica per combinare l'inibizione di CDK4/6 con l'inibizione di mTOR — una strategia già convalidata per produrre inibizione della crescita sinergica in più modelli tumorali.

La previsione TxGNN è direttamente rafforzata da uno studio di Fase 2 in corso (NCT03114527) che valuta Ribociclib (inibitore di CDK4/6) più Everolimus in DDL avanzato e leiomiosarcoma, con risultati pubblicati già apparsi in Clinical Cancer Research (PMID 37967116, 2024). Insieme, i dati meccanistici, le evidenze di sinergia preclinica e i dati clinici di fase precoce formano una razionale coerente e biologicamente plausibile per Everolimus nel liposarcoma.

---

## Evidenza da studi clinici

| Numero dello studio | Fase | Stato | Arruolamento | Risultati chiave |
|---|---|---|---|---|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Fase 2 | Attivo, non in arruolamento | 48 | Studio in due centri, due bracci, che valuta Ribociclib + Everolimus nel liposarcoma dedifferenziato avanzato (Braccio A) e leiomiosarcoma (Braccio B) in pazienti con ≥1 terapia sistemica precedente. Ribociclib 300 mg/giorno 3 settimane on/1 settimana off; Everolimus 2.5 mg giornalieri. Completamento previsto dicembre 2025. |

---

## Evidenza dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati chiave |
|---|---|---|---|---|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Risultati Fase 2 | Clinical Cancer Research | Risultati pubblicati dello studio di Fase 2 Ribociclib + Everolimus (NCT03114527) in DDL e LMS avanzati; l'inibizione duale di CDK4 e mTOR dimostra attività antitumorale sinergica in più modelli tumorali |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Studio traslazionale | Tumour Biology | Analisi immunoistochimica di 99 campioni di DDLS che dimostrano l'attivazione della via Akt/mTOR e MAPK; i dati in vitro confermano l'effetto antitumorale dell'inibitore di mTOR, fornendo una razionale meccanistica diretta |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Revisione | Frontiers in Oncology | Revisione completa degli inibitori di CDK nei sarcomi utilizzando modelli di xenotrapianto ortotopico derivato da pazienti (PDOX); identifica le strategie di combinazione CDK4/6 + mTOR come candidati ad alta priorità per la traduzione clinica |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclinico | Anticancer Research | Valutazione dell'eribulina in combinazione con agenti antitumorali meccanicamente distinti in modelli di xenotrapianto tumorale umano includendo liposarcoma; supporta l'esplorazione di approcci multi-agente |
| [41991999](https://pubmed.ncbi.nlm.nih.gov/41991999/) | 2026 | Studio molecolare | Oncogene | L'inibitore di XPO1 (Selinexor) interrompe il circuito regolatoria trascrizionale centrale di DDLPS modulando la traduzione; evidenzia la regolazione traslazionale come una vulnerabilità oncogenica chiave e sottolinea il continuo bisogno insoddisfatto di terapie mirate efficaci in DDLPS |

---

## Citotossicità

| Elemento | Contenuto |
|---|---|
| Classificazione della citotossicità | Terapia mirata — inibitore di mTOR (rapalogo); non è un agente citotossico convenzionale |
| Rischio di mielosoppressione | Basso-moderato — anemia, trombocitopenia e linfopenia sono stati segnalati, ma la gravità è generalmente inferiore alla chemioterapia convenzionale |
| Classificazione dell'emetogenicità | Bassa |
| Elementi di monitoraggio | Emocromo con differenziale, glicemia a digiuno, lipidi sierici (trigliceridi e colesterolo), creatinina sierica, test della funzionalità epatica (ALT/AST) e valutazione polmonare (rischio di polmonite non infettiva) |
| Protezione della manipolazione | Precauzioni standard di manipolazione degli oncologici orali; consultare la politica istituzionale di manipolazione dei farmaci citotossici per gli agenti mirati orali |

---

## Considerazioni di sicurezza

Si prega di fare riferimento al foglio illustrativo per informazioni sulla sicurezza.

---

## Conclusione e prossimi passi

**Decisione: Procedere con misure di salvaguardia**

**Razionale:**
Uno studio di Fase 2 attivo (NCT03114527) con risultati pubblicati con revisione paritaria valuta direttamente Everolimus nel liposarcoma dedifferenziato, supportato da dati meccanistici solidi che dimostrano l'attivazione della via mTOR in questo tipo di tumore. Tuttavia, l'evidenza attuale copre un regime di combinazione (Ribociclib + Everolimus) piuttosto che la monoterapia con Everolimus, lo studio non è ancora formalmente completato, e il farmaco non ha autorizzazione al commercio in questa giurisdizione.

**Per procedere, è necessario quanto segue:**
- Risultati finali di NCT03114527 al completamento dello studio (previsto dicembre 2025)
- Chiarimento della strategia di trattamento: monoterapia con Everolimus vs. combinazione con un inibitore di CDK4/6 per DDL
- Valutazione dell'autorizzazione al commercio o percorso di uso compassionevole per Everolimus in questa giurisdizione
- Recupero formale dei dati del meccanismo d'azione di DrugBank per completare la documentazione meccanistica
- Piano completo di monitoraggio della sicurezza che copra polmonite, tossicità metaboliche (iperglicemia, dislipidemia), mielosoppressione e rilevanti interazioni farmaco-farmaco

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

