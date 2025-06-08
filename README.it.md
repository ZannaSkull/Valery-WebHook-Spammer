# Valery WebHook Spammer

[🇬🇧 English](README.md) | [🇮🇹 Italiano](README.it.md)

<p align="center">
<img src="https://i.pinimg.com/564x/a5/c1/1b/a5c11b552c3afd0d08273fd5f1677f59.jpg" width="500" height="500">
</p>

**Valery WebHook Spammer** è uno strumento avanzato e moderno per l’invio massivo di messaggi tramite webhook. Progettato per essere veloce, configurabile e affidabile, sfrutta le capacità asincrone di Python per offrire alte prestazioni e una gestione intelligente dei limiti imposti dalle piattaforme come Discord.

---

## 🚀 Caratteristiche Principali

- Invio rapido e massivo di messaggi.
- Gestione avanzata e automatica dei proxy: scarica proxy pubblici, con rotazione automatica e rimozione dei proxy non funzionanti.
- Bypass intelligente dei rate limit di Discord, rispettando sia i limiti globali che quelli specifici per bucket, per evitare blocchi e ban temporanei.
- Interfaccia utente migliorata con input guidato, banner colorato e notifiche desktop.
- Completamente asincrono, utilizza `asyncio` per massimizzare velocità e scalabilità.
- Personalizzazione completa di messaggio, avatar, delay, timeout, numero di messaggi e altro.
- Integrazione con Discord Rich Presence per mostrare lo stato dello spamming direttamente sul tuo profilo Discord.

---

## 🔄 Gestione e Bypass dei Rate Limit

Discord applica limiti rigorosi alle richieste webhook per prevenire abusi e garantire la stabilità del servizio. Valery WebHook Spammer implementa un meccanismo sofisticato per gestire e bypassare questi limiti in modo efficace:

- Quando viene rilevato un rate limit (codice HTTP 429), il programma legge l’header `Retry-After` fornito da Discord, che specifica quanti secondi attendere prima di riprovare.
- Lo spammer rispetta sia i limiti **globali** che quelli **bucket-specifici** implementando una logica di bucket, assicurando che le richieste siano inviate con la giusta frequenza per evitare blocchi o ban.
- Le richieste che incontrano un rate limit vengono automaticamente ritentate dopo il ritardo specificato, mantenendo un processo di spamming fluido e continuo senza intervento manuale.
- Questo approccio previene errori inutili e massimizza il throughput, rispettando le policy delle API di Discord.
- Inoltre, il programma gestisce in modo intelligente le richieste concorrenti utilizzando code asincrone e semafori per bilanciare velocità e rispetto dei limiti.

Questa gestione avanzata dei rate limit assicura che Valery WebHook Spammer possa inviare grandi volumi di messaggi in modo efficiente senza essere bloccato o andare in timeout da parte di Discord.

---

## 🛠️ Requisiti

- Python 3.8 o superiore
- Gestore pacchetti `pip`

---

## 📝 Come si Usa

1. Scarica o clona il progetto.
2. Apri un terminale nella cartella del progetto.
3. Avvia lo script con: python Valery.py
4. Segui le istruzioni a schermo per inserire:
- Messaggio da inviare
- URL del webhook
- Delay tra i messaggi
- Numero di messaggi da inviare
- Timeout delle richieste
- Utilizzo dei proxy (automatico)
5. Monitora il progresso nella console, nelle notifiche desktop e tramite Discord Rich Presence.

---

## ⛔ Disclaimer

Valery WebHook Spammer è fornito esclusivamente per scopi educativi e di test.  
L’autore e i collaboratori non sono responsabili per eventuali abusi o danni causati da questo software.  
Usa questo strumento responsabilmente e a tuo rischio.

---

## 👤 Crediti

Valery WebHook Spammer è stato creato da **Hisako**.

---

> **Nota:** L’uso di strumenti di spamming è vietato dai Termini di Servizio di molte piattaforme. Utilizza questo software solo su webhook di tua proprietà o in ambienti di test controllati.
