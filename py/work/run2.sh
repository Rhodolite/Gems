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

    for version in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
    do
        echo
        echo "===  $version $i  ==="
        echo

        python $Main_py $version
    done
done
