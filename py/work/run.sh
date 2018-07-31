#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
set -e$-

usage=false
Main_py=pick

case $# in
    0) ;;

    1)
        case "$1" in
            h) Main_py=../Parser/PythonParser/Main.py ;;
            r) Main_py=../Tremolite/TremoliteParser/Main.py ;;
            z) Main_py=../UnitTest/UnitTest/Main.py ;;
            *) usage=true ;;
        esac
        ;;

    *) usage=true ;;
esac

if $usage
then
    echo "? usage: $0" >&2
    exit 1
fi

tmp_dir='../tmp'

if [ ! -d $tmp_dir ]
then
    mkdir $tmp_dir
fi

tmp1=$tmp_dir/tmp.1.$$.txt
tmp2=$tmp_dir/tmp.2.$$.txt
tmp3=$tmp_dir/tmp.3.$$.txt

for i in 1 2 3 15
do
    trap "trap $i; rm -f $tmp1 $tmp2 $tmp3; kill -$i $$; exit $i" $i
done

if [ $Main_py == pick ]; then
    Main_py=../Old/Beryl/Main.py
    Main_py=../PPK/KeyExample/Main.py
    Main_py=../ErrorCorrecting/Remedy/Main.py
    Main_py=../Other/LearningPython/Main.py
    Main_py=../UnitTest/UnitTest/Main.py
    Main_py=../Parser/PythonParser/Main.py
    Main_py=../Tremolite/TremoliteParser/Main.py
    Main_py=../Other/Chess5x2/Main.py
    Main_py=../Other/CodeGenerator/Main.py
    Main_py=../Parser/Mothballed/JavaParser/Main.py
    Main_py=../Other/LockFree/Main.py
    Main_py=../Other/MultiProcessingExample/Main.py
    Main_py=../Other/Mothballed/Rubber/Main.py
    Main_py=../Parser/Mothballed/SqlParser/Main.py
fi

show=2
all=false
#all=true
total=75

command="python -sS $Main_py"
commandO="python -O $Main_py"
command3="python3 $Main_py"
command3O="python3 -O $Main_py"
#command="../bin/x"

option="dev"

cat >$tmp1 <<END
Rhodolite
ABCDEFGHIJKLMNOP
Joy Diamond
her
y
y
END

echo -en '\E[H\E[J'

if [ -f $show ]; then
    tail -$total $show
else
    touch $show
fi

while :
do
    if [ $show = 2 -o $all = true ]; then
        if $command $option <$tmp1 >&$tmp2; then
            :
        fi

        #diff ../Topaz/GeneratedConjureDual.gpy ../Topaz/GeneratedConjureDual.py >>$tmp2
        #diff ../Topaz/GeneratedNew.gpy ../Topaz/GeneratedNew.py >>$tmp2
        if cmp -s $tmp2 2; then
            :
        else
            mv $tmp2 2

            if [ $show = 2 ]; then
                echo -en '\E[H\E[J'
                tail -$total 2
            fi
        fi
    fi

    if [ $show = 2o -o $all = true ]; then
        if $commandO $option <$tmp1 >&$tmp3; then
            :
        fi

        mv $tmp3 2o
    fi
   
    if [ $show = 3 -o $all = true ]; then
        if $command3 $option <$tmp1 >&$tmp3; then
            :
        fi

        if cmp -s $tmp3 3; then
            :
        else
            mv $tmp3 3
   
            if [ $show = 3 ]; then
                echo -en '\E[H\E[J'
                tail -$total 3
            fi
        fi
    fi
   
    if [ $show = 3o -o $all = true ]; then
       $command3O $option <$tmp1 >&$tmp3
       mv $tmp3 3o
    fi

    sleep 0.01
done
