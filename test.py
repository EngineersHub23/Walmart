 These are some git commands
 * git log --> It will give commit msg,ID,email,author

 * git show (commit id) --> this will entire details of committed file

 * git show --pretty="" --name-only (id) --> this will give file name only

 * git commit -a -m "commit msg" --> this directly move the updated file from working area to local repository
 
 * git commit --amend -m "commit msg" --> to change the last commit msg 
 
 * git push wm master --> to push the code from local repo to the remote repository

 * git rest test.py --> this file will come back to working area from staging area
 
 * git revert (commit id) --> 

   This will delete the newly created file in that commit id

   Also deletes the modified content in the file of that commit id 

 * git clean -n --> It will display the files that are going to delete

 * git clean -f --> It will the files

 * .gitignore file will have all the unwanted files like

   .classpath    file
   .project      file
   /node_modules directory

 * git branch --> display all the branches that are present

 * git branch QA --> creates new branch

 * git checkout QA --> move to QA from current branch

 * git branch -m QA development --> changes the branch name from QA to development

 * git branch -d development --> deletes that branch

 * git stash save "test.py" --> It will create a back up of the incompletd work

 * git stash apply test.py --> to start the incomplete work 

 * git stash list 

 * git stash drop --> to delete the backup off stash

 
