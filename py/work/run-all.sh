#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
set -e$-

python2=/usr/bin/python
python3=/usr/bin/python3

python=python2

for command in \
    "$python2 ../ErrorCorrecting/Remedy/Main.py"          \
    "$python  ../Games/Chess5x2/Main.py"                  \
    "$python  ../Games/Storyquest/Main.py"                \
    "$python  ../Other/CodeGenerator/Main.py"             \
    "$python  ../Other/CodeGenerator/Main.py ascii"       \
    "$python  ../Other/CodeGenerator/Main.py dev"         \
    "$python  ../Other/LearningPython/Main.py"            \
    "$python2 ../Other/LockFree/Main.py"                  \
    "$python2 ../Other/Mothballed/Rubber/Main.py"         \
    "$python  ../Other/MultiProcessingExample/Main.py"    \
    "$python  ../Parser/Mothballed/JavaParser/Main.py"    \
    "$python  ../Parser/Mothballed/SqlParser/Main.py"     \
    "$python  ../Parser/PythonParser/Main.py"             \
    "$python  ../PPK/KeyExample/Main.py"                  \
    "$python  ../Tremolite/Restructure/Main.py"           \
    "$python  ../Tremolite/TremoliteParser/Main.py"       \
    "$python  ../UnitTest/UnitTest/Main.py"               \
    "$python  ../Parser/PythonParser/Main.py combine"     \
    "../../bin/x combine"
do
    echo "===   $command   ==="

    $command >/dev/null
done
