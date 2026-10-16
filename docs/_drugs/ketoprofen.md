---
layout: default
title: Ketoprofen
parent: Solo previsione del modello (L5)
nav_order: 249
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ketoprofen: nuova indicazione prevista, Displasia acromesomelica di tipo Hunter-Thompson (livello di evidenza L5). Indicazione originale: Artrite reumatoide, osteoartrosi…"
---

# Ketoprofen
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

# Ketoprofene: dall'artropatia e artrite reumatoide alla displasia acromesomelica di tipo Hunter-Thompson

## Sintesi in una frase

Il ketoprofene è un farmaco antinfiammatorio non steroideo (FANS) usato in origine per artrite reumatoide, osteoartrosi e artropatie.
Il modello TxGNN prevede una possibile efficacia per la **displasia acromesomelica di tipo Hunter-Thompson**, ma al momento **non risultano studi clinici né pubblicazioni** a supporto: la previsione si basa solo sul modello.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Artrite reumatoide, osteoartrosi, artropatia (da indicazioni del grafo di conoscenza; i testi delle autorizzazioni AIFA non riportano l'indicazione) |
| Nuova indicazione prevista | Displasia acromesomelica di tipo Hunter-Thompson |
| Punteggio di previsione TxGNN | 99,98% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 20 (tutte cancellate) |
| Decisione raccomandata | Hold |

## Perché questa previsione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione registrati per questo farmaco. Il ketoprofene è un FANS non selettivo, inibitore delle ciclossigenasi (COX), con effetti analgesici e antinfiammatori sintomatici; la sua efficacia in artrite reumatoide e osteoartrosi è nota.

Per la displasia acromesomelica di tipo Hunter-Thompson **non emerge un legame meccanicistico chiaro**. La malattia è una rara displasia scheletrica dovuta a mutazioni con perdita di funzione di CDMP1/GDF5, che alterano la via di segnalazione BMP e la condrogenesi. L'inibizione delle COX non agisce sulla base genetica o dello sviluppo della malattia. Il punteggio molto alto sembra riflettere la vicinanza nel grafo di conoscenza a fenotipi di artropatia e scheletrici, più che una reale motivazione farmacologica.

Lo stesso vale per gran parte delle altre previsioni di vertice (sindrome brachiolmia-amelogenesi imperfetta, miosclerosi, brachiolmia, sindrome microftalmia colobomatosa-displasia rizomelica, sindrome brachidattilia-sindattilia, sindrome WHIM): nessun legame plausibile con il meccanismo del ketoprofene. Fra le previsioni successive, più plausibili ma solo in via indiretta e di classe, figurano:
- **Pseudoacondroplasia**: i FANS possono alleviare il dolore articolare, ma senza modificare la malattia.
- **Spondiloartropatia (suscettibilità)**: i FANS sono terapia di prima linea nelle spondiloartriti.
- **Artrite giovanile da difetto di LACC1**: possibile sollievo sintomatico; per il controllo della malattia servirebbero probabilmente terapie biologiche o mirate.

## Evidenze da studi clinici

Attualmente non risultano studi clinici correlati registrati.

## Evidenze dalla letteratura

Attualmente non è disponibile letteratura correlata.

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate; nessuna è attualmente valida. Testo dell'indicazione e forma farmaceutica non sono riportati nei dati compilati. Principali autorizzazioni (prime 5):

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 023183205 | ORUDIS 6 fiale IM 100 mg 2 ml | SANOFI Srl | Cancellata |
| 034925040 | DOLGOSIN 28 cps 200 mg rilascio prolungato | DYMALIFE PHARMACEUTICAL Srl | Cancellata |
| 023401110 | FLEXEN 30 cps 200 mg rilascio prolungato | ITALFARMACO SpA | Cancellata |
| 023183027 | ORUDIS 30 cps 50 mg | SANOFI Srl | Cancellata |
| 034513022 | STEOFEN 30 cps 200 mg rilascio prolungato | LANOVA FARMACEUTICI Srl | Cancellata |

## Considerazioni sulla sicurezza

**Controindicazioni (dal grafo di conoscenza, non dal foglietto illustrativo):** ipertensione/disturbi ipertensivi, insufficienza epatica, malattia renale, ulcera peptica (anche attiva), disturbi della coagulazione, infarto del miocardio, trombosi coronarica, emoglobinopatie, malattie cardiovascolari e cardiache, piouretere.

**Interazioni farmacologiche:** sono state rilevate 226 interazioni complessive. Tra quelle elencate:
- **Moderate:** acido acetilsalicilico, corticosteroidi (idrocortisone, desametasone, betametasone, budesonide, triamcinolone), metformina, glimepiride, clorpropamide, mesalazina, balsalazide, naltrexone, citrato e bicarbonato di potassio, acido picosolfurico, polietilenglicole con elettroliti.
- **Minori:** famotidina, ranitidina, cimetidina, linaclotide.

Avvertenze e controindicazioni ufficiali del foglietto illustrativo AIFA non sono disponibili; per la sicurezza completa fare riferimento al foglietto illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione è basata solo sul modello (L5), senza studi clinici né letteratura e senza un legame meccanicistico plausibile con una malattia genetica dello sviluppo scheletrico. Inoltre tutte le autorizzazioni italiane sono cancellate.

**Per procedere sarebbe necessario:**
- Dati sul meccanismo d'azione (MOA) del ketoprofene.
- Foglietto illustrativo AIFA con avvertenze e controindicazioni, indispensabile per lo screening di sicurezza.
- Evidenze precliniche o cliniche specifiche per la displasia acromesomelica di tipo Hunter-Thompson.
- Eventuale riorientamento verso indicazioni sintomatiche più plausibili (spondiloartropatia, artrite giovanile da difetto di LACC1, pseudoacondroplasia) come questioni di ricerca, con valutazione dello stato regolatorio e della via di somministrazione.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

