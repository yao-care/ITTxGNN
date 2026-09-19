---
layout: default
title: Risperidone
parent: Prove elevate (L1-L2)
nav_order: 179
evidence_level: L1
indication_count: 6
---

# Risperidone
{: .fs-9 }

Livello di evidenza: **L1** | Indicazioni previste: **6** 
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

# Risperidone: From Schizophrenia to Major Affective Disorder

## Riassunto in una frase

Risperidone è un antipsicotidco atipico di seconda generazione consolidato nel trattamento della schizofrenia e della mania bipolare acuta.
Il modello TxGNN — valutato in 6 indicazioni previste in questo pacchetto multidisciplinare — identifica **Major Affective Disorder** (che comprende il disturbo depressivo maggiore e le condizioni dello spettro bipolare) come il bersaglio di riproposizionamento con il miglior supporto di evidenze,
supportato da **37 studi clinici** e **20 pubblicazioni**, incluse 5 revisioni sistematiche e meta-analisi.

---

## Panoramica rapida

| Item | Contenuto |
|------|---------|
| Indicazione originale | Schizofrenia / Mania bipolare (profilo farmacologico consolidato; nessuna autorizzazione italiana registrata) |
| Indicazione prevista | Major Affective Disorder |
| Punteggio di previsione TxGNN | 99.11% |
| Livello di evidenza | L1 |
| Stato di mercato italiano | ✗ Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Proceed with Guardrails |

---

## Perché questa previsione è ragionevole?

I dati formali sui meccanismi d'azione da DrugBank non sono stati acquisiti in questo pacchetto di evidenze. Tuttavia, la farmacologia della risperidone è ampiamente caratterizzata nella letteratura pubblicata: agisce come un antagonista combinato del **recettore D2 della dopamina** e del **recettore 5-HT2A della serotonina**. Il blocco D2 fornisce effetti antiman­iacali e antipsicotici attenuando l'eccesso di tono dopaminergico, mentre l'antagonismo 5-HT2A disinibisce la trasmissione serotoninergica prefrontale — un percorso direttamente collegato all'incremento antidepressivo. Questo profilo di doppio recettore si mappa precisamente sul substrato neurobiologico del disturbo affettivo maggiore.

Il disturbo affettivo maggiore è caratterizzato patofisiologicamente da disregolazione di circuiti dopaminergici e serotoninergici. La mania bipolare comporta iperattività dopaminergica sensibile all'antagonismo D2, mentre la depressione resistente al trattamento (TRD) riflette spesso segnalazione serotoninergica insufficiente che beneficia della disinibizione 5-HT2A quando la risperidone viene aggiunta a un antidepressivo. Questa dualità meccanicistica pone la risperidone in una posizione unica nello spettro affettivo, come confermato dall'ampiezza delle evidenze degli RCT di Fase 3 in questo pacchetto.

Un importante avvertimento normativo deve essere sottolineato: risperidone ha già un'approvazione FDA per la mania bipolare acuta e l'irritabilità correlata all'ASD. Il campo `original_indications: []` in questo pacchetto di evidenze quasi certamente riflette un gap nell'estrazione dati piuttosto che l'assenza di approvazioni precedenti. La previsione TxGNN rappresenta quindi probabilmente un mix di **conferma di indicazione esistente** (mania bipolare) e **vero riproposizionamento** (incremento TRD) — il confine deve essere chiarito con l'AIFA prima che questo sia classificato come un'applicazione di riproposizionamento novel.

---

## Evidenza da studi clinici

