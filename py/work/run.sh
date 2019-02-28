#
#   Copyright (c) 2017-2019 Joy Diamond.  All rights reserved.
#
set -e$-

usage=false
Main_py=pick

case $# in
    0) ;;

    1)
        case "$1" in
            a) Main_py=../Other/Grow/1/Z.py ;;
            h) Main_py=../Parser/PythonParser/Main.py ;;
            j) Main_py=../Parser/Mothballed/JavaParser/Main.py ;;
            r) Main_py=../Tremolite/TremoliteParser/Main.py ;;
            q) Main_py=../Games/Storyquest/Main.py ;;
            ts) Main_py=../Other/TeacherSample/Test_SchoolIdentifer.py ;;
            x) Main_py=Vision.z;;
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
    Main_py=../UnitTest/UnitTest/Main.py
    Main_py=../Parser/PythonParser/Main.py
    Main_py=../Tremolite/TremoliteParser/Main.py
    Main_py=../Other/CodeGenerator/Main.py
    Main_py=../Parser/Mothballed/JavaParser/Main.py
    Main_py=../Other/LockFree/Main.py
    Main_py=../Other/MultiProcessingExample/Main.py
    Main_py=../Other/Mothballed/Rubber/Main.py
    Main_py=../Parser/Mothballed/SqlParser/Main.py
    Main_py=../Games/Chess5x2/Main.py
    Main_py=../Other/LearningPython/Main.py
fi

show=2
all=false
#all=true
total=75

case $Main_py in
    Vision.z) show=5 ;;
esac


command="python -sS $Main_py"
commandO="python -O $Main_py"
command3="python3 $Main_py"
command3O="python3 -O $Main_py"
#command="../bin/x"

option="development"

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

    if [ $show = 4 ]; then
        if (cd ../Other/TeacherSample; py.test --capture=no Test_*.py) <$tmp1 >&$tmp3; then
            :
        fi

        if cmp -s $tmp3 4; then
            :
        else
            mv $tmp3 4
   
            if [ $show = 4 ]; then
                echo -en '\E[H\E[J'
                tail -$total 4
            fi
        fi
    fi

    if [ $show = 5 ]; then
#        if (cd ../Other/Grow/1/b; python Test.py) <$tmp1 >&$tmp3; then
        if (cd ../Other/Grow/1/b; python $Main_py; python Vision.py) <$tmp1 >&$tmp3; then
            :
        fi

        if cmp -s $tmp3 5; then
            :
        else
            mv $tmp3 5
   
            if [ $show = 5 ]; then
                echo -en '\E[H\E[J'
                tail -$total 5
            fi
        fi
    fi

    sleep 0.1
done
