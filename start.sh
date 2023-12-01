source .env

source venv/bin/activate

alias aoc="python solution.py < in.txt"

function aoc-load () {
    if [ $1 ]
    then
        curl --cookie "session=$AOC_COOKIE" https://adventofcode.com/$1/day/$2/input > in.txt
    else
        curl --cookie "session=$AOC_COOKIE" `date +https://adventofcode.com/%Y/day/%-d/input` > in.txt
    fi
}

function aoc-go () {
    today=$(date +%d)
    if [ ! -d "$today" ]; then
        mkdir $today
        cd $today
        aoc-load
        echo "f = open(0).read().splitlines()" > solution.py
    else
        cd $today
    fi
}

aoc-go