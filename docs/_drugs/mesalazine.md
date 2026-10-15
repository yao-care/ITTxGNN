---
layout: default
title: Mesalazine
parent: Solo previsione del modello (L5)
nav_order: 287
evidence_level: L5
indication_count: 7
---

# Mesalazine
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **7** 
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

# Mesalazina: Dalla colite ulcerosa alla congenital hypotrichosis with juvenile macular dystrophy

## Sintesi in una frase

La mesalazina (acido 5-aminosalicilico, 5-ASA) è un antinfiammatorio intestinale usato originariamente per la colite ulcerosa e le altre malattie infiammatorie croniche intestinali. Il modello TxGNN la indica come potenzialmente efficace per la **congenital hypotrichosis with juvenile macular dystrophy** (ipotricosi congenita con distrofia maculare giovanile), ma questa previsione si basa solo sul grafo di conoscenza: **non sono presenti studi clinici né pubblicazioni** a supporto.

## Quadro di sintesi

| Voce | Contenuto |
|------|------|
| Indicazione originale | Colite ulcerosa, malattia infiammatoria intestinale, proctosigmoidite ulcerosa (dal grafo di conoscenza PrimeKG; il testo delle indicazioni AIFA non è disponibile) |
| Nuova indicazione prevista | Congenital hypotrichosis with juvenile macular dystrophy |
| Punteggio di predizione TxGNN | 99,65% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 20 (tutte cancellate; nessuna valida) |
| Decisione raccomandata | Hold |

## Perché questa previsione è plausibile?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. In base alle informazioni note, la mesalazina ha attività antinfiammatoria (inibizione di COX e lipossigenasi, agonismo su PPAR-gamma, modulazione di NF-kB), con efficacia dimostrata nella colite ulcerosa.

Per la condizione prevista **non è stato identificato alcun legame meccanicistico plausibile**. Si tratta di una rara malattia genetica legata a mutazioni di CDH3, senza un bersaglio antinfiammatorio su cui la mesalazina possa agire. L'elevato punteggio (0,996) è quindi un risultato basato esclusivamente sulla prossimità nel grafo e va interpretato con grande cautela.

## Evidenza dagli studi clinici

Attualmente non risultano studi clinici correlati registrati.

## Evidenza dalla letteratura

Attualmente non è disponibile letteratura correlata per questa indicazione.

## Altre indicazioni previste (per contesto)

Tra le altre previsioni del modello, solo due presentano un minimo di letteratura, comunque non dirimente:

| Indicazione | Punteggio TxGNN | Livello di evidenza | Note |
|------|------|------|------|
| Osteoartrosi | 99,63% | L5 | Nessuno studio clinico. L'unico lavoro (PMID 38491514, 2024) è un'analisi trascrittomica che genera ipotesi, non evidenza clinica sulla mesalazina. |
| Artrite reumatoide | 99,57% | L4 | Nessuno studio clinico registrato. La letteratura riguarda la sulfasalazina (di cui la mesalazina è la frazione attiva, ma l'effetto antireumatico è attribuito soprattutto alla sulfapiridina o alla molecola intera) e segnalazioni di reazioni avverse. Nessuna evidenza diretta di efficacia. |
| Cheratosi seborroica, suscettibilità all'osteoartrosi, cheratosi follicolare invertita vulvare, pseudoacondroplasia | 99,18%–99,50% | L5 | Nessuno studio né letteratura; nessun razionale meccanicistico. |

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate; non ve ne sono di valide. Il testo delle indicazioni approvate e la forma farmaceutica non sono riportati nei dati compilati. Principali autorizzazioni (prime 5):

| N. autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 026416154 | ASACOL 7 clismi 4 g 100 ml sospensione rettale | Giuliani SpA | Cancellata |
| 034836039 | MESALAZINA 7 clismi 4 g sospensione rettale + 7 cannule | Sandoz SpA | Cancellata |
| 035509013 | PROCTASACOL 20 dosi 500 mg gel rettale | Giuliani SpA | Cancellata |
| 034836027 | MESALAZINA 7 clismi 2 g sospensione rettale + 7 cannule | Sandoz SpA | Cancellata |
| 037734011 | MESAVANCOL 60 cpr gastroresistenti 1.200 mg a rilascio prolungato | Giuliani SpA | Cancellata |

## Considerazioni sulla sicurezza

- **Controindicazioni derivate dal grafo di conoscenza** (relazioni farmaco-malattia di PrimeKG, non testo del foglietto illustrativo): malattia renale, piouretere, malattia epatica, malattia della colecisti, neutropenia, agranulocitosi, anemia (inclusa anemia macrocitica), stenosi del piloro, nefrosi lipoidea, nefrite interstiziale.
- **Interazioni**: è stata rilevata una sola relazione di tipo farmacologico, con il recettore PPAR-gamma (PPARG), bersaglio della mesalazina; non si tratta di un'interazione con altri farmaci e non è indicato alcun livello di gravità.
- **Segnalazioni dalla letteratura**: reazioni avverse gravi descritte con la mesalazina, tra cui sindrome DRESS con insufficienza renale acuta e colite indotta da 5-ASA.

Per avvertenze e controindicazioni ufficiali si rimanda al foglietto illustrativo, non disponibile nei dati compilati.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione è supportata solo dal punteggio del modello (livello L5), senza studi clinici, letteratura o razionale meccanicistico. Inoltre, in Italia non esistono autorizzazioni valide per la mesalazina.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione (ad es. da DrugBank) per valutare qualsiasi legame con la patologia
- Recupero e analisi dei foglietti illustrativi AIFA (avvertenze e controindicazioni)
- Verifica dello stato regolatorio effettivo in Italia, dato che tutte le autorizzazioni risultano cancellate
- Evidenza preclinica che colleghi la mesalazina alla via di CDH3 o alla patologia
- Valutazione di priorità alternative con maggiore plausibilità (ad es. artrite reumatoide), oggi comunque solo con evidenza indiretta
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

