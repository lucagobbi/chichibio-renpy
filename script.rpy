define corrado = Character("Corrado", color="#7b2b2b", image="corrado")
define chichibio = Character("Chichibio", color="#34583f", image="chichibio")
define brunetta = Character("Brunetta", color="#846117", image="brunetta")
define narrator = Character(None, what_italic=True)
define decameron = Character("Decameron", color="#4f3104") # Guida educativa

# Variabili per il sistema di punteggio
default knowledge_points = 0

# Immagini dei personaggi - espressioni base
# Corrado
image corrado normal = "characters/corrado/normal.png"
image corrado angry = "characters/corrado/angry.png"
image corrado laughing = "characters/corrado/laughing.png"

# Chichibio
image chichibio normal = "characters/chichibio/normal.png"
image chichibio worried = "characters/chichibio/worried.png"
image chichibio happy = "characters/chichibio/happy.png"

# Brunetta
image brunetta normal = "characters/brunetta/normal.png"
image brunetta pleading = "characters/brunetta/pleading.png"

# Backgrounds
image bg kitchen:
    "bg/kitchen.png"
    xysize(1920, 1080)

image bg dining_room:
    "bg/dining_room.png"
    xysize(1920, 1080)

image bg bedroom:
    "bg/bedroom.png"
    xysize(1920, 1080)

image bg riverside:
    "bg/riverside.png"
    xysize(1920, 1080)

image bg florence:
    "bg/florence.png"
    xysize(1920, 1080)

init python:
    def show_happy_reaction():
        renpy.show("chichibio happy", at_list=[])
        renpy.with_statement(dissolve)
    
    def show_worried_reaction():
        renpy.show("chichibio worried", at_list=[])
        renpy.with_statement(dissolve)
    
    def return_to_normal():
        renpy.show("chichibio normal", at_list=[])
        renpy.with_statement(dissolve)

# Schermata per informazioni sul Decameron
screen decameron_info(title, content):
    modal True
    
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 40
        ypadding 30
        xsize 800
        
        vbox:
            spacing 15
            
            text title:
                xalign 0.5
                size 30
                color "#302300"
                
            text content:
                size 22
                
            textbutton "Chiudi":
                xalign 0.5
                yalign 0.9
                action Hide("decameron_info")

# Notifica punti
screen knowledge_notification(amount):
    zorder 100
    frame:
        xalign 0.5
        yalign 0.1
        padding (20, 10)
        
        text "+[amount] Conoscenza Decameron" color "#423500" size 24
    
    timer 2.0 action Hide("knowledge_notification")

# Inizio del gioco
label start:
    scene black

    play music "audio/music/medieval_theme.mp3" fadein 2.0
    
    # Introduzione
    show text "Il Decamerone\n\ndi Giovanni Boccaccio" with dissolve
    $ renpy.pause(2.0, hard=True)
    
    show text "La novella di Chichibio e la Gru appartiene alla sesta giornata del Decameron, dedicata ai motti di spirito e alle risposte argute." with dissolve
    $ renpy.pause(3.0, hard=True)
    
    # Inizio della storia
    scene bg florence with fade
    
    # Elemento educativo iniziale
    show screen decameron_info("Il Contesto Storico", "La novella è ambientata a Firenze nel XIV secolo, periodo di grande splendore artistico, ma anche di contrasti sociali. La figura del servo astuto che si salva con l'ingegno è un tema ricorrente nel Decameron.")
    $ renpy.pause()
    hide screen decameron_info
    
    $ knowledge_points += 5
    show screen knowledge_notification(5)
    
    narrator "Firenze, XIV secolo."
    
    narrator "In questa città viveva Corrado Gianfigliazzi, uno dei cittadini più in vista, famoso per la sua passione per la caccia."
    
    narrator "Un giorno, Corrado catturò una gru e la fece portare al suo cuoco veneziano, Chichibio, ordinandogli di arrostirla per cena."
    
    scene bg kitchen with fade
    
    play sound "audio/sfx/cooking.mp3"

    show chichibio normal at left
    
    decameron "Nel Medioevo, la cucina delle case nobili richiedeva grande abilità e conoscenza. I cuochi erano figure importanti nella gerarchia della servitù."
    
    $ knowledge_points += 5
    show screen knowledge_notification(5)
    
    chichibio "Una bellissima gru! La preparerò con la massima cura per il mio signore."
    
    narrator "Chichibio si mise all'opera per preparare la gru. Mentre la cuoceva con attenzione, il profumo delizioso si diffuse per tutta la cucina."
    
    # Quiz educativo sulla cucina medievale
    decameron "Quali spezie erano più preziose nella cucina medievale?"
    
    jump cooking_minigame

