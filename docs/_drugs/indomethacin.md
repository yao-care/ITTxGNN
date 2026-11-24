---
layout: default
title: Indomethacin
parent: Solo previsione del modello (L5)
nav_order: 238
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "Indomethacin"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "WHIM syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "brachyolmia", "myosclerosis", "juvenile idiopathic arthritis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis", "rheumatoid nodulosis"]
description: "Indomethacin: nuova indicazione prevista, Sindrome brachidattilia-sindattilia (brachydactyly-syndactyly syndrome) (livello di evidenza L5). In Italia, confezioni AIFA: 3 (autorizzate: 3)"
---

# Indomethacin
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **10** 
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

## Indomethacin: Sindrome brachidattilia-sindattilia (brachydactyly-syndactyly syndrome)
{: .text-alpha }

## Riepilogo in una frase

L'indometacina è un farmaco antinfiammatorio non steroideo (FANS) utilizzato da tempo per l'artrite reumatoide, la spondilite anquilosante, l'osteoartrosi, la gotta, la borsite e la tendinite, oltre che per la pervietà del dotto arterioso.
Il modello TxGNN la indica come possibile candidata per la **sindrome brachidattilia-sindattilia** (primo risultato per punteggio), ma per questa indicazione non esiste alcuna evidenza clinica o bibliografica. L'unica direzione con un minimo di supporto è l'**artrite idiopatica giovanile (AIG)**, con **0 studi clinici registrati** e **20 pubblicazioni**, in gran parte revisioni storiche sull'uso sintomatico dei FANS.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione prevista (primo risultato) | Sindrome brachidattilia-sindattilia (brachydactyly-syndactyly syndrome) |
| Punteggio di predizione TxGNN | 0.9997 |
| Livello di evidenza | L5 (per il primo risultato); L3 per l'AIG |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 3 su 3) |
| Numero di autorizzazioni | 3 (valide: 3) |
| Decisione raccomandata | Hold (sospendere) |

## Perché questa predizione è ragionevole?

Secondo la sezione «Mechanism of Action» delle informazioni di prescrizione approvate dalla FDA statunitense (Prescribing Information) per Indomethacin (traduzione non ufficiale): «Indometacina possiede proprietà analgesiche, antinfiammatorie e antipiretiche. Il meccanismo d'azione di INDOCIN, come quello degli altri FANS, non è completamente compreso, ma comporta l'inibizione della cicloossigenasi (COX-1 e COX-2).» Testo originale in inglese: "Indomethacin has analgesic, anti-inflammatory, and antipyretic properties. The mechanism of action of INDOCIN, like that of other NSAIDs, is not completely understood but involves inhibition of cyclooxygenase (COX-1 and COX-2)." ([DailyMed: Indocin (indomethacin) prescribing information, Zyla Life Sciences US LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=73878376-1d24-423b-9f37-3666e83c95da), versione del 2024-12-16; consultato il 2026-11-19). In base alle conoscenze note, l'indometacina è un inibitore non selettivo delle ciclossigenasi (COX-1 e COX-2), che riduce la sintesi di prostaglandine e quindi infiammazione, dolore e febbre. I dati compilati riportano inoltre interazioni farmacologiche con PTGDR2 (recettore DP2), PPARG e il trasportatore del folato accoppiato ai protoni (SLC46A1).

Per il primo risultato (sindrome brachidattilia-sindattilia) **non emerge alcun legame meccanicistico plausibile**: si tratta di una malformazione scheletrica dello sviluppo e non è evidente un percorso che colleghi la sintesi di prostaglandine a tale patologia. Lo stesso vale per gli altri risultati ad alto punteggio (displasia acromesomelica tipo Hunter-Thompson, sindrome WHIM, brachiolmia, miosclerosi e altre sindromi genetiche rare): il punteggio elevato riflette probabilmente la vicinanza nella rete di conoscenza alle indicazioni muscoloscheletriche, più che una rilevanza biologica.

Diverso è il caso dell'**artrite idiopatica giovanile** (8° risultato, punteggio 0,9984): qui il razionale è biologicamente plausibile, perché l'effetto antinfiammatorio e analgesico dell'indometacina è coerente con l'uso approvato nell'artrite reumatoide. Va però precisato che si tratta di un uso sintomatico da FANS già noto e in gran parte storico, non di un vero riposizionamento. La gestione attuale della AIG si basa su DMARD e farmaci biologici; l'indometacina ha un ruolo solo adiuvante o sintomatico, anche per le preoccupazioni di sicurezza in età pediatrica. Anche l'artrite idiopatica giovanile sieropositiva per fattore reumatoide e la noduolosi reumatoide (indirettamente collegata all'artrite reumatoide) sono plausibili per estensione, ma senza evidenza specifica.

