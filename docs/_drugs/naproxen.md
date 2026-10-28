---
layout: default
title: Naproxen
parent: Solo previsione del modello (L5)
nav_order: 315
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
monitor_inn: "naproxen"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome"]
description: "Naproxen: nuova indicazione prevista, Sindrome brachidattilia-sindattilia (brachydactyly-syndactyly syndrome) (livello di evidenza L5). Indicazione originale: Non riportata nei dati locali"
---

# Naproxen
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **4** 
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

## Naproxen: Sindrome brachidattilia-sindattilia (brachydactyly-syndactyly syndrome)
{: .text-alpha }

## Sintesi in una frase

Il naprossene è un antinfiammatorio non steroideo (FANS) utilizzato per il trattamento di patologie muscolo-scheletriche dolorose e infiammatorie, come artrite reumatoide, osteoartrosi, spondilite anchilosante, gotta ed emicrania.
Il modello TxGNN lo prevede come potenzialmente efficace per la **sindrome brachidattilia-sindattilia**, ma si tratta di una previsione esclusivamente computazionale: tra i dati compilati per questo report risultano **0 sperimentazioni cliniche** e **0 pubblicazioni** a supporto.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione prevista | Sindrome brachidattilia-sindattilia (brachydactyly-syndactyly syndrome) |
| Punteggio di predizione TxGNN | 0.9935 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 11 su 11) |
| Numero di autorizzazioni | 11 (valide: 11) |
| Decisione raccomandata | Hold |

---

## Perché questa previsione potrebbe essere ragionevole?

I dati compilati non contengono una descrizione dettagliata del meccanismo d'azione. In generale il naprossene è un inibitore non selettivo di COX-1 e COX-2 che riduce la sintesi delle prostaglandine, con effetto antinfiammatorio, analgesico e antipiretico.

La sindrome brachidattilia-sindattilia è una malformazione scheletrica congenita di origine genetica, che interessa lo sviluppo e la formazione degli arti. L'inibizione delle prostaglandine non è attesa correggere un difetto strutturale di patterning degli arti. Al massimo, un FANS potrebbe alleviare un dolore muscolo-scheletrico secondario, con un effetto solo sintomatico e non modificante la malattia.

Non emerge quindi alcun legame meccanicistico sostenuto dai dati: il punteggio elevato (0,9935) proviene dal modello TxGNN (deep learning) e può riflettere somiglianze che il modello ha appreso tra malattie correlate, non una prova biologica o clinica. Anche le altre tre predizioni di alto rango (sindrome colobomatosa con microftalmia e displasia rizomelica, displasia acromesomelica tipo Hunter-Thompson, sindrome brachiolmia-amelogenesi imperfetta) sono malattie genetiche dello sviluppo scheletrico, prive di studi e di un razionale meccanicistico.

---

## Evidenze da sperimentazioni cliniche

Attualmente non risultano sperimentazioni cliniche correlate registrate.

---

## Evidenze dalla letteratura

Attualmente non risulta alcuna letteratura correlata disponibile.

---

## Informazioni sul mercato italiano

Il testo delle indicazioni approvate e la forma farmaceutica non sono riportati nei dati compilati.

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 023177189 | NAPROSYN 20 cpr 750 mg rilascio modificato | Recordati SpA | Valida |
| 023886082 | LASER 20 cpr 750 mg rilascio modificato | Euro-Pharma Srl | Valida |
| 050505027 | NAPROSSENE 30 cpr rivestite 550 mg | Aurobindo Pharma Italia Srl | Valida |
| 024667139 | NAPRIUS 30 cpr 500 mg | Aesculapius Farmaceutici Srl | Valida |
| 034792010 | NAPROXENE SODICO 30 cpr rivestite 550 mg | DOC Generici Srl | Valida |

Elencate le prime 5 delle 11 autorizzazioni.

---

## Considerazioni sulla sicurezza

- **Controindicazioni nel grafo di conoscenza** (non derivate dal foglio illustrativo): ipertensione, insufficienza epatica e malattie epatiche, malattie renali, scompenso cardiaco congestizio, coronaropatia, infarto miocardico, ictus e disturbi cerebrovascolari, osteoporosi, diabete mellito e chetoacidosi diabetica, epilessia, malattie della coagulazione, anemia, malattie della colecisti, iperplasia prostatica benigna, obesità e abuso/dipendenza da sostanze.
- **Interazioni farmacologiche**: sono state individuate 309 interazioni; nell'elenco disponibile quelle mostrate sono di livello moderato, ad esempio con acido acetilsalicilico, corticosteroidi (idrocortisone, desametasone, betametasone, budesonide, triamcinolone), metformina, clorpropamide, inibitori di pompa protonica (rabeprazolo, dexlansoprazolo), anti-H2 (famotidina, ranitidina, cimetidina), mesalazina, balsalazide e aprepitant.

Per avvertenze e controindicazioni ufficiali si rimanda al foglio illustrativo, non disponibile tra i dati compilati.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione si basa solo sul modello (livello L5), senza sperimentazioni né pubblicazioni, e non vi è alcun legame meccanicistico plausibile tra l'inibizione delle COX e una malformazione scheletrica congenita di origine genetica. Inoltre, tutte le autorizzazioni italiane del prodotto risultano cancellate.

**Per procedere sarebbe necessario:**
- Acquisire il meccanismo d'azione dettagliato (ad esempio da DrugBank) e valutare un eventuale razionale biologico specifico.
- Scaricare e analizzare il foglio illustrativo AIFA per avvertenze e controindicazioni (lacuna bloccante per lo screening di sicurezza).
- Cercare evidenze precliniche o cliniche specifiche sulla sindrome brachidattilia-sindattilia.
- Verificare la disponibilità attuale di formulazioni di naprossene sul mercato italiano, dato che tutte le autorizzazioni risultano cancellate.
- Chiarire se un eventuale beneficio sarebbe solo sintomatico (gestione del dolore) e quindi non rappresenterebbe un vero riposizionamento terapeutico.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

