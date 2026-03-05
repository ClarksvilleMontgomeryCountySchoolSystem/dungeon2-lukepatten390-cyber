good = r"""        _
                 /' `\
                 k___y
                 th  j
                 /`Y'\
          .,--,. \___/   
  ...   ,'  __  ',    _
  |||  j  /'  `\  t  f |
  t j  f |      | j  t_|
   T   j  \    /  t   Y|
   |    ', `--' ,'    ||
   U      '~--~'      LJ"""
bad = r"""        _
                 /' `\
                 k___y
                 th  j
                 /`Y'\
          .,--,. \___/   
  ...   ,'  __  ',    _
  |||  j  /'  `\  t  f |
  t j  f |      | j  t_|
   T   j  \    /  t   Y|
   |    ', `--' ,'    ||
   U      '~--~'      LJ"""

escaped = True
if escaped:
    outcome = ("Legend: We did it!")
    print(good)
else:
    outcome = ("Doom: We were so close!")
    print(bad)
print(outcome)