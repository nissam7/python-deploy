pipeline {
  agent any

  stages {

    stage('Clone Code') {
      steps {
        git branch: 'main', url: 'https://github.com/nissam7/python-deploy.git'
      }
    }

    stage('Build') {
      steps {
        sh 'docker-compose build'
      }
    }

    stage('Deploy') {
      steps {
        sh '''
        docker-compose down
        docker-compose up -d
        '''
      }
    }
  }
}