| Numero di studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT00391222](https://clinicaltrials.gov/study/NCT00391222) | Fase 3 | Completato | 585 | RCT in doppio cieco, controllato con placebo e con controllo attivo, di monoterapia LAI con risperidone vs placebo (+ comparatore olanzapina) per la prevenzione della ricorrenza dell'episodio di umore nel disturbo bipolare I; lo studio più grande e ad alta potenza in questo dataset |
| [NCT00057681](https://clinicaltrials.gov/study/NCT00057681) | Fase 3 | Completato | 379 | Studio TEAM — confronto testa a testa di litio, acido valproico e risperidone in bambini/adolescenti con mania ad esordio precoce; RCT di Fase 3 pediatrica di riferimento |
| [NCT00095134](https://clinicaltrials.gov/study/NCT00095134) | Fase 3 | Completato | 630 | Risperidone aggiuntivo vs placebo in pazienti con MDD e risposta antidepressiva subottimale; uno dei più grandi RCT di Fase 3 per il riproposizionamento nella MDD resistente al trattamento |
| [NCT00044681](https://clinicaltrials.gov/study/NCT00044681) | Fase 3 | Completato | 258 | Incremento con risperidone della monoterapia SSRI nella TRD — include fase di mantenimento a lungo termine che confronta risperidone vs placebo aggiunto per dimostrare la durabilità della risposta |
| [NCT00277654](https://clinicaltrials.gov/study/NCT00277654) | Fase 3 | Completato | 111 | Monoterapia con risperidone vs placebo nel disturbo bipolare ambulatoriale con comorbidità di panico o disturbo d'ansia generalizzato; RCT in doppio cieco che valuta l'efficacia del singolo agente |
| [NCT00176202](https://clinicaltrials.gov/study/NCT00176202) | Fase 3 | Completato | 65 | Risperidone vs valpromato di sodio nel disturbo bipolare pediatrico con valutazione del circuito di neuroimaging; verifica l'ipotesi di equivalenza nei bambini |
| [NCT00174577](https://clinicaltrials.gov/study/NCT00174577) | Fase 3 | Sconosciuto | 84 | Incremento con risperidone in pazienti che hanno fallito o solo parzialmente risposto ad un'adeguata prova di antidepressivo; valuta la sicurezza e l'efficacia nella popolazione di risponditori parziali |
| [NCT00167479](https://clinicaltrials.gov/study/NCT00167479) | Fase 4 | Completato | 60 | Monoterapia con risperidone nel disturbo bipolare ambulatoriale con ansia moderatamente grave; dati di efficacia nel mondo reale controllati con placebo in doppio cieco |
| [NCT00203723](https://clinicaltrials.gov/study/NCT00203723) | Fase 4 | Terminato | 45 | ECT combinato con risperidone vs ECT solo per la depressione resistente al trattamento; la terminazione precoce limita le conclusioni, ma fornisce un segnale preliminare di incremento specifico per MDD |
| [NCT01282632](https://clinicaltrials.gov/study/NCT01282632) | Fase 1/2 | Completato | 42 | Confronto in doppio cieco tra risperidone vs olanzapina come aggiunta a un SSRI fallito nella TRD; primo confronto testa a testa diretto di antipsicotici atipici nella depressione resistente al trattamento |

---

## Evidenza dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | Revisione sistematica e meta-analisi di rete | J Affect Disorders | Ha confrontato l'efficacia e i tassi di interruzione tra gli agenti di incremento per la TRD dell'adulto utilizzando la meta-analisi di rete; risperidone incluso come comparatore attivo |
| [35861202](https://pubmed.ncbi.nlm.nih.gov/35861202/) | 2023 | Revisione sistematica e meta-analisi | J Psychopharmacology | Ha valutato i trattamenti aggiuntivi e combinati per la TRD in fase iniziale; le SGA inclusa risperidone valutate per il beneficio di risposta e remissione rispetto alla monoterapia antidepressiva |
| [34238049](https://pubmed.ncbi.nlm.nih.gov/34238049/) | 2021 | Revisione sistematica e meta-analisi | J Psychopharmacology | Ha confrontato antidepressivi + SGA vs esketamina vs litio per il trattamento del MDD; fornisce contesto di tollerabilità e efficacia testa a testa per l'incremento con risperidone |
| [35510505](https://pubmed.ncbi.nlm.nih.gov/35510505/) | 2023 | Revisione sistematica e meta-analisi | Psychological Medicine | Meta-analisi completa degli antipsicotici sia come monoterapia che come terapia aggiuntiva nel MDD; dati di efficacia e tollerabilità della risperidone aggregati attraverso molteplici RCT |
| [21154393](https://pubmed.ncbi.nlm.nih.gov/21154393/) | 2010 | Revisione sistematica | Cochrane Database Syst Rev | Revisione Cochrane degli antipsicotici di seconda generazione per MDD e distimia; sintesi di evidenze fondamentale che mostra risperidone come un agente efficace di potenziamento antidepressivo |
| [17975181](https://pubmed.ncbi.nlm.nih.gov/17975181/) | 2007 | RCT | Ann Intern Med | Studio randomizzato di incremento con risperidone per MDD refrattaria al trattamento pubblicato in Annals of Internal Medicine; ha dimostrato un beneficio di risposta significativo vs aggiunta di placebo |
| [25295435](https://pubmed.ncbi.nlm.nih.gov/25295435/) | 2014 | Studio basato sulla popolazione | J Clin Psychiatry | Studio basato sulla popolazione a livello nazionale che ha valutato l'efficacia nel mondo reale dell'incremento di aripiprazolo, olanzapina, quetiapina e risperidone per il MDD utilizzando i dati dell'assicurazione sanitaria nazionale |
| [21189367](https://pubmed.ncbi.nlm.nih.gov/21189367/) | 2011 | Revisione clinica | Ann Pharmacother | Ha revisionato l'efficacia e la sicurezza dell'incremento con risperidone in pazienti con MDD che hanno fallito la monoterapia antidepressiva; sintetizza le evidenze a livello di studio per supportare la guida della pratica clinica |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Revisione della pratica clinica | Acta Psychiatr Scand | Algoritmi di trattamento basati su evidenze per la mania bipolare; rivede il posizionamento della risperidone accanto agli stabilizzatori dell'umore con raccomandazioni di gestione clinica |
| [20486830](https://pubmed.ncbi.nlm.nih.gov/20486830/) | 2010 | Revisione clinica | Expert Opin Pharmacother | LAI risperidone come monoterapia e terapia aggiuntiva nel mantenimento del Bipolare I; affronta la profilassi a lungo termine e la non aderenza al trattamento con formulazione iniettabile |

---

## Informazioni sul mercato italiano

Risperidone attualmente non ha autorizzazioni registrate nel record in Italia (AIFA). Nessun nome di prodotto, forma di dosaggio o indicazioni approvate è stato restituito in questo pacchetto di evidenze.

> ⚠️ **Questo risultato è anomalo.** Risperidone è un antipsicotidco ampiamente utilizzato con approvazioni normative negli USA, UE, Giappone e nella maggior parte dei mercati importanti. Un risultato di zero autorizzazioni quasi certamente riflette una limitazione nell'estrazione di dati piuttosto che l'effettiva assenza dal mercato italiano. **La verifica diretta tramite il registro online dell'AIFA (farmaci.agenziafarmaco.gov.it) è obbligatoria prima di trarre qualsiasi conclusione normativa.**

---

## Considerazioni sulla sicurezza

Si prega di fare riferimento al foglio illustrativo per le informazioni sulla sicurezza.

> Il database delle interazioni farmacologiche (DDI) non ha restituito risultati, e gli avvertimenti del foglio illustrativo specifico dell'Italia non sono stati acquisiti in questo pacchetto di evidenze. In base al profilo farmacologico consolidato di risperidone, le seguenti aree dovrebbero essere affrontate proattivamente in qualsiasi protocollo clinico:
> - **Monitoraggio metabolico**: peso, glicemia a digiuno, HbA1c, profilo lipidico (rischio di sindrome metabolica con uso a lungo termine)
> - **Monitoraggio neurologico**: sintomi extrapiramidali (EPS), discinesie tardive (scala AIMS), acatisia
> - **Cardiovascolare**: prolungamento QTc, ECG basale e follow-up
> - **Endocrino**: iperprolattinemia (soprattutto nelle donne in età riproduttiva)
>
> È necessario il recupero formale dei dati di sicurezza dal SmPC dell'EMA o dal foglio illustrativo approvato dall'AIFA prima che qualsiasi applicazione clinica proceda.

---

## Conclusione e prossimi passi

**Decisione: Proceed with Guardrails**

**Razionale:**
Molteplici RCT di Fase 3 completati — incluso uno studio di mantenimento del disturbo bipolare I in doppio cieco su 585 pazienti (NCT00391222), lo Studio TEAM nella mania pediatrica (NCT00057681, N=379) e uno studio di incremento TRD su 630 pazienti (NCT00095134) — combinati con cinque revisioni sistematiche/meta-analisi, costituiscono evidenze di grado L1. Il meccanismo duale D2/5-HT2A della risperidone è direttamente allineato con la fisiopatologia dopaminergica e serotoninergica del disturbo affettivo maggiore, e la base di evidenze è sufficiente a supportare il passaggio a una fase formale di revisione della fattibilità e normativa.

**Per procedere, è necessario quanto segue:**

- **Chiarimento del confine normativo**: Confermare se "Major Affective Disorder" si sovrappone parzialmente alle indicazioni già approvate di risperidone (mania bipolare, schizofrenia). Risolvere il gap nei dati `original_indications: []` prima di classificare questo come un vero riproposizionamento vs un'applicazione di estensione dell'indicazione — questa distinzione ha implicazioni normative e commerciali significative
- **Verifica dello stato del mercato italiano AIFA**: Il risultato di 0 autorizzazioni deve essere confermato direttamente tramite il registro dell'AIFA; le approvazioni UE esistenti (EMA) potrebbero già coprire l'indicazione target
- **Recupero dei dati di sicurezza**: Ottenere lo SmPC dell'EMA o il foglio illustrativo registrato dall'AIFA per popolare avvertimenti formali, controindicazioni e profili DDI
- **Stratificazione di sottogruppi di indicazione**: La qualità dell'evidenza differisce per sottotipo affettivo — progettare percorsi di analisi separati per (a) mantenimento Bipolare I, (b) aggiuntivo/incremento MDD e (c) TRD; non unire questi come un singolo percorso di sviluppo
- **Definizione del protocollo di monitoraggio**: Stabilire la pianificazione di monitoraggio basale e di follow-up per i parametri metabolici, EPS/discinesie tardive, QTc e prolattina prima di qualsiasi presentazione di studio patrocinato da investigatori
- **Triage di indicazioni secondarie**: Questo pacchetto multidisciplinare segnala anche **Trichotillomania** (L3, 10 pubblicazioni, Domanda di ricerca) e **Sindrome di Phelan-McDermid** (L4, dati preclinici di zebrafish + rapporti di casi) come candidati per ricerca esplorativa futura dopo che la traccia del disturbo affettivo maggiore è stata risolta

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

