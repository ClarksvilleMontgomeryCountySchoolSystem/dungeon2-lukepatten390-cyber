good = r""".
  / \__        .. _
  \.'  '._o    \_|_) ))
__(  __ / /      ).
\  _( ,/ /.____.' /
 '' '..-'        |
        \    _   (
         )v /-'._ )
        ////   |//
       // \\   //
      //   \\ ||\\
   --"------"-"--"--"""
bad = r"""   ,-'"`-.
     /    _ _\
     |   (@(@|
     \       /
     |    `-/
     /      |
    /       \
  ,'         `.
 /             \
(               )
|               |
(               )
 \             /
  `.         ,'
hh  `-.___,-'
"""
guard_awake = True
if not guard_awake:
    outcome = ("Shadow: He's here!")
    print(bad)
else:
    outcome = ("Doom: We're all good!")
    print(good)
print(outcome)