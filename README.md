# launch

launches all processes in the AUV

creates shared memory for processes to communicate


## how to use git submodules

`git clone --recursive https://github.com/Package-Repository/launch.git`


#### stage, commit, and push changes

if you have changes on a bunch of branches

`git submodule foreach git add .`

`git submodule foreach git commit -m "message"`

`git submodule foreach git push`

if you only have a change on one branch, you can just do the normal stuff

#### add submodule

`git submodule add (link)`

example:

`git submodule add https://github.com/Package-Repository/ColorFilter.git`

#### everythings broken

you can either 
`git reset --hard origin/main`
on each submodule

or rm -rf the whole thing and reclone

SAVE SOMEWHERE ELSE BEFORE YOU DO THIS!