label cooking_minigame:
    $ ingredients_selected = []
    $ correct_steps = 0
    $ total_steps = 5
    $ cooking_score = 0
    
    narrator "Per preparare la gru alla perfezione, Chichibio deve fare le scelte giuste."
    show chichibio normal at left
    
    chichibio "Vediamo cosa serve per questa ricetta speciale..."    
    # Primo passo: scegliere le spezie
    chichibio "Prima di tutto, devo scegliere le spezie giuste."
    
    menu:
        "Quali spezie dovrebbe usare Chichibio?"
        
        "Pepe e zafferano":

            $ correct_steps += 1
            $ cooking_score += 20
            
            $ show_happy_reaction()

            play sound "audio/sfx/correct.mp3"

            chichibio "Perfetto! Il pepe darà sapore e lo zafferano un bel colore dorato. Proprio come piace al mio signore!"
            
            decameron "Lo zafferano era una spezia preziosa, usata nelle tavole nobili. Conferiva ai cibi un colore dorato, simbolo di ricchezza."
            $ knowledge_points += 5
            show screen knowledge_notification(5)

            $ return_to_normal()

            
        "Origano e basilico":

            $ show_worried_reaction()

            play sound "audio/sfx/wrong.mp3"

            chichibio "Hmm... non sono sicuro che siano le spezie tradizionali per questo piatto nobile."
            
            $ return_to_normal()

        "Cannella e chiodi di garofano":

            $ show_worried_reaction()

            play sound "audio/sfx/wrong.mp3"

            chichibio "Queste spezie sono troppo dolci per la gru. Meglio usarle per un dolce."
    
            $ return_to_normal()

    # Secondo passo: scelta del liquido
    chichibio "Ora devo bagnare la gru con qualcosa per mantenerla succosa durante la cottura..."
    
    menu:
        "Con quale liquido bagnare la gru?"
        
        "Vino bianco":
            $ correct_steps += 1
            $ cooking_score += 20

            $ show_happy_reaction()

            play sound "audio/sfx/correct.mp3"

            chichibio "Il vino bianco darà un sapore delicato ed elegante! Una scelta degna del mio signore."
            
            decameron "Il vino era fondamentale nella cucina rinascimentale, sia per il consumo che per la preparazione dei cibi."
            $ knowledge_points += 5
            show screen knowledge_notification(5)

            $ return_to_normal()
            
        "Aceto":

            $ show_worried_reaction()
 
            play sound "audio/sfx/wrong.mp3"

            chichibio "L'aceto potrebbe essere troppo forte per questo piatto delicato. Corrado non apprezzerebbe."

            $ return_to_normal()
            
        "Acqua semplice":

            $ show_worried_reaction()

            play sound "audio/sfx/wrong.mp3"

            chichibio "Un po' semplice... manca di carattere. La gru merita di meglio!"
    
            $ return_to_normal()

    # Terzo passo: scegliere il ripieno
    chichibio "Per rendere la gru più saporita, devo aggiungere un ripieno..."
    
    menu:
        "Quale ripieno usare per la gru?"
        
        "Erbe aromatiche e cipolla":

            $ show_worried_reaction()

            play sound "audio/sfx/wrong.mp3"

            chichibio "Non male, ma potrei fare di meglio per un piatto così importante."
            
            $ return_to_normal()

        "Castagne e mele":
            $ correct_steps += 1
            $ cooking_score += 20

            $ show_happy_reaction()

            play sound "audio/sfx/correct.mp3"

            chichibio "Eccellente! Le castagne e le mele daranno un sapore autunnale e ricco."
            
            decameron "Questo tipo di ripieno era tipico della cucina medievale, che amava combinare sapori dolci e salati."
            $ knowledge_points += 5
            show screen knowledge_notification(5)
            
            $ return_to_normal()

        "Pane raffermo e uova":

            $ show_worried_reaction()

            play sound "audio/sfx/wrong.mp3"

            chichibio "Hmm, questo potrebbe funzionare per un pollo, ma non per una gru nobile."
    
            $ return_to_normal()

    # Quarto passo: scelta del metodo di cottura
    chichibio "Ora, come dovrei cuocere questo magnifico uccello?"
    
    menu:
        "Quale metodo di cottura è migliore?"
        
        "Arrostire lentamente, girandola spesso":
            $ correct_steps += 1
            $ cooking_score += 20

            $ show_happy_reaction()

            play sound "audio/sfx/correct.mp3"

            chichibio "Perfetto! La cottura lenta e il girare spesso garantiranno una gru dorata e succosa!"
            
            $ return_to_normal()

        "Cuocere rapidamente a fiamma alta":

            $ show_worried_reaction()

            play sound "audio/sfx/wrong.mp3"

            chichibio "Troppo rapido! La carne diventerebbe dura e asciutta."
            
            $ return_to_normal()

        "Bollire prima, poi arrostire":

            $ show_worried_reaction()

            play sound "audio/sfx/wrong.mp3"

            chichibio "Questo metodo è adatto per carni più dure, non per un uccello delicato come la gru."
    
            $ return_to_normal()

    # Quinto passo: guarnizione finale
    chichibio "Infine, come dovrei guarnire la gru prima di servirla?"
    
    menu:
        "Come guarnire il piatto finale?"
        
        "Con salsa di agrumi":

            $ show_worried_reaction()

            play sound "audio/sfx/wrong.mp3"

            chichibio "Gli agrumi sono rari e preziosi, ma non si sposano bene con questo piatto."
            
            $ return_to_normal()

        "Con una spruzzata di aceto balsamico":

            $ show_worried_reaction()

            play sound "audio/sfx/wrong.mp3"

            chichibio "L'aceto balsamico è un condimento troppo moderno per questa ricetta tradizionale."
            
            decameron "Alcuni condimenti che oggi diamo per scontati non erano disponibili o comuni nel XIV secolo."
            $ knowledge_points += 5
            show screen knowledge_notification(5)
            
            $ return_to_normal()

        "Con una salsa a base di vino e miele":
            $ correct_steps += 1
            $ cooking_score += 20

            $ show_happy_reaction()

            play sound "audio/sfx/correct.mp3"

            chichibio "Eccellente! Il vino e il miele creeranno una glassa lucida e saporita. Corrado sarà impressionato!"
    
            $ return_to_normal()
            
    # Risultato finale
    $ cooking_success = (correct_steps >= 3)
    $ gru_quality = cooking_score
    
    if correct_steps == 5:
        play sound "audio/sfx/perfect.mp3"
        narrator "Chichibio ha preparato una gru assolutamente perfetta! Un capolavoro culinario degno dei migliori banchetti!"
        $ cooking_score += 20  # Bonus per perfezione
        
    elif correct_steps >= 3:
        play sound "audio/sfx/good.mp3"
        narrator "La gru è venuta molto bene. Corrado dovrebbe essere soddisfatto."
        
    else:
        play sound "audio/sfx/bad.mp3"
        narrator "La gru non è venuta proprio come Chichibio sperava. Speriamo che Corrado sia distratto dalle buone conversazioni a tavola..."
    
    # Quiz rapido sul significato culturale
    decameron "Nella cultura del tempo, cosa rappresentava la gru nella tavola di un nobile?"
    
    menu:
        "Cosa rappresentava la gru nel contesto sociale?"
        
        "Un simbolo di prestigio e ricchezza":
            $ knowledge_points += 10
            show screen knowledge_notification(10)
            
            decameron "Esatto! La gru era una preda nobile, e poterla servire a tavola dimostrava lo status sociale elevato del padrone di casa."
            
        "Solo un cibo prelibato":
            $ knowledge_points += 3
            show screen knowledge_notification(3)
            
            decameron "Non solo. Oltre ad essere prelibata, la gru era un simbolo di prestigio sociale. Nel Medioevo, ciò che si mangiava rifletteva il proprio rango."
            
        "Un animale comune nell'alimentazione medievale":
            decameron "In realtà, la gru non era affatto comune. Era una preda pregiata e prestigiosa, riservata alle tavole dei più abbienti."
    
    jump continue_cooking_story

