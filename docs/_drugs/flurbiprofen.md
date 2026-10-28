---
layout: default
title: Flurbiprofen
parent: Solo previsione del modello (L5)
nav_order: 206
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
monitor_inn: "flurbiprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "ankylosing spondylitis", "pseudoachondroplasia", "hypermobility of coccyx"]
description: "Flurbiprofen: nuova indicazione prevista, Displasia acromesomelica tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type) (livello di evidenza L5). Indicazione originale: Non riportata …"
---

# Flurbiprofen
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **9** 
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

## Flurbiprofen: Displasia acromesomelica tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type)
{: .text-alpha }

## Sintesi in una frase

Il flurbiprofene è un farmaco antinfiammatorio non steroideo (FANS), originariamente usato per artrite reumatoide, osteoartrosi e artropatie. Tra le predizioni del modello TxGNN, quella con il supporto più concreto è la **spondilite anchilosante**: **nessuno studio clinico registrato**, ma **20 pubblicazioni** (in gran parte studi comparativi degli anni '70-'80). Le altre predizioni con punteggio elevato riguardano malattie genetiche rare dello scheletro e sono prive di qualsiasi evidenza.

---

## Quadro di sintesi

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione predetta (rank 1 del modello) | Displasia acromesomelica tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type) |
| Nuova indicazione con evidenza più solida | Acromesomelic dysplasia, Hunter-Thompson type |
| Punteggio TxGNN | 0.9999 |
| Livello di evidenza | L5 (rank 1); L3 (spondilite anchilosante) |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 2 su 2) |
| Numero di autorizzazioni | 2 (valide: 2) |
| Decisione raccomandata | Hold (rank 1); Proceed with Guardrails limitato alla spondilite anchilosante come indicazione di classe |

---

## Perché questa predizione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione registrati per questo farmaco. In base alle conoscenze note, il flurbiprofene è un FANS non selettivo che inibisce COX-1 e COX-2, riducendo la sintesi di prostaglandine e quindi infiammazione e dolore. La sua efficacia nelle patologie reumatiche è documentata.

**Spondilite anchilosante.** Il legame è solido: i FANS sono terapia di prima linea per la spondiloartrite assiale e la patologia è biologicamente affine alle indicazioni reumatiche originali. Si tratta però di un effetto di classe più che di un vero riposizionamento. Mancano evidenze moderne di modificazione della malattia.

**Predizione di rank 1 e altre malattie rare dello scheletro.** Per la displasia acromesomelica tipo Hunter-Thompson (mutazioni di perdita di funzione di CDMP1/GDF5), la sindrome brachidattilia-sindattilia, la sindrome microftalmia colobomatosa-displasia rizomelica, la sindrome brachiolmia-amelogenesi imperfetta, la brachiolmia e la pseudoacondroplasia (mutazioni COMP) non esiste un legame meccanicistico plausibile. L'inibizione di COX non incide su difetti genetici dello sviluppo; i punteggi elevati provengono dal modello TxGNN (deep learning) e possono riflettere somiglianze apprese dal modello tra malattie correlate (fenotipi scheletrici condivisi), non evidenza biologica. Al massimo i FANS potrebbero alleviare il dolore secondario. Per la miosclerosi il legame è debole e speculativo; per l'ipermobilità del coccige (coccigodinia) è plausibile un sollievo sintomatico, ma non supportato da dati. La "suscettibilità alla spondiloartropatia" è un'etichetta genetica, non una condizione trattabile: l'evidenza rilevante ricade sotto la spondilite anchilosante.

---

## Evidenze da studi clinici

Per la predizione di rank 1 e per la spondilite anchilosante non risultano al momento studi clinici registrati correlati.

---

## Evidenze dalla letteratura

