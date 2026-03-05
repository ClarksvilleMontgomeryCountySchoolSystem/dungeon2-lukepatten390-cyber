good = r"""   _            _                  
      (_)          | |                 
  __ _ _ _ __ _ __ | | __ _ _ __   ___ 
 / _` | | '__| '_ \| |/ _` | '_ \ / _ \
| (_| | | |  | |_) | | (_| | | | |  __/
 \__,_|_|_|  | .__/|_|\__,_|_| |_|\___|
             | |                       
             |_|                       """
bad = r"""
  *    .  *       .             *
                         *
 *   .        *       .       .       *
   .     *
           .     .  *        *
       .                .        .
.  *           *                     *
                             .
         *          .   *
"""
has_key = True
if has_key:
    outcome = ("Click: We can get in!")
    print(good)
else:
    outcome = ("Doom: We can't get in!")
    print(bad)
print(outcome)