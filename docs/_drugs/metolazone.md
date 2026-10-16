---
layout: default
title: Metolazone
parent: Solo previsione del modello (L5)
nav_order: 295
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Metolazone: nuova indicazione prevista, Malattia renale ipertensiva maligna (livello di evidenza L5). Indicazione originale: Ipertensione (disturbo ipertensivo)…"
monitor_inn: "METOLAZONE"
predicted_indications: ["malignant hypertensive renal disease", "malignant renovascular hypertension", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
---

# Metolazone
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **5** 
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

# Metolazone: Dall'ipertensione alla malattia renale ipertensiva maligna

## Sintesi in una frase

Metolazone è un diuretico simil-tiazidico, originariamente utilizzato per il trattamento dell'ipertensione. Il modello TxGNN prevede una possibile efficacia nella **malattia renale ipertensiva maligna**, ma al momento **non sono disponibili studi clinici né pubblicazioni** a supporto di questa direzione: la previsione si basa unicamente sul modello.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Ipertensione (disturbo ipertensivo), secondo gli archi di indicazione del grafo di conoscenza TxGNN; il testo dell'indicazione approvata AIFA non è disponibile |
| Nuova indicazione prevista | Malattia renale ipertensiva maligna |
| Punteggio di previsione TxGNN | 99,84% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 2 (entrambe cancellate) |
| Decisione raccomandata | Hold |

## Perché questa previsione è ragionevole?

I dati sul meccanismo d'azione dettagliato non sono al momento disponibili. In base alle informazioni note, metolazone è un diuretico simil-tiazidico (inibisce il riassorbimento di sodio nel tubulo distale), la sua efficacia nell'ipertensione è consolidata e, in via teorica, il controllo della volemia e della pressione arteriosa potrebbe essere rilevante anche per forme ipertensive più gravi con coinvolgimento renale.

Tuttavia, la plausibilità è limitata. L'ipertensione maligna è un'emergenza ipertensiva, che di solito richiede farmaci parenterali ad azione rapida; un diuretico orale a lunga durata d'azione difficilmente può essere la terapia principale. I diuretici tiazidici possono essere meno efficaci con un filtrato glomerulare ridotto, anche se metolazone è noto per mantenere attività nell'insufficienza renale.

Altre previsioni del modello presentano la stessa debolezza:
- **Ipertensione nefrovascolare maligna** (punteggio 99,84%): è una forma grave dell'indicazione già approvata, più che un uso realmente nuovo. Nell'ipertensione nefrovascolare domina l'attivazione del sistema renina-angiotensina, che la deplezione di volume indotta dal diuretico potrebbe stimolare ulteriormente.
- **Ipertensione polmonare** (forma multifattoriale e forma associata a malattie polmonari/ipossia, punteggio 99,83%): è fisiopatologicamente distinta dall'ipertensione sistemica. Il diuretico potrebbe al massimo alleviare il sovraccarico di volume del cuore destro, in modo sintomatico e non modificante la malattia. Il punteggio elevato riflette probabilmente il termine «ipertensione» condiviso nel grafo di conoscenza.
- **Sindrome di Braddock** (punteggio 99,78%): non è possibile stabilire alcun razionale meccanicistico; sembra un artefatto del grafo di conoscenza.

## Evidenza dagli studi clinici

Attualmente non risulta registrato alcuno studio clinico correlato.

## Evidenza dalla letteratura

Per l'indicazione principale (malattia renale ipertensiva maligna) non è disponibile alcuna letteratura correlata. Per un'indicazione prevista di rango inferiore (ipertensione polmonare da malattia polmonare/ipossia) è stato individuato un solo articolo, privo di rilevanza dimostrata:

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [2916665](https://pubmed.ncbi.nlm.nih.gov/2916665/) | 1989 | Ricerca preclinica | Am J Physiol | Studio sul ratto: dopo ischemia renale acuta i recettori dei diuretici tiazidici (misurati con [3H]metolazone) si riducono del 90% in modo reversibile. È fisiologia renale di base, senza rilevanza dimostrata per l'ipertensione polmonare |

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 024488090 | ZAROXOLYN*50 cpr 10 mg (TEOFARMA Srl) | Non indicata | Non disponibile (autorizzazione cancellata) |
| 024488064 | ZAROXOLYN*50 cpr 5 mg (TEOFARMA Srl) | Non indicata | Non disponibile (autorizzazione cancellata) |

## Considerazioni sulla sicurezza

I dati del foglietto illustrativo AIFA (avvertenze e controindicazioni) non sono disponibili; si rimanda al foglietto illustrativo per le informazioni di sicurezza ufficiali.

Dai dati compilati per questo report emergono le seguenti informazioni complementari:

- **Condizioni associate a controindicazione nel grafo di conoscenza** (non derivano dal testo dell'etichetta): insufficienza epatica, encefalopatia epatica e coma epatico, anuria, pancreatite, gotta, diabete mellito e chetoacidosi diabetica, carenza di potassio, ipercalcemia, nefrocalcinosi, disturbi del metabolismo del fosforo, ipotensione ortostatica, sindrome da tachicardia posturale ortostatica, atrofia multisistemica, lupus eritematoso sistemico (anche pediatrico) e sindrome HELLP.
- **Interazioni farmacologiche**: la ricerca ha individuato 100 interazioni (fonte DDInter). Tra quelle di livello moderato figurano acarbosio, albiglutide, alogliptin (antidiabetici, rischio sul controllo glicemico), idrocortisone, desametasone, betametasone, triamcinolone e beclometasone (corticosteroidi), amfotericina B, colecalciferolo, fosfato di calcio, bupropione, morfina, omeprazolo, rabeprazolo e bisacodile. Di livello lieve: doxiciclina, iosciamina e atropina.
- **Considerazione specifica**: nell'ipertensione polmonare associata a ipossia, gli effetti su volume ed elettroliti (ad es. alcalosi metabolica che peggiora l'ipoventilazione) rappresentano un rischio da valutare.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione ha livello di evidenza L5: nessuno studio clinico e nessuna letteratura pertinente sostengono le nuove indicazioni. Inoltre, le autorizzazioni italiane sono tutte cancellate, e l'indicazione principale è una emergenza ipertensiva in cui un diuretico orale difficilmente sarebbe terapia primaria.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione (ad es. da DrugBank) per analizzare il legame meccanicistico
- Avvertenze e controindicazioni dal foglietto illustrativo AIFA (attualmente un blocco per la valutazione di sicurezza)
- Una revisione sistematica della letteratura su metolazone nella malattia renale ipertensiva e nell'ipertensione grave
- Chiarimento dello stato regolatorio (autorizzazioni cancellate) e della disponibilità del prodotto in Italia
- Valutazione del rischio-beneficio nei pazienti con compromissione renale grave o disturbi elettrolitici, alla luce delle condizioni controindicate emerse dal grafo di conoscenza
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

