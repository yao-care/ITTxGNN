---
layout: default
title: Miglustat
parent: Prove elevate (L1-L2)
nav_order: 148
evidence_level: L2
indication_count: 10
---

# Miglustat
{: .fs-9 }

Livello di evidenza: **L2** | Indicazioni previste: **10** 
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

# Miglustat: dalla malattia di Gaucher alla malattia di Tay-Sachs

## Riassunto in una frase

Miglustat (Zavesca®) è una terapia orale con riduzione del substrato originariamente approvata per la malattia di Gaucher di tipo 1, che agisce inibendo la glucosilceramide sintasi (GCS) per ridurre la produzione di glicosfingolipidi nelle cellule sottoposte a stress lisosomiale.
Il modello TxGNN predice che potrebbe essere efficace per la **malattia di Tay-Sachs** (gangliosidosi GM2), supportato da **5 studi clinici** e **20 pubblicazioni**.
Sebbene la razionalità meccanicistica sia scientificamente convincente, gli studi di Fase 3 nella forma infantile sono stati interrotti anticipatamente — l'opportunità più realistica risiede nella **variante a insorgenza tardiva**, dove l'attività enzimatica residua consente alla terapia di riduzione del substrato di avere più spazio per agire.

---

## Panoramica rapida

| Elemento | Contenuto |
|------|------|
| Indicazione originale | Malattia di Gaucher di tipo 1 (secondo la letteratura pubblicata; nessuna autorizzazione di commercializzazione in Italia registrata) |
| Nuova indicazione prevista | Malattia di Tay-Sachs |
| Punteggio di previsione TxGNN | 99.75% |
| Livello di evidenza | L2 |
| Stato del mercato italiano | Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Procedere con salvaguardie |

---

## Perché questa previsione è ragionevole?

Miglustat è un imino-zucchero di piccole dimensioni che inibisce la glucosilceramide sintasi (GCS), il primo enzima impegnato nella biosintesi dei glicosfingolipidi. Piuttosto che sostituire un enzima carente, funziona come una **terapia di riduzione del substrato (SRT)**: rallentando la velocità con cui il substrato viene prodotto, riduce il carico lisosomiale a un livello in cui l'attività enzimatica residua può mantenere l'equilibrio metabolico.

La malattia di Tay-Sachs è causata da una deficienza di β-esosaminidasi A (HexA, codificata da *HEXA*), che normalmente degrada il glicoside GM2 nei lisosomi. Senza HexA funzionante, il GM2 si accumula implacabilmente nei neuroni, determinando neurodegenerazione progressiva. Poiché il GM2 è sintetizzato **a valle** della glucosilceramide nella via dei sfingolipidi, l'inibizione della GCS da parte del miglustat riduce l'apporto a monte dei precursori del GM2 — targeting direttamente la cascata di accumulo che HexA non può più risolvere.

Questo è precisamente lo stesso principio meccanicistico dietro l'uso approvato di miglustat nella malattia di Gaucher, dove la deficienza di glucocerebrosidasi porta all'accumulo di glucosilceramide. Sia la malattia di Gaucher che Tay-Sachs sono disturbi dell'immagazzinamento lisosomiale causati da difetti negli enzimi di catabolismo dei glicosfingolipidi, rendendo il concetto di SRT meccanicisticamente trasferibile. La distinzione clinica critica è che la **malattia di Tay-Sachs a insorgenza tardiva** (con attività HexA residua e accumulo più lento) rappresenta un bersaglio molto più trattabile della forma acuta infantile, dove la quasi-totale deficienza enzimatica e la progressione della malattia rapida rendono la SRT insufficiente da sola.

> I dati formali del meccanismo di azione da DrugBank non erano disponibili per questo rapporto. L'analisi meccanicistica di cui sopra è derivata dalla letteratura pubblicata contenuta nel pacchetto di prove.

---

## Prove da studi clinici

| Numero dello studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT00418847](https://clinicaltrials.gov/study/NCT00418847) | Fase 2 | Completato | 5 | PK e tollerabilità del miglustat nella gangliosidosi GM2 giovanile; conferma la penetrazione nel SNC ma il campione è troppo piccolo per conclusioni sull'efficacia |
| [NCT00672022](https://clinicaltrials.gov/study/NCT00672022) | Fase 3 | Completato | 10 | PK e sicurezza del miglustat nella gangliosidosi GM2 infantile (Tay-Sachs/Sandhoff); stabilisce la fattibilità del dosaggio ma non è progettato per valutare l'efficacia |
| [NCT03822013](https://clinicaltrials.gov/study/NCT03822013) | Fase 3 | Interrotto | 30 | Efficacia del miglustat in Sandhoff infantile/Tay-Sachs — interrotto anticipatamente; segnale negativo significativo per il fenotipo infantile |
| [NCT02030015](https://clinicaltrials.gov/study/NCT02030015) | Fase 4 | Interrotto | 16 | Studio Syner-G: miglustat + dieta chetogenica nella gangliosidosi — interrotto anticipatamente; la strategia combinata rimane irrisolta |
| [NCT07399704](https://clinicaltrials.gov/study/NCT07399704) | Fase 2 | In corso di reclutamento | 21 | Sicurezza a lungo termine di Nizubaglustat (AZ-3102) in GM2/NPC; include coorte in transizione da miglustat stabile — segnali di competizione attiva con SRT di prossima generazione |

---

## Prove dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [19346952](https://pubmed.ncbi.nlm.nih.gov/19346952/) | 2009 | RCT (Fase 2) | Genetics in Medicine | RCT di 12 mesi + estensione di 24 mesi che valuta la sicurezza e l'efficacia del miglustat nella gangliosidosi GM2 **a insorgenza tardiva** (Tay-Sachs/Sandhoff); base di prove principale per questa indicazione |
| [37209042](https://pubmed.ncbi.nlm.nih.gov/37209042/) | 2023 | Revisione sistematica | European Journal of Neurology | Revisione sistematica completa del miglustat nella gangliosidosi GM2; i risultati sono incoerenti tra gli studi — quadro di efficacia complessivamente misto |
| [32867370](https://pubmed.ncbi.nlm.nih.gov/32867370/) | 2020 | Revisione | Int J Molecular Sciences | Caratteristiche cliniche, fisiopatologia e opzioni terapeutiche attuali in tutte le gangliosidosi GM2; panoramica utile della malattia |
| [30524313](https://pubmed.ncbi.nlm.nih.gov/30524313/) | 2018 | Revisione | Frontiers in Physiology | Approcci terapeutici emergenti per Tay-Sachs inclusi SRT, terapia genica e potenziamento enzimatico — SRT posizionato come terapia ponte |
| [12808890](https://pubmed.ncbi.nlm.nih.gov/12808890/) | 2003 | Revisione del profilo del farmaco | Curr Opin Investigational Drugs | Profilo iniziale del farmaco miglustat; documenta l'approvazione originale di Gaucher e il programma di sviluppo in fase iniziale per Tay-Sachs/Fabry/NPC |
| [16434676](https://pubmed.ncbi.nlm.nih.gov/16434676/) | 2006 | Serie di casi | Neurology | Miglustat SRT in 2 pazienti infantili con TSD; il deterioramento neurologico non è stato fermato, ma è stata confermata l'esposizione del farmaco nel CSF — supporta l'accesso al SNC, non l'efficacia infantile |
| [28476546](https://pubmed.ncbi.nlm.nih.gov/28476546/) | 2017 | Osservazionale | Mol Genetics and Metabolism | Storia naturale della gangliosidosi GM2 infantile; nota il miglustat limitato da effetti collaterali gastrointestinali — segnale di tollerabilità rilevante |
| [33738443](https://pubmed.ncbi.nlm.nih.gov/33738443/) | 2021 | Coorte/Multi-malattia | Brain Communications | Acetil-leucina nei disturbi dell'immagazzinamento lisosomiale inclusa la gangliosidosi GM2; contesto per approcci di terapia combinata con SRT |
| [18618288](https://pubmed.ncbi.nlm.nih.gov/18618288/) | 2008 | Studio pilota | J Inherited Metabolic Disease | Test neurocognitivo nella Tay-Sachs a insorgenza tardiva come potenziale misura di outcome; informa il disegno dello studio per futuri studi sul miglustat |
| [9572057](https://pubmed.ncbi.nlm.nih.gov/9572057/) | 1998 | Revisione di scienze di base | Molecular Medicine Today | Biologia fondamentale della gangliosidosi GM2 e razionalità per strategie di riduzione del substrato; base scientifica storica |

---

## Informazioni sul mercato italiano

Miglustat non ha alcuna autorizzazione di commercializzazione in Italia. Non sono registrate licenze di prodotto.

> Per riferimento: In altri stati membri dell'UE, il miglustat (Zavesca®, Actelion/Janssen) è autorizzato per la malattia di Gaucher di tipo 1 nei pazienti per i quali la terapia sostitutiva enzimatica è inappropriata, e per la malattia di Niemann-Pick di tipo C. Qualsiasi applicazione di repositioning in Italia dovrebbe procedere attraverso i percorsi AIFA per i farmaci orfani o l'accesso off-label.

---

## Considerazioni sulla sicurezza

Nessun dato formale di sicurezza è stato recuperato per questo rapporto (le avvertenze del foglio illustrativo e il database di interazioni tra farmaci hanno entrambi restituito nessun risultato).

In base alla letteratura pubblicata all'interno del pacchetto di prove:
- **Effetti gastrointestinali**: Diarrea, flatulenza e dolore addominale sono gli eventi avversi più comunemente segnalati; questi sono stati abbastanza significativi da limitare il dosaggio nei pazienti pediatrici con gangliosidosi.
- **Effetti neurologici**: Il tremore è stato segnalato; richiede monitoraggio in un contesto di malattia neurodegenerativa.

> Si prega di fare riferimento al Riassunto delle caratteristiche del prodotto (RCP) di Zavesca® per il profilo di sicurezza completo prima di qualsiasi decisione clinica o prescrittiva.

---

## Conclusioni e prossimi passi

**Decisione: Procedere con salvaguardie**

**Razionalità:**
La base meccanicistica per il miglustat nella malattia di Tay-Sachs è scientificamente solida e direttamente analoga al suo uso approvato nella malattia di Gaucher — entrambe sono disturbi dell'immagazzinamento di glicosfingolipidi lisosomiali amenevoli alla riduzione del substrato. Un RCT di Fase 2 completato e una revisione sistematica del 2023 forniscono prove cliniche reali, anche se i risultati sono incoerenti e in gran parte limitati al fenotipo a insorgenza tardiva. La forma infantile non è un bersaglio praticabile data la terminazione anticipata della Fase 3.

**Per procedere, è necessario quanto segue:**

- **Specificare la popolazione target**: Lo sviluppo clinico dovrebbe concentrarsi esclusivamente sulla **malattia di Tay-Sachs a insorgenza tardiva (giovanile/adulta)**, dove l'attività HexA residua e l'accumulo più lento rendono meccanicisticamente fattibile la SRT; la Tay-Sachs infantile ha prove negative della Fase 3 (NCT03822013 interrotto)
- **Compilare DG001**: Ottenere le avvertenze del foglio illustrativo TFDA/AIFA e le controindicazioni prima che qualsiasi valutazione della sicurezza possa avanzare a S1
- **Compilare DG002**: Recuperare dati meccanicistici completi da DrugBank per il dossier meccanicistico completo
- **Valutare il panorama competitivo**: Nizubaglustat (AZ-3102, NCT07399704) sta attivamente reclutando come SRT di prossima generazione e potrebbe surclassare il miglustat in questo spazio
- **Definire gli endpoint di outcome**: Le misure di stabilità neurocognitiva e neurologica (informate da PMID 18618288) dovrebbero ancorare qualsiasi disegno di studio prospettico
- **Percorso normativo**: Valutare la fattibilità della designazione di farmaco orfano AIFA o dell'accesso secondo la Legge 648 prima di avviare qualsiasi programma specifico per l'Italia

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

