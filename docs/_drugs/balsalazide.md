---
layout: default
title: Balsalazide
parent: Solo previsione del modello (L5)
nav_order: 62
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Balsalazide: nuova indicazione prevista, Gotta (livello di evidenza L5). Indicazione originale: Colite ulcerosa"
---

# Balsalazide
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **10** 
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

# Balsalazide: dalla colite ulcerosa alla gotta

## Sintesi

Balsalazide è un profarmaco dell'acido 5-aminosalicilico (5-ASA, mesalazina), utilizzato originariamente per la colite ulcerosa e le malattie infiammatorie croniche intestinali. Il modello TxGNN prevede una possibile efficacia nella **gotta** (punteggio 99,75%), ma i dati compilati per questo report non includono **nessuno studio clinico** né **alcuna pubblicazione** a supporto: la previsione è basata solo sul modello.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Colite ulcerosa; malattia infiammatoria cronica intestinale (dal grafo di conoscenza; il testo autorizzativo AIFA non è disponibile) |
| Nuova indicazione prevista | Gotta |
| Punteggio di previsione TxGNN | 99,75% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 1 (0 valide, 1 cancellata) |
| Decisione raccomandata | Hold |

## Perché questa previsione potrebbe essere ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. Balsalazide rilascia nel colon il 5-ASA, che ha attività antinfiammatoria locale sulla mucosa intestinale; il carrier inerte è l'acido 4-aminobenzoil-β-alanina.

Il legame con la gotta è **speculativo**. Si potrebbe ipotizzare un coinvolgimento dell'infiammazione guidata dai neutrofili o dalla via NLRP3/IL-1β, ma il 5-ASA non è noto per influenzare il metabolismo dell'urato. L'elevato punteggio del modello (0,998) non è quindi verificabile con i dati disponibili.

Tra le altre previsioni di TxGNN, alcune hanno una plausibilità biologica maggiore della gotta, anche se tutte restano senza evidenza clinica diretta:
- **Spondilite anchilosante** (99,71%) e **spondilopatia infiammatoria** (99,53%): condividono l'asse intestino-articolazioni con le IBD; la sulfasalazina (che condivide il 5-ASA) è stata studiata nelle spondiloartriti, ma il beneficio riguarda soprattutto le articolazioni periferiche e potrebbe dipendere dalla sulfapiridina, assente in balsalazide.
- **Artrite reumatoide** (99,64%) e **artrite reumatoide giovanile poliarticolare** (99,43%): l'estrapolazione dalla sulfasalazina è incerta per lo stesso motivo.
- Altre previsioni (ipotricosi congenita con distrofia maculare giovanile, ipermobilità del coccige, malattia di Kümmell) sembrano artefatti del grafo di conoscenza, senza un legame biologico plausibile.

## Evidenza da studi clinici

Attualmente non risultano studi clinici registrati correlati.

## Evidenza dalla letteratura

Attualmente non è disponibile letteratura correlata.

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 033858022 | BALZIDE 112 capsule 750 mg (Menarini) | Non specificata | Non specificata (autorizzazione cancellata) |

## Considerazioni sulla sicurezza

- **Controindicazioni dal grafo di conoscenza** (non tratte dal foglietto illustrativo): malattia renale, piouretere, stenosi del piloro.
- **Interazioni farmacologiche**: sono state identificate 100 interazioni. Tra quelle elencate:
  - **Maggiore**: immunoglobulina G umana (endovenosa).
  - **Moderate** (esempi): azatioprina, ibuprofene, ketorolac, celecoxib, aciclovir, foscarnet, amfotericina B, amikacina, doxiciclina, amoxicillina, ampicillina, azitromicina, bacitracina, fosfomicina, nitrato di gallio, acetoesamide.
  - Diverse di queste combinazioni (FANS, aminoglicosidi, amfotericina B, foscarnet) riguardano farmaci con tossicità renale, coerentemente con le controindicazioni renali sopra riportate.

Per le avvertenze e le controindicazioni ufficiali, consultare il foglietto illustrativo.

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione per la gotta si basa unicamente sul modello (L5), senza studi clinici né letteratura, con un legame meccanicistico speculativo. Inoltre, l'unica autorizzazione italiana è cancellata, quindi il prodotto non è attualmente commercializzato.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione e una revisione meccanicistica del legame tra 5-ASA e infiammazione gottosa
- Ricerca di letteratura e studi preclinici o clinici su balsalazide/5-ASA nella gotta
- Avvertenze e controindicazioni dal foglietto illustrativo AIFA, indispensabili per lo screening di sicurezza
- Verifica della disponibilità del farmaco in Italia, data la cancellazione dell'autorizzazione
- Eventuale rivalutazione di indicazioni più plausibili (spondiloartriti associate a IBD), definendo sottotipi specifici e rivedendo i dati su sulfasalazina e 5-ASA
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

