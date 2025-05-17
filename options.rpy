## Informazioni di base
define config.name = "Chichibio e la Gru"
define gui.show_name = True
define config.version = "1.0"
define gui.about = _p("""
Una visual novel basata sulla novella di Boccaccio "Chichibio e la Gru".

Tratta dal Decamerone, Giornata VI, Novella 4.
Sviluppato con Ren'Py.
""")

## Configurazioni grafiche
define build.name = "ChichibioELaGru"
define config.window_icon = "gui/window_icon.png"
define config.window_title = "Chichibio e la Gru - Una Novella del Decamerone"

## Dimensioni finestra e schermo
define config.screen_width = 1280
define config.screen_height = 720

## Tema e colori principali - Tavolozza Medievale
define gui.accent_color = '#7B3F00'       # Marrone pergamena scuro
define gui.idle_color = '#5C4033'         # Bruno terra di siena per elementi inattivi
define gui.hover_color = '#D4AF37'        # Oro antico per hover
define gui.selected_color = '#8B0000'     # Rosso scuro per elementi selezionati
define gui.muted_color = '#4A3728'        # Bruno scuro per elementi attenuati
define gui.interface_text_color = '#EDE0D4' # Avorio chiaro per testo
define gui.button_text_idle_color = '#C8B99E' # Beige pergamena per testo pulsanti
define gui.button_text_hover_color = '#F8F0E3' # Pergamena chiaro per hover
define gui.button_text_selected_color = '#FFFFFF' # Bianco puro per selezione

## Dimensioni testo
define gui.text_size = 24                 # Testo principale più grande per stile antico
define gui.name_text_size = 34            # Nomi personaggi più evidenti
define gui.interface_text_size = 26       # Interfaccia più leggibile
define gui.label_text_size = 30           # Etichette più grandi
define gui.notify_text_size = 18          # Notifiche moderate

## Velocità del testo - Più lenta per atmosfera medievale
default preferences.text_cps = 25         # Caratteri al secondo ridotti per tono solenne

## Configurazioni salvataggio
define config.has_autosave = True
define config.autosave_frequency = 200
define config.autosave_slots = 10
define config.save_directory = "ChichibioELaGru"

## Transizioni più teatrali
define config.enter_transition = Dissolve(1.0)          # Dissolvenza più lenta
define config.exit_transition = Dissolve(1.0)
define config.intra_transition = Dissolve(0.8)
define config.main_game_transition = Dissolve(1.0)
define config.game_main_transition = Dissolve(1.0)
define config.end_game_transition = Fade(0.5, 1.0, 0.5) # Dissolvenza più drammatica

## Stile pulsanti e menu - Aspetto pergamena
define gui.button_width = 350                           # Pulsanti più ampi
define gui.button_height = 45
define gui.button_borders = Borders(6, 6, 6, 6)         # Bordi più evidenti
define gui.button_text_xalign = 0.5
define gui.button_text_yalign = 0.5

## Preferenze
default preferences.afm_time = 20  # Tempo avanzamento automatico più lento
default preferences.music_volume = 0.8
default preferences.sfx_volume = 0.8