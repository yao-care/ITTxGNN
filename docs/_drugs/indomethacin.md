---
layout: default
title: Indomethacin
parent: Solo previsione del modello (L5)
nav_order: 238
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Indomethacin: nuova indicazione prevista, Sindrome brachidattilia-sindattilia (livello di evidenza L5). Indicazione originale: Artrite reumatoide, spondilite anchilosante, osteoartrosi, gotta…"
monitor_inn: "Indomethacin"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "WHIM syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "brachyolmia", "myosclerosis", "rheumatoid nodulosis"]
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

# Indometacina: da artrite reumatoide e patologie muscoloscheletriche infiammatorie a artrite idiopatica giovanile

## Riepilogo in una frase

L'indometacina è un farmaco antinfiammatorio non steroideo (FANS) utilizzato da tempo per l'artrite reumatoide, la spondilite anquilosante, l'osteoartrosi, la gotta, la borsite e la tendinite, oltre che per la pervietà del dotto arterioso.
Il modello TxGNN la indica come possibile candidata per la **sindrome brachidattilia-sindattilia** (primo risultato per punteggio), ma per questa indicazione non esiste alcuna evidenza clinica o bibliografica. L'unica direzione con un minimo di supporto è l'**artrite idiopatica giovanile (AIG)**, con **0 studi clinici registrati** e **20 pubblicazioni**, in gran parte revisioni storiche sull'uso sintomatico dei FANS.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Artrite reumatoide, spondilite anchilosante, osteoartrosi, gotta, borsite, tendinite, dotto arterioso pervio (dal grafo di conoscenza; il testo autorizzativo AIFA non è disponibile) |
| Nuova indicazione prevista (primo risultato) | Sindrome brachidattilia-sindattilia |
| Punteggio di predizione TxGNN | 99,97% |
| Livello di evidenza | L5 (per il primo risultato); L3 per l'AIG |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 3 (tutte cancellate) |
| Decisione raccomandata | Hold (sospendere) |

## Perché questa predizione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione registrati per questo rapporto. In base alle conoscenze note, l'indometacina è un inibitore non selettivo delle ciclossigenasi (COX-1 e COX-2), che riduce la sintesi di prostaglandine e quindi infiammazione, dolore e febbre. I dati compilati riportano inoltre interazioni farmacologiche con PTGDR2 (recettore DP2), PPARG e il trasportatore del folato accoppiato ai protoni (SLC46A1).

Per il primo risultato (sindrome brachidattilia-sindattilia) **non emerge alcun legame meccanicistico plausibile**: si tratta di una malformazione scheletrica dello sviluppo e non è evidente un percorso che colleghi la sintesi di prostaglandine a tale patologia. Lo stesso vale per gli altri risultati ad alto punteggio (displasia acromesomelica tipo Hunter-Thompson, sindrome WHIM, brachiolmia, miosclerosi e altre sindromi genetiche rare): il punteggio elevato riflette probabilmente la vicinanza nella rete di conoscenza alle indicazioni muscoloscheletriche, più che una rilevanza biologica.

Diverso è il caso dell'**artrite idiopatica giovanile** (8° risultato, punteggio 99,84%): qui il razionale è biologicamente plausibile, perché l'effetto antinfiammatorio e analgesico dell'indometacina è coerente con l'uso approvato nell'artrite reumatoide. Va però precisato che si tratta di un uso sintomatico da FANS già noto e in gran parte storico, non di un vero riposizionamento. La gestione attuale della AIG si basa su DMARD e farmaci biologici; l'indometacina ha un ruolo solo adiuvante o sintomatico, anche per le preoccupazioni di sicurezza in età pediatrica. Anche l'artrite idiopatica giovanile sieropositiva per fattore reumatoide e la noduolosi reumatoide (indirettamente collegata all'artrite reumatoide) sono plausibili per estensione, ma senza evidenza specifica.

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

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 022559037 | LIOMETACEN, 6 fiale EV 50 mg + 6 fiale solvente 2 ml (PROMEDICA Srl) | Non indicata | Non disponibile (autorizzazione cancellata) |
| 020676021 | INDOXEN, 25 capsule 50 mg (ALFASIGMA SpA) | Capsula | Non disponibile (autorizzazione cancellata) |
| 020676019 | INDOXEN, 25 capsule 25 mg (ALFASIGMA SpA) | Capsula | Non disponibile (autorizzazione cancellata) |

## Considerazioni di sicurezza

- **Controindicazioni (dal grafo di conoscenza, non dal foglio illustrativo):** ipertensione, epilessia, ulcera gastrica e duodenale, ulcera peptica attiva, malattie renali, epatiche e della colecisti, trombocitopenia, asma (intrinseco e allergico), disturbi della coagulazione, infarto del miocardio, trombosi coronarica, malattie cardiovascolari e cardiache, colite ulcerosa, malattie infiammatorie intestinali, enterocolite necrotizzante, emorragia intracerebrale, discinesia esofagea, disturbi d'ansia, disturbi nevrotici e distimici, emoglobinopatie, malattie infettive.
- **Interazioni:** i dati compilati riportano soltanto interazioni a livello di bersagli farmacologici (COX-1, COX-2, PPARG, DP2, SLC46A1) e non interazioni con altri farmaci. In letteratura è segnalato un effetto additivo di indometacina e metotrexato sulla soppressione della crescita nel ratto (studio preclinico), rilevante in ambito pediatrico.
- Un lavoro sull'inibizione della placca di crescita da parte dei FANS in ossa di ratto coltivate risulta ritirato.

Per le avvertenze complete fare riferimento al foglio illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
- Per il primo risultato (sindrome brachidattilia-sindattilia) esiste solo una predizione computazionale, senza studi, letteratura né legame meccanicistico plausibile (livello L5). Per l'AIG l'evidenza è L3, ma si tratta di uso sintomatico da FANS già noto e prevalentemente storico, quindi più una questione di ricerca che un vero riposizionamento.
- In Italia tutte e tre le autorizzazioni risultano cancellate e mancano i dati di sicurezza del foglio illustrativo (lacuna bloccante).

**Per procedere sono necessari:**
- Scaricare e analizzare il foglio illustrativo AIFA per avvertenze e controindicazioni
- Dati dettagliati sul meccanismo d'azione (ad esempio da DrugBank)
- Verifica sistematica della letteratura sull'AIG (studi controllati recenti, confronto con i DMARD/biologici attuali) e valutazione del profilo di sicurezza in età pediatrica
- Chiarimento dello stato regolatorio attuale in Italia (autorizzazioni cancellate, prodotti eventualmente disponibili con altri nomi)
- Eventuale riesame dei candidati con punteggio elevato ma senza evidenza, che al momento non giustificano ulteriori investimenti
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

