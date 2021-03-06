def add_hostname_segment(powerline):
    host_prompt = ''

    if powerline.args.shell == 'bash':
        host_prompt = ' \\h '
    elif powerline.args.shell == 'zsh':
        host_prompt = ' %m '
    else:
        import socket
        host_prompt = ' %s ' % socket.gethostname().split('.')[0]

    if powerline.args.colorize_hostname:
        from lib.color_compliment import stringToHashToColorAndOpposite
        from lib.colortrans import rgb2short
        FG, BG = stringToHashToColorAndOpposite(hostname)
        FG, BG = (rgb2short(*color) for color in [FG, BG])

        powerline.append(host_prompt, FG, BG)
    else:

        powerline.append(host_prompt, Color.HOSTNAME_FG, Color.HOSTNAME_BG)
