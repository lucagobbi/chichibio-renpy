# File principale dello script Ren'Py per "Chichibio e la Gru"

# Definizione dei personaggi
define corrado = Character("Corrado", color="#8B0000", image="corrado")
define chichibio = Character("Chichibio", color="#1E90FF", image="chichibio")
define brunetta = Character("Brunetta", color="#FF69B4", image="brunetta")
define narrator = Character(None, what_italic=True)

# Immagini dei personaggi
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
image bg kitchen = "bg/kitchen.jpg"
image bg dining_room = "bg/dining_room.jpg"
image bg bedroom = "bg/bedroom.jpg"
image bg riverside = "bg/riverside.jpg"

# Inizio del gioco
label start:
    # Introduzione
    scene black
    play music "audio/music/medieval_theme.mp3" fadein 2.0
    
    narrator "Firenze, XIV secolo."
    
    narrator "In questa città viveva Corrado Gianfigliazzi, uno dei cittadini più in vista, famoso per la sua passione per la caccia."
    
    scene bg kitchen with fade
    
    narrator "Un giorno, Corrado catturò una gru e la fece portare al suo cuoco veneziano, Chichibio, ordinandogli di arrostirla per cena."
    
    show chichibio normal at center
    
    chichibio "Una bellissima gru! La preparerò con la massima cura per il mio signore."
    
    play sound "audio/sfx/cooking.mp3"
    
    narrator "Preparare una gru alla perfezione richiede abilità e conoscenza delle giuste tecniche culinarie medievali."
    
    jump cooking_minigame

label cooking_minigame:
    $ ingredients_selected = []
    $ correct_steps = 0
    $ total_steps = 5
    $ cooking_score = 0
    
    narrator "Per preparare la gru alla perfezione, Chichibio deve scegliere gli ingredienti giusti e seguire i passaggi corretti."
    
    show chichibio normal at center
    
    chichibio "Vediamo cosa serve per questa ricetta speciale..."
    
    # Primo passo: scegliere le spezie
    chichibio "Prima di tutto, devo scegliere le spezie giuste."
    
    menu:
        "Quali spezie dovrebbe usare Chichibio?"
        
        "Pepe e zafferano":
            $ correct_steps += 1
            $ cooking_score += 20
            chichibio "Perfetto! Il pepe darà sapore e lo zafferano un bel colore dorato. Proprio come piace al mio signore!"
            play sound "audio/sfx/correct.mp3"
            
        "Origano e basilico":
            chichibio "Hmm... non sono sicuro che siano le spezie tradizionali per questo piatto nobile."
            play sound "audio/sfx/wrong.mp3"
            
        "Cannella e chiodi di garofano":
            chichibio "Queste spezie sono troppo dolci per la gru. Meglio usarle per un dolce."
            play sound "audio/sfx/wrong.mp3"
    
    # Secondo passo: scelta del liquido per arrostire
    chichibio "Ora devo bagnare la gru con qualcosa per mantenerla succosa durante la cottura..."
    
    menu:
        "Con quale liquido bagnare la gru?"
        
        "Vino bianco":
            $ correct_steps += 1
            $ cooking_score += 20
            chichibio "Il vino bianco darà un sapore delicato ed elegante! Una scelta degna del mio signore."
            play sound "audio/sfx/correct.mp3"
            
        "Aceto":
            chichibio "L'aceto potrebbe essere troppo forte per questo piatto delicato. Corrado non apprezzerebbe."
            play sound "audio/sfx/wrong.mp3"
            
        "Acqua semplice":
            chichibio "Un po' semplice... manca di carattere. La gru merita di meglio!"
            play sound "audio/sfx/wrong.mp3"
    
    # Terzo passo: scegliere il ripieno
    chichibio "Per rendere la gru più saporita, devo aggiungere un ripieno..."
    
    menu:
        "Quale ripieno usare per la gru?"
        
        "Erbe aromatiche e cipolla":
            chichibio "Non male, ma potrei fare di meglio per un piatto così importante."
            play sound "audio/sfx/wrong.mp3"
            
        "Castagne e mele":
            $ correct_steps += 1
            $ cooking_score += 20
            chichibio "Eccellente! Le castagne e le mele daranno un sapore autunnale e ricco."
            play sound "audio/sfx/correct.mp3"
            
        "Pane raffermo e uova":
            chichibio "Hmm, questo potrebbe funzionare per un pollo, ma non per una gru nobile."
            play sound "audio/sfx/wrong.mp3"
    
    # Quarto passo: scelta del metodo di cottura
    chichibio "Ora, come dovrei cuocere questo magnifico uccello?"
    
    menu:
        "Quale metodo di cottura è migliore?"
        
        "Arrostire lentamente, girandola spesso":
            $ correct_steps += 1
            $ cooking_score += 20
            chichibio "Perfetto! La cottura lenta e il girare spesso garantiranno una gru dorata e succosa!"
            play sound "audio/sfx/correct.mp3"
            
        "Cuocere rapidamente a fiamma alta":
            chichibio "Troppo rapido! La carne diventerebbe dura e asciutta."
            play sound "audio/sfx/wrong.mp3"
            
        "Bollire prima, poi arrostire":
            chichibio "Questo metodo è adatto per carni più dure, non per un uccello delicato come la gru."
            play sound "audio/sfx/wrong.mp3"
    
    # Quinto passo: guarnizione finale
    chichibio "Infine, come dovrei guarnire la gru prima di servirla?"
    
    menu:
        "Come guarnire il piatto finale?"
        
        "Con salsa di agrumi":
            chichibio "Gli agrumi sono rari e preziosi, ma non si sposano bene con questo piatto."
            play sound "audio/sfx/wrong.mp3"
            
        "Con una spruzzata di aceto balsamico":
            chichibio "L'aceto balsamico è un condimento troppo moderno per questa ricetta tradizionale."
            play sound "audio/sfx/wrong.mp3"
            
        "Con una salsa a base di vino e miele":
            $ correct_steps += 1
            $ cooking_score += 20
            chichibio "Eccellente! Il vino e il miele creeranno una glassa lucida e saporita. Corrado sarà impressionato!"
            play sound "audio/sfx/correct.mp3"
    
    # Risultato finale
    $ cooking_success = (correct_steps >= 3)
    
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
    
    # Mostra il punteggio
    narrator "Punteggio di cucina: [cooking_score] / 100"
    
    # Salva il risultato per influenzare la storia successivamente
    $ gru_quality = cooking_score
    
    # Torna alla storia principale
    jump continue_cooking_story


