#
#   Copyright (c) 2017-2019 Joy Diamond.  All rights reserved.
#
set -e$-

Main_py=../Other/Grow/3/Z.py

for i in 3*.py; do
    case $i in
        3j.py)      continue ;;
        3jst.py)    continue ;;
        3test.py)   continue ;;
    esac

    cp $i 3test.py

    for version in 1 15 8 4 12 16 14 2 6 10 3 5 7 9 11 13
    do
        echo
        echo "===  $version $i  ==="
        echo

        python $Main_py $version
    done
done
