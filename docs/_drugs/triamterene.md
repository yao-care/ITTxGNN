---
layout: default
title: Triamterene
parent: Solo previsione del modello (L5)
nav_order: 452
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Triamterene: nuova indicazione prevista, Malattia renale ipertensiva maligna (livello di evidenza L5). Indicazione originale: Ipertensione e scompenso cardiaco congestizio (dal grafo di conoscenz…"
---

# Triamterene
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **6** 
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

# Triamterene: Dall'ipertensione alla malattia renale ipertensiva maligna

## Sintesi in una frase

Il triamterene è un diuretico risparmiatore di potassio, originariamente usato per ipertensione e scompenso cardiaco congestizio.
Il modello TxGNN prevede che possa essere efficace per la **malattia renale ipertensiva maligna**, ma al momento **non risultano studi clinici né pubblicazioni** che supportino questa indicazione: la predizione si basa solo sul modello.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Ipertensione e scompenso cardiaco congestizio (dal grafo di conoscenza TxGNN; il testo di indicazione AIFA non è disponibile) |
| Nuova indicazione prevista | Malattia renale ipertensiva maligna |
| Punteggio di predizione TxGNN | 99,89% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni annullate |
| Numero di autorizzazioni | 1 (annullata) |
| Decisione raccomandata | Hold |

## Perché questa predizione è ragionevole?

Il triamterene blocca il canale epiteliale del sodio (ENaC) ed esercita un effetto diuretico risparmiatore di potassio. È già impiegato nell'ipertensione, quindi un legame meccanicistico con il controllo pressorio nella malattia renale ipertensiva è plausibile. Al momento non sono disponibili dati dettagliati sul meccanismo d'azione.

Tuttavia, la predizione va letta con molta cautela. L'ipertensione maligna con coinvolgimento renale è un'emergenza ipertensiva che richiede una terapia rapida, per lo più parenterale. Inoltre, un diuretico risparmiatore di potassio comporta un rischio di iperkaliemia in presenza di insufficienza renale. Il punteggio elevato è probabilmente dovuto alla somiglianza con l'indicazione ipertensiva già esistente, più che a prove specifiche.

Altre indicazioni previste con lo stesso livello di evidenza (L5) sono state valutate e non risultano più solide:
- **Ipertensione renovascolare maligna** (punteggio 99,89%): la forma maligna è un'emergenza e i diuretici risparmiatori di potassio non sono una terapia standard. Nessuno studio disponibile.
- **Ipertensione polmonare ad eziologia multifattoriale non chiara** (99,88%): il triamterene non ha effetti noti sul rimodellamento o sulla resistenza vascolare polmonare. Nessuno studio disponibile.
- **Ipertensione polmonare da malattia polmonare e/o ipossia** (99,88%): esiste solo un legame teorico tramite l'ENaC nell'epitelio alveolare. Le due pubblicazioni trovate non supportano l'efficacia (un caso di edema polmonare associato a idroclorotiazide e uno studio di elettrofisiologia nel colon di ratto).
- **Sindrome di Braddock** (99,84%): nessun legame meccanicistico plausibile; probabile artefatto del grafo.
- **Cuore polmonare cronico** (99,75%): evidenza indiretta di livello L4 (vedi sotto), perché riguarda lo scompenso cardiaco in generale.

## Evidenze da studi clinici

Al momento non risultano studi clinici correlati registrati.

## Evidenze dalla letteratura

La malattia renale ipertensiva maligna, indicazione principale prevista, non ha pubblicazioni correlate. Di seguito la letteratura disponibile per le indicazioni previste di rango inferiore, indiretta e datata.

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [2924690](https://pubmed.ncbi.nlm.nih.gov/2924690/) | 1989 | Revisione (come classificata) | Dtsch Med Wochenschr | Confronto in 16 pazienti con scompenso cardiaco tra diuretico (idroclorotiazide + triamterene) e digitale (cuore polmonare cronico) |
| [1916562](https://pubmed.ncbi.nlm.nih.gov/1916562/) | 1991 | Studio emodinamico clinico | Fortschr Med | Combinazione verapamil/triamterene/idroclorotiazide in 12 pazienti con insufficienza cardiaca cronica: calo di pressione arteriosa e frequenza cardiaca in 4 settimane |
| [2766837](https://pubmed.ncbi.nlm.nih.gov/2766837/) | 1989 | Caso clinico | Chest | Edema polmonare a bassa pressione dopo una compressa di triamterene-idroclorotiazide, attribuito all'idroclorotiazide (evento avverso, non efficacia) |
| [5639361](https://pubmed.ncbi.nlm.nih.gov/5639361/) | 1968 | Preclinico (fisiologia animale) | J Physiol | Fattori che influenzano il potenziale elettrico della mucosa del colon di ratto; non pertinente |

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 021360021 | FLUSS*20 cpr 40 mg + 25 mg (ACARPIA FARMACEUTICI Srl) | Non indicata | Non indicata (autorizzazione annullata) |

## Considerazioni sulla sicurezza

I dati del foglietto illustrativo AIFA (avvertenze e controindicazioni) non sono disponibili. Di seguito le informazioni ricavate dal grafo di conoscenza e dalle banche dati sulle interazioni.

- **Controindicazioni dal grafo di conoscenza (non da testo di scheda tecnica)**: insufficienza epatica, malattia renale, anuria, encefalopatia e coma epatico, pancreatite, malattie della colecisti, lupus eritematoso sistemico (anche pediatrico), diabete mellito di tipo 1 e 2, chetoacidosi diabetica, iperuricemia, gotta, nefropatia acuta da urati, iperparatiroidismo, osteite fibrosa, ipercalcemia, nefrocalcinosi, nefrolitiasi, disturbi del metabolismo del fosforo, ittero neonatale, anemia da carenza di folati, acidosi e acidosi lattica acquisita, piourete.
- **Interazioni farmacologiche**: sono state identificate 104 interazioni. Tra quelle principali:
  - **Maggiore**: citrato di potassio (rischio di iperkaliemia).
  - **Moderata**: idrocortisone, desametasone, betametasone, triamcinolone, budesonide, metformina, bupropione, morfina, canagliflozin, dapagliflozin, dronabinolo, bisacodile, acido picosolforico, polietilenglicole con elettroliti.
  - **Minore**: famotidina, ranitidina, cimetidina, doxiciclina, minociclina.

Per le informazioni complete sulla sicurezza si rimanda al foglietto illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione è basata solo sul modello (livello L5), senza studi clinici né letteratura pertinente. Il contesto clinico (emergenza ipertensiva, insufficienza renale con rischio di iperkaliemia) è sfavorevole a un diuretico risparmiatore di potassio, e l'unica autorizzazione italiana è annullata.

**Per procedere sono necessari:**
- Foglietto illustrativo AIFA con avvertenze e controindicazioni (lacuna bloccante per lo screening di sicurezza)
- Dati sul meccanismo d'azione (DrugBank)
- Studi clinici o letteratura specifici sull'uso del triamterene nella malattia renale ipertensiva maligna
- Valutazione del rischio di iperkaliemia nei pazienti con compromissione renale
- Verifica della compatibilità di via di somministrazione e della disponibilità di un prodotto autorizzato in Italia
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