label continue_cooking_story:

    narrator "Chichibio finì di preparare la gru e la mise sul fuoco ad arrostire."
    
    narrator "L'uccello era quasi pronto e dalla cucina si diffondeva un profumo delizioso..."
    
    show brunetta normal at right with moveinright
    
    narrator "...quando una giovane donna del quartiere, Brunetta, per la quale Chichibio aveva perso la testa, entrò in cucina attirata proprio da quel profumo."
    
    show chichibio happy
    
    chichibio "Brunetta mia! Che piacere vederti!"
    
    show brunetta pleading
    
    brunetta "Chichibio, che buon profumo! È gru quella che stai cucinando?"
    
    chichibio "Sì, è per la cena del mio signore Corrado."
    
    brunetta "Ti prego, Chichibio, potresti darmi una coscia? Mi è venuta una tale voglia..."
    
    show chichibio worried
    
    chichibio "Oh no, non posso! Il signor Corrado se ne accorgerebbe subito!"
    
    # Scelta del giocatore
    menu:
        "Come dovrebbe comportarsi Chichibio?"
        
        "Resistere e non dare la coscia a Brunetta":
            jump resist_temptation
            
        "Cedere e dare la coscia a Brunetta":
            jump give_leg
            
label resist_temptation:
    chichibio "Mi dispiace, Brunetta, non posso proprio. Corrado è un padrone esigente e si accorgerebbe subito."
    
    show brunetta normal
    
    brunetta "Capisco... Pazienza, sarà per un'altra volta."
    
    hide brunetta with moveoutright
    
    narrator "Brunetta se ne andò delusa, ma Chichibio mantenne intatta la gru."
    
    jump dinner_scene
    
label give_leg:
    narrator "Dopo un tira e molla, Chichibio non resistette alle suppliche di Brunetta."
    
    show chichibio normal
    
    chichibio "E va bene... ma solo per te, amore mio!"
    
    narrator "Chichibio staccò una coscia dalla gru e la diede a Brunetta."
    
    show brunetta normal
    
    brunetta "Grazie, Chichibio! Sei il cuoco più bravo e gentile di tutta Firenze!"
    
    chichibio "Shh! Non farne parola con nessuno!"
    
    hide brunetta with moveoutright
    
    show chichibio worried at center
    
    chichibio "Oh cielo... e ora come faccio con il signor Corrado?"
    
    jump dinner_scene
    
