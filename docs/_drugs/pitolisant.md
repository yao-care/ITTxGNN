---
layout: default
title: Pitolisant
parent: Prove moderate (L3-L4)
nav_order: 167
evidence_level: L4
indication_count: 3
---

# Pitolisant
{: .fs-9 }

Livello di evidenza: **L4** | Indicazioni previste: **3** 
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

# Pitolisant: dalla narcolessia all'insonnia

## Riassunto in una frase

Pitolisant è il primo di una nuova classe di antagonisti inversi selettivi del recettore istaminergico H3, approvato a livello internazionale (Europa e USA) per il trattamento della narcolessia con o senza cataplessia. Il modello TxGNN lo predice come potenzialmente efficace per l'**Insonnia**, con **1 trial clinico** (ritirato, nessun arruolamento, e nemmeno specificamente mirato all'insonnia) e **8 pubblicazioni** recuperate — tuttavia, praticamente tutta la letteratura affronta la narcolessia o l'eccessiva sonnolenza diurna. Il meccanismo consolidato di promozione della veglia di pitolisant è fondamentalmente opposto a ciò che richiede il trattamento dell'insonnia, rendendo questa una probabile **falso positivo** di predizione guidata dalla prossimità nel grafo della malattia piuttosto che da una genuina plausibilità farmacologica.

---

## Panoramica rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione originale | Non registrata localmente; approvata a livello internazionale per narcolessia con o senza cataplessia |
| Indicazione predetta nuova | Insonnia |
| Punteggio di predizione TxGNN | 99.71% |
| Livello di evidenza | L4 |
| Stato di mercato in Italia | Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | In sospeso |

---

## Perché questa predizione è ragionevole?

Attualmente, i dati dettagliati sul meccanismo d'azione non sono disponibili in questo Evidence Pack. In base alla letteratura recuperata, pitolisant è un antagonista inverso selettivo del recettore istaminergico H3. Bloccando gli autorecettori H3 sui neuroni istaminergici nell'ipotalamo posteriore, pitolisant previene l'autoinibirzione tonica del rilascio di istamina, aumentando così la neurotrasmissione istaminergica in tutto il cervello. L'attivazione a valle dei recettori H1 postsinaptici promuove il risveglio e la veglia. Questo è esattamente il motivo per cui pitolisant è efficace nella narcolessia — un disturbo caratterizzato dall'incapacità patologica di mantenere la veglia.

Questo meccanismo è tuttavia **farmacologicamente opposto** a ciò che è richiesto per il trattamento dell'insonnia. L'insonnia richiede la promozione del sonno, non la promozione della veglia. Non è una coincidenza che i sedativi-ipnotici ben consolidati nella pratica clinica — inclusi doxepina, difenidramina, e la classe degli antistaminici in generale — agiscono come **antagonisti del recettore H1**, attenuando l'attività istaminergica per facilitare il sonno. Pitolisant amplifica lo stesso sistema nella direzione diametralmente opposta. Una revisione in *Current Neuropharmacology* (PMID 34521328) contrasta esplicitamente pitolisant antagonista inverso H3R (veglia) con doxepina antagonista H1R (trattamento dell'insonnia), sottolineando questa dicotomia meccanicistica.

Il modello TxGNN ha assegnato un punteggio eccezionalmente alto (99.71%) a questa predizione, il che molto probabilmente riflette la prossimità topologica tra i nodi della narcolessia e dell'insonnia all'interno del grafo di conoscenza biomedica — entrambe sono classificate come disturbi del sonno e condividono descrittori fenotipici sovrapponibili. Questa è una limitazione riconosciuta dei modelli di repurposing basati su grafi: possono identificare la vicinanza strutturale senza catturare la natura direzionale dell'azione farmacodinamica di un farmaco. Questa predizione è valutata come un **probabile falso positivo** e non giustifica uno sviluppo clinico senza una reinterpretazione meccanicistica convincente.

---

## Evidenza da trial clinici

