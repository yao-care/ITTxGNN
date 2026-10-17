---
layout: default
title: Ketorolac
parent: Solo previsione del modello (L5)
nav_order: 250
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
monitor_inn: "KETOROLAC"
predicted_indications: ["headache disorder", "rosacea conjunctivitis", "trigeminal autonomic cephalalgia"]
description: "Ketorolac: nuova indicazione prevista, Disturbo da cefalea (headache disorder) (livello di evidenza L5)."
---

# Ketorolac
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

# Ketorolac: Dalla congiuntivite allergica al disturbo da cefalea

## Riepilogo in una frase

Il ketorolac è un antinfiammatorio non steroideo (FANS) le cui indicazioni originarie, secondo i dati compilati per questo report, riguardano le congiuntiviti allergiche (atopica, papillare e primaverile). Il modello TxGNN prevede che possa essere efficace per i **disturbi da cefalea**, in particolare l'emicrania, con **18 studi clinici** e **18 pubblicazioni** a supporto di questa direzione. In Italia tutte le autorizzazioni risultano revocate o cancellate.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originaria | Congiuntivite atopica, papillare e primaverile (da grafo di conoscenza; il testo delle indicazioni autorizzate AIFA non è disponibile) |
| Nuova indicazione prevista | Disturbo da cefalea (headache disorder) |
| Punteggio di predizione TxGNN | 99,43% |
| Livello di evidenza | L1 (al limite con L2, vedi note) |
| Stato di mercato in Italia | Solo autorizzazioni cancellate |
| Numero di autorizzazioni | 13 (0 valide, 13 cancellate) |
| Decisione raccomandata | Proceed with Guardrails (procedere con cautele) |

---

## Perché questa predizione è ragionevole?

Il ketorolac è un FANS che inibisce in modo non selettivo gli enzimi COX-1 e COX-2, riducendo la sintesi di prostaglandine. Al momento non sono disponibili dati dettagliati sul meccanismo d'azione per l'indicazione originaria, ma il meccanismo di classe dei FANS è ben noto.

Le prostaglandine contribuiscono all'infiammazione neurogena, alla sensibilizzazione trigemino-vascolare e all'attivazione dei nocicettori periferici, processi coinvolti nell'emicrania e nella cefalea tensiva. L'inibizione della COX fornisce quindi un razionale analgesico plausibile. Anche l'uso originario nelle congiuntiviti allergiche si basa sull'effetto antinfiammatorio e antiprostaglandinico.

**Nota sul livello di evidenza:** le prove poggiano su diversi RCT di fase 4 (NCT01807234, NCT01011673, NCT01596166, NCT03221569), su una revisione sistematica con meta-analisi (PMID 35138658) e su linee guida (PMID 41321235, 25600718). Non esiste un RCT di fase 3 sul ketorolac stesso: l'unico studio di fase 3 elencato che lo riguarda direttamente per confronto di vie di somministrazione è NCT02358681 (ketorolac intranasale vs endovenoso, pediatrico), mentre NCT05102591 testa un dispositivo di neuromodulazione. L'assegnazione di L1 è quindi una valutazione discrezionale al confine tra L1 e L2.

### Altre predizioni nel ranking

- **Congiuntivite da rosacea** (punteggio 99,40%): nessuno studio clinico né pubblicazione. Evidenza L5, decisione **Hold**. Il punteggio probabilmente riflette la vicinanza alle indicazioni oculari esistenti nel grafo, non nuove prove.
- **Cefalea autonomica trigeminale** (punteggio 99,39%): evidenza L4, decisione **Hold**. L'unico studio (NCT04353505) è stato ritirato senza arruolamento e non verifica il ketorolac in modo specifico. I FANS in genere non sono efficaci nella cefalea a grappolo (eccetto l'indometacina in alcune forme), e un caso clinico segnala tossicità da litio indotta dal ketorolac (PMID 7928331).

---

## Evidenze da studi clinici