label dinner_scene:
    scene bg dining_room with fade
    play music "audio/music/tense.mp3" fadein 2.0
    
    show corrado normal at left
    
    narrator "Quando la gru fu servita a tavola..."
    
    show chichibio normal at right
    
    chichibio "Ecco a voi, signore, la gru arrostita come avete ordinato."
    
    if "give_leg" in _game_menu_screen:
        show corrado angry
        
        corrado "Chichibio! Questa gru ha solo una coscia! Che fine ha fatto l'altra?"
        
        show chichibio worried
        
        chichibio "Messere, lo sanno tutti che le gru hanno una sola coscia e una sola zampa."
        
        corrado "Che assurdità stai dicendo? Tutte le gru hanno due zampe!"
        
        chichibio "Vi assicuro, signore, è proprio così!"
        
        corrado "Basta con queste sciocchezze! Domani mattina andremo a verificarlo, e guai a te se non è come dici!"
    else:
        show corrado normal
        
        corrado "Ottimo lavoro, Chichibio. La gru sembra perfetta."
        
        show chichibio happy
        
        chichibio "Grazie, signore. Ho fatto del mio meglio."
        
        jump happy_ending
    
    jump morning_scene
    
label morning_scene:
    scene bg bedroom with fade
    
    narrator "La mattina dopo, appena spuntata l'alba..."
    
    show corrado angry at center
    
    corrado "Il mio cavallo! E fate montare anche Chichibio su un ronzino!"
    
    scene bg riverside with fade
    
    show corrado angry at left
    show chichibio worried at right
    
    narrator "Corrado portò Chichibio nei pressi di un fiume, dove spesso si potevano vedere le gru."
    
    narrator "Chichibio cavalcava terrorizzato, guardandosi intorno disperatamente."
    
    narrator "Finalmente, vide delle gru che stavano ritte su una zampa sola, come fanno spesso quando dormono."
    
    chichibio "Messere, guardate quelle là! Visto che ieri sera ho detto la verità? Le gru hanno una sola coscia e una sola zampa!"
    
    corrado "Aspetta, adesso ti faccio vedere io che ne hanno due."
    
    corrado "HOHÒ!"
    
    play sound "audio/sfx/hoho.mp3"
    
    narrator "Al grido di Corrado, le gru abbassarono l'altra zampa, presero la rincorsa e volarono via."
    
    play sound "audio/sfx/crane_flying.mp3"
    
    corrado "Che te ne pare, Chichibio? Sei convinto ora che hanno due zampe?"
    
    menu:
        "Come dovrebbe rispondere Chichibio?"
        
        "Ammettere di aver mentito":
            jump admit_lie
            
        "Rispondere con una battuta spiritosa":
            jump witty_response
    
label admit_lie:
    show chichibio worried
    
    chichibio "Avete ragione, signore. Vi chiedo perdono. Ho dato una coscia a Brunetta perché me l'ha chiesta con tanta insistenza..."
    
    show corrado angry
    
    corrado "Dunque mi hai mentito e hai rubato la mia cena! Sarai punito severamente!"
    
    narrator "Corrado non apprezzò la sincerità tardiva di Chichibio e lo punì privandolo del suo lavoro."
    
    narrator "Fine."
    
    return
    
label witty_response:
    show chichibio normal
    
    chichibio "Sì, messere, ma voi a quella di ieri sera non le avete mica gridato 'hohò!' perché, se aveste gridato così, quella avrebbe tirato fuori l'altra coscia e l'altra zampa, come hanno fatto queste qui."
    
    show corrado normal
    
    narrator "Corrado rimase sorpreso per un momento..."
    
    show corrado laughing
    
    play sound "audio/sfx/laughter.mp3"
    
    corrado "Ahahahaha!"
    
    narrator "Corrado esplose in una fragorosa risata, divertendosi così tanto che tutta la sua rabbia svanì."
    
    jump happy_ending
    
label happy_ending:
    play music "audio/music/happy_ending.mp3" fadein 2.0
    
    show corrado normal
    show chichibio happy
    
    corrado "Chichibio, sei un furbo matricolato, ma la tua prontezza di spirito merita un elogio."
    
    chichibio "Grazie, signore! Cercherò di servirvi sempre con la stessa dedizione... e magari con tutte e due le cosce della prossima gru!"
    
    narrator "E così Chichibio evitò il castigo grazie alla sua pronta risposta, continuando a servire come cuoco nella casa di Corrado."
    
    narrator "Questa storia ci insegna che talvolta una risposta pronta e spiritosa può salvare da situazioni difficili."
    
    narrator "Fine."
    
    return