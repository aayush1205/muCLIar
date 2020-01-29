# muCLIar

[![Development Stage](https://img.shields.io/badge/Development-Private_Alpha-red)]() [![License](https://img.shields.io/badge/License-Apache-blue)](https://github.com/aayush1205/muCLIar/blob/master/LICENSE)


Coffee, Music and Code! What else could we developers ask for?

But then, long gone are days of slow internet and locally stored songs. **muCLIar** is a command line utility that lets you play the song you wish to listen to, directly through your command line. muCLIar lets you log in to **Youtube** and hence plays your "similar song" playlist as well, so you can search a song and then enjoy the mood for a long while. 


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

1. Selenium
2. ChromeDriver

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Selenium](https://selenium.dev/) - Automating Tool
* [ChromeDriver](https://chromedriver.chromium.org/) - Web Driver

## Contributing

### How to Contribute?
* Make sure that your changes do not conflict with the core files (changing file directories will require a change in all called paths)
* Follow the original code structure
* Refactoring contributions are welcome, explicitly mention "[Refractor]" in your pull request
* Give a few days to review PRs, code reviews are welcome 

<br>

### Steps to sync fork with master (Open Source Contributors):
If you fork is behind from the master project you can do these to get the latest version in the master branch of your fork.
First go to your(cloned) project folders.
Open the terminal in this directory then enter the following commands in the terminal:
 - Configuring a remote for fork

       $ git remote -v 
       //Lists the current configured remote repository for your fork//
       $ git remote add upstream https://github.com/Purukitto/Yuso_TravelApp.git
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

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

   <table><tr><td align="center"><a href="https://github.com/aayush1205"><img src="https://avatars1.githubusercontent.com/u/39720355?s=400&v=4" width="100px;" alt="Aayush Upadhyay"/><br /><sub><b>Aayush Upadhyay</b></a></sub><br /><sub><b>Author</b></sub><br /><a href="https://github.com/aayush1205/muCLIar/commits?author=aayush1205" title="Commits">💻</a></td><td align="center"><a href="https://github.com/Purukitto"><img src="https://avatars3.githubusercontent.com/u/49859368?s=460&v=4" width="100px;" alt="Pulkit Sambhavi Singh"/><br /><sub><b>Pulkit Sambhavi Singh</b></sub></a></sub><br /><sub><b>Contributor</b></sub><br /><a href="https://github.com/aayush1205/muCLIar/commits?author=Purukitto" title="Commits">💻</a></td></tr></table>   


See also the list of all the [contributors](https://github.com/aayush1205/muCLIar/contributors) who participated in this project.

## License

This project is licensed under the Apache License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
