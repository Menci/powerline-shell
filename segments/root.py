def add_root_segment(powerline):
    root_indicators = {
        'bash': u' (っ･ω･)っ',
        'zsh': ' %# ',
        'bare': ' $ ',
    }
    bg = Color.CMD_PASSED_BG
    fg = Color.CMD_PASSED_FG
    if powerline.args.prev_error != 0:
        fg = Color.CMD_FAILED_FG
        bg = 3 # Color.CMD_FAILED_BG
        root_indicators['bash'] = u' (｡•́︿•̀｡) '
    powerline.append(root_indicators[powerline.args.shell], fg, bg)
