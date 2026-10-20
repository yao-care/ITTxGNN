---
layout: default
title: Warfarin
parent: Prove moderate (L3-L4)
nav_order: 468
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-15
description: "Warfarin: nuova indicazione prevista, Carenza di cofattore eparinico II (livello di evidenza L4). Indicazione originale: Embolia polmonare, malattia trombotica…"
monitor_inn: "WARFARIN"
predicted_indications: ["heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "thrombophilia", "rheumatoid arthritis", "breast fibrocystic disease", "benign mammary dysplasia"]
---

# Warfarin
{: .fs-9 }

Livello di evidenza: **L4** | Indicazioni previste: **7** 
{: .fs-6 .fw-300 }

---

## Indice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Relazione di valutazione farmaceutica

</div>

# Warfarin: Dalla trombosi alla carenza di cofattore eparinico II

## Sintesi in una frase

Il warfarin è un anticoagulante orale antagonista della vitamina K, utilizzato per embolia polmonare, malattie trombotiche ed embolia intracranica. Il modello TxGNN prevede che possa essere efficace per la **carenza di cofattore eparinico II**, ma le evidenze si limitano a **3 case report** e a nessuno studio clinico registrato. Si tratta inoltre di una condizione trombofilica che rientra di fatto negli usi già noti del farmaco, quindi non è un vero riposizionamento.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Embolia polmonare, malattia trombotica, embolia intracranica (dal grafo di conoscenza TxGNN; il testo AIFA non riporta l'indicazione) |
| Nuova indicazione prevista | Carenza di cofattore eparinico II |
| Punteggio di predizione TxGNN | 99,87% |
| Livello di evidenza | L4 |
| Stato di mercato in Italia | Solo autorizzazioni revocate |
| Numero di autorizzazioni | 1 |
| Decisione raccomandata | Hold |

---

## Perché questa predizione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione registrati per questo farmaco. È però noto che il warfarin riduce la sintesi dei fattori della coagulazione vitamina K-dipendenti ed è un anticoagulante standard a lungo termine per la prevenzione della trombosi.

La carenza di cofattore eparinico II è una trombofilia ereditaria che causa trombosi venosa ricorrente. Il collegamento con l'uso già consolidato del warfarin nelle malattie trombotiche è quindi plausibile. Tuttavia l'indicazione prevista rientra nell'uso esistente: non si tratta di una vera estensione terapeutica, ma di una predisposizione trombotica all'interno dell'ambito già approvato.

Il modello ha prodotto altre predizioni a punteggio elevato. Alcune sono coerenti con il meccanismo anticoagulante: eccesso di fattore V con trombosi spontanea, carenza di antitrombina di tipo 2 e trombofilia in generale. Altre non hanno alcun fondamento terapeutico: artrite reumatoide, malattia fibrocistica della mammella e displasia mammaria benigna. In questi ultimi casi il punteggio sembra riflettere co-prescrizioni e interazioni farmacologiche (ad esempio con leflunomide o danazolo), non l'efficacia.

---

## Evidenze da studi clinici

Per la carenza di cofattore eparinico II non risultano studi clinici registrati.

Per completezza, per la predizione di rango 4 (trombofilia) è presente uno studio di fase 3:

| Numero studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT00895505](https://clinicaltrials.gov/study/NCT00895505) | Fase 3 | Sconosciuto | 300 | Strategia guidata dal D-dimero per stabilire la durata della profilassi secondaria del tromboembolismo venoso dopo una trombosi venosa profonda non provocata. Valuta la durata della terapia, non l'efficacia diretta del warfarin. |

---

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [2214444](https://pubmed.ncbi.nlm.nih.gov/2214444/) | 1990 | Case report | Kyobu Geka | Trombosi ventricolare destra in una ragazza di 14 anni con carenza familiare di cofattore eparinico II, rimossa chirurgicamente |
| [2033902](https://pubmed.ncbi.nlm.nih.gov/2033902/) | 1991 | Case report | Nihon Kyobu Shikkan Gakkai Zasshi | Carenza congenita di antitrombina con infarto polmonare; la paziente era stata trattata con warfarin per 7 anni, poi passata a eparina |
| [11570053](https://pubmed.ncbi.nlm.nih.gov/11570053/) | 2001 | Case report (famiglia) | Journal of UOEH | Famiglia con trombosi multiple, inclusa l'infanzia; una paziente ha avuto una nuova trombosi nonostante il warfarin |

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 016366027 | COUMADIN*30 cpr div 5 mg (TEOFARMA Srl) | Non indicata | Non indicata (autorizzazione revocata) |

---

## Considerazioni sulla sicurezza

**Controindicazioni segnalate dal grafo di conoscenza** (non provengono dal foglio illustrativo): ipertensione, insufficienza e malattie epatiche, malattie della colecisti, insufficienza cardiaca congestizia, ipotiroidismo, sindrome nefrosica, disturbi psicotici e mentali, malattie del tessuto connettivo, malattie ossee e cartilaginee, abuso/dipendenza da sostanze, disturbi della coagulazione, iperlipidemia, anemia, insufficienza renale, colestasi e malattie diarroiche croniche.

**Interazioni farmacologiche**: sono state rilevate 100 interazioni; tra quelle mostrate le principali sono:
- **Maggiori**: acido acetilsalicilico, metronidazolo
- **Moderate**: ranitidina, rabeprazolo, doxiciclina, idrocortisone, metformina, amoxicillina, bupropione, aprepitant, mesalazina, triamcinolone, balsalazide, desametasone, betametasone, budesonide, acido chenodesossicolico
- **Minori**: acarbosio, albiglutide, acido ascorbico

Per le avvertenze e le controindicazioni ufficiali si rimanda al foglio illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
Per la carenza di cofattore eparinico II esistono solo case report, senza studi clinici. L'indicazione si sovrappone agli usi già noti del warfarin e non costituisce un riposizionamento nuovo. Inoltre l'unica autorizzazione italiana è revocata.

**Per procedere è necessario:**
- Recuperare dal sito AIFA il foglio illustrativo con avvertenze e controindicazioni
- Reperire i dati sul meccanismo d'azione (ad esempio da DrugBank)
- Raccogliere evidenze più solide (coorti o studi controllati) sul warfarin nella carenza di cofattore eparinico II
- Verificare la disponibilità commerciale del farmaco in Italia, dato che l'autorizzazione è revocata
- Definire un piano di monitoraggio dell'INR e del rischio emorragico, considerando le numerose interazioni farmacologiche
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

