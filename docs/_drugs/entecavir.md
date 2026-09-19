---
layout: default
title: Entecavir
parent: Prove moderate (L3-L4)
nav_order: 93
evidence_level: L4
indication_count: 10
---

# Entecavir
{: .fs-9 }

Livello di evidenza: **L4** | Indicazioni previste: **10** 
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

# Entecavir: dall'epatite B all'infezione cronica da virus dell'epatite C

## Riassunto in una frase

L'entecavir è un potente antivirale analogo nucleosidico della guanosina, riconosciuto a livello globale come terapia orale di prima linea per l'infezione cronica da virus dell'epatite B (HBV).
Il modello TxGNN assegna il suo punteggio predittivo più alto all'**infezione cronica da virus dell'epatite C (HCV)** (99,98%), collocandola al rango 1 tra tutte le indicazioni nuove previste.
Tuttavia, **nessuna sperimentazione clinica dedicata o evidenza meccanicistica diretta** supporta l'attività anti-HCV dell'entecavir; il punteggio elevato riflette la sovrapposizione del vicinato di co-infezione nel grafo della conoscenza piuttosto che un vero potenziale di riposizionamento farmacologico.

---

## Panoramica rapida

| Voce | Contenuto |
|------|----------|
| Indicazione originale | Non registrato in Italia; indicazione stabilita globalmente per l'infezione cronica da virus dell'epatite B (HBV) |
| Nuova indicazione prevista | Infezione cronica da virus dell'epatite C |
| Punteggio di predizione TxGNN | 99,98% |
| Livello di evidenza | L4 |
| Stato del mercato italiano | ✗ Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Hold |

---

## Perché questa previsione è ragionevole?

L'entecavir è un analogo nucleosidico della deossiguanosina che, dopo la trifosforilazioneintracellulare, inibisce competitivamente tre funzioni sequenziali della DNA polimerasi dell'HBV: la sintesi della base-primer, la trascrizione inversa dell'RNA prigenomico in DNA a filamento meno e la sintesi del DNA a filamento positivo. La sua selettività per la replicazione dell'HBV è eccezionalmente elevata (IC₅₀ ≈ 0,004 µM). Numerosi studi clinici randomizzati Phase 3 completati hanno stabilito il suo ruolo di antivirale di prima linea con un'elevata barriera genetica alla resistenza, e viene raccomandato in tutte le principali linee guida internazionali per il trattamento dell'HBV.

L'assegnazione da parte del modello TxGNN di un punteggio del 99,98% per l'infezione cronica da HCV è principalmente guidata dalla topologia del grafo della conoscenza: nel grafo di co-occorrenza delle malattie, i nodi HBV e HCV condividono un vicinato denso a causa della co-infezione, delle vie di trasmissione condivise e dei contesti clinici di gestione sovrapposti. L'entecavir appare frequentemente insieme all'HCV nella letteratura proprio perché viene utilizzato per *prevenire la riattivazione dell'HBV* nei pazienti che ricevono terapia con antivirali ad azione diretta (DAA) per l'HCV — non perché tratti l'HCV stesso. L'HCV è un virus a RNA di senso positivo che si replica esclusivamente attraverso un'RNA polimerasi dipendente dall'RNA (RdRp NS5B), che è strutturalmente e funzionalmente distinta dalla trascrittasi inversa/DNA polimerasi dell'HBV bersaglio dell'entecavir. Nessun dato in vitro o clinico documenta alcuna attività anti-HCV NS5B per l'entecavir o i suoi metaboliti.

In sintesi, la previsione TxGNN al rango 1 per l'epatite C cronica dovrebbe essere interpretata come un **falso positivo del grafo della conoscenza** derivante dal segnale di co-occorrenza delle malattie, non come un'ipotesi di riposizionamento farmacologicamente fondata. Il risultato più azionabile in questo dossier di evidenza è la previsione al rango 2 — **infezione da virus dell'epatite B** — che porta evidenza L1 da numerosi studi clinici randomizzati Phase 3 completati e corrisponde all'indicazione già stabilita globalmente dell'entecavir. Il farmaco semplicemente non è ancora registrato in Italia, il che potrebbe rappresentare un'opportunità normativa e commerciale.

