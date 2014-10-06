vagrant-gae
===========

Vagrant development box to run Google AppEngine


#### Basic python App
    # install vagrant plugin to handle hostnames
    vagrant plugin install vagrant-hostmanager
    
    # boot box
    vagrant up
    vagrant ssh
    
    # run development server
    ./demo_app/run.sh
    
    (open your browser on http://demo-app.dev:8777/)
    

#### Basic Django App
    adding soon...
    

#### Issues
    # ssh connection
    # remove existing keys
    # ssh-keygen -R demoapp.dev 
    # ssh-keygen -R 192.168.100.120
    
    # PIL instalation
    ...
    
    # Sync
    ...