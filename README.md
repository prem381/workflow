Task: Create a Git workflow archetecture which will run a test when push will happen to feature branch.
Upon succeeding the test on feature it will merge to the master branch and run a test again.
Upon succeeding test on master, it will merger to release branch and final release will run on 25th of every month.

#===Solution==#

Step 1--> Create a GitHub repository.
        
Step 2--> Create a directory on local system.

          mkdir workflow
          
Step 3--> Initial and link repository to the GitHub repo.

Commands:
         cd workflow
         git init
         git remote add origin <repo url>
         # Add secret token to grant access for git hub repo.
         git remote set-url origin https://<secret_key>@github.com/prem381/workflow.git

         
Step 4--> Create an action.yml file at ./GitHub/workflow/ directory.

Command:

        mkdir .github/workflows
        cd .github/workflows     
        sudo nano action.yml    # refer the workflow code from action.yml file in this repo.
        sudo nano action1.yml    # refer the second workflow code from action1.yml file in this repo.
        sudo nano action2.yml    # refer the third workflow code from action2.yml file in this repo.
        
Step 5--> Create new_fearure.txt file on master branch.

Command: 

        sudo nano master.yml
        git add master.txt
        git commit -m "created github action file"
        
Step 6--> Create other branches in the below structure.

master --> Test --> feature

  |
  --> release

Step --> checkout to feature branch and create a feature.txt file and push it to feature branch to test the workflow.
       
       git checkout feature
       nano new_feature.txt
       git add new_feature.txt
       git comit -m "Created feature code"
       git push origin feature

