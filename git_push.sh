echo [$(date)]: "START"
echo [$(date)]: "initializing git"
git init
echo [$(date)]: "add files to git repository"
git add . 
echo [$(date)]: "commiting changes"
git commit -m "integrated docker"
echo [$(date)]: "git push"
git push -u origin main
echo [$(date)]: "END"