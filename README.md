Vagrant GAE
----------------------------------------

Vagrant development box to run Google AppEngine.

Documentation
----------------------------------------

### Install Vagrant & VirtualBox (OSX Instructions)
    brew cask install virtualbox
    brew cask install vagrant
  
### Run development box
    vagrant up  
    vagrant ssh  

    cd project
    make run

### Application access

Access **website** from:
- [http://projectdemo.dev:8080/](http://projectdemo.dev:8080/) 
- [http://projectdemo.dev:8000/](http://projectdemo.dev:8000/) (GAE)