Riferite alla spondilite anchilosante (le più rilevanti, studi comparativi o in doppio cieco prima, poi revisioni):

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [71969](https://pubmed.ncbi.nlm.nih.gov/71969/) | 1977 | Studio randomizzato in doppio cieco | Curr Med Res Opin | Flurbiprofene vs indometacina in 26 pazienti: efficacia sovrapponibile su dolore e dolorabilità |
| [329422](https://pubmed.ncbi.nlm.nih.gov/329422/) | 1977 | Studio comparativo randomizzato | South Med J | Stessa casistica: flurbiprofene e indometacina ugualmente efficaci |
| [324773](https://pubmed.ncbi.nlm.nih.gov/324773/) | 1977 | Studio comparativo in doppio cieco | Eur J Clin Pharmacol | Flurbiprofene vs fenilbutazone in 27 pazienti: efficacia simile |
| [3963017](https://pubmed.ncbi.nlm.nih.gov/3963017/) | 1986 | Studio comparativo randomizzato | Am J Med | 90 pazienti, 26 settimane: 200 mg/die di flurbiprofene equivalenti a 300 mg di fenilbutazone |
| [3963018](https://pubmed.ncbi.nlm.nih.gov/3963018/) | 1986 | Studio comparativo randomizzato | Am J Med | 57 pazienti, 26 settimane: flurbiprofene efficace quanto l'indometacina |
| [4611579](https://pubmed.ncbi.nlm.nih.gov/4611579/) | 1974 | Studio crossover in doppio cieco | Br Med J | 35 pazienti: efficacia vicina a quella della fenilbutazone, ben tollerato |
| [7003449](https://pubmed.ncbi.nlm.nih.gov/7003449/) | 1980 | Studio comparativo crossover | N Z Med J | Flurbiprofene vs naprossene: nessuna differenza di efficacia; più effetti collaterali con flurbiprofene |
| [4595274](https://pubmed.ncbi.nlm.nih.gov/4595274/) | 1974 | Crossover in doppio cieco | Ann Rheum Dis | Confronto tra indometacina, flurbiprofene e placebo |
| [391529](https://pubmed.ncbi.nlm.nih.gov/391529/) | 1979 | Revisione | Drugs | Proprietà farmacologiche e uso terapeutico nelle malattie reumatiche |
| [3963024](https://pubmed.ncbi.nlm.nih.gov/3963024/) | 1986 | Analisi aggregata | Am J Med | Dati su fegato e rene da 9 studi di fase III (1.677 pazienti) |

Nota: gli studi sono datati e la classificazione come RCT di fase 3 non è confermata dai dati disponibili.

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 024284034 | FROBEN*30 cpr rivestite 100 mg (VIATRIS ITALIA Srl) | Compresse rivestite | Non disponibile (autorizzazione valida) |
| 024284073 | FROBEN*1 flacone 160 ml 5 mg/ml sciroppo (VIATRIS ITALIA Srl) | Sciroppo | Non disponibile (autorizzazione valida) |

---

## Considerazioni di sicurezza

I dati del foglio illustrativo AIFA non sono disponibili; si rimanda al foglio illustrativo per avvertenze e controindicazioni ufficiali.

- **Condizioni associate a controindicazione nel grafo di conoscenza** (non derivate dal testo di etichetta): ipertensione, malattie renali, malattie epatiche, malattie della colecisti, ulcera peptica (anche attiva), infarto del miocardio, trombosi coronarica, malattie cardiovascolari e cardiache, disturbi della coagulazione, emoglobinopatie, abuso/dipendenza da sostanze, piureter.
- **Interazioni farmacologiche**: individuate 352 interazioni. Tra quelle mostrate, la maggior parte è di livello moderato: corticosteroidi (idrocortisone, desametasone, betametasone, budesonide, triamcinolone), acido acetilsalicilico, metformina, glimepiride, clorpropamide, mesalazina, balsalazide, aprepitant, sali di potassio e lassativi osmotici. Di livello minore: famotidina, cimetidina, linaclotide.

---

## Conclusioni e prossimi passi

**Decisione: Hold** (per la predizione di rank 1 e per le malattie genetiche rare); per la **spondilite anchilosante** il quadro è quello di una domanda di ricerca (L3), non di un vero riposizionamento.

**Motivazione:**
- Le predizioni principali non hanno alcun supporto meccanicistico, clinico o bibliografico. Per la spondilite anchilosante l'efficacia sintomatica è documentata, ma si tratta di un effetto di classe dei FANS, con studi datati, e il farmaco non ha attualmente autorizzazioni valide in Italia.

**Per procedere sono necessari:**
- Foglio illustrativo AIFA (avvertenze e controindicazioni), attualmente un blocco per lo screening di sicurezza
- Dati sul meccanismo d'azione (ad esempio da DrugBank)
- Verifica del disegno degli studi sulla spondilite anchilosante (fase, randomizzazione) ed evidenze più recenti
- Valutazione della fattibilità regolatoria, data la situazione di autorizzazioni cancellate
- Per le malattie rare, evidenze precliniche prima di qualsiasi considerazione di sviluppo
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

