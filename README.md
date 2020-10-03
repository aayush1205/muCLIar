# muCLIar <img src="https://i.ibb.co/641Jhrt/MUCLEAR2-001.png" alt="hydrogen animated logo" height="70px" align="right" />

[![Development Stage](https://img.shields.io/badge/Development-v.2.1.0-blue)]() [![License](https://img.shields.io/github/license/aayush1205/muCLIar)](https://github.com/aayush1205/muCLIar/blob/master/LICENSE) [![Issues](https://img.shields.io/github/issues/aayush1205/muCLIar)]() [![Stars](https://img.shields.io/github/stars/aayush1205/muCLIar?style=social)]()


**Imp: Multiple new features were added. Do consider uninstalling once and installing the fresh version.**

Coffee, Music and Code! What else could we developers ask for?

But then, long gone are days of slow internet and locally stored songs. **muCLIar** is a command line utility that lets you play the song you wish to listen to, directly through your command line. muCLIar lets you log in to **Youtube** and hence plays your "similar song" playlist as well, so you can search a song and then enjoy the mood for a long while.



<p align = "center">
<img src="https://i.imgur.com/MgLqMH0.gif">
 </p>


<br>

## Note
1. **muCLIar** is in **active development**. If you land into unprecedented errors, please feel free to open an issue. We would work on it as soon as possible. 
2. We are still working on finding a workaround to let you login to your YouTube account so that your "favourite songs playlist" starts playing after the current song finishes. We did have the login functionality before, but turns out, Google is now rejecting automated login.

## Features

1. Enjoy your music, advertisement and hassle free, right from your terminal in a single lined command.
2. Play/Pause/Switch between the songs using simple keypresses.
3. Play the YouTube mix relevant to your song.


## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Supported Distributions:
1. [Ubuntu](https://ubuntu.com/)
2. [Arch Linux](https://www.archlinux.org/)

### Prerequisites
1. [Conda](https://docs.conda.io/en/latest/miniconda.html)
2. [Google Chrome](https://www.google.com/chrome/?brand=CHBD&gclid=CjwKCAiA1fnxBRBBEiwAVUouUvzpOpZoXXgKyvMqvzo2yqnAOjBgWZXuuIWLdlD4libk5FFPlI0urhoC_2sQAvD_BwE&gclsrc=aw.ds)

### Installing
The repository has the installer script. This is what you need to do to get muCLIar running on your system:

1. Clone the repository:

```
git clone https://github.com/aayush1205/muCLIar.git
```

2. Get into the muCLIar directory:

```
cd muCLIar or cd /path/to/muCLIar
```

3. Run the installer: 


a. For Ubuntu:
```
./env.sh
```
b. For Arch Linux(might work in arch-based distros too: Manjaro, Velt etc.):

```
./arch_install.sh
```

~~4. You might encounter a XVFB display error. Just to ensure it doesn't happen, do the following:~~

**UPD**: Player uses PyVirtualDisplay now.

### Uninstalling

Use the uninstaller script. It will handle all the deletions and script removal.

```
./uninstall.sh
```

<br>

## Using muCLIar
1. Once you are done installing muCLIar, now its time to enjoy this utility. All you have to do is run:

```
mu -s "name of the song"
```
**UPD** : The player shows the controller on the terminal. 

## Built With
* [Selenium](https://selenium.dev/) - Automation Tool
* [ChromeDriver](https://chromedriver.chromium.org/) - Web Driver

<br>

## Contributing
### How to Contribute?
* Make sure that your changes do not conflict with the core files (changing file directories will require a change in all called paths)
* Follow the original code structure
* Refactoring contributions are welcome, explicitly mention "[Refactor]" in your pull request
* Give a few days to review PRs, code reviews are welcome 

### Steps to sync fork with master (Open Source Contributors):
If you fork is behind from the master project you can do these to get the latest version in the master branch of your fork.
First go to your(cloned) project folders.
Open the terminal in this directory then enter the following commands in the terminal:
 - Configuring a remote for fork

       $ git remote -v 
       //Lists the current configured remote repository for your fork//
       $ git remote add upstream https://github.com/aayush1205/muCLIar.git
       //Specifies a new remote upstream repository that will be synced with the fork//
       $ git remote -v
       //Should show the newly made remote *upstream* along with your previous remote//

 - Syncing the fork

       $ git fetch upstream
       //Fetch the branches and their respective commits from the upstream repository//
       $ git checkout master
       //Switches to local master branch//
       $ git merge upstream/master
       //Merges the upstearm remote (Main repo) into your local fork//
       
<br>

## Python Code Style
PEP8

<br>

## Contributors
<a href="https://github.com/aayush1205/muCLIar/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=aayush1205/muCLIar" />
</a>

<br>

## License
This project is licensed under the Apache License - see the [LICENSE.md](LICENSE.md) file for details

<br>

## Acknowledgments
* [AdBlocking Extension](https://chrome.google.com/webstore/detail/video-ad-blocker-plus-for/hegneaniplmfjcmohoclabblbahcbjoe?hl=en) 
