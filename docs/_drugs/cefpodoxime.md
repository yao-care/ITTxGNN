---
layout: default
title: Cefpodoxime
parent: Solo previsione del modello (L5)
nav_order: 95
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Cefpodoxime: nuova indicazione prevista, Osteoartrite susceptibility (predizione di rango 1) (livello di evidenza L5). Indicazione originale: Non disponibile nei dati compilati (il testo delle indica…"
---

# Cefpodoxime
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **3** 
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

# Cefpodoxime: Dalle infezioni batteriche all'osteoartrite (predizione computazionale)

## Riepilogo in una frase

Cefpodoxime è un antibiotico cefalosporinico di terza generazione, usato per il trattamento di infezioni batteriche. Il modello TxGNN predice una possibile efficacia per l'**osteoartrite** (con punteggio elevato), ma al momento **non risultano studi clinici né pubblicazioni** a sostegno di questa ipotesi: si tratta di una predizione puramente computazionale.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non disponibile nei dati compilati (il testo delle indicazioni autorizzate è vuoto; la classe farmacologica è quella di un antibiotico cefalosporinico) |
| Nuova indicazione predetta | Osteoartrite susceptibility (predizione di rango 1); l'osteoartrite (rango 2) e l'artrite reumatoide (rango 3) sono le alternative successive |
| Punteggio di predizione TxGNN | 99,35% (rango 1, "osteoartrite susceptibility"); 99,25% per l'osteoartrite |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 11 (tutte cancellate; nessuna valida) |
| Decisione raccomandata | Hold (sospendere) |

---

## Perché questa predizione è (poco) ragionevole?

I dati compilati non riportano il meccanismo d'azione ufficiale. In base alle conoscenze generali, cefpodoxime è una cefalosporina di terza generazione che agisce inibendo la sintesi della parete cellulare batterica attraverso il legame con le proteine che legano la penicillina (PBP).

**Non emerge alcun legame meccanicistico supportato dai dati** con l'osteoartrite:

- Il primo risultato, «osteoartrite susceptibility», è un concetto di associazione genetica e non una condizione clinica trattabile: non rappresenta un bersaglio terapeutico significativo per un farmaco.
- Per l'osteoartrite non è nota alcuna attività antinfiammatoria, condroprotettiva o analgesica di cefpodoxime. Qualsiasi ipotesi (ad esempio un effetto indiretto su patologie articolari legate a infezioni o sul microbioma) è puramente speculativa.
- Per l'artrite reumatoide, malattia autoimmune guidata da segnali immunitari disregolati (TNF, IL-6, JAK/STAT, attivazione di linfociti B e T), il meccanismo beta-lattamico non agisce su tali vie. Tra gli antibiotici, l'uso storico in questa malattia è limitato a tetracicline (minociclina, doxiciclina), con meccanismi diversi e non estendibili alle cefalosporine.

L'elevato punteggio TxGNN è con ogni probabilità un artefatto della topologia del grafo di conoscenza e non un segnale di efficacia.

---

## Evidenza da studi clinici

Attualmente non risultano studi clinici correlati registrati.

## Evidenza dalla letteratura

Attualmente non è disponibile letteratura correlata.

---

## Informazioni sul mercato italiano

Tutte le 11 autorizzazioni risultano cancellate; non esistono prodotti attualmente validi. Le indicazioni approvate e le forme farmaceutiche non sono riportate nei dati compilati.

| N. autorizzazione | Nome del prodotto | Titolare |
|---------|------|------|
| 040010035 | PROXEDOX orale sosp grat 100 ml 40 mg/5 ml | SO.SE.PHARM Srl |
| 028463040 | CEFODOX 6 cpr rivestite 200 mg | SCHARPER SpA |
| 040010011 | PROXEDOX 12 cpr rivestite 100 mg | SO.SE.PHARM Srl |
| 028463014 | CEFODOX 12 cpr rivestite 100 mg | SCHARPER SpA |
| 041859188 | CEFPODOXIMA 12 cpr rivestite 100 mg | MYLAN SpA |

(Elencate le prime 5 delle 11 autorizzazioni, tutte cancellate.)

---

## Considerazioni sulla sicurezza

- **Interazioni farmacologiche**: sono state identificate **78 interazioni** note. Tra quelle di livello moderato compaiono:
  - antiacidi e sali di alluminio, calcio e magnesio (idrossido di alluminio, carbonato di calcio, magaldrato, carbonato/idrossido/ossido di magnesio);
  - antagonisti dei recettori H2 (famotidina, ranitidina, cimetidina, nizatidina, ranitidina bismuto citrato);
  - inibitori di pompa protonica (omeprazolo, esomeprazolo, lansoprazolo, dexlansoprazolo, pantoprazolo, rabeprazolo);
  - aminoglicosidi (kanamicina, neomicina) e balsalazide.

  Gli agenti che riducono l'acidità gastrica possono ridurre l'assorbimento di cefpodoxime.

Per avvertenze e controindicazioni, consultare il foglio illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione si basa unicamente sul modello (livello L5), senza studi clinici né pubblicazioni, e non esiste un legame meccanicistico plausibile con l'osteoartrite o l'artrite reumatoide. Inoltre, tutte le autorizzazioni italiane sono cancellate, il che rende ancora meno praticabile un percorso di riposizionamento.

**Per procedere sarebbe necessario:**
- Reperire e analizzare il foglio illustrativo AIFA (avvertenze, controindicazioni), attualmente mancante e bloccante per lo screening di sicurezza.
- Ottenere i dati sul meccanismo d'azione da DrugBank e valutare un'eventuale ipotesi biologica credibile.
- Individuare dati preclinici o osservazionali che colleghino il farmaco a una condizione articolare trattabile (non a un semplice concetto di "suscettibilità").
- Valutare la compatibilità delle vie di somministrazione e la situazione regolatoria (autorizzazioni attualmente non valide).
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

