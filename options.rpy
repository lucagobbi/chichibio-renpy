# Configurazioni per "Chichibio e la Gru"

## Informazioni di base
define config.name = "Chichibio e la Gru"
define gui.show_name = True
define config.version = "1.0"
define gui.about = _p("""
Una visual novel basata sulla novella di Boccaccio "Chichibio e la Gru".

Sviluppato con Ren'Py.
""")

## Configurazioni grafiche
define build.name = "ChichibioELaGru"
define config.window_icon = "gui/window_icon.png"
define config.window_title = "Chichibio e la Gru"

## Dimensioni finestra e schermo
define config.screen_width = 1280
define config.screen_height = 720

## Tema e colori principali
define gui.accent_color = '#8B0000'  # Rosso scuro per rappresentare il periodo storico
define gui.idle_color = '#888888'
define gui.hover_color = '#B8860B'   # Oro scuro per hover
define gui.selected_color = '#B22222'
define gui.muted_color = '#666666'
define gui.interface_text_color = '#ffffff'
define gui.button_text_idle_color = '#888888'
define gui.button_text_hover_color = '#ffffff'
define gui.button_text_selected_color = '#ffffff'

## Dimensioni testo
define gui.text_size = 22
define gui.name_text_size = 30
define gui.interface_text_size = 24
define gui.label_text_size = 28
define gui.notify_text_size = 16

## Velocità del testo
default preferences.text_cps = 30  # Caratteri al secondo - abbastanza lento per l'atmosfera storica

## Configurazioni di salvataggio e autosalvataggio
define config.has_autosave = True
define config.autosave_frequency = 200
define config.autosave_slots = 10
define config.save_directory = "ChichibioELaGru"

## Immagine di transizione tra le scene
define config.end_splash_transition = dissolve

## Disabilità alcune funzionalità opzionali che non usiamo
define config.has_sound = True
define config.has_music = True
define config.has_voice = False  # Non ci sono dialoghi vocali

## Volume default
define config.default_music_volume = 0.7
define config.default_sfx_volume = 0.8

## Transizioni tra scene
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.main_game_transition = dissolve
define config.game_main_transition = dissolve
define config.end_game_transition = fade

## Preferenze dell'utente
default preferences.afm_time = 15  # Tempo per avanzamento automatico