| Numero di trial | Fase | Stato | Arruolamento | Risultati chiave |
|---------|------|------|------|---------|
| [NCT02800083](https://clinicaltrials.gov/study/NCT02800083) | Fase 2 | Ritirato | 0 | Ha mirato al **disturbo da uso di alcol**, non all'insonnia — l'endpoint primario era la riduzione dei giorni con forti consumi di alcol al mese. Il trial è stato ritirato prima di arruolare qualsiasi partecipante, generando nessun dato clinico. Rappresenta un segnale negativo sia per la fattibilità che per la rilevanza rispetto all'indicazione dell'insonnia. |

---

## Evidenza da letteratura

| PMID | Anno | Tipo | Rivista | Risultati chiave |
|------|------|------|---------|---------|
| [36931805](https://pubmed.ncbi.nlm.nih.gov/36931805/) | 2023 | RCT | The Lancet Neurology | RCT di fase 3 in bambini ≥6 anni con narcolessia; pitolisant ha dimostrato sicurezza ed efficacia per l'eccessiva sonnolenza diurna e la cataplessia. Interamente focalizzato sulla narcolessia — non sull'insonnia. |
| [33121980](https://pubmed.ncbi.nlm.nih.gov/33121980/) | 2021 | RCT | Chest | Pitolisant ha ridotto l'eccessiva sonnolenza diurna residua nei pazienti con OSA aderenti a CPAP. Dimostra un effetto di **promozione della veglia** — l'opposto del trattamento dell'insonnia. |
| [31917607](https://pubmed.ncbi.nlm.nih.gov/31917607/) | 2020 | RCT | Am J Respir Crit Care Med | RCT internazionale di pitolisant per la sonnolenza diurna in pazienti con OSA da moderata a grave che rifiutano CPAP; ha confermato l'efficacia della promozione della veglia. Nessun dato sull'insonnia. |
| [36169322](https://pubmed.ncbi.nlm.nih.gov/36169322/) | 2022 | Coorte (Mondo reale) | Revista de neurologia | Studio nel mondo reale in pazienti con narcolessia di tipo 1 non responsivi ai precedenti trattamenti standard; pitolisant ha mostrato efficacia e tollerabilità in questa popolazione refrattaria. |
| [34521328](https://pubmed.ncbi.nlm.nih.gov/34521328/) | 2022 | Revisione | Current Neuropharmacology | Esamina i cambiamenti del sistema istaminergico nei disturbi neuropsichiatrici; contrasta esplicitamente pitolisant (antagonista inverso H3R → veglia) con doxepina (antagonista H1R → trattamento dell'insonnia) — evidenzia l'incompatibilità meccanicistica con l'indicazione predetta. |
| [34225942](https://pubmed.ncbi.nlm.nih.gov/34225942/) | 2021 | Revisione | Handbook of Clinical Neurology | Panoramica completa di tutti e quattro i sottotipi di recettore istaminico e dei loro bersagli farmacologici; fornisce la base meccanicistica per la farmacologia H3R nel cervello. |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Revisione | Drug Design, Development and Therapy | Profilo di pitolisant per la gestione della narcolessia; conferma l'autorizzazione europea e caratterizza l'antagonismo inverso H3 come il meccanismo definente del farmaco. |
| [22356925](https://pubmed.ncbi.nlm.nih.gov/22356925/) | 2012 | Revisione/Meccanismo | Clinical Neuropharmacology | Pitolisant come stimolante alternativo per gli adolescenti con narcolessia refrattaria alla terapia convenzionale; sottolinea il meccanismo di potenziamento della veglia attraverso il blocco dell'autorecettore H3. |

---

## Informazioni di mercato in Italia

Pitolisant attualmente non ha autorizzazioni registrate in Italia (0 licenze). Il farmaco non è commercializzato localmente.

> **Nota:** Pitolisant (nome commerciale **Wakix**) ha ricevuto l'approvazione dell'EMA per la narcolessia con o senza cataplessia negli adulti, e successivamente per i bambini dai 6 anni in su (EMA/CHMP). È stato inoltre approvato dalla FDA (2019) per l'eccessiva sonnolenza diurna nella narcolessia in adulti. Queste approvazioni internazionali non sono riflesse nel database delle autorizzazioni locali interrogato per questo rapporto.

---

## Considerazioni di sicurezza

Si rimanda al foglio illustrativo per le informazioni sulla sicurezza.

---

## Conclusioni e prossimi passi

**Decisione: In sospeso**

**Razionale:**
L'azione farmacologica centrale di pitolisant — promozione della veglia attraverso l'antagonismo inverso del recettore istaminico H3 — è direzionalmente incompatibile con il trattamento dell'insonnia, che richiede la facilitazione del sonno piuttosto che il risveglio. L'unico trial clinico recuperato è stato ritirato senza arruolamenti e mirava a un'indicazione completamente diversa (disturbo da uso di alcol), e tutte le otto pubblicazioni nel corpus di letteratura affrontano la narcolessia o l'eccessiva sonnolenza diurna. L'alto punteggio di TxGNN quasi certamente riflette un falso positivo della topologia del grafo tra disturbi del sonno piuttosto che un genuino potenziale di repurposing.

**Per procedere, è necessario quanto segue:**

- Un'ipotesi meccanicistica credibile che spieghi come un agente che promuove la veglia potrebbe paradossalmente beneficiare i pazienti con insonnia (ad es., reset circadiano, induzione di sonno di rimbalzo, o un sottotipo specifico di insonnia come l'insonnia correlata all'ipereccitazione — nessuno dei quali è attualmente supportato da evidenze)
- Dati di trial clinici de novo specificamente in popolazioni con insonnia; nessuno di tali trial esiste
- Profilazione della sicurezza nei pazienti con insonnia, che differiscono sostanzialmente dalla popolazione con narcolessia nell'architettura del sonno, nelle comorbidità e nell'uso di farmaci concomitanti
- Rivalutazione delle prestazioni del modello TxGNN nel sottografo dei disturbi del sonno per quantificare il tasso sistematico di falsi positivi per le indicazioni farmacodinamicamente opposte

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

