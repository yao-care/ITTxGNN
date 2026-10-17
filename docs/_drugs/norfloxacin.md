---
layout: default
title: Norfloxacin
parent: Solo previsione del modello (L5)
nav_order: 322
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Norfloxacin: nuova indicazione prevista, Sindrome da iperviscosità policlonale (livello di evidenza L5). Indicazione originale: Infezioni batteriche (infezioni delle vie urinarie, febbre tifoide…"
monitor_inn: "Norfloxacin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "diffuse scleroderma", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
---

# Norfloxacin
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

# Norfloxacina: da infezioni batteriche a sindrome da iperviscosità policlonale

## Sintesi in una frase

La norfloxacina è un fluorochinolone antibatterico, impiegato in origine per infezioni delle vie urinarie, infezioni gastrointestinali (dissenteria, malattie diarroiche, salmonellosi, febbre tifoide) e altre infezioni batteriche.
Il modello TxGNN le attribuisce un punteggio molto alto per la **sindrome da iperviscosità policlonale**, ma questa previsione ha **0 studi clinici** e **0 pubblicazioni** a supporto ed è priva di una base meccanicistica plausibile.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Infezioni batteriche (infezioni delle vie urinarie, febbre tifoide, salmonellosi, dissenteria, malattie diarroiche, bronchite, polmonite batterica e altre) |
| Nuova indicazione prevista | Sindrome da iperviscosità policlonale |
| Punteggio di previsione TxGNN | 99,70% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate |
| Numero di autorizzazioni | 3 (tutte revocate) |
| Decisione raccomandata | Hold |

---

## Perché questa previsione è ragionevole?

Dai dati compilati per questo report non sono attualmente disponibili informazioni dettagliate sul meccanismo d'azione. Per conoscenza generale, la norfloxacina inibisce la DNA girasi e la topoisomerasi IV batteriche, e la sua efficacia nelle infezioni batteriche (soprattutto urinarie e intestinali) è consolidata.

**Non esiste un legame meccanicistico plausibile** con la sindrome da iperviscosità policlonale: il farmaco non ha alcun effetto noto sui livelli di immunoglobuline sieriche né sulla viscosità del sangue. L'alto punteggio TxGNN riflette una previsione basata su grafo della conoscenza, non una motivazione biologica o clinica.

Anche le altre previsioni con punteggio elevato risultano deboli o prive di fondamento:

| Rango | Malattia prevista | Punteggio | Livello | Valutazione |
|---|---|---|---|---|
| 2 | Iperamilasemia | 99,70% | L5 | Nessun meccanismo terapeutico; i fluorochinoloni sono rari cause di pancreatite, quindi il segnale è più di sicurezza che di beneficio |
| 3 | Analbuminemia congenita | 99,67% | L5 | Nessun legame con la sintesi dell'albumina |
| 4 | Incompatibilità di gruppo sanguigno | 99,55% | L5 | Nessuna azione immunomodulante rilevante |
| 5 | Cheratocongiuntivite epiteliale puntata | 99,54% | L4 | Evidenza indiretta (2 serie di casi su cheratocongiuntivite microsporidica); il beneficio sembra derivare dal debridement meccanico, non dalla norfloxacina |
| 6 | Malattia ematologica premaligna | 99,48% | L5 | Nessun legame identificato |
| 7 | Sclerodermia diffusa | 99,44% | L5 | Nessun meccanismo; gli effetti avversi su tendini e tessuto connettivo suggeriscono cautela |
| 8 | Gammopatia monoclonale | 99,42% | L4 | Un solo studio, su resistenza e profilassi antibatterica, non sul trattamento della gammopatia |
| 9 | Malattia ematologica con neuropatia periferica acquisita | 99,38% | L5 | La neuropatia periferica è un effetto avverso dei fluorochinoloni: possibile problema di sicurezza |
| 10 | Peste setticemica | 99,37% | L4 | Plausibile a livello di classe (fluorochinoloni attivi su *Yersinia pestis*), ma dati solo preclinici e non specifici per la norfloxacina; scarso assorbimento sistemico, inadatta alla setticemia |

---

## Evidenza clinica (studi clinici)

Attualmente non risultano studi clinici correlati registrati per la sindrome da iperviscosità policlonale.

---

## Evidenza dalla letteratura

Attualmente non è disponibile letteratura correlata per la sindrome da iperviscosità policlonale.

Per le previsioni di rango inferiore sono state individuate alcune pubblicazioni, tutte indirette o precliniche:

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [12867402](https://pubmed.ncbi.nlm.nih.gov/12867402/) | 2003 | Serie di casi | Ophthalmology | 6 casi di cheratocongiuntivite microsporidica in individui sani (previsione: cheratocongiuntivite epiteliale puntata) |
| [22959880](https://pubmed.ncbi.nlm.nih.gov/22959880/) | 2012 | Serie di casi | American Journal of Ophthalmology | Effetto dello scraping corneale ripetuto nella cheratocongiuntivite microsporidica |
| [8834911](https://pubmed.ncbi.nlm.nih.gov/8834911/) | 1996 | Coorte/osservazionale | Antimicrobial Agents and Chemotherapy | Comparsa di *E. coli* resistente ai fluorochinoloni nella flora fecale di pazienti oncologici in profilassi con norfloxacina (122 campioni, 25 pazienti; resistenza nel 40%) |
| [10987101](https://pubmed.ncbi.nlm.nih.gov/10987101/) | 2000 | Preclinico (animale) | Antibiotiki i Khimioterapiya | Profilassi d'emergenza della peste con fluorochinoloni combinata a vaccino nel topo; effetto della norfloxacina inferiore a quello di altri fluorochinoloni |
| [11057367](https://pubmed.ncbi.nlm.nih.gov/11057367/) | 2000 | Preclinico/in vitro | Antibiotiki i Khimioterapiya | Resistenza sperimentale di *Vibrio cholerae* El Tor ad acido nalidixico e fluorochinoloni (fuori tema) |

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 034401024 (EG SpA, revocata) | NORFLOXACINA 14 compresse rivestite 400 mg | Compresse rivestite | — |
| 034941043 (Sandoz SpA, revocata) | NORFLOXACINA 14 compresse rivestite 400 mg | Compresse rivestite | — |
| 025000023 (ABC Farmaceutici SpA, revocata) | NORFLOXACINA 14 capsule 400 mg | Capsule | — |

---

## Citotossicità

Non applicabile: la norfloxacina è un antibatterico e non un farmaco antineoplastico.

---

## Considerazioni sulla sicurezza

I dati di sicurezza provengono dal grafo della conoscenza e non dal testo del foglio illustrativo.

- **Controindicazioni/condizioni a rischio (da grafo della conoscenza)**: sindrome del QT lungo (anche familiare) e torsione di punta; insufficienza epatica, epatopatie, cirrosi e malattie della colecisti; epilessia; disturbi d'ansia, psicotici e altri disturbi mentali; malattia renale; trombocitopenia; carenza di potassio; tendinite e altre patologie tendinee/periarticolari; diabete mellito e chetoacidosi diabetica; neuropatia periferica; rabdomiolisi; anemia.
- **Interazioni farmacologiche**: sono state rilevate 100 interazioni; tra le principali di gravità **maggiore** figurano corticosteroidi (idrocortisone, triamcinolone, desametasone, betametasone), bupropione e clorpropamide. Tra quelle di gravità moderata: antidiabetici (acarbosio, metformina, pioglitazone, alogliptin, albiglutide, canagliflozin), famotidina, loperamide, acido acetilsalicilico, balsalazide, bisacodile e sali di calcio o potassio.

Per le avvertenze complete fare riferimento al foglio illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione per la sindrome da iperviscosità policlonale si basa solo sul modello (L5), senza studi clinici né letteratura e senza un meccanismo plausibile. Le autorizzazioni italiane sono tutte revocate e il profilo di sicurezza (QT, tendini, neuropatia) rende sfavorevole la ricerca di nuove indicazioni non infettive.

**Per procedere sarebbe necessario:**
- Dati sul meccanismo d'azione e una giustificazione biologica per l'indicazione prevista
- Il foglio illustrativo AIFA (avvertenze e controindicazioni), oggi mancante e bloccante per lo screening di sicurezza
- Se si vuole esplorare un'ipotesi, valutare le previsioni di tipo infettivo (es. peste) con fluorochinoloni meglio caratterizzati, dato che la norfloxacina è poco adatta alle infezioni sistemiche
- Verificare nei testi completi il ruolo eventuale della norfloxacina nella cheratocongiuntivite epiteliale puntata
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

