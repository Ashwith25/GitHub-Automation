#!/bin/bash#

function github() {
    cd
    python3 PythonProjects/githubAutomate.py $1
    cd /home/ashwith/MyProjects/$1
    git init
    git remote add origin git@github.com:Ashwith25/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    code .
}