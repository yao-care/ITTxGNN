---
layout: default
title: Isotretinoin
parent: Solo previsione del modello (L5)
nav_order: 246
evidence_level: L5
indication_count: 2
---

# Isotretinoin
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **2** 
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

# Isotretinoina: Dall'ipertensione alla malattia renale ipertensiva maligna

## Riepilogo in una frase

L'isotretinoina è un retinoide noto soprattutto per il trattamento dell'acne grave; nel grafo di conoscenza utilizzato dal modello compaiono come indicazioni originali "ipertensione" e "disturbo ipertensivo", che non corrispondono a un uso clinico consolidato e potrebbero essere un artefatto della fonte dati.
Il modello TxGNN prevede un possibile effetto sulla **malattia renale ipertensiva maligna** (punteggio 99,01%), ma a oggi sono disponibili **0 studi clinici** e **0 pubblicazioni** a supporto: si tratta di una predizione puramente computazionale.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Ipertensione / disturbo ipertensivo (secondo il grafo di conoscenza; il testo delle indicazioni nelle autorizzazioni AIFA non è disponibile) |
| Nuova indicazione prevista | Malattia renale ipertensiva maligna |
| Punteggio di predizione TxGNN | 99,01% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 15 (tutte cancellate) |
| Decisione raccomandata | Hold |

---

## Perché questa predizione potrebbe essere ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. L'isotretinoina è un retinoide utilizzato principalmente nell'acne grave, e le indicazioni ipertensive registrate nel grafo di conoscenza non rappresentano usi clinici stabiliti.

Il segnalamento dei retinoidi è stato studiato in ambito renale e vascolare (ad esempio effetti sui podociti, sull'espressione della renina e sul rimodellamento vascolare), ma si tratta di ipotesi speculative non supportate dai dati compilati per questo report.

Va inoltre osservato che anche la seconda indicazione prevista (ipertensione renovascolare maligna) ha lo stesso identico punteggio (0,990). Ciò suggerisce che la predizione derivi da un vicinato comune di nodi del grafo legati all'ipertensione, piuttosto che da un segnale specifico per la singola malattia. Nessun legame meccanicistico può quindi essere verificato.

---

## Evidenze da studi clinici

Attualmente non risultano studi clinici correlati registrati.

---

## Evidenze dalla letteratura

Attualmente non risulta disponibile letteratura correlata.

---

## Informazioni sul mercato italiano

Tutte le 15 autorizzazioni risultano cancellate; il testo delle indicazioni approvate e la forma farmaceutica non sono riportati nei dati. Si elencano le prime 5:

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 051504013 | Isotretinoina 30 cps molli 10 mg | DOC Generici Srl | Cancellata |
| 035258021 | Aisoskin 30 cps molli 20 mg | Fidia Farmaceutici SpA | Cancellata |
| 041853072 | Isdiben 30 cps molli 20 mg | ISDIN Srl | Cancellata |
| 041853045 | Isdiben 30 cps molli 10 mg | ISDIN Srl | Cancellata |
| 037551076 | Isoriac 30 cps molli 20 mg | Pierre Fabre Italia SpA | Cancellata |

---

## Considerazioni sulla sicurezza

- **Controindicazioni derivate dal grafo di conoscenza** (non provenienti dal foglio illustrativo): tra le condizioni associate figurano malattia renale, malattia epatica, pancreatite, malattie della colecisti, angioedema (incluse le forme ereditarie e acquisite), malattia infiammatoria intestinale, osteoporosi, lupus eritematoso sistemico, disturbi psicotici e mentali (inclusi ansia e disturbi distimici), diabete mellito e chetoacidosi diabetica, neutropenia e agranulocitosi, carenza di potassio, ipotensione. Molte di queste condizioni sono rilevanti in pazienti con malattia renale e cardiovascolare.
- **Interazioni farmacologiche**: sono registrate 98 interazioni. Tra quelle di livello **maggiore** figurano tetracicline (doxiciclina, minociclina, tetraciclina) e vitamina A. Tra quelle di livello **moderato** si segnalano corticosteroidi (betametasone, budesonide, desametasone, idrocortisone, prednisolone, prednisone, triamcinolone), warfarin e dicumarolo, etanolo, naltrexone, nitisinone, fostamatinib, ivacaftor, lumacaftor e abametapir.
- **Profilo generale noto**: teratogenicità, effetti epatici e sui lipidi, insieme all'elevato numero di interazioni, rappresentano ulteriori preoccupazioni in una popolazione con patologie renali e cardiovascolari.

Per avvertenze e controindicazioni ufficiali fare riferimento al foglio illustrativo, che non è stato ottenuto per questo report.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione si basa unicamente sul modello (livello L5), senza studi clinici né pubblicazioni; le indicazioni originali nel grafo sembrano non corrispondere all'uso reale del farmaco, e tutte le autorizzazioni italiane sono cancellate. Il profilo di sicurezza (teratogenicità, effetti epatici e lipidici, molte interazioni) sconsiglia di procedere senza dati a supporto.

**Per procedere sarebbe necessario:**
- Scaricare e analizzare il foglio illustrativo AIFA per avvertenze e controindicazioni (lacuna bloccante per lo screening di sicurezza)
- Ottenere i dati sul meccanismo d'azione (ad esempio da DrugBank) per valutare un legame meccanicistico
- Verificare e correggere le indicazioni originali registrate nel grafo di conoscenza
- Condurre una revisione sistematica della letteratura preclinica sul segnalamento dei retinoidi nel rene e nel sistema renina-angiotensina
- Valutare se un punteggio identico per due malattie correlate rifletta un artefatto del grafo piuttosto che un segnale specifico
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

