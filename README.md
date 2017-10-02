
#Purpose

Grep-ing for 1 value in a file or files is ok - but somedays I need to grep literally hundreds of items.

As I could not see a utility to do this - I rolled my own.

I it a little "heavy" (due to yaml and logging), but sometimes logging is the only thing that you can rely on.


#Performance

I have not spent too much time testing this

    time  python filestringsearch.py  -m /Users/tim/Dev/SecLists/Passwords/alleged-gmail-passwords.txt -k keys.txt

 This took

    real	0m1.579s
    user	0m1.521s
    sys	0m0.034s


As a bash script

    for a in $(cat keys.txt)
    do
        grep $a /Users/tim/Dev/SecLists/Passwords/alleged-gmail-passwords.txt
    done


This took

    real	0m5.542s
    user	0m5.012s
    sys	0m0.215s
