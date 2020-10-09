# Snyk Overview

[Snyk](https://snyk.io) helps detect vulnerabilities in your application. It specifically identifies the different external libraries used and highlights any known vulnerabilities in those libraries.

It is free to use for open-source projects.

There are other similar such products if you'd like to explore alternatives.

## Snyk set-up

To get going, register for an account with Snyk.

You will then need to tell it about your Github account and the repo you'd like to scan.

For Python projects, Snyk reviews the `requirements.txt` file to see if any of the packages have known vulnerabilities. These are reported in the Snyk UI and also via email.

One nice feature is that sometimes Snyk can fix the issue directly. It will deintify if the underlying package has been fixed along with the version. It will then create a PR with an amendment to the requirements.txt file. It will update the file to use the new version of the offending package. This is nice as less work for you to do!

You can also configure your repo such that Snyk runs this check on all PRs. That way, you can reject a PR if Snyk detects an open vulnerability.





