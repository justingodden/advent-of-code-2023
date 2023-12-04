source .env

source venv/bin/activate

alias aoc="python solution.py < in.txt"
alias aot="python solution.py < test.txt"

function aoc_load () {
    if [ $1 ]
    then
        curl --cookie "session=$AOC_COOKIE" `date +https://adventofcode.com/%Y/day/$1/input` > in.txt
        python ./../get_test_input.py $1 1> test.txt
    else
        curl --cookie "session=$AOC_COOKIE" `date +https://adventofcode.com/%Y/day/%-d/input` > in.txt
        python ./../get_test_input.py 1> test.txt
    fi
}

function aoc_go () {
    if [ $1 ]
    then
        day=$(printf "%02d" $1)
        if [ ! -d $day ]; then
            mkdir $day
            cd $day
            aoc_load $1
            echo "with open(0) as file:\n    f = file.read().splitlines()" > solution.py
        else
            cd $day
        fi
    else
        day=$(date +%d)
        if [ ! -d $day ]; then
            mkdir $day
            cd $day
            aoc_load
            echo "with open(0) as file:\n    f = file.read().splitlines()" > solution.py
        else
            cd $day
        fi
    fi    
}

if [ $1 ]
    then
        aoc_go $1
    else
        aoc_go
fi