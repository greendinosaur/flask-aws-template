# SonarCloud overview

[SonarCloud](https://sonarcloud.io) is a static code analysis tool. It scans your code for issues that may cause problems in the future.

For example, it looks to see how maintainable your code is. Are there any security issues? Is the test coverage acceptable.

It's another product that is free to use for open-source projects.

## Sonarcloud set-up

You will need to register for a free account.

Then you need to point it at your Github account and the repo that you wish to scan.

You can configure Sonar to either scan your code whenever there is a change or to scan as part of a CI job. The former method is easier to configure. However, you will not get test coverage figures. If you'd like to use Sonar to help manage your test coverage then you will need to configure it as part of your CI job.

As you configure Sonarcloud, it will ask you to update the [sonar-project.properties](../sonar-project.properties) file with details of your repo and setup. Make the necessary changes.

The Sonarcloud set-up process takes you through the steps to perform. 

### CircleCI configuration

If you wish to use CircleCI and have set-it up as outlined in this [doc](cicdwithcircleci.md) then you can easily add an additional step to scan your code and send the results to SonarCloud.

Firstly, define a new Context in CircleCI called `sonarcloud`. Within this context, you need to define an environment variable called `SONAR_TOKEN` and set this to the token SonarCloud provides.

Secondly, amend the .circleci file and add the following line

```yaml
      - sonarcloud/scan`
```

directly above the `store_test_results` line so the file looks as below. Ensure the indentation remains the same.

```yaml
      - sonarcloud/scan
      - store_test_results:
          path: test-reports
```

Now when CircleCI runs, it will scan and send the results to sonarcloud for view there.