label continue_cooking_story:
    
    narrator "La gru era quasi pronta e ne proveniva un delizioso profumino..."
    
    show brunetta normal at right with moveinright
    
    narrator "...quando una donnetta del quartiere, Brunetta, per la quale Chichibio aveva perso la testa, entrò in cucina attirata proprio dal profumo della gru."
    
    decameron "I personaggi femminili nel Decameron sono spesso rappresentati come astuti e capaci di ottenere ciò che vogliono con intelligenza."
    
    $ knowledge_points += 5
    show screen knowledge_notification(5)
    
    show chichibio happy
    
    chichibio "Brunetta mia! Che piacere vederti!"
    
    show brunetta pleading
    
    brunetta "Chichibio, che buon profumo! È gru quella che stai cucinando?"
    
    chichibio "Sì, è per la cena del mio signore Corrado."
    
    brunetta "Ti prego, Chichibio, potresti darmi una coscia? Mi è venuta una tale voglia..."
    
    show chichibio worried
    
    chichibio "Oh no, non posso! Il signor Corrado se ne accorgerebbe subito!"
    
    show brunetta pleading
    
    narrator "Brunetta continuò a supplicare Chichibio, che inizialmente resistette, ma poi..."
    
    decameron "Come pensi che prosegua la storia, secondo la novella originale?"
    
    menu:
        "Cosa fa Chichibio nella novella originale?"
        
        "Cede alle suppliche e dà la coscia a Brunetta":
            $ knowledge_points += 10
            show screen knowledge_notification(10)
            
            decameron "Esatto! Nella novella di Boccaccio, dopo un tira e molla, Chichibio cede alle suppliche di Brunetta e le dà una coscia della gru."
            
        "Resiste e non le dà la coscia":
            $ knowledge_points += 3
            show screen knowledge_notification(3)
            
            decameron "In realtà, nella novella originale, Chichibio alla fine cede e dà la coscia della gru a Brunetta. Questo creerà il problema centrale della storia."
    
    narrator "Dopo un'interminabile tira e molla, alla fine, per non far arrabbiare Brunetta, Chichibio staccò una coscia della gru e gliela diede."
    
    show brunetta normal
    
    brunetta "Grazie, Chichibio! Sei il cuoco più gentile di tutta Firenze!"
    
    hide brunetta with moveoutright
    
    show chichibio worried
    
    chichibio "Oh cielo... e ora come faccio con il signor Corrado?"
    
    # Avanzamento alla scena della cena - seguendo la novella originale
    jump dinner_scene

