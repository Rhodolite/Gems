set -e$-

for command in \
    "python ../ErrorCorrecting/Remedy/Main.py"          \
    "python ../Other/Chess5x2/Main.py"                  \
    "python ../Other/CodeGenerator/Main.py"             \
    "python ../Other/CodeGenerator/Main.py dev"         \
    "python ../Other/LearningPython/Main.py"            \
    "python ../Other/LockFree/Main.py"                  \
    "python ../Other/Mothballed/Rubber/Main.py"         \
    "python ../Other/MultiProcessingExample/Main.py"    \
    "python ../Parser/Mothballed/JavaParser/Main.py"    \
    "python ../Parser/Mothballed/SqlParser/Main.py"     \
    "python ../Parser/PythonParser/Main.py"             \
    "python ../PPK/KeyExample/Main.py"                  \
    "python ../Tremolite/Restructure/Main.py"           \
    "python ../Tremolite/TremoliteParser/Main.py"       \
    "python ../UnitTest/UnitTest/Main.py"               \
    "python ../Parser/PythonParser/Main.py combine"     \
    "../../bin/x combine"
do
    echo "===   $command   ==="

    $command >/dev/null
done