---

## Evidenza da studi clinici

| Numero dello studio | Fase | Stato | Arruolamento | Risultati principali |
|-------------|------|--------|-----------|--------------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completato | 23 | Studio prospettico della terapia DAA in pazienti co-infetti HCV/HBV; l'entecavir è stato utilizzato per gestire il rischio di riattivazione dell'HBV durante il trattamento anti-HCV — non come trattamento per l'HCV stesso. Studio più direttamente rilevante in questo dataset. |
| [NCT03662568](https://clinicaltrials.gov/study/NCT03662568) | Phase 1 | Completato | 56 | Studio di interazioni farmacologiche e farmacocinetica di Morphothiadine Mesilate/Ritonavir (un agente HCV investigazionale) combinato con entecavir o tenofovir in soggetti sani; nessun dato di efficacia HCV per l'entecavir. |
| [NCT00065507](https://clinicaltrials.gov/study/NCT00065507) | Phase 3 | Completato | 195 | Studio randomizzato Phase 3 cardine dell'entecavir vs. adefovir in HBV cronico con scompenso epatico; dati di efficacia HBV di base, nessuna rilevanza HCV. |
| [NCT00371150](https://clinicaltrials.gov/study/NCT00371150) | Phase 4 | Completato | 131 | Studio osservazionale dell'effetto antivirale dell'entecavir in pazienti HBV neri/africani e ispanici; focalizzato su HBV, nessun dato HCV. |
| [NCT01020565](https://clinicaltrials.gov/study/NCT01020565) | Phase 2 | Completato | 60 | Sicurezza e attività antivirale dell'entecavir (0,1 mg e 0,5 mg) in adulti giapponesi con HBV cronico a 52 settimane; focalizzato su HBV. |
| [NCT03272009](https://clinicaltrials.gov/study/NCT03272009) | Phase 1 | Completato | 73 | Sicurezza, farmacocinetica e farmacodinamica dell'agonista FXR EYP001a in soggetti con HBV cronico (alcuni riceventi terapia di base con entecavir); focalizzato su HBV. |
| [NCT01270178](https://clinicaltrials.gov/study/NCT01270178) | N/A | Sconosciuto | 420 | Studio prospettico dell'entecavir in pazienti HBV-positivi con HCC dopo ablazione a radiofrequenza; il riassunto cita HCC correlato a HCV ma la popolazione arruolata è costituita da pazienti HBV. |
| [NCT01848743](https://clinicaltrials.gov/study/NCT01848743) | Phase 3 | Sconosciuto | 120 | Tenofovir vs. lamivudina per HBV cronico con grave esacerbazione acuta; focalizzato su HBV, stato sconosciuto. |
| [NCT01354652](https://clinicaltrials.gov/study/NCT01354652) | Phase 4 | Terminato | 5 | Incidenza di acidosi lattica durante il trattamento con entecavir in pazienti HBV con grave cirrosi; terminato anticipatamente a causa di arruolamento molto basso (n=5). |
| [NCT05416008](https://clinicaltrials.gov/study/NCT05416008) | N/A | Sconosciuto | 150 | Studio osservazionale che indaga se i nucleosidi/nucleotidi a lungo termine (incluso l'entecavir) promuovono la steatosi epatica in pazienti con HBV cronico; focalizzato su HBV. |

> **Avvertenza importante:** Nessuno degli studi di cui sopra valuta l'entecavir come trattamento per l'infezione da HCV. NCT02555943 è l'unico studio con rilevanza contestuale HCV, e in quello studio il ruolo dell'entecavir è rigorosamente la soppressione dell'HBV. Nessuno studio Phase 2 o successivo ha testato prospetticamente l'entecavir contro la replicazione dell'HCV.

---

## Evidenza dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|------|------|---------|--------------|
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Coorte retrospettiva | *Viruses* | In 66 pazienti con HBV anti-HCV-positivi che ricevono analoghi nucleos(t)idici (incluso l'entecavir), l'RNA dell'HCV era rilevabile al basale in molti; la riattivazione dell'HCV è stata osservata durante/dopo la terapia anti-HBV. L'entecavir sopprime l'HBV ma non sopprime l'HCV — l'RNA dell'HCV non è stato ridotto dal trattamento con entecavir. |
| [28230928](https://pubmed.ncbi.nlm.nih.gov/28230928/) | 2017 | Osservazionale | *Journal of Gastroenterology and Hepatology* | Il rischio di riattivazione dell'HBV è stato indagato in pazienti CHC che ricevono terapia DAA; supporta la pratica della profilassi con entecavir in pazienti co-infetti HBV/HCV che iniziano il trattamento anti-HCV. Ruolo dell'entecavir = protezione HBV, non trattamento HCV. |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Revisione | *Expert Opinion on Pharmacotherapy* | Revisione completa del trattamento della co-infezione HBV/HCV; discute l'entecavir per il componente HBV nei pazienti co-infetti. Sottolinea l'alto rischio di cirrosi e HCC nella co-infezione e la necessità di una soppressione efficace dell'HBV. |
| [22959099](https://pubmed.ncbi.nlm.nih.gov/22959099/) | 2013 | Revisione + Caso | *Clinics and Research in Hepatology and Gastroenterology* | La co-infezione HBV/HCV è una sfida terapeutica; presenta un caso gestito con trattamento sequenziale. L'entecavir è identificato come il componente HBV appropriato; nessuna attività anti-HCV gli è attribuita. |
| [35327336](https://pubmed.ncbi.nlm.nih.gov/35327336/) | 2022 | Revisione | *Biomedicines* | Revisione panoramica della terapia dell'epatite virale cronica (HBV, HCV, HDV); discute come l'entecavir e il tenofovir raggiungono la soppressione virale nell'HBV ma sottolinea che l'HBV e l'HCV richiedono classi di farmaci completamente diverse. |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Revisione | *Wiener Medizinische Wochenschrift* | Revisione narrativa precoce che confronta i paesaggi terapeutici HBV e HCV; l'interferone pegilato è discusso per entrambi, mentre gli analoghi nucleosidici incluso l'entecavir sono identificati come specifici dell'HBV. |
| [32173307](https://pubmed.ncbi.nlm.nih.gov/32173307/) | 2020 | Revisione | *Clinics and Research in Hepatology and Gastroenterology* | Gestione dell'HBV e dell'HCV nei bambini; l'entecavir è riferito come una terapia HBV approvata per l'uso pediatrico. Nessuna indicazione pediatrica o nell'adulto per HCV è discussa per l'entecavir. |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Revisione | *Minerva Gastroenterologica e Dietologica* | Esamina gli effetti renali degli antivirali per l'HBV e l'HCV; classifica l'entecavir come analogo nucleosidico per l'HBV. Per l'HCV, classi di farmaci separate (inibitori delle proteasi, inibitori NS5B) sono discusse. |
| [21497740](https://pubmed.ncbi.nlm.nih.gov/21497740/) | 2011 | Revisione | *Best Practice & Research Clinical Gastroenterology* | Progressione della fibrosi nell'epatite virale cronica; dimostra che il trattamento con entecavir porta a miglioramento istologico e regressione della fibrosi nei pazienti HBV, supportando la soppressione virale dell'HBV sostenuta come meccanismo. |
| [24868325](https://pubmed.ncbi.nlm.nih.gov/24868325/) | 2014 | Revisione | *World Journal of Hepatology* | Gestione dell'HBV e dell'HCV nei riceventi di trapianto epatico e renale; l'entecavir e il tenofovir sono identificati come agenti HBV preferiti con elevata barriera genetica alla resistenza. L'HCV è trattato separatamente con regimi basati su interferone o DAA. |

---

## Informazioni sul mercato italiano

L'entecavir non è attualmente **commercializzato in Italia** (i registri AIFA documentano 0 autorizzazioni; `market_status: Not marketed`). Nessuna licenza di prodotto esiste da tabulare.

L'entecavir è disponibile commercialmente in numerosi altri mercati con nomi commerciali come **Baraclude®** (Bristol-Myers Squibb), con approvazioni della FDA (USA, 2005), EMA, PMDA (Giappone) e altre agenzie normative per il trattamento dell'infezione HBV cronica in adulti e bambini ≥2 anni. La sua assenza dal registro AIFA italiano potrebbe riflettere una decisione commerciale o normativa storica piuttosto che una barriera di sicurezza o efficacia.

---

## Considerazioni sulla sicurezza

Si prega di fare riferimento al foglio illustrativo (ad es., SmPC Baraclude® o etichetta FDA) per informazioni complete sulla sicurezza, poiché i dati di etichettatura italiani non sono disponibili (nessuna autorizzazione AIFA nel file).

**Segnale critico di sicurezza — co-infezione da HIV (basato sulla letteratura pubblicata):**
L'entecavir **non deve** essere utilizzato come monoterapia in pazienti con co-infezione HIV/HBV che non ricevono un regime antiretrovirale (ART) completamente soppressivo. Una serie di casi cardine del 2007 ha dimostrato che l'entecavir esercita un'attività parziale di inibizione della trascrittasi inversa dell'HIV-1 e può selezionare per la mutazione di resistenza alla lamivudina M184V dell'HIV, compromettendo gravemente le opzioni di trattamento futuro dell'HIV (la "sorpresa dell'entecavir," PMID 17582071). Questa è una restrizione di sicurezza di classe applicabile a tutti i prescrittori.

---

## Conclusioni e prossimi passi

**Decisione: Hold**

**Razionale:**
La previsione TxGNN al rango 1 per l'epatite C cronica è un falso positivo del grafo della conoscenza: il meccanismo d'azione dell'entecavir (inibizione della DNA polimerasi dell'HBV) non ha reattività incrociata con l'RNA polimerasi NS5B dell'HCV, e nessuno studio clinico o pre-clinico ha documentato alcuna attività anti-HCV. Perseguire l'entecavir come trattamento per l'HCV sarebbe scientificamente ingiustificato data la disponibilità di regimi DAA altamente curativi già approvati per l'HCV.

**Nota contestuale — il risultato più azionabile:**
La previsione TxGNN al rango 2, **infezione da virus dell'epatite B** (punteggio 99,85%, livello di evidenza L1), corrisponde all'indicazione approvata globale ben stabilita dell'entecavir. Numerosi studi clinici randomizzati Phase 3 completati confermano la sua superiorità rispetto ai comparatori nelle popolazioni HBV naive al trattamento e con esperienza terapeutica precedente. Il farmaco è semplicemente assente dal mercato italiano. Un percorso di registrazione AIFA per l'indicazione HBV potrebbe rappresentare un'opportunità più significativa dal punto di vista clinico e immediatamente azionabile rispetto a qualsiasi ipotesi di riposizionamento HCV.

**Per colmare i divari nei dati prima di qualsiasi ulteriore valutazione:**

- Ottenere il foglio illustrativo dell'entecavir (SmPC EMA o etichetta FDA) per risolvere DG001 (avvertimenti di sicurezza/controindicazioni) e DG002 (documentazione formale del MOA)
- Confermare lo stato di registrazione AIFA e identificare qualsiasi razionale storico di ritiro dall'UE o di mancata presentazione
- Se il riposizionamento HCV deve essere formalmente valutato nonostante quanto sopra, condurre saggi in vitro con replicon HCV per determinare se esiste alcuna attività inibitrice NS5B alle concentrazioni di entecavir clinicamente raggiungibili prima di impegnare risorse cliniche
- Implementare il protocollo di screening obbligatorio per la co-infezione da HIV in qualsiasi piano di uso clinico italiano futuro

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

