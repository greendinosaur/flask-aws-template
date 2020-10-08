# Contributing

Welcome! We love receiving contributions from our community, so thanks for stopping by! There are many ways to contribute, including submitting bug reports, improving documentation, submitting feature requests, reviewing new submissions, or contributing code that can be incorporated into the project.

This document describes our development process. Following these guidelines shows that you respect the time and effort of the developers managing this project. In return, you will be shown respect in addressing your issue, reviewing your changes, and incorporating your contributions.

If you're not looking for some kinds of contributions, note that up front:

**Table of Contents:**

1. [Code of Conduct](#code-of-conduct)
2. [Important Resources](#important-resources)
2. [Questions](#questions)
3. [Feature Requests](#feature-requests)
4. [Improving Documentation](#improving-documentation)
5. [Reporting Bugs](#reporting-bugs)
6. [Contributing Code](#contributing-code)
	1. [Getting Started](#getting-started)
	1. [Finding an Issue!](#finding-an-issue)
	1. [Development Process](#development-process)
	1. [Building the Project](#building-the-project)
	1. [Testing](#testing)
	1. [Style Guidelines](#style-guidelines)
1. [Pull Request Guidelines](#pull-request-guidelines)
	1. [Review Process](#review-process)
	1. [Addressing Feedback](#addressing-feedback)


## Code of Conduct


By participating in this project, you agree to abide by our [Code of Conduct](CODE-OF-CONDUCT.md). We expect all contributors to follow the [Code of Conduct](CODE-OF-CONDUCT.md) and to treat fellow humans with respect.


## Important Resources

* Checkout the [README.md](readme.md) for info about this project
* The issue tracker shows current issues

## Questions

Questions? Please raise an issue in the repo's issue tracker.

## Feature Requests


Please create a new GitHub issue for any major changes and enhancements that you wish to make. Please provide the feature you would like to see, why you need it, and how it will work. Discuss your ideas transparently and get community feedback before proceeding.

Major Changes that you wish to contribute to the project should be discussed first in an GitHub issue that clearly outlines the changes and benefits of the feature.

Small Changes can directly be crafted and submitted to the GitHub Repository as a Pull Request. See the section about Pull Request Submission Guidelines, and for detailed information the core development documentation.

## Reporting Bugs

Before you submit your issue, please look at the issue tracker to see if it's been raised previously.

If you find a bug in the source code, you can help us by submitting an issue to our GitHub issue tracker. Even better, you can submit a Pull Request with a fix.

## Improving Documentation

Should you have a suggestion for the documentation, you can open an issue and outline the problem or improvement you have - however, creating the doc fix yourself is much better!

If you want to help improve the docs, it's a good idea to let others know what you're working on to minimize duplication of effort. Create a new issue (or comment on a related existing one) to let others know what you're working on. If you're making a small change (typo, phrasing) don't worry about filing an issue first.

## Contributing Code

Unsure where to begin contributing? You can start by looking through these beginner and help-wanted issues: Beginner issues - issues which should only require a few lines of code, and a test or two. Help wanted issues - issues which should be a bit more involved than beginner issues.

### Getting Started

Follow the guidance on the [README](README.md) for getting the Flask application up-and-running on your local machine.

You will need to fork the main repository to work on your changes. Simply navigate to our GitHub page and click the "Fork" button at the top. Once you've forked the repository, you can clone your new repository and start making edits.

In git it is best to isolate each topic or feature into a “topic branch”. While individual commits allow you control over how small individual changes are made to the code, branches are a great way to group a set of commits all related to one feature together, or to isolate different efforts when you might be working on multiple topics at the same time.

While it takes some experience to get the right feel about how to break up commits, a topic branch should be limited in scope to a single issue

```
# Checkout the master branch - you want your new branch to come from master
git checkout master

# Create a new branch named newfeature (give your branch its own simple informative name)
git branch newfeature

# Switch to your new branch
git checkout newfeature
```

### Finding an Issue

The list of outstanding feature requests and bugs can be found on our on our issue tracker. Pick an unassigned issue that you think you can accomplish and add a comment that you are attempting to do it.

> `starter` labeled issues are deemed to be good low-hanging fruit for newcomers to the project
> `help-wanted` labeled issues may be more difficult than `starter` and may include new feature development
> `doc` labeled issues must only touch content in the `docs` folder.

### Development Process

This project follows the [git flow](http://nvie.com/posts/a-successful-git-branching-model/) branching model of product development.

You should be using the master branch for the most stable release

### Building the Project

Make the necessary changes in the feature branch.


### Testing

If you add code you need to add tests! We’ve learned the hard way that code without tests is undependable. If your pull request reduces our test coverage because it lacks tests then it will be rejected.

The Makefile is configured to run all tests in the [tests](tests/) folder. pytest is the underlying test runner. Either add tests to the existing test files or create new test files.

```
Make test
```

### Style Guidelines

For Python, PEP8 defines the style guidelines. pylint and flake8 are used to check the code meets the PEP8 guidelines. These can be run as:

```
pylint
```

and

```
flake8
```

### Git Commit Guidelines

The first line of the commit log must be treated as as an email subject line.  It must be strictly no greater than 50 characters long. The subject must stand on its own and not only make external
references such as to relevant bug numbers.

The second line must be blank.

The third line begins the body of the commit message (one or more paragraphs) describing the details of the commit.  Paragraphs are each
separated by a blank line.  Paragraphs must be word wrapped to be no longer than 76 characters.

The last part of the commit log should contain all "external references", such as which issues were fixed.

## Pull Request Process

When you are ready to generate a pull request, either for preliminary review, or for consideration of merging into the project you must first push your local topic branch back up to GitHub:

```
git push origin newfeature
```

Once you've committed and pushed all of your changes to GitHub, go to the page for your fork on GitHub, select your development branch, and click the pull request button. If you need to make any adjustments to your pull request, just push the updates to your branch. Your pull request will automatically track the changes on your development branch and update.

1. Ensure any install or build dependencies are removed before the end of the layer when doing a
   build.
2. Update the README.md with details of changes to the interface, this includes new environment
   variables, exposed ports, useful file locations and container parameters.
3. You may request the reviewer to merge it for you.

### Review Process

PRs will be reviewed on a daily basis by the core project maintainer.

### Addressing Feedback

Once a PR has been submitted, your changes will be reviewed and constructive feedback may be provided. Feedback isn't meant as an attack, but to help make sure the highest-quality code makes it into our project. Changes will be approved once required feedback has been addressed.

If a maintainer asks you to "rebase" your PR, they're saying that a lot of code has changed, and that you need to update your fork so it's easier to merge.

To update your forked repository, follow these steps:

```
# Fetch upstream master and merge with your repo's master branch
git fetch upstream
git checkout master
git merge upstream/master

# If there were any new commits, rebase your development branch
git checkout newfeature
git rebase master
```

If too much code has changed for git to automatically apply your branches changes to the new master, you will need to manually resolve the merge conflicts yourself.

Once your new branch has no conflicts and works correctly, you can override your old branch using this command:

```
git push -f
```

Note that this will overwrite the old branch on the server, so make sure you are happy with your changes first!

