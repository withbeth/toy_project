# Commit checker bot

Commit Checker Bot checks if there was a new commit of one of the tracked GitHub repositories every day.

## Memo and TODO's
- [] Logics
    - [] RepoName, LastCommitId, LastCommitDate, LastCommitterName, LastCommitMessage 
- [] Check how twitterbot check "last release" since last check
    - [] Cron style schedule using python
- [] Configurations
    - [] Configuration JSON or yml
- [] Logging
    - [] STDOUT -> LOGGER
- [] Building CLI to expose small chucks of functionality
- [] Send alert message to admin
- [] Deployment(Deploying code directly into cloud)

## Usage

## Features


### Logging
```
(TimeStamp) (LogLevel) : Execution #Number starts
(TimeStamp) (LogLevel) : Commits since last deployment: {NUMBER OF COMMITS since layst deployment}
(TimeStamp) (LogLevel) : {RepoName}: {CommitMessage} ({CommitId})
(TimeStamp) (LogLevel) : Execution end
```