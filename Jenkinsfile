pipeline {
  agent any
  stages {
    stage('git') {
      steps {
        git(url: 'git@github.com:kriszhi/scripts.git', branch: 'master', changelog: true, poll: true)
      }
    }
    stage('Maven') {
      steps {
        sh 'maven clean package'
      }
    }
    stage('artifacts') {
      steps {
        archiveArtifacts '*.jar'
      }
    }
  }
}