# Scena della cena - conforme alla novella originale
label dinner_scene:
    scene bg dining_room with fade
    play music "audio/music/tense.mp3" fadein 2.0
    
    show corrado normal at left
    
    narrator "Quando la gru fu poi servita a tavola..."
    
    show chichibio normal at right
    
    chichibio "Ecco a voi, signore, la gru arrostita come avete ordinato."
    
    show corrado angry
    
    corrado "Chichibio! Questa gru ha solo una coscia! Che fine ha fatto l'altra?"
    
    # Quiz sulla reazione di Chichibio
    decameron "Come risponde Chichibio a questa domanda nella novella originale?"
    
    menu:
        "Quale risposta dà Chichibio?"
        
        "Confessa di averla data a Brunetta":
            $ knowledge_points += 3
            show screen knowledge_notification(3)
            
            decameron "In realtà, nella novella originale Chichibio non confessa subito. Inventa invece una bugia creativa."
        
        "Dice che le gru hanno una sola coscia":
            $ knowledge_points += 10
            show screen knowledge_notification(10)
            
            decameron "Esatto! Chichibio, senza pensarci troppo, risponde proprio così: 'Messere, lo sanno tutti che le gru hanno una sola coscia e una sola zampa'."
    
    show chichibio worried
    
    chichibio "Messere, lo sanno tutti che le gru hanno una sola coscia e una sola zampa."
    
    show corrado angry
    
    corrado "Che assurdità stai dicendo? Tutte le gru hanno due zampe!"
    
    chichibio "Vi assicuro, signore, è proprio così!"
    
    decameron "Qui Chichibio si trova in una situazione difficile. La sua bugia è inverosimile, ma non può tornare indietro."
    
    $ knowledge_points += 5
    show screen knowledge_notification(5)
    
    corrado "Basta con queste sciocchezze! Domani mattina andremo a verificarlo, ma guai a te se non è come dici tu!"
    
    # Passaggio alla scena del fiume - seguendo la novella originale
    jump river_scene