| Numero studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT01807234](https://clinicaltrials.gov/study/NCT01807234) | Fase 4 | Completato | 72 | Spray nasale di ketorolac vs sumatriptan nasale vs placebo nell'emicrania acuta |
| [NCT01011673](https://clinicaltrials.gov/study/NCT01011673) | Fase 4 | Completato | 123 | RCT metoclopramide/difenidramina vs ketorolac da solo nella cefalea tensiva |
| [NCT01596166](https://clinicaltrials.gov/study/NCT01596166) | Fase 4 | Completato | 56 | Ketorolac EV + metoclopramide nell'emicrania pediatrica al pronto soccorso |
| [NCT01267864](https://clinicaltrials.gov/study/NCT01267864) | Fase 4 | Completato | 330 | Valproato EV vs metoclopramide vs ketorolac nell'emicrania acuta |
| [NCT02358681](https://clinicaltrials.gov/study/NCT02358681) | Fase 3 | Completato | 59 | Ketorolac intranasale vs endovenoso (non inferiorità) nell'emicrania pediatrica |
| [NCT00483717](https://clinicaltrials.gov/study/NCT00483717) | Fase 2 | Completato | 173 | Ketorolac intranasale vs placebo, doppio cieco, nell'emicrania acuta |
| [NCT03221569](https://clinicaltrials.gov/study/NCT03221569) | Fase 4 | Sconosciuto | 60 | Ketamina vs ketorolac nella cefalea tensiva |
| [NCT06083571](https://clinicaltrials.gov/study/NCT06083571) | Fase 2 | Terminato | 41 | Ketorolac intranasale + adiuvanti orali vs ketorolac EV nell'emicrania pediatrica; terminato in anticipo |
| [NCT03066544](https://clinicaltrials.gov/study/NCT03066544) | Fase 1/2 | Sconosciuto | 50 | Responder vs non responder nello stato di male emicranico |
| [NCT02681211](https://clinicaltrials.gov/study/NCT02681211) | Non applicabile | Sconosciuto | 80 | Agopuntura auricolare vs farmaci EV (incl. ketorolac) nello stato di male emicranico pediatrico |

Sono elencati i 10 studi più rilevanti. Altri studi hanno rilevanza limitata (ad esempio NCT05102591, che testa un dispositivo di neuromodulazione, o studi ritirati senza arruolamento).

---

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [35138658](https://pubmed.ncbi.nlm.nih.gov/35138658/) | 2022 | Revisione sistematica e meta-analisi | Acad Emerg Med | Efficacia del ketorolac parenterale nell'attacco emicranico acuto |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Linea guida | Headache | Aggiornamento 2025 AHS sulle terapie parenterali per l'emicrania acuta in pronto soccorso |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Linea guida / valutazione delle evidenze | Headache | Valutazione AHS delle farmacoterapie per l'emicrania acuta |
| [37849443](https://pubmed.ncbi.nlm.nih.gov/37849443/) | 2024 | Revisione sistematica e meta-analisi | Adv Clin Exp Med | Ketorolac EV vs metoclopramide nell'emicrania dell'adulto |
| [23298250](https://pubmed.ncbi.nlm.nih.gov/23298250/) | 2013 | Revisione sistematica | Headache | Efficacia del ketorolac parenterale nell'emicrania acuta, con evidenze contrastanti |
| [24433525](https://pubmed.ncbi.nlm.nih.gov/24433525/) | 2014 | Revisione sistematica | Headache | Trattamento parenterale della cefalea tensiva episodica |
| [35670115](https://pubmed.ncbi.nlm.nih.gov/35670115/) | 2022 | RCT | Headache | Metoclopramide da sola vs associata a ketorolac EV nell'emicrania pediatrica |
| [34822214](https://pubmed.ncbi.nlm.nih.gov/34822214/) | 2022 | RCT | Acad Emerg Med | Ketorolac intranasale vs endovenoso nell'emicrania pediatrica |
| [30783794](https://pubmed.ncbi.nlm.nih.gov/30783794/) | 2019 | RCT | Neurol Sci | Desametasone, metoclopramide, ketorolac e clorpromazina EV: sollievo dal dolore e prevenzione delle recidive |
| [1514724](https://pubmed.ncbi.nlm.nih.gov/1514724/) | 1992 | RCT | Ann Emerg Med | Ketorolac IM vs meperidina e idrossizina nell'emicrania acuta |

---

## Informazioni sul mercato italiano

Tutte le 13 autorizzazioni risultano cancellate. Il testo delle indicazioni approvate e la forma farmaceutica non sono disponibili nei dati compilati. Le prime 5 sono:

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 038205023 | Ketorolac, 3 fiale IM/EV 30 mg/ml | Eugia Pharma (Malta) Limited | Cancellata |
| 037745015 | Ketorolac, 3 fiale IM/EV 30 mg/ml | Towa Pharmaceutical SpA | Cancellata |
| 037850017 | Ketorolac, 3 fiale IM/EV 30 mg/ml | DOC Generici Srl | Cancellata |
| 027253020 | Toradol, 3 fiale IM/EV 30 mg | Recordati SpA | Cancellata |
| 027257056 | Lixidol, 3 fiale IM/EV 30 mg | Atnahs Pharma Netherlands BV | Cancellata |

---

## Considerazioni di sicurezza

I dati su avvertenze e controindicazioni del foglio illustrativo non sono disponibili. Le informazioni seguenti derivano dal grafo di conoscenza e dalle banche dati sulle interazioni, non dal testo dell'etichetta.

- **Condizioni associate a controindicazione (grafo di conoscenza):** ipertensione, ulcera gastrica e ulcera peptica attiva, malattie epatiche e della colecisti, artrite reumatoide, malattia infiammatoria intestinale, asma (intrinseca e allergica), diabete mellito e chetoacidosi diabetica, disturbi della coagulazione ed emofilia, ictus e malattie cerebrovascolari, infarto del miocardio, emoglobinopatie e anemie, insufficienza renale, malattie cardiovascolari e cardiache, sindrome dell'occhio secco.
- **Interazioni farmacologiche:** sono state rilevate 100 interazioni. Tra quelle mostrate:
  - **Maggiore:** acido acetilsalicilico.
  - **Moderate:** corticosteroidi (betametasone, budesonide, desametasone, idrocortisone), sulfoniluree (acetoexamide, clorpropamide, glimepiride, glipizide, gliburide), balsalazide, exenatide, fenfluramina e dexfenfluramina, kanamicina, levofloxacina.
  - **Minori:** famotidina, ranitidina, cimetidina, linaclotide.
  - Dalla letteratura emerge inoltre un caso di tossicità da litio indotta dal ketorolac (PMID 7928331).
- **Rischi noti della classe FANS:** emorragia gastrointestinale, danno renale e rischio cardiovascolare; l'uso dovrebbe essere di breve durata e preceduto da screening delle controindicazioni.

---

## Conclusione e prossimi passi

**Decisione: Proceed with Guardrails**

**Motivazione:**
Per l'emicrania e la cefalea tensiva esistono più RCT randomizzati e comparativi, meta-analisi e linee guida che sostengono il ruolo del ketorolac parenterale. Mancano però RCT di fase 3 sul ketorolac, il farmaco non ha autorizzazioni valide in Italia e il profilo di interazioni e rischi è rilevante. Le altre due predizioni (congiuntivite da rosacea e cefalea autonomica trigeminale) restano in **Hold** per assenza di evidenze dirette.

**Per procedere sono necessari:**
- Il foglio illustrativo AIFA con avvertenze e controindicazioni (lacuna bloccante per lo screening di sicurezza).
- I dati sul meccanismo d'azione da DrugBank.
- Una valutazione della disponibilità di formulazioni (endovenosa, intramuscolare, intranasale) e dello stato regolatorio in Italia, dato che tutte le autorizzazioni sono cancellate.
- Un piano di monitoraggio della sicurezza (rischio gastrointestinale, renale e cardiovascolare, interazioni con anticoagulanti, litio e ACE-inibitori), con durata limitata del trattamento.
- Una verifica più approfondita dell'evidenza per i sottotipi di cefalea diversi dall'emicrania.
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

