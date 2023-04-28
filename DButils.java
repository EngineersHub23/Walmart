"Hello guys this file contains DB connection logic"
Adding codes like
1.cd desktop
2.mkdir master 
3.git init
4.vi DButils.java
5.git status
6.git add (file name) or git add *.java
7.git config --global user.name
8.git config --global user.email
9.git config --global --list
10.git config --global user.name "shyamchow" --> to change the user name
11.git commit -m "commit msg"
12.git commit --amend -m "you can update the last commit msg"
13.git log --> to see the list commit id,msg,author
14.git -a -m "commit msg" --> you can directly move only the modified file from working area to local repo
15.git push wm(remote repo alias name) master(local repo master branch) ---> it is used to push the files in local repo to remote repo
16.git show (commit ID) --> shows the commit details (you can get the commit id by giving git log)
17.git show --pretty="" --name-only (commit id) --> it will give only the file name of that particular commit id
18.touch (file name)
19.git reset test.c --> it will move the file from staging area to working area
