source .env

source venv/bin/activate

alias aoc="python solution.py < in.txt"

function aoc_load () {
    if [ $1 ]
    then
        curl --cookie "session=$AOC_COOKIE" https://adventofcode.com/$1/day/$2/input > in.txt
    else
        curl --cookie "session=$AOC_COOKIE" `date +https://adventofcode.com/%Y/day/%-d/input` > in.txt
    fi
}

function aoc_go () {
    today=$(date +%d)
    if [ ! -d $today ]; then
        mkdir $today
        cd $today
        aoc_load
        echo "with open(0) as file:\n    f = file.read().splitlines()" > solution.py
    else
        cd $today
    fi
}

aoc_go