## Evidenza dagli studi clinici

Attualmente non risultano studi clinici correlati registrati, né per il primo risultato né per l'AIG.

## Evidenza dalla letteratura

Per il primo risultato (sindrome brachidattilia-sindattilia) non è disponibile alcuna letteratura. Di seguito le principali pubblicazioni per l'AIG (il candidato con maggiore evidenza); sono stati valutati solo titoli e abstract, quindi i risultati non possono essere verificati in dettaglio.

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [362571](https://pubmed.ncbi.nlm.nih.gov/362571/) | 1978 | RCT | South African Medical Journal | Studio in doppio cieco crossover su 30 bambini con artrite cronica giovanile: ketoprofene e indometacina sicuri ed efficaci come analgesici/antinfiammatori; l'indometacina è risultata il farmaco preferito |
| [1379157](https://pubmed.ncbi.nlm.nih.gov/1379157/) | 1992 | Revisione | Drugs | Gestione farmacologica dell'artrite reumatoide giovanile; l'indometacina è tra i FANS disponibili |
| [8422565](https://pubmed.ncbi.nlm.nih.gov/8422565/) | 1993 | Revisione | British Journal of Rheumatology | Uso dei FANS nelle malattie reumatiche pediatriche; salicilati e indometacina non più efficaci ma più tossici di altri FANS |
| [1884567](https://pubmed.ncbi.nlm.nih.gov/1884567/) | 1991 | Revisione | Clinical Pharmacokinetics | Farmacocinetica dei farmaci usati nell'artrite giovanile, inclusi i FANS |
| [19078081](https://pubmed.ncbi.nlm.nih.gov/19078081/) | 1996 | Revisione/indagine | Journal of Clinical Rheumatology | Indagine tra reumatologi pediatrici: indometacina usata nell'11% dei pazienti con AR giovanile (naprossene 48%) |
| [28770976](https://pubmed.ncbi.nlm.nih.gov/28770976/) | 2017 | Revisione sistematica | Cochrane Database of Systematic Reviews | FANS per dolore cronico non oncologico in bambini e adolescenti |
| [4678956](https://pubmed.ncbi.nlm.nih.gov/4678956/) | 1972 | Revisione | JAMA | Rassegna generale sull'indometacina |
| [3278840](https://pubmed.ncbi.nlm.nih.gov/3278840/) | 1988 | Revisione | Comprehensive Therapy | Pratiche terapeutiche nelle spondiloartropatie; indometacina e fenilbutazone tra i più efficaci (riportata per la noduolosi reumatoide, ma non la riguarda direttamente) |
| [22472933](https://pubmed.ncbi.nlm.nih.gov/22472933/) | 2011 | Caso clinico | Acta Reumatologica Portuguesa | Associazione tra AIG sistemica e celiachia |
| [23312448](https://pubmed.ncbi.nlm.nih.gov/23312448/) | 2013 | Studio preclinico | Cytotherapy | Le cellule stromali mesenchimali da bambini con AIG sistemica sopprimono le risposte immunitarie |

## Informazioni sul mercato italiano

<!-- licenses:begin -->

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|------|------|------|------|
| 022559037 | LIOMETACEN\*6 fiale EV 50 mg + 6 fiale solv 2 ml | PROMEDICA Srl | Autorizzata |
| 020676021 | INDOXEN\*25 cps 50 mg | ALFASIGMA SpA | Autorizzata |
| 020676019 | INDOXEN\*25 cps 25 mg | ALFASIGMA SpA | Autorizzata |

Fonte: AIFA, elenco delle confezioni autorizzate (open data), stato amministrativo; confezioni autorizzate per prime.

<!-- licenses:end -->

## Considerazioni di sicurezza

- **Controindicazioni (dal grafo di conoscenza, non dal foglio illustrativo):** ipertensione, epilessia, ulcera gastrica e duodenale, ulcera peptica attiva, malattie renali, epatiche e della colecisti, trombocitopenia, asma (intrinseco e allergico), disturbi della coagulazione, infarto del miocardio, trombosi coronarica, malattie cardiovascolari e cardiache, colite ulcerosa, malattie infiammatorie intestinali, enterocolite necrotizzante, emorragia intracerebrale, discinesia esofagea, disturbi d'ansia, disturbi nevrotici e distimici, emoglobinopatie, malattie infettive.
- **Interazioni:** i dati compilati riportano soltanto interazioni a livello di bersagli farmacologici (COX-1, COX-2, PPARG, DP2, SLC46A1) e non interazioni con altri farmaci. In letteratura è segnalato un effetto additivo di indometacina e metotrexato sulla soppressione della crescita nel ratto (studio preclinico), rilevante in ambito pediatrico.
- Un lavoro sull'inibizione della placca di crescita da parte dei FANS in ossa di ratto coltivate risulta ritirato.

Per le avvertenze complete fare riferimento al foglio illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
- Per il primo risultato (sindrome brachidattilia-sindattilia) esiste solo una predizione computazionale, senza studi, letteratura né legame meccanicistico plausibile (livello L5). Per l'AIG l'evidenza è L3, ma si tratta di uso sintomatico da FANS già noto e prevalentemente storico, quindi più una questione di ricerca che un vero riposizionamento.
- Mancano i dati di sicurezza del foglio illustrativo (lacuna bloccante).

<!-- review:begin it-lic-20261106-indomethacin-1 -->

> **Correzione di verifica (2026-11-24)**: Testo originale: «In Italia tutte e tre le autorizzazioni risultano cancellate e mancano i dati di sicurezza del foglio illustrativo (lacuna bloccante).» Rimosso: l'affermazione che le autorizzazioni fossero revocate, annullate o non valide non corrispondeva ai dati delle autorizzazioni (AIFA, elenco delle confezioni autorizzate, al 2026-11-06). I numeri aggiornati delle autorizzazioni sono nella panoramica rapida e nella tabella delle informazioni sul mercato. Fonte: [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv).

<!-- review:end it-lic-20261106-indomethacin-1 -->

**Per procedere sono necessari:**
- Scaricare e analizzare il foglio illustrativo AIFA per avvertenze e controindicazioni
- Dati dettagliati sul meccanismo d'azione (ad esempio da DrugBank)
- Verifica sistematica della letteratura sull'AIG (studi controllati recenti, confronto con i DMARD/biologici attuali) e valutazione del profilo di sicurezza in età pediatrica
- Chiarimento dello stato regolatorio attuale in Italia
- Eventuale riesame dei candidati con punteggio elevato ma senza evidenza, che al momento non giustificano ulteriori investimenti

<!-- review:begin it-lic-20261106-indomethacin-2 -->

> **Correzione di verifica (2026-11-24)**: Testo originale: «Chiarimento dello stato regolatorio attuale in Italia (autorizzazioni cancellate, prodotti eventualmente disponibili con altri nomi)» Rimosso: l'affermazione che le autorizzazioni fossero revocate, annullate o non valide non corrispondeva ai dati delle autorizzazioni (AIFA, elenco delle confezioni autorizzate, al 2026-11-06). I numeri aggiornati delle autorizzazioni sono nella panoramica rapida e nella tabella delle informazioni sul mercato. Fonte: [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv).

<!-- review:end it-lic-20261106-indomethacin-2 -->

<!-- review:begin log -->

## Registro delle verifiche

Di seguito il registro delle verifiche di questa pagina: affermazioni controllate sui dati ufficiali delle autorizzazioni (AIFA, elenco delle confezioni autorizzate). Le correzioni riguardano solo dati di base; le previsioni del modello, i livelli di evidenza e le conclusioni non sono stati riscritti. La frase secondo cui non erano disponibili dati sul meccanismo d'azione è stata sostituita da un estratto delle informazioni di prescrizione ufficiali citate (con traduzione non ufficiale).

| Data di verifica | Voce | Intervento | Fonte |
|------|------|------|------|
| 2026-11-24 | Rimosso: «In Italia tutte e tre le autorizzazioni risultano cancellate e m» | Corretto (rivisto il 2026-11-24; versione precedente conservata nel registro) | [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv) |
| 2026-11-24 | Rimosso: «(autorizzazioni cancellate, prodotti eventualmente disponibili con altri nomi)» | Corretto (rivisto il 2026-11-24; versione precedente conservata nel registro) | [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv) |
| 2026-11-19 | Frase «dati sul meccanismo d'azione non disponibili» sostituita da un estratto del foglietto statunitense | Frase sull'assenza di dati sul meccanismo d'azione sostituita da un estratto con fonte | [DailyMed: Indocin (indomethacin) prescribing information, Zyla Life Sciences US LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=73878376-1d24-423b-9f37-3666e83c95da) |

<!-- review:end log -->

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

