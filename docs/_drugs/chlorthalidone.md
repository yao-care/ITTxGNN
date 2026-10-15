---
layout: default
title: Chlorthalidone
parent: Solo previsione del modello (L5)
nav_order: 104
evidence_level: L5
indication_count: 10
---

# Chlorthalidone
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

# Clortalidone: Da ipertensione e scompenso cardiaco congestizio a glaucoma primario ereditario

## Sintesi in una frase

Il clortalidone è un diuretico tiazidico-simile, utilizzato in origine per il trattamento di ipertensione e scompenso cardiaco congestizio.
Il modello TxGNN prevede che possa essere efficace per il **glaucoma primario ereditario**, ma al momento **non risultano né studi clinici né pubblicazioni** a sostegno di questa ipotesi: si tratta di una pura predizione del modello.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Ipertensione, scompenso cardiaco congestizio (dal grafo di conoscenza TxGNN; il testo autorizzativo AIFA non è disponibile) |
| Nuova indicazione prevista | Glaucoma primario ereditario |
| Punteggio di predizione TxGNN | 99,92% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cessate |
| Numero di autorizzazioni | 19 (tutte cessate; nessuna valida) |
| Decisione raccomandata | Hold |

---

## Perché questa predizione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. Il clortalidone è un diuretico tiazidico-simile, la cui efficacia nell'ipertensione e nello scompenso cardiaco congestizio è nota; riduce la pressione arteriosa tramite diuresi e natriuresi.

Un legame meccanicistico diretto con il glaucoma primario ereditario **non è stabilito** dai dati compilati per questo report. Qualsiasi effetto sulla pressione intraoculare o sulla dinamica dell'umor acqueo sarebbe speculativo. Il punteggio molto alto (0,999) deriva esclusivamente dal modello e non è supportato da evidenze cliniche.

Anche le altre predizioni di rilievo vanno lette con cautela:

| Rank | Indicazione prevista | Punteggio | Livello | Note |
|---|---|---|---|---|
| 2 | Glaucoma ad angolo aperto | 99,90% | L5 | Nessuna evidenza |
| 3 | Nefropatia ipertensiva maligna | 99,89% | L5 | Plausibile per vicinanza all'ipertensione, ma i diuretici tiazidici sono meno efficaci a basso eGFR |
| 4 | Ipertensione nefrovascolare maligna | 99,89% | L5 | Guidata dall'attivazione del RAAS; un diuretico da solo non è terapia mirata |
| 5–6 | Ipertensione polmonare (da malattia polmonare/ipossia; multifattoriale) | 99,88% | L5 | Solo gestione sintomatica del volume |
| 7 | Sindrome di Braddock | 99,85% | L5 | Verosimile artefatto del grafo |
| 8 | Cuore polmonare cronico | 99,82% | L4 | Evidenza indiretta e storica (vedi sotto) |
| 9 | Cuore polmonare acuto | 99,32% | L5 | Diuresi aggressiva potenzialmente dannosa |
| 10 | Ipotricosi congenita con milia | 99,19% | L5 | Nessun legame identificabile |

Tra le predizioni, il cuore polmonare cronico è l'unica con un minimo di supporto: la decongestione nello scompenso destro da cor pulmonale cronico è meccanicisticamente coerente con l'indicazione approvata per lo scompenso cardiaco congestizio.

---

## Evidenze da studi clinici

Al momento non risultano studi clinici registrati correlati al glaucoma primario ereditario (né alle altre indicazioni previste).

---

## Evidenze dalla letteratura

Per l'indicazione principale (glaucoma primario ereditario) al momento non è disponibile letteratura correlata.