# Scena del fiume - seguendo fedelmente la novella
label river_scene:
    scene bg bedroom with fade
    
    narrator "La mattina dopo, appena spuntata l'alba, Corrado, a cui il sonno non era riuscito a far sbollire la rabbia, si alzò ancora tutto infuriato."
    
    show corrado angry at left
    
    corrado "Il mio cavallo! E fate montare anche Chichibio su un ronzino!"
    
    decameron "Nella società medievale, il tipo di cavallo assegnato rifletteva lo status sociale. Un 'ronzino' era un cavallo di qualità inferiore, adatto ai servitori."
    
    $ knowledge_points += 5
    show screen knowledge_notification(5)
    
    scene bg riverside with fade
    
    show corrado angry at left
    show chichibio worried at right
    
    narrator "Corrado portò Chichibio nei pressi di un fiume, dove spesso si potevano vedere le gru."
    
    narrator "Chichibio, vedendo che a Corrado la rabbia non era ancora passata e che gli toccava fornire una spiegazione per la sua bugia, non sapendo che fare, cavalcava vicino a Corrado con la più grande strizza del mondo."
    
    narrator "Si guardava intorno ma tutto quello che vedeva erano gru ben piantate sulle due zampe."
    
    # Quiz sullo stato d'animo di Chichibio
    decameron "Come si sente Chichibio in questo momento?"
    
    menu:
        "Qual è lo stato d'animo di Chichibio?"
        
        "Tranquillo e sicuro della sua bugia":
            decameron "No, il testo originale è chiaro: Chichibio ha 'la più grande strizza del mondo'. È terrorizzato perché sa di aver mentito e teme la punizione."
        
        "Terrorizzato e in cerca di una via d'uscita":
            $ knowledge_points += 10
            show screen knowledge_notification(10)
            
            decameron "Esatto! Chichibio è terrorizzato e cerca disperatamente un modo per salvarsi dalla situazione che lui stesso ha creato."
    
    narrator "Finalmente, arrivati vicini al fiume, Chichibio intravide delle gru che stavano ritte su una zampa sola, come stanno di solito quando dormono."
    
    show chichibio normal
    
    chichibio "Messere, guardate quelle là! Visto che ieri sera ho detto la verità? Visto che le gru hanno una sola coscia e una sola zampa?"
    
    # Quiz sulla reazione di Corrado
    decameron "Come reagisce Corrado a questa affermazione?"
    
    menu:
        "Cosa fa Corrado?"
        
        "Accetta la spiegazione di Chichibio":
            decameron "No, Corrado non si lascia convincere così facilmente."
        
        "Dimostra che Chichibio ha torto gridando alle gru":
            $ knowledge_points += 10
            show screen knowledge_notification(10)
            
            decameron "Esatto! Corrado decide di smascherare la bugia di Chichibio in modo pratico."
    
    corrado "Aspetta, adesso ti faccio vedere io che ne hanno due."
    
    narrator "Perciò si diresse verso quelle più vicine e gridò:"
    
    corrado "HOHÒ!"
    
    play sound "audio/sfx/hoho.mp3"
    
    narrator "Le gru tirarono fuori l'altra zampa, presero la rincorsa e scapparono via."
    
    play sound "audio/sfx/crane_flying.mp3"
    
    corrado "Che te ne pare? Sei convinto o no che ne hanno due?"
    
    # Quiz sulla risposta finale di Chichibio
    decameron "Ecco il momento cruciale della novella. Come risponde Chichibio a questa domanda?"
    
    menu:
        "Quale risposta dà Chichibio?"
        
        "Confessa di aver dato una coscia a Brunetta":
            decameron "No, nella novella originale Chichibio non confessa mai. Trova invece una risposta ingegnosa."
        
        "Risponde che Corrado non aveva gridato 'hohò' alla gru di ieri sera":
            $ knowledge_points += 15
            show screen knowledge_notification(15)
            
            decameron "Esattamente! Questa risposta arguta è ciò che salva Chichibio nella novella originale."
    
    show chichibio normal
    
    chichibio "Sì messere, ma voi a quella di ieri sera non le avete mica gridato 'hohò!' perché, se aveste gridato così, quella avrebbe tirato fuori l'altra coscia e l'altra zampa, come hanno fatto queste qui."
    
    # Momento di suspense
    show corrado normal
    
    narrator "Corrado rimase sorpreso per un momento..."
    
    # Quiz sull'esito finale
    decameron "Come reagisce Corrado a questa risposta arguta?"
    
    menu:
        "Qual è la reazione finale di Corrado?"
        
        "Si arrabbia ancora di più":
            decameron "No, la reazione di Corrado è completamente diversa."
        
        "Scoppia a ridere, apprezzando l'ingegno di Chichibio":
            $ knowledge_points += 10
            show screen knowledge_notification(10)
            
            decameron "Esatto! Corrado apprezza talmente l'arguzia di Chichibio da perdonarlo."
    
    show corrado laughing
    
    play sound "audio/sfx/laughter.mp3"
    
    corrado "Ahahahaha!"
    
    narrator "Corrado, a sentire una tale risposta, esplose in una fragorosa risata e si divertì così tanto che tutta la sua rabbia svanì."
    
    jump happy_ending

