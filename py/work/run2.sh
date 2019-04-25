#
#   Copyright (c) 2017-2019 Joy Diamond.  All rights reserved.
#
set -e$-

Main_py=../Other/Grow/3/Z.py

for i in 3*.py; do
    echo
    echo "===  $i  ==="
    echo

    cp $i 3test.py
    python $Main_py development
done