Per completezza, riportiamo la letteratura reperita per le altre indicazioni previste:

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [5597001](https://pubmed.ncbi.nlm.nih.gov/5597001/) | 1967 | Rapporto clinico (storico, probabile serie di casi) | La Clinica terapeutica | Terapia diuretica con clortalidone nello scompenso cardiaco congestizio da cuore polmonare cronico (indicazione: cuore polmonare cronico) |
| [28711447](https://pubmed.ncbi.nlm.nih.gov/28711447/) | 2017 | Revisione | JACC. Heart failure | Transizione dall'ipertensione allo scompenso cardiaco; rilevanza solo indiretta (indicazione: cuore polmonare cronico) |
| [14288313](https://pubmed.ncbi.nlm.nih.gov/14288313/) | 1965 | Ricerca di base | Journal of cellular and comparative physiology | Trasporto attivo nell'intestino medio di Cecropia; non pertinente (indicazione: ipertensione polmonare) |

---

## Informazioni sul mercato italiano

Tutte le 19 autorizzazioni risultano cessate; non ci sono autorizzazioni valide. Il testo delle indicazioni approvate non è disponibile nei dati compilati. Principali autorizzazioni (elenco parziale):

| N. autorizzazione | Nome prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 016861015 | IGROTON 30 cpr 25 mg | AMDIPHARM LTD | Cessata |
| 024737025 | TENORETIC 28 cpr 100 mg + 25 mg | ATNAHS PHARMA NETHERLANDS BV | Cessata |
| 024728038 | EUPRES 21 cpr 100 mg + 25 mg | VIATRIS HEALTHCARE LIMITED | Cessata |
| 033054014 | ATENOLOLO CLORTALIDONE 28 cpr 50 mg + 12,5 mg | RATIOPHARM GMBH | Cessata |
| 032805020 | ATENOLOLO CLORTALIDONE 30 cpr rivestite 50 mg + 12,5 mg | SANDOZ SpA | Cessata |

La maggior parte delle autorizzazioni riguarda l'associazione fissa con atenololo.

---

## Considerazioni sulla sicurezza

Le informazioni dal foglietto illustrativo AIFA (avvertenze e controindicazioni) non sono disponibili: si rimanda al foglietto illustrativo.

- **Controindicazioni dal grafo di conoscenza (non da testo di etichetta)**: insufficienza epatica, malattia renale, anuria, pancreatite, ulcera peptica, lupus eritematoso sistemico (anche pediatrico), asma (intrinseco e allergico), carenza di potassio, psoriasi e parapsoriasi, iperuricemia, gotta, ipercalcemia, nefrocalcinosi, disturbi del metabolismo del fosforo, infarto miocardico e trombosi coronarica, emoglobinopatie, diabete mellito (incluso tipo 2), arresto cardiaco improvviso, epilessia, disturbo d'ansia, disturbo nevrotico, disturbo distimico, piureter.
- **Interazioni farmacologiche**: 210 interazioni totali rilevate. Tra quelle di gravità **maggiore**: cisapride e dolasetron. Tra quelle di gravità moderata: metformina, acarbose, alogliptin, albiglutide, bupropione, morfina, idrocortisone, desametasone, triamcinolone, beclometasone, omeprazolo, rabeprazolo, amfotericina B e colecalciferolo. Interazioni minori: doxiciclina, atropina, iosciamina.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
L'evidenza è solo di livello L5 (predizione del modello), senza studi clinici né letteratura pertinente, e senza un legame meccanicistico plausibile con il glaucoma. Inoltre il prodotto non ha attualmente autorizzazioni valide in Italia.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione (MOA) da DrugBank
- Foglietto illustrativo AIFA con avvertenze e controindicazioni (lacuna bloccante per lo screening di sicurezza)
- Una revisione sistematica della letteratura sull'effetto dei diuretici tiazidici sulla pressione intraoculare
- Valutazione di indicazioni cardiovascolari più vicine (ad es. cuore polmonare cronico) come possibile quesito di ricerca, partendo dal rapporto storico del 1967
- Verifica dello stato regolatorio e della disponibilità commerciale del principio attivo in Italia
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