# Finale - conforme alla novella originale
label happy_ending:
    scene bg kitchen with fade
    play music "audio/music/happy_ending.mp3" fadein 2.0
    
    show corrado normal at left
    show chichibio happy at right
    
    narrator "Corrado fece quindi pace col suo cuoco, il quale evitò così il castigo."
    
    decameron "Qual è il tema centrale della novella di Chichibio e la Gru?"
    
    menu:
        "Qual è il tema principale della novella?"
        
        "Il valore dell'onestà":
            decameron "Non esattamente. La novella non premia l'onestà, poiché Chichibio mente due volte e ne esce vincitore."
        
        "L'importanza dell'ingegno e della prontezza di spirito":
            $ knowledge_points += 15
            show screen knowledge_notification(15)
            
            decameron "Perfetto! La novella celebra proprio questo: come l'ingegno e la prontezza di spirito (il 'motto') possano salvare anche dalle situazioni più difficili."
        
        "I rapporti tra servi e padroni nel Medioevo":
            $ knowledge_points += 5
            show screen knowledge_notification(5)
            
            decameron "Questo è un tema presente, ma non è il principale. Il focus è sull'ingegno e sulla prontezza di spirito che permettono a Chichibio di salvarsi."
    
    narrator "Questa novella ci insegna che talvolta una risposta pronta e spiritosa può salvare da situazioni difficili."
    
    decameron "La sesta giornata del Decameron, a cui appartiene questa novella, è interamente dedicata ai motti di spirito e alle risposte argute che salvano da situazioni pericolose."
    
    $ knowledge_points += 10
    show screen knowledge_notification(10)
    
    # Quiz finale di collegamento letterario
    decameron "A quale altra opera della letteratura italiana potremmo paragonare questo aspetto del Decameron?"
    
    menu:
        "Quale opera ha temi simili?"
        
        "La Divina Commedia di Dante":
            decameron "Non proprio. La Divina Commedia ha un impianto morale e teologico molto diverso dal Decameron, che celebra l'astuzia terrena."
        
        "Il Principe di Machiavelli":
            $ knowledge_points += 15
            show screen knowledge_notification(15)
            
            decameron "Ottima risposta! Nel Principe, Machiavelli celebra la virtù dell'uomo che sa usare l'ingegno per vincere la fortuna avversa, in modo simile a come fa Boccaccio."
        
        "I Promessi Sposi di Manzoni":
            $ knowledge_points += 5
            show screen knowledge_notification(5)
            
            decameron "Interessante paragone, ma I Promessi Sposi hanno un impianto morale più vicino a quello cristiano, mentre Boccaccio celebra l'ingegno umano in modo più laico e pragmatico."
    
    # Mostra punteggio finale
    scene black with fade
    
    show text "Hai completato lo studio della novella 'Chichibio e la Gru'" with dissolve
    $ renpy.pause(2.0, hard=True)
    
    show text "Punteggio conoscenza: [knowledge_points] punti" with dissolve
    $ renpy.pause(2.0, hard=True)
    
    # Messaggio finale basato sul punteggio
    if knowledge_points >= 80:
        show text "Eccellente! Hai dimostrato una comprensione profonda della novella e del contesto del Decameron!" with dissolve
    elif knowledge_points >= 50:
        show text "Molto bene! Hai acquisito una buona conoscenza della novella e dei suoi temi principali." with dissolve
    else:
        show text "Hai completato lo studio della novella. Rigiocando potresti scoprire altri aspetti interessanti del Decameron!" with dissolve
    
    $ renpy.pause(3.0, hard=True)
    
    # Suggerimenti per approfondire
    show screen decameron_info("Per approfondire", "• Leggi altre novelle della sesta giornata del Decameron\n• Confronta questa novella con altre storie che celebrano l'ingegno\n• Esplora il contesto storico e sociale della Firenze del XIV secolo")
    $ renpy.pause()
    
    return