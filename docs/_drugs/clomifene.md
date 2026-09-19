---
layout: default
title: Clomifene
parent: Prove elevate (L1-L2)
nav_order: 55
evidence_level: L1
indication_count: 10
---

# Clomifene
{: .fs-9 }

Livello di evidenza: **L1** | Indicazioni previste: **10** 
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

# Clomifene: Dall'induzione dell'ovulazione all'anovulazione

## Sintesi a una frase

Il Clomifene (citrato di clomifene) è un modulatore selettivo dei recettori degli estrogeni (SERM) con oltre 60 anni di uso clinico globale come agente di prima linea per l'induzione dell'ovulazione nell'infertilità anovulatoria, sebbene non sia attualmente registrato in Italia.
Il modello TxGNN ha generato 10 indicazioni previste; **anovulazione** (rank #10, score 99.52%) è l'unica previsione con robuste prove cliniche, supportata da **50 trial clinici** e **20 pubblicazioni** — l'unico risultato di livello L1 nell'intero set di previsioni.
Le previsioni con ranking più alto (rank 1–9) sono state valutate come Sospensione o Domanda di ricerca a causa di assenti legami meccanicistici o mancanza di qualsiasi evidenza clinica, rendendo l'anovulazione il singolo candidato attuabile da questa esecuzione TxGNN.

---

## Panoramica rapida

| Elemento | Contenuto |
|---------|---------|
| Indicazione originaria | Non registrata in Italia; globalmente consolidata per l'induzione dell'ovulazione nell'infertilità anovulatoria (incl. PCOS) |
| Indicazione prevista nuova | Anovulazione (Gruppo II OMS) |
| Score di previsione TxGNN | 99.52% |
| Livello di evidenza | L1 |
| Stato del mercato italiano | Non registrata |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Procedere con protezioni |

---

## Perché questa previsione è ragionevole?

I dati formali del meccanismo d'azione di DrugBank per il Clomifene non sono stati recuperati in questo pacchetto di evidenze. Sulla base della letteratura clinica ben consolidata, il Clomifene è un SERM della classe trifeniletilidene. Occupa competitivamente i recettori degli estrogeni (ERα/ERβ) nel nucleo arcuato ipotalamico, bloccando il normale segnale di feedback negativo degli estrogeni. Questa interruzione aumenta la frequenza e l'ampiezza degli impulsi di Kisspeptina/GnRH, determinando un aumento sincronizzato di FSH e LH ipofisari. L'aumento di gonadotropine risultante stimola il reclutamento dei follicoli, la maturazione del follicolo dominante e infine l'ovulazione.

Questo meccanismo affronta direttamente la fisiopatologia di base dei disturbi anovulatori del Gruppo II OMS — inclusa la sindrome dell'ovaio policistico (PCOS) — dove l'asse ipotalamico-ipofisario-ovarico (HPO) è funzionalmente disregolato ma la macchina ovarica rimane in grado di rispondere. Per questi pazienti, rimuovere il blocco ipotalamico del feedback degli estrogeni è sufficiente per ripristinare la cascata ormonale endogena necessaria per l'ovulazione. Questo è il motivo per cui il Clomifene rimane la spina dorsale della terapia di induzione dell'ovulazione di prima linea da più di sei decenni, con molteplici RCT di Fase 3/4 e diverse revisioni sistematiche Cochrane che confermano la sua efficacia.

> **Contesto della previsione TxGNN — Rank 1–9:** Le nove previsioni con ranking più alto includono disturbi della copia numero cromosomico (trisomia parziale/tetrasomia di chr5, chr12, chr18), difetti strutturali anatomici (setti vaginali trasversali e longitudinali) e sindromi genetiche rare (difetto della steroidogenesi testicolare 46,XY, portatrice di X fragile femmina, BPES e sua variante 3q23). Ognuno è stato valutato come **Sospensione** o **Domanda di ricerca**: le anomalie del dosaggio cromosomico sono inaccessibili a qualsiasi meccanismo SERM; i difetti anatomici strutturali richiedono correzione chirurgica; e sebbene BPES e insufficienza ovarica prematura associata a X fragile condividano un'intersezione teorica dell'asse estrogenico, non esiste alcuna evidenza clinica. Score TxGNN quasi identici su molteplici voci cromosomiche (0.99537–0.99538) suggeriscono fortemente artefatti di clustering del grafo della conoscenza nel vicinato del nodo del sistema riproduttivo piuttosto che vero segnale biologico. L'anovulazione rimane l'unica previsione supportata da evidenza diretta meccanicistica e clinica.

---

## Evidenza da trial clinici

| Numero trial | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT00478504](https://clinicaltrials.gov/study/NCT00478504) | Fase 4 | Completato | 159 | RCT crossover in doppio cieco: letrozolo vs Clomifene per induzione dell'ovulazione in PCOS; valutato tasso di gravidanza, tasso di gravidanza multipla e tasso di nascita viva — confronto head-to-head primario di Fase 4 |
| [NCT00610077](https://clinicaltrials.gov/study/NCT00610077) | Fase 3 | Completato | 55 | Trial multicentrico randomizzato aperto: letrozolo vs Clomifene nell'infertilità anovulatoria; risposta follicolare ciclo per ciclo e risultati di gravidanza confrontati tra 59 e 68 cicli |
| [NCT00296465](https://clinicaltrials.gov/study/NCT00296465) | Fase 2/3 | Completato | 132 | RCT multicentrico in doppio cieco controllato con placebo: GnRH pulsatile (IV/SC) vs Clomifene nell'infertilità anovulatoria/oligoovulatoria; ha valutato direttamente l'efficacia e la sicurezza dell'induzione dell'ovulazione con Clomifene |
| [NCT00213148](https://clinicaltrials.gov/study/NCT00213148) | Fase 2 | Completato | 271 | Studio multicentrico in doppio cieco di ricerca della dose: anastrozolo vs Clomifene nella disfunzione ovulatoria; ampio campione che fornisce dati dose-risposta per la crescita follicolare e l'induzione dell'ovulazione |
| [NCT00795808](https://clinicaltrials.gov/study/NCT00795808) | Fase 4 | Completato | 171 | RCT multicentrico: Metformina + Clomifene vs Clomifene da solo vs Metformina da sola nella PCOS anovulatoria; stratificato per BMI (≤32 vs >32) per valutare il beneficio additivo della sensibilità all'insulina |
| [NCT01573858](https://clinicaltrials.gov/study/NCT01573858) | N/A | Completato | 1,000 | Trial PCOSAct — RCT a quattro bracci: due protocolli di agopuntura combinati con Clomifene vs placebo in donne PCOS anovulatorie; endpoint primario tasso di nascita viva; evidenza reale su larga scala |
| [NCT01896492](https://clinicaltrials.gov/study/NCT01896492) | Fase 4 | Completato | 200 | RCT in doppio cieco: Clomifene + N-acetilcisteina (aggiunta antiossidante) vs Clomifene da solo in PCOS di nuova diagnosi; valutato impatto su tassi di ovulazione e gravidanza |
| [NCT00558077](https://clinicaltrials.gov/study/NCT00558077) | Fase 4 | Completato | 50 | RCT: diatermocoagulazione laparoscopica ovarica vs Metformina + Clomifene come trattamento di seconda linea dopo fallimento della monoterapia con Clomifene nella PCOS anovulatoria |
| [NCT02381184](https://clinicaltrials.gov/study/NCT02381184) | Fase 2/3 | Completato | 160 | RCT: regime Clomifene esteso (10 giorni) vs drilling ovarico laparoscopico nella PCOS resistente a Clomifene; tasso di ovulazione, spessore endometriale e tasso di gravidanza come outcome co-primari |
| [NCT06486870](https://clinicaltrials.gov/study/NCT06486870) | Fase 3 | Completato | 183 | RCT a tre bracci che confronta due terapie di induzione dell'ovulazione vs drilling ovarico laparoscopico in donne PCOS resistenti a Clomifene; completato gennaio 2024 — evidenza di Fase 3 più recente in questa indicazione |

---

## Evidenza dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|------|------|------|---------|
| [36165742](https://pubmed.ncbi.nlm.nih.gov/36165742/) | 2022 | Cochrane SR / Meta-analisi | Cochrane Database Syst Rev | Letrozolo vs Clomifene per induzione dell'ovulazione in PCOS: letrozolo produce tassi più elevati di nascita viva e ovulazione; Clomifene confermato come standard storico di prima linea rispetto al quale tutti gli alternative sono valutati |
| [29273245](https://pubmed.ncbi.nlm.nih.gov/29273245/) | 2018 | RCT fattoriale 2×2 | Lancet | Trial M-OVIN: gonadotropine vs Clomifene ± IUI nell'anovulazione normogonadotropica con fallimento del Clomifene; definisce quando passare da Clomifene alla terapia di seconda linea |
| [29183107](https://pubmed.ncbi.nlm.nih.gov/29183107/) | 2017 | Cochrane SR | Cochrane Database Syst Rev | Farmaci che aumentano la sensibilità all'insulina (metformina, TZD) vs Clomifene per subfertilità PCOS; supporta il ruolo centrale del Clomifene negli algoritmi di trattamento standard per PCOS anovulatoria |
| [28143834](https://pubmed.ncbi.nlm.nih.gov/28143834/) | 2017 | Meta-analisi di rete | BMJ | Revisione sistematica + meta-analisi di rete che confronta tutti i trattamenti di prima linea per anovulazione del Gruppo II OMS; fornisce efficacia comparativa classificata incluso il Clomifene |
| [15674894](https://pubmed.ncbi.nlm.nih.gov/15674894/) | 2005 | Cochrane SR | Cochrane Database Syst Rev | Anti-estrogeni orali e adiuvanti per subfertilità correlata all'anovulazione; revisione fondamentale che stabilisce lo status di prima linea del Clomifene e valuta tamoxifene, desametasone, bromocriptina e inibitori dell'aromatasi per la resistenza |
| [36622200](https://pubmed.ncbi.nlm.nih.gov/36622200/) | 2023 | Analisi di follow-up RCT | Hum Reprod | Risultati a lungo termine dopo il passaggio a gonadotropine vs continuazione di Clomifene ± IUI nell'anovulazione normogonadotropica; evidenza critica per decisioni di sequenziamento del trattamento post-fallimento del Clomifene |
| [41863134](https://pubmed.ncbi.nlm.nih.gov/41863134/) | 2026 | Revisione | Gynecol Endocrinol | Revisione più recente e completa del citrato di clomifene nell'anovulazione: MOA, epidemiologia, efficacia clinica, predittori di esito del trattamento e limitazioni attuali |
| [25681838](https://pubmed.ncbi.nlm.nih.gov/25681838/) | 2015 | Revisione clinica | Obstet Gynecol Clin North Am | Revisione dell'induzione dell'ovulazione: farmacologia, indicazioni, schemi di dosaggio, efficacia, terapie adiuvanti e monitoraggio — riferimento clinico standard per l'uso del Clomifene |
| [21406133](https://pubmed.ncbi.nlm.nih.gov/21406133/) | 2010 | Revisione clinica | BMJ Clin Evid | Revisione basata su evidenze dei trattamenti dell'infertilità femminile, incluso il Clomifene per il fallimento ovulatorio; contestualizza il Clomifene nel percorso più ampio di gestione dell'infertilità |
| [2282740](https://pubmed.ncbi.nlm.nih.gov/2282740/) | 1990 | Revisione farmacologica | Baillières Clin Obstet Gynaecol | Revisione farmacologica seminale del citrato di clomifene: meccanismo, uso clinico, principi di dosaggio e profilo degli effetti collaterali — il riferimento fondamentale che stabilisce il suo ruolo nel trattamento dell'anovulazione |

---

## Informazioni sul mercato italiano

Il Clomifene attualmente **non è registrato presso AIFA** in Italia. Non sono presenti autorizzazioni di commercializzazione (0 licenze). Qualsiasi uso clinico in Italia in questo momento richiederebbe sia una domanda formale di autorizzazione di commercializzazione che l'accesso attraverso un percorso di uso compassionevole / prescrizione off-label secondo la normativa italiana applicabile.

---

## Considerazioni sulla sicurezza

Si prega di fare riferimento al foglio illustrativo per le informazioni sulla sicurezza.

> Sulla base della letteratura clinica consolidata, i seguenti aspetti di sicurezza sono riconosciuti per il Clomifene nell'induzione dell'ovulazione:
> - **Gravidanza multipla**: Il tasso di gemelli è approssimativamente 5–10%; i multipli di ordine superiore sono possibili, in particolare a dosi più elevate
> - **Sindrome da iperstimolazione ovarica (OHSS)**: Rischio più basso rispetto ai protocolli basati su gonadotropine FSH, ma si consiglia il monitoraggio ecografico durante i cicli di stimolazione
> - **Effetti periferici anti-estrogenici**: Può ridurre lo spessore endometriale e la qualità del muco cervicale, abbassando potenzialmente i tassi di impianto nonostante l'ovulazione riuscita — un gap riconosciuto tra il tasso di ovulazione (~80%) e il tasso di gravidanza (~40%) per ciclo

---

## Conclusioni e prossimi passi

**Decisione: Procedere con protezioni**

**Razionale:**
Il Clomifene ha il più alto livello di evidenza possibile (L1) per l'anovulazione, supportato da molteplici RCT di Fase 3/4 completati, revisioni sistematiche Cochrane e sei decenni di pratica clinica globale. Il modello TxGNN assegna uno score di previsione del 99.52%, e il meccanismo SERM del farmaco affronta direttamente e specificamente la disregolazione dell'asse HPO sottostante all'infertilità anovulatoria del Gruppo II OMS. La barriera primaria all'uso in Italia è l'attuale assenza di registrazione AIFA piuttosto che qualsiasi gap nell'evidenza di efficacia clinica.

**Per procedere, è necessario quanto segue:**
- Ottenere il foglio illustrativo formale per il Clomifene (controindicazioni, avvertenze, profilo di sicurezza completo) per completare lo screening di sicurezza S1 attualmente bloccato dal gap di dati
- Recuperare la documentazione completa del MOA di DrugBank (attualmente contrassegnata come gap di dati DG002)
- Valutare il percorso normativo AIFA: domanda di autorizzazione di commercializzazione vs. framework di uso off-label/compassionevole
- Sviluppare un protocollo di monitoraggio della sicurezza clinica che copra: sorveglianza ecografica per ciclo di stimolazione, consulenza sulla gravidanza multipla, stratificazione del rischio OHSS e una politica di durata massima del trattamento (pratica standard: ≤6 cicli consecutivi)
- Esaminare il posizionamento attuale di prima linea del Clomifene rispetto al letrozolo nel contesto clinico italiano, dato che l'evidenza Cochrane recente (2022) e le linee guida PCOS internazionali sempre più favoriscono il letrozolo come preferito di prima linea per l'anovulazione correlata a PCOS

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

