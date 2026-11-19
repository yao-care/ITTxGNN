---
layout: default
title: Colchicina
parent: Solo previsione del modello (L5)
nav_order: 126
evidence_level: L5
indication_count: 2
drugbank_id: DB01394
monitor_inn: "Colchicine"
predicted_indications: ["Plasmodium falciparum malaria", "dermatofibrosarcoma protuberans"]
last_modified_at: 2026-11-16
description: "Colchicina: nuova indicazione prevista, Malaria da Plasmodium falciparum (Plasmodium falciparum malaria) (livello di evidenza L5). In Italia, confezioni AIFA: 2 (autorizzate: 2)"
---

# Colchicina
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **2** 
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

## Colchicina: Malaria da Plasmodium falciparum (Plasmodium falciparum malaria)
{: .text-alpha }

## Sintesi in una frase

La colchicina è un principio attivo che agisce sui microtubuli cellulari ed è registrato in Italia come medicinale a singolo principio attivo. Il modello TxGNN prevede una possibile efficacia nella **malaria da Plasmodium falciparum (Plasmodium falciparum malaria)**, ma per questa indicazione non risulta alcuno studio clinico registrato e le due pubblicazioni raccolte non testano la colchicina come trattamento antimalarico.

## Quadro d'insieme

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione prevista | Malaria da Plasmodium falciparum (Plasmodium falciparum malaria) |
| Punteggio di predizione TxGNN | 0.9960 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 2 su 2) |
| Numero di autorizzazioni | 2 (valide: 2) |
| Decisione raccomandata | Hold (sospendere) |

## Perché questa predizione potrebbe essere ragionevole?

I dati sul meccanismo d'azione non sono al momento disponibili nelle informazioni compilate per questo report. Sul piano teorico, la colchicina si lega alla tubulina e ostacola la polimerizzazione dei microtubuli. I parassiti del genere Plasmodium dipendono dai microtubuli per la formazione del fuso mitotico e per il citoscheletro nelle diverse fasi del ciclo vitale, per cui esiste un'ipotesi antiparassitaria plausibile.

Vi sono però limiti importanti. La tubulina di Plasmodium sembra meno sensibile alla colchicina rispetto a quella dei mammiferi. Inoltre la colchicina ha un indice terapeutico ristretto, con tossicità dose-limitante nell'uomo (gastrointestinale, mielosoppressione, neuromiopatia). Il punteggio TxGNN, pur elevato, è soltanto una previsione computazionale.

## Evidenze dagli studi clinici

Attualmente non risultano studi clinici registrati correlati.

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | Ricerca di base (in vitro) | Molecular and Cellular Biology | L'espressione del gene plasmodiale pfmdr1 in cellule di mammifero è associata a una maggiore sensibilità alla clorochina; riguarda la resistenza mediata da trasportatori, non dimostra efficacia antimalarica della colchicina |
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | Ricerca di base (in vitro) | PLoS One | La curcumina altera i microtubuli di P. falciparum; lo studio non valuta la colchicina come trattamento |

Nessuno dei due studi esamina direttamente la colchicina nella malaria da P. falciparum; per questo il livello di evidenza resta L5.

## Informazioni sul mercato italiano

| N. autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 009964038 | COLCHICINA LIRCA*2x30 cpr div 1 mg | Non indicata | Non registrata nei dati locali |
| 009964040 | COLCHICINA LIRCA*60 cpr 0,5 mg | Non indicata | Non registrata nei dati locali |

Entrambe le autorizzazioni sono valide e riguardano medicinali a singolo principio attivo (titolare: ACARPIA FARMACEUTICI Srl).

## Considerazioni sulla sicurezza

Per le informazioni di sicurezza si rimanda al foglio illustrativo. Si ricorda in particolare che la colchicina ha un indice terapeutico ristretto, con tossicità dose-limitante (gastrointestinale, midollare, neuromuscolare).

## Conclusioni e prossimi passi

**Decisione: Hold (sospendere)**

**Motivazione:**
La predizione si basa solo su un punteggio computazionale elevato; non esistono studi clinici né studi che testino direttamente la colchicina contro P. falciparum, e la ridotta sensibilità della tubulina del parassita unita alla tossicità umana ne limita la plausibilità.

**Per procedere sono necessari:**
- Dati di efficacia in vitro della colchicina su colture di P. falciparum, con confronto tra concentrazioni attive e concentrazioni tollerabili nell'uomo
- Dati sul meccanismo d'azione e sulla sensibilità della tubulina plasmodiale
- Avvertenze e controindicazioni dal foglio illustrativo AIFA, per la valutazione della sicurezza
- Valutazione del margine terapeutico e delle interazioni farmacologiche prima di qualsiasi studio clinico

<!-- review:begin log -->

## Registro delle verifiche

Di seguito il registro delle verifiche di questa pagina: affermazioni controllate sui dati ufficiali delle autorizzazioni (AIFA, elenco delle confezioni autorizzate). Le correzioni riguardano solo dati di base; le previsioni del modello, i livelli di evidenza e le conclusioni non sono stati riscritti.

| Data di verifica | Voce | Intervento | Fonte |
|------|------|------|------|
| 2026-11-06 | Rimosso: «Nessuna autorizzazione di commercializzazione è stata restituita dalla query del registro» | Non più presente dopo la rigenerazione del rapporto (2026-11-16: il rapporto è stato rigenerato a novembre 2026 e non contiene più questa affermazione; prima: Corretto) | [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv) |
| 2026-11-06 | Rimosso: «poiché il risultato di 0 licenze attuali può riflettere una limitazione dell'ambito della query piuttosto che una vera assenza di mercato» | Non più presente dopo la rigenerazione del rapporto (2026-11-16: il rapporto è stato rigenerato a novembre 2026 e non contiene più questa affermazione; prima: Corretto) | [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv) |

<!-- review:end log -